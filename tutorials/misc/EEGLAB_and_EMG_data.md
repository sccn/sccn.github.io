---
layout: default
title: EEGLAB and EMG data
long_title: EEGLAB and EMG data
parent: Reference Topics
grand_parent: Tutorials
---
EEGLAB and EMG data
====================

EEGLAB supports processing electromyography (EMG) data in addition to EEG and MEG data. This tutorial demonstrates how to analyze EMG data in BIDS format, compute EMG event-related potentials (EMG-ERPs), and compare muscle activation patterns across different conditions.

We will use the [emg2qwerty dataset](https://nemar.org/dataexplorer/detail?dataset_id=nm000104) available on NEMAR, which contains surface EMG recordings from forearm muscles during touch typing on a QWERTY keyboard.

## Dataset Overview

The emg2qwerty dataset includes:
- 32 bipolar EMG channels (16 per forearm)
- Surface EMG recordings from wristband sensors
- Keystroke events with precise timing
- Sampling rate: ~2000 Hz
- Task: Touch typing prompted text

This dataset is ideal for demonstrating EMG-ERP analysis because:
1. Events (keystrokes) have precise timing
2. Different keys activate different muscle patterns
3. Left vs right hand comparisons are possible
4. High trial counts for common keys

## Importing EMG BIDS data

EEGLAB can import BIDS-formatted EMG data using the [bids-matlab-tools](https://github.com/sccn/bids-matlab-tools) plugin. After starting EEGLAB, use menu item <span style="color: brown">File > Import data > From BIDS folder structure</span>.

![BIDS Import Dialog](/assets/images/emg-bids-dialogbox-shot.png)

Alternatively, you can import programmatically:

```matlab
% Start EEGLAB
addpath('/path/to/eeglab');
eeglab nogui;

% Define BIDS root directory
bids_root = '/path/to/nm000104';
subject_id = 'sub-03734552';
session_id = 'ses-1620588853';

% Import using pop_importbids
[STUDY, ALLEEG] = pop_importbids(bids_root, ...
    'bidstask', 'typing', ...
    'subjects', subject_id(5:end));  % Remove 'sub-' prefix

EEG = ALLEEG(1);
```

After import, EEGLAB shows the dataset information:

![BIDS Import Result](/assets/images/emg-bidsimport-shot.png)

![EEGLAB Interface](/assets/images/emg-eeglabview-shot.png)

You can also load the BDF files directly:

```matlab
% Load BDF file
emg_file = fullfile(bids_root, subject_id, session_id, 'emg', ...
    sprintf('%s_%s_task-typing_emg.bdf', subject_id, session_id));
EEG = pop_biosig(emg_file);

% Load events from TSV file
events_file = fullfile(bids_root, subject_id, session_id, 'emg', ...
    sprintf('%s_%s_task-typing_events.tsv', subject_id, session_id));
events_table = readtable(events_file, 'FileType', 'text', 'Delimiter', '\t');

% Convert to EEGLAB event structure
for i = 1:height(events_table)
    EEG.event(i).latency = events_table.onset(i) * EEG.srate;
    EEG.event(i).type = char(events_table.value(i));
    if ~strcmp(events_table.key{i}, 'n/a')
        EEG.event(i).key = char(events_table.key(i));
    end
end

% Set data type
EEG.etc.datatype = 'emg';
EEG = eeg_checkset(EEG);
```

## Sanity checks: Visualizing the data

Before preprocessing, it's important to verify the data quality and structure using EEGLAB's visualization tools.

### Plotting raw EMG data

Use EEGLAB's scrolling data viewer to inspect raw EMG signals and events:

```matlab
% Use EEGLAB menu: Plot > Channel data (scroll)
% Or from command line:
pop_eegplot(EEG, 1, 1, 1);
```

This opens an interactive window where you can:
- Scroll through the continuous EMG data
- See keystroke events marked with vertical lines
- Identify noisy channels or artifacts
- Adjust the display scale and time window

![Raw EMG Data Viewer](/assets/images/emg-rawdata-shot.png)

**Note for EMG:** The scrolling viewer works the same as for EEG, but expect:
- Higher amplitude signals (µV to mV range)
- High-frequency oscillations (20-250 Hz)
- Bursts of activity aligned with keystroke events

### Inspecting event structure

Use EEGLAB's event viewer to check event timing and types:

```matlab
% View events: Edit > Event values
% Or list event types from command line:
unique_events = unique({EEG.event.type});
fprintf('Found %d event types\n', length(unique_events));
fprintf('Total events: %d\n', length(EEG.event));

% Count specific keystroke types
keystroke_idx = find(contains({EEG.event.type}, 'keystroke_'));
fprintf('Keystroke events: %d\n', length(keystroke_idx));
```

### Computing power spectral density (PSD)

Use EEGLAB's spectral plotting function to verify EMG frequency content:

```matlab
% Use EEGLAB menu: Plot > Channel spectra and maps
% Or from command line:
% Note: 'freq', [] disables topoplots which are NOT meaningful for EMG
figure; pop_spectopo(EEG, 1, [0 EEG.xmax*1000], 'EEG', ...
    'freqrange', [0 500], ...
    'freq', []);
```

This displays:
- Power spectral density for all channels overlaid
- Frequency range up to 500 Hz (appropriate for EMG)
- **Important**: We set `'freq', []` to disable topoplots - they are NOT meaningful for EMG data since electrodes are on forearm muscles, not scalp

![EMG Power Spectrum](/assets/images/emg-spectopo-shot.png)

**Expected pattern:** Most EMG power should be concentrated in the 20-250 Hz range, with peaks around 50-150 Hz for muscle activity.

## EMG preprocessing

EMG signals require different preprocessing than EEG:

### Frequency ranges
EMG contains higher frequencies than EEG:
- **EEG**: Typically 1-50 Hz
- **EMG**: Typically 20-450 Hz (motor tasks: 20-250 Hz)

### Bandpass filtering

```matlab
% Apply bandpass filter for EMG
lowcut = 20;   % Hz - removes slow drifts
highcut = 250; % Hz - removes high-frequency noise

EEG = pop_eegfiltnew(EEG, 'locutoff', lowcut, 'hicutoff', highcut);
```

### Channel quality check

For EMG, check channels with unusual variance:

```matlab
% Calculate variance for each channel
channel_vars = var(EEG.data, 0, 2);
mean_var = mean(channel_vars);
std_var = std(channel_vars);

% Flag channels outside 3 standard deviations
bad_chan_idx = find(channel_vars < mean_var - 3*std_var | ...
                    channel_vars > mean_var + 3*std_var);
```

### Comparison: Original vs Filtered

After filtering, you should see:
- Reduced low-frequency drift
- Cleaner baseline
- Preserved event-related transients

![Preprocessing Comparison](/assets/images/emg_preprocessed_comparison.png)

## Data cleaning with clean_rawdata

**Important:** EMG data can have extremely noisy channels or bad segments. These must be cleaned BEFORE computing the envelope, otherwise artifacts will be preserved in the ERP.

### Why cleaning is critical for EMG

- **Electrode displacement**: Wristband movement creates large amplitude artifacts
- **Bad channels**: Some channels may have poor contact throughout the session
- **Motion artifacts**: Arm/wrist movement during typing
- **Session variability**: Some sessions have much worse quality than others

### Installing clean_rawdata plugin

If not already installed:

```matlab
% From EEGLAB menu: File > Manage EEGLAB extensions
% Search for 'clean_rawdata' and install

% Or from command line:
plugin_askinstall('clean_rawdata');
```

### Using ASR (Artifact Subspace Reconstruction)

ASR removes bad data portions while preserving good segments:

```matlab
% Apply clean_rawdata with ASR
% Parameters tuned for EMG data (more conservative than EEG defaults)
EEG = clean_rawdata(EEG, ...
    'FlatlineCriterion', 5, ...        % Remove channels flat for >5 seconds
    'ChannelCriterion', 0.8, ...       % Remove channels with <0.8 correlation to robust estimate
    'LineNoiseCriterion', 4, ...       % Line noise threshold
    'Highpass', [0.25 0.75], ...       % Already filtered, set to preserve
    'BurstCriterion', 20, ...          % ASR burst criterion (higher = more aggressive)
    'WindowCriterion', 0.25, ...       % Remove windows with >25% bad channels
    'BurstRejection', 'on', ...        % Enable ASR burst correction
    'Distance', 'Euclidean', ...       % Distance metric
    'WindowCriterionTolerances', [-Inf 7]); % Window tolerance

EEG = eeg_checkset(EEG);
```

### Understanding ASR parameters for EMG

**Key parameters to adjust:**

1. **BurstCriterion** (default: 20 for EMG, 5 for EEG)
   - Higher values = less aggressive cleaning
   - EMG has naturally higher amplitudes than EEG
   - Too aggressive (low value) removes genuine muscle activity
   - Recommended: 15-25 for EMG

2. **ChannelCriterion** (0.8 recommended)
   - Removes channels that don't correlate well with neighbors
   - Important for wristband arrays where channels should be similar

3. **WindowCriterion** (0.25)
   - Removes time windows where >25% of channels are bad
   - Useful for movement artifacts affecting multiple channels

### Visual inspection after cleaning

Always visualize the data after cleaning:

```matlab
% Plot scrolling data to inspect cleaning results
pop_eegplot(EEG, 1, 1, 1);

% Check which channels were removed
if isfield(EEG.etc, 'clean_channel_mask')
    removed_chans = find(~EEG.etc.clean_channel_mask);
    fprintf('Removed %d channels: ', length(removed_chans));
    for i = 1:length(removed_chans)
        fprintf('%s ', EEG.chanlocs(removed_chans(i)).labels);
    end
    fprintf('\n');
end

% Check how much data was removed
if isfield(EEG.etc, 'clean_sample_mask')
    samples_removed = sum(~EEG.etc.clean_sample_mask);
    pct_removed = 100 * samples_removed / length(EEG.etc.clean_sample_mask);
    fprintf('Removed %.1f%% of data samples\n', pct_removed);
end
```

### Alternative: Manual bad channel removal

If you prefer manual control:

```matlab
% Mark bad channels
bad_channels = [5, 12, 23];  % Example indices

% Remove bad channels
EEG = pop_select(EEG, 'nochannel', bad_channels);

% Or interpolate (if you have spatial information)
% EEG = pop_interp(EEG, bad_channels, 'spherical');
```

### Session quality metrics

Before cleaning, compute quality metrics to decide if a session should be excluded:

```matlab
% Compute RMS per channel
channel_rms = sqrt(mean(EEG.data.^2, 2));

% Identify outlier sessions (>3 SD from mean)
if mean(channel_rms) > subject_mean_rms + 3*subject_std_rms
    fprintf('WARNING: This session may be an outlier (high RMS)\n');
    fprintf('Consider excluding from group analysis\n');
end

% Check percentage of extreme values
pct_extreme = 100 * sum(abs(EEG.data(:)) > 1000) / numel(EEG.data);
if pct_extreme > 1
    fprintf('WARNING: %.2f%% of samples exceed 1000 µV\n', pct_extreme);
end
```

### Cleaning workflow summary

**Recommended cleaning order:**
1. Bandpass filter (20-250 Hz) - removes low/high frequency noise
2. Identify obviously bad channels (visual inspection)
3. Apply ASR with conservative parameters (BurstCriterion=20)
4. Visual inspection of cleaned data
5. Compute session quality metrics
6. Decide whether to keep or exclude session

**When to exclude entire sessions:**
- >30% of data removed by ASR
- >50% of channels removed
- Extreme amplitude artifacts persisting after cleaning
- Subject-level RMS >3 SD from mean

### Important notes

- **Clean BEFORE envelope**: Artifacts in filtered data will be preserved in the envelope
- **Conservative for EMG**: EMG has higher amplitudes than EEG, don't over-clean
- **Session-level decisions**: Some sessions may be too noisy to salvage
- **Document exclusions**: Keep track of which sessions/channels were excluded

## Computing the linear envelope (CRITICAL for EMG-ERP)

**Important:** Standard ERP analysis does NOT work well for raw EMG data. Here's why:

### Why raw EMG ERPs fail

EMG is a high-frequency oscillatory signal (20-250 Hz). When you average raw EMG epochs together:
- Positive phases of the oscillation cancel out negative phases
- Result: Weak, noisy ERPs that don't reflect true muscle activation
- The averaging destroys the amplitude information we care about

### Solution: The linear envelope

The **linear envelope** preserves amplitude information while removing the problematic oscillations:

1. **Rectification**: Take the absolute value (makes all values positive)
2. **Low-pass filtering**: Smooth the rectified signal (10-20 Hz)

```matlab
% Step 1: Rectify the filtered EMG
EEG.data = abs(EEG.data);

% Step 2: Low-pass filter to create envelope
envelope_cutoff = 20;  % Hz - 20 Hz provides faster response for typing tasks
EEG = pop_eegfiltnew(EEG, 'hicutoff', envelope_cutoff);

% Clip any negative values from zero-phase filtering
EEG.data(EEG.data < 0) = 0;

% Mark as envelope data
EEG.etc.is_envelope = true;
EEG.etc.envelope_cutoff = envelope_cutoff;
```

### Visualization: Linear envelope computation

![Envelope Computation](/assets/images/emg_envelope_computation.png)

This figure shows the four processing stages for two representative channels (left and right wristband). The red dashed line marks a keystroke event:

1. **Raw signal** (blue): Unfiltered EMG with baseline noise and drift
2. **Band-pass filter** (green): 20-250 Hz filtered EMG - removes low-frequency drift and high-frequency noise
3. **Rectified** (purple): Absolute value of filtered signal - all values positive
4. **Low-pass filter / linear envelope** (magenta): Smooth envelope (20 Hz cutoff) capturing muscle activation amplitude

![Why Envelope Needed](/assets/images/emg_envelope_needed.png)

This comparison demonstrates why the envelope is critical:
- **Top row**: Filtered EMG epochs and resulting ERP - oscillations cancel out during averaging
- **Middle row**: Envelope epochs and resulting ERP - clear event-related response
- **Bottom**: Direct comparison showing filtered EMG ERP (blue, noisy) vs envelope ERP (red, clear)

### Parameters for envelope computation

**Envelope low-pass cutoff frequency:**
- **5-10 Hz**: Maximum smoothing, for slow movements
- **20 Hz**: Standard for fast tasks like typing (recommended)
- **30-40 Hz**: Minimal smoothing, for very fast movements

For typing tasks, **20 Hz** is recommended as it provides faster response to capture rapid finger movements while still smoothing the high-frequency oscillations.

## Epoching EMG data

**Important**: Epoch the **envelope data**, not the raw filtered EMG!

Extract epochs around keystroke events:

```matlab
% Define epoch window
epoch_start = -0.5;  % seconds before keystroke
epoch_end = 1.0;     % seconds after keystroke

% Find keystroke events
keystroke_types = {};
for i = 1:length(EEG.event)
    if contains(EEG.event(i).type, 'keystroke_')
        keystroke_types{end+1} = EEG.event(i).type;
    end
end
unique_keystrokes = unique(keystroke_types);

% Extract epochs
EEG = pop_epoch(EEG, unique_keystrokes, [epoch_start epoch_end], 'epochinfo', 'yes');
```

### Baseline correction

Remove baseline to focus on event-related activity:

```matlab
% Define baseline window (avoid 100ms immediately before keystroke)
baseline_window = [-0.5, -0.1];  % seconds

% Remove baseline
EEG = pop_rmbase(EEG, baseline_window * 1000);  % Convert to ms
```

## Balancing trial counts for fair comparison

**Important:** When comparing ERPs across conditions, unequal trial counts can bias results due to different signal-to-noise ratios.

### Why trial balancing matters

In typing data, key occurrence varies dramatically:
- Common keys (e, t, a): 200-500 occurrences
- Rare keys (z, q, x): 5-20 occurrences

**Problems with unbalanced comparisons:**
- High-trial-count condition has better SNR (lower noise)
- Statistical comparisons are biased
- Visual differences may reflect SNR, not true effects

### Strategy 1: Select keys with similar counts

```matlab
% Count occurrences for each keystroke type
keystroke_counts = struct();

for i = 1:length(EEG.event)
    if contains(EEG.event(i).type, 'keystroke_')
        key_type = EEG.event(i).type;
        if ~isfield(keystroke_counts, key_type)
            keystroke_counts.(key_type) = 0;
        end
        keystroke_counts.(key_type) = keystroke_counts.(key_type) + 1;
    end
end

% Display sorted by count
key_names = fieldnames(keystroke_counts);
key_values = cellfun(@(x) keystroke_counts.(x), key_names);
[sorted_values, sort_idx] = sort(key_values, 'descend');

fprintf('Keystroke occurrence counts:\n');
for i = 1:length(key_names)
    fprintf('  %s: %d\n', key_names{sort_idx(i)}, sorted_values(i));
end

% Select keys with similar counts for comparison
% Example: Compare 'a' (left hand) vs 'k' (right hand)
% Only if they have similar trial counts (within 20%)
count_a = keystroke_counts.keystroke_a;
count_k = keystroke_counts.keystroke_k;

if abs(count_a - count_k) / mean([count_a, count_k]) < 0.2
    fprintf('\nKeys "a" and "k" have similar trial counts - good for comparison\n');
else
    fprintf('\nWarning: Keys "a" and "k" have different trial counts\n');
    fprintf('Consider subsampling the higher-count condition\n');
end
```

### Strategy 2: Subsample high-count condition

```matlab
% Match trial counts by random subsampling
% Example: Balance key 'e' (high count) with key 'x' (low count)

% Extract epochs
EEG_e = pop_epoch(EEG, {'keystroke_e'}, [epoch_start epoch_end]);
EEG_x = pop_epoch(EEG, {'keystroke_x'}, [epoch_start epoch_end]);

fprintf('Before balancing:\n');
fprintf('  Key "e": %d trials\n', EEG_e.trials);
fprintf('  Key "x": %d trials\n', EEG_x.trials);

% Determine minimum trial count
min_trials = min(EEG_e.trials, EEG_x.trials);

% Randomly select trials to match
if EEG_e.trials > min_trials
    % Subsample key 'e'
    rng(42);  % Set seed for reproducibility
    selected_trials = randperm(EEG_e.trials, min_trials);
    EEG_e = pop_select(EEG_e, 'trial', selected_trials);
end

if EEG_x.trials > min_trials
    % Subsample key 'x'
    rng(42);
    selected_trials = randperm(EEG_x.trials, min_trials);
    EEG_x = pop_select(EEG_x, 'trial', selected_trials);
end

fprintf('After balancing:\n');
fprintf('  Key "e": %d trials\n', EEG_e.trials);
fprintf('  Key "x": %d trials\n', EEG_x.trials);

% Now compute ERPs with equal SNR
ERP_e = mean(EEG_e.data, 3);
ERP_x = mean(EEG_x.data, 3);
```

### Strategy 3: Bootstrap confidence intervals

For unequal trial counts, use bootstrap to estimate uncertainty:

```matlab
% Compute ERP with confidence intervals using bootstrap
n_bootstrap = 1000;

% Example: Key 'a' with many trials
EEG_a = pop_epoch(EEG, {'keystroke_a'}, [epoch_start epoch_end]);
n_trials = EEG_a.trials;
n_timepoints = EEG_a.pnts;

% Select channel and initialize
chan_idx = 1;
bootstrap_erps = zeros(n_bootstrap, n_timepoints);

% Bootstrap resampling
rng(42);
for i = 1:n_bootstrap
    % Resample trials with replacement
    trial_indices = randi(n_trials, n_trials, 1);
    bootstrap_erps(i, :) = mean(squeeze(EEG_a.data(chan_idx, :, trial_indices)), 2);
end

% Compute mean and confidence intervals
erp_mean = mean(bootstrap_erps, 1);
erp_ci_lower = prctile(bootstrap_erps, 2.5, 1);  % 95% CI
erp_ci_upper = prctile(bootstrap_erps, 97.5, 1);

% Plot with confidence intervals
time_vec = EEG_a.times / 1000;
figure;
fill([time_vec, fliplr(time_vec)], ...
     [erp_ci_lower, fliplr(erp_ci_upper)], ...
     'b', 'FaceAlpha', 0.2, 'EdgeColor', 'none');
hold on;
plot(time_vec, erp_mean, 'b', 'LineWidth', 2);
plot([0, 0], ylim, 'r--', 'LineWidth', 1.5);
xlabel('Time (s)');
ylabel('Amplitude (\muV)');
title('ERP with 95% Bootstrap Confidence Intervals');
grid on;
```

### Recommendations

For ERP comparisons:

1. **Same-hand comparisons** (e.g., different fingers): Use keys with similar occurrence
   - Example: 'a', 'e', 't' all have high counts for left hand

2. **Left vs right hand**: Balance trial counts by subsampling
   - Example: Match 'a' (left) with 'k' (right) by subsampling

3. **Statistical testing**: Always report trial counts
   - Use bootstrap or permutation tests for significance
   - Account for unequal variance if trial counts differ

4. **Minimum trial count**: Aim for at least 30 trials per condition
   - Fewer trials = noisy ERPs
   - More trials = better SNR but diminishing returns beyond ~100

## Computing EMG-ERPs

EMG-ERPs are computed by averaging **envelope data** across trials:

```matlab
% Identify channel groups
% NOTE: Verified empirically - adjust based on your hardware setup
left_wristband = 1:16;    % LEFT hand (EMG0-EMG15)
right_wristband = 17:32;  % RIGHT hand (EMG16-EMG31)

% NOTE: EEG should contain envelope data from step 2b!
% Extract epochs for specific keys
EEG_a = pop_epoch(EEG, {'keystroke_a'}, [epoch_start epoch_end]);
EEG_a = pop_rmbase(EEG_a, baseline_window * 1000);

EEG_k = pop_epoch(EEG, {'keystroke_k'}, [epoch_start epoch_end]);
EEG_k = pop_rmbase(EEG_k, baseline_window * 1000);

% Compute ERPs from envelope (average across trials)
ERP_a_left = mean(EEG_a.data(left_wristband, :, :), 3);
ERP_k_right = mean(EEG_k.data(right_wristband, :, :), 3);
```

### Visualizing EMG-ERPs with EEGLAB

Use EEGLAB's ERP plotting functions to visualize event-related muscle activation:

**Option 1: Plot ERPs for all channels**

```matlab
% Use EEGLAB menu: Plot > Channel ERPs > In rectangular array
% Or from command line:
figure; pop_plottopo(EEG_a, [1:16], 'EMG-ERP for key "a" (left channels)', ...
    0, 'ydir', 1);
```

This displays ERPs for multiple channels in a grid layout, making it easy to compare activation patterns across the electrode array.

**Option 2: Plot average ERP with scalp maps** (less useful for EMG)

```matlab
% For EMG, we typically skip topographic maps since they don't represent brain activity
% Instead, plot channel ERPs directly:
figure; pop_plotdata(EEG_a, 1, [1:8], 'EMG-ERP: Selected Channels');
```

**Option 3: Overlay ERPs for specific channels**

```matlab
% Select representative left-hand channels
left_channels = [1 5 9 13];  % Sample across the array

% Use EEGLAB menu: Plot > Channel ERPs > With scalp maps
% Or plot selected channels:
figure; pop_plotdata(EEG_a, 1, left_channels, 'EMG-ERP: Left Hand Key "a"');
```

![EMG-ERP Lateralization](/assets/images/emg_erp_lateralization.png)

The figure below shows individual channel ERPs, allowing you to see the variability across electrodes on each wristband:

![Individual Channel ERPs](/assets/images/emg_all_channels.png)

**Important for EMG:**
- EEGLAB's topoplot (scalp maps) is NOT meaningful for EMG data
- Focus on channel ERPs and time-course plots
- Use `pop_plottopo()` without the topographic map option
- Compare ERPs across channels on the same limb

## Comparing conditions with EEGLAB

### Comparing multiple conditions

To compare ERPs across different conditions (e.g., different keys or hands), use EEGLAB's comparison tools:

**Method 1: Overlay plots for selected channels**

```matlab
% Compare key 'a' (left hand) vs key 'k' (right hand) for specific channels
% Use EEGLAB menu: Plot > Channel ERPs > With scalp maps
% Then select specific channels and conditions

% Or from command line:
% First, select left-hand channels for key 'a'
figure; pop_plotdata(EEG_a, 1, [1 5 9], 'Key "a" - Left hand channels');

% Then, select right-hand channels for key 'k'
figure; pop_plotdata(EEG_k, 1, [17 21 25], 'Key "k" - Right hand channels');
```

**Method 2: Compare using EEGLAB's STUDY framework**

For systematic comparison across multiple subjects or conditions:

```matlab
% Create a STUDY structure with multiple datasets
% Use EEGLAB menu: File > Create study > Browse for datasets
% Then use: Study > Precompute channel measures
% Finally: Study > Plot channel measures

% This allows statistical comparison across conditions
```

**Expected patterns:**
- **Contralateral dominance**: Stronger activation in the hand performing the keystroke
- **Timing differences**: Peak latency may differ between hands
- **Amplitude differences**: May vary based on finger position and force

## Complete pipeline script

A complete pipeline for EMG-ERP analysis is available in the [EMG-2-BIDS repository](https://github.com/sccn/EMG-2-BIDS). The pipeline includes:

1. **step1_load_bids_data.m** - Import BIDS-formatted EMG data (includes sanity checks: raw data plots, events, PSD)
2. **step2_preprocess_emg.m** - Bandpass filter (20-250 Hz) and check channel quality
3. **step2a_clean_data.m** - Clean data with ASR and remove bad channels/segments (optional but recommended)
4. **step2b_compute_envelope.m** - Compute linear envelope (CRITICAL: rectify + 20 Hz low-pass)
5. **step3_epoch_and_select.m** - Extract epochs using burst-initial keystrokes (keystrokes after 500ms pause)
6. **step4_compute_erp.m** - Compute and visualize EMG-ERPs with lateralization analysis

Run the complete pipeline:

```matlab
% Add EEGLAB to path
addpath('/path/to/eeglab');
eeglab nogui;

% Navigate to tutorial scripts
cd /path/to/EMG-2-BIDS/tutorial_scripts

% Run all steps
run_all_steps
```

**Critical steps:**
- **step2a_clean_data.m**: Remove artifacts and bad segments (highly recommended for noisy sessions)
- **step2b_compute_envelope.m**: Creates the linear envelope needed for meaningful EMG-ERP analysis

**Recommended workflow:**
```
Load → Sanity Checks → Filter (20-250 Hz) → Clean (ASR) → Envelope (20 Hz) → Epoch (burst-initial) → ERP
```

**Note on epoching**: For rapid typing data (~5 keystrokes/second), standard epochs overlap heavily. Using "burst-initial" keystrokes (those preceded by >500ms pause) provides cleaner baselines and clearer ERPs.

## Key differences: EMG vs EEG

| Aspect | EEG | EMG |
|--------|-----|-----|
| **Frequency range** | 1-50 Hz | 20-450 Hz |
| **Amplitude** | Microvolts | Microvolts to millivolts |
| **Spatial resolution** | Brain regions | Specific muscles |
| **Common artifacts** | Eye blinks, muscle tension | Motion, electrode displacement |
| **Baseline** | Pre-stimulus period | Pre-movement period |
| **ERP computation** | Direct averaging works | Requires linear envelope first! |
| **Summary measures** | ERP amplitude/latency | RMS, integrated EMG, envelope amplitude |

## Tips for EMG-ERP analysis with EEGLAB

1. **ALWAYS use the linear envelope**: Direct averaging of raw EMG does not work! Rectify and low-pass filter (~20 Hz for typing) before epoching and averaging.

2. **Use EEGLAB visualization tools**:
   - `pop_eegplot()` for scrolling raw data inspection
   - `pop_spectopo()` for frequency analysis (extend range to 500 Hz for EMG)
   - `pop_plottopo()` or `pop_plotdata()` for ERP visualization
   - Avoid EEGLAB's topographic maps (topoplot) - not meaningful for EMG

3. **Choose appropriate filters**: Use higher cutoff frequencies than EEG (20-250 Hz for motor tasks) via `pop_eegfiltnew()`.

4. **Baseline correction is critical**: Use `pop_rmbase()` to remove pre-event baseline. The envelope should have near-zero baseline.

5. **Sanity checks with EEGLAB**:
   - Plot raw data with `pop_eegplot(EEG, 1, 1, 1)`
   - Check PSD with `pop_spectopo()` - verify power in 20-250 Hz
   - Inspect events via menu: Edit > Event values

6. **Account for trial count**: More trials = better SNR. Use `pop_epoch()` and check `.trials` field. Balance conditions using `pop_select()`.

7. **Check lateralization**: Expect stronger activation in the hand performing the movement.

8. **Visualize individual trials**: Use `pop_eegplot(EEG_epoched, 0, 1, 1)` to inspect trial-by-trial variability.

9. **For multi-subject analysis**: Use EEGLAB's STUDY framework (menu: File > Create study) for group-level statistics.

10. **Compare envelope parameters**: If ERPs look noisy, try adjusting the envelope cutoff (5-20 Hz) and re-epoch.

## Additional resources

- **Dataset**: [emg2qwerty on NEMAR](https://nemar.org/dataexplorer/detail?dataset_id=nm000104)
- **Paper**: [emg2qwerty at NeurIPS 2024](https://arxiv.org/abs/2410.20081)
- **Code repository**: [EMG-2-BIDS on GitHub](https://github.com/sccn/EMG-2-BIDS)
- **BIDS-EMG specification**: [BIDS EEG/EMG](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/03-electroencephalography.html)

## Related tutorials

- [EEGLAB and MEG data](EEGLAB_and_MEG_data.html)
- [Automated processing pipelines](../11_Scripting/automated_pipeline.html)
- [Analyzing EEG BIDS data in EEGLAB](../11_Scripting/Analyzing_EEG_BIDS_data_in_EEGLAB.html)
