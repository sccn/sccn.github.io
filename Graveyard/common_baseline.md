---
layout: default
---
Common baseline across ERSP condition
=========

When computing event-related spectral power (ERSP)
transforms for sets of data epochs from two or more experimental
conditions, the user may want to subtract the same (log) power baselinevector from all conditions. Both the [pop_newtimef.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_newtimef.m) function
and the [newtimef.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=newtimef.m) function it calls return spectral baseline

values that can be used in subsequent ''newtimef() '' computations. For
instance, assuming that three sets of data epochs from three
experimental conditions have been stored for 10 subjects in EEGLAB
dataset files named *subj\[1:10\]data\[1:3\].set* in directory
*/home/user/eeglab*, and that the three datasets for each subject
contain the same ICA weights, the following MATLAB code would plot the
ICA component-1 ERSPs for the three conditions using a common spectral
baseline for each of the 10 subjects:

``` matlab
eeglab; % Start eeglab
Ns = 10; Nc = 3; % Ns - number of subjects; Nc - Number of conditions;'
for S = 1:Ns  % For each of the subjects
    mean_powbase = []; % Initialize the baseline spectra average over all conditions for each subject
    for s =1:Nc  % Read in existing EEGLAB datasets for all three conditions
        setname = ['subj' int2str(S) 'data' int2str(s) '.set'];  % Build dataset name
        EEG = pop_loadset(setname,'/home/user/eeglab/'); % Load the dataset
        [ALLEEG EEG] = eeg_store(ALLEEG, EEG, Nc*(S-1) + s);  % Store the dataset in ALLEEG
        [ersp,itc,powbase{s}] =pop_timef( ALLEEG(s),0, 1, [-100 600], 0, 'plotitc', 'off', 'plotersp', 'off' );
        % Run simple newtimef() for each dataset, No figure is created because of options 'plotitc', 'off', 'plotersp', 'off'
        mean_powbase = [mean_powbase; powbase{s}];  % Note: curly braces
    end % condition
    % Below, average the baseline spectra from all conditions
    mean_powbase = mean(mean_powbase, 1);

    % Now recompute and plot the ERSP transforms using the same baseline
    figure;  % Create a new figure (optional figure('visible', 'off'); would create an invisible figure)
    for s = 1:Nc; % For each of the three conditions
        sbplot(1,3,s); % Select a plotting region
        pop_newtimef( ALLEEG(s), 0, 1, [-100 600], 0, 'powbase', mean_powbase, ...
        title', ['Subject ' int2str(S)]); % Compute ERSP using mean_powbase''
    end % End condition plot
    plotname = ['subj' int2str(S) 'ersp' ];  % Build plot name
    eval(['print -depsc ' plotname]); % Save plot as a color .eps (postcript) vector file
end % End subject
eeglab redraw  % Update the main EEGLAB window
```

Repetitive processes, such as the computation performed above, may be
time consuming to perform by hand if there are many epochs in each
dataset and many datasets. Therefore it may be best performed by an
EEGLAB MATLAB script that is left to run until finished in a MATLAB
session. Writing scripts using EEGLAB functions makes keeping track of
data parameters and events relatively easy, while maintaining access to
the flexibility and power of the MATLAB signal processing and graphics
environment.

<u>Notes: </u>

-   Normally, the user might want to accumulate and save the ERSPs and
    other output variables returned by *newtimef.m* above to make possible
    further quantitative comparisons between subjects.

-   In the current version of EEGLAB, the cross-coherence function {
    {File\|crossf.m} } can calculate significance of differences between
    coherences in two conditions.-   In the future, [newtimef.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=newtimef.m) will be extended to allow

    comparisons between multiple ERSP and ITC transforms directly.
-   The same type of iterative normalization (illustrated above) may be
    applied for the "baseamp" parameter returned by {
    {File\|pop_erpimage.m} }