---
layout: default
title: Analyzing EEG data in EEGLAB The Wakeman-Henson dataset
permalink: /docs/Analyzing_EEG_data_in_EEGLAB_The_Wakeman-Henson_dataset
parent: Docs
---

[right|830px](/Image:RMC_SfN_poster_2018_2print.jpg "wikilink")

## Analyzing EEG data with EEGLAB: The Wakeman-Henson dataset

EEGLAB (sccn.ucsd.edu/eeglab) is a rich, easily extensible, and growing
open source signal processing environment for electrophysiological
signal processing running on MATLAB (Mathworks, Natick MA). The EEGLAB
architecture makes it suited to data exploration and visualization as
well as to applying customized analysis including general linear model
statistics. EEGLAB evolved from a set of Matlab functions for
decomposing electroencephalographic (EEG) data using independent
component analysis (ICA) and performing time/frequency analysis,
focusing on the dynamics of effective source processes revealed by ICA
decomposition, both in event-related averages and across sorted
collections of single trials. EEGLAB (sccn.ucsd.edu/eeglab) features a
root EEG data structure and a main graphic user interface (GUI) menu
calling pop_ functions that first prompt users to enter necessary
arguments, then call relevant signal processing and plotting functions.
User interface command history allows users to easily replicate or
enrich a series of actions they performed first using the EEGLAB menu,
thereby easing the process of learning to code standard or custom
analysis pipelines. Calling links to EEGLAB plug-in extensions
downloaded from the EEGLAB Extension Manager appear in the user’s menu.
More than 75 extensions from many laboratories offer tools to apply a
wide and growing range of signal processing approaches. Here we
demonstrate results of some basic EEGLAB methods focusing on ICA
decompositions of EEG data made available by Wakeman & Henson
(https://openfmri.org/dataset/ds000117/) and study the dynamics of the
resulting effective brain sources following face image presentations and
ensuing motor responses.

### The Wakeman-Henson dataset

Human perception of suddenly presented face images produces a large
negative peak near 170 ms (dubbed ‘the N170’) in averaged event-related
potentials (ERPs) for posterior scalp channels [Bentin et
al., 1996](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2927138/). This
potential has been localized by several methods, including direct
electrocorticographic (ECoG) recording from the cortical surface, to the
bilateral fusiform gyrus. Henson and Wakeman (2015) apply joint EEG/MEG
source analysis to the N170 peak scalp maps to estimate the areas of
inferior temporal cortex that produce the response feature. A BOLD
signal increase in the same areas is seen in fMRI studies ([Kanwisher et
al., 1997](https://www.ncbi.nlm.nih.gov/pubmed/9151747)). A long train
of functional imaging and EEG experiments have considered the question
of whether activation of fusiform gyrus by face image presentations
indexes face-specific processing ([Kanwisher &
Yovel, 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1857737/)) or
processing supporting more general expert identification of individuals
or subcategories for any large set of important and long-studied objects
-- for example, automobile grilles by automobile experts ([Gauthier et
al., 1999](https://www.ncbi.nlm.nih.gov/pubmed/10448223)). Generally,
face presentations produce much larger ‘N170’ potentials (and ensuing
fusiform BOLD activations) than do presentations of ‘face-like’ images
of houses, etc. Wakeman and Henson (2015) developed the paradigm used to
collect the data treated here to determine how repetition (of the same
face image) in a series of tachistoscopically presented ‘face versus
house’ images experiment affected EEG and concurrent MEG responses, and
how responses to well-known, unknown, and scrambled faces in the same
sequence differed. See details of the paradigm in the figure below.

[`center|400px`](/Image:Wakeman_henson_eegset.jpg "wikilink")

## Data processing

### Raw data importation

The data was first imported using *FileIO* plugin for EEGLAB. Then, EEG
and event channel (STI101) were selected. Location of the fiducials were
added to the channel location and the montage was rotated to match
EEGLAB format. Events from the STI101 event channel were imported
events. Then we imported the information about the image presented into
the event structure as well as button presses. Numerical events were
renamed to more meaningful text labels. We then corrected event
latencies which were shitted by 34 ms. Finally, we merged the 6 session
file for each subject and saved the preprocessed data. This the code for
this processing can be accessed at
(https://bitbucket.org/sccn_eeglab/wh_eeglabcodes/src/master/wh_extracteeg.m)

### Downsample the data

The sampling rate of the recording was 1100 Hz per channel. Because
local field potential signals from cortex have a near-1/f power spectral
density, most EEG data variance is contained in lower frequencies. To
reduce data size and processing time, we chose to reduce the data
sampling rate to 500 Hz per channel. This process applied an
anti-aliasing filter below the Nyquist frequency (250 Hz) using a cutoff
frequency 500/2 x 0.9 = 225 Hz (-6dB) with transition bandwidth 500/2 x
0.2 = 50 Hz (Kaiser window, scalar maximum passband deviation 0.002). As
a result, the spectrum of the recorded signals could be analyzed to near
250 Hz. EEGLAB sample code:

``` matlab
EEG = pop_resample(EEG, 500);
```

### High-pass filter the data

To remove DC and infra-low frequency drifts, and to center the
time-series data around zero, a high-pass filter with (-6 dB) cutoff
frequency 1 Hz was applied (FIR, Hamming windowed; transition bandwidth,
1 Hz; filter order, 1650). Another important purpose of this high-pass
filter is to improve ICA results, as our experience and a recent report
have shown that removing near-DC portions of the EEG data improves ICA
performance [Winkler et
al., 2015](https://www.ncbi.nlm.nih.gov/pubmed/26737196). In particular,
the number of ICs with brain-localizable component scalp maps (e.g.,
strongly resembling the ‘dipolar’ projection of potential coherent
across a single, locally coherent cortical patch) is larger when low
frequencies are omitted from the data to be decomposed. We believe this
to be in part because large, low-frequency drifts can arise from scalp
temperature shifts, etc. that are not spatially stationary, in contrast
to the ICA source model.

``` matlab
EEG = pop_eegfiltnew(EEG, 1,   0,   1650, 0, [], 0);  % High pass at 1Hz
```

### Remove line noise

We first used the EEGLAB plug-in CleanLine to adaptively estimate and
remove line-frequency artifacts using frequency-domain (multi-taper)
regression. However, in these data the amplitude of the line artifact
(at 50 Hz and its harmonics) proved to be so large (approaching 40 dB)
that went on to apply notch filters at the line frequency and its
harmonics (e.g., centered at 50 Hz, 100 Hz, 150 Hz, and 200 Hz) to make
visible the brain source phenomena of interest.

``` matlab
EEG = pop_eegfiltnew(EEG, 49,  51,  1650, 1, [], 0);  % Line noise suppression ~50Hz
EEG = pop_eegfiltnew(EEG, 99,  101, 1650, 1, [], 0);  % Line noise suppression ~100Hz
EEG = pop_eegfiltnew(EEG, 149, 151, 1650, 1, [], 0);  % Line noise suppression ~150Hz
EEG = pop_eegfiltnew(EEG, 199, 201, 1650, 1, [], 0);  % Line noise suppression ~200Hz
```

### Detect and reject bad channels

Here, we first performed outlier channel detection and, rejection, and
interpolation using the clean_rawdata plug-in of Christian Kothe. This
plug-in calculates each scalp channel signal’s correlation to its random
sample consensus (RANSAC) estimate computed from nearby scalp channel
signals in successive 5-s segments. Channel signals exhibiting low
correlation to signals in neighboring scalp channels in individual
windows (here, r \< 0.8 at more than 40% of the data points) were
rejected.

``` matlab
EEG = clean_rawdata(EEG, -1, -1, 0.80, -1, -1, -1);
```

### Re-reference the scalp-channel data to average reference

We performed common average reference (CAR). We first interpolated all
the rejected channels in the dataset. These channels were obtained by
comparing the current channels on the current EEG structure with the
backup of the original channels in the same structure (EEG.urchanlocs).
Then, CAR was performed and the interpolated channels were removed. This
processing was all performed with the function *pop_reref.m*.

``` matlab
EEG = pop_reref(EEG,[],'interpchan',[]);
```

### Extract data epochs

For experimental events of interest in three categories, i.e.,
presentations of Famous (*famous_new, famous_second_early,
famous_second_late*), Unfamiliar (*unfamiliar_new,
unfamiliar_second_early, unfamiliar_second_late*), and Scrambled
(*scrambled_new, scrambled_second_early, scrambled_second_late*)
faces, respectively, data epochs extending from -1 s to 2 s relative to
these event markers were extracted from the data and stored.

``` matlab
 EEG = pop_epoch( EEG, {'famous_new' 'famous_second_early' 'famous_second_late' ...
                        'scrambled_new' 'scrambled_second_early' 'scrambled_second_late'...
                        'unfamiliar_new' 'unfamiliar_second_early' 'unfamiliar_second_late'},...
                        [-1  2], 'newname', 'Epoched', 'epochinfo', 'yes');;
```

### Rejecting noisy epochs

We then performed two-stage rejection of noisy event-related data
epochs. In the first stage, we rejected epochs in which any channel
value exceeded a two-sided rejection amplitude threshold (±400 uV). Then
a joint probability test (shown to be more effective than the simple
thresholding) was performed using ±4-SD single-channel and ±3-SD
global-channel thresholds ([Delorme et
al., 2007](https://www.ncbi.nlm.nih.gov/pubmed/17188898)). Data epochs
containing channel data exceeding either threshold were rejected.

``` matlab
[EEG, rejindx] = pop_eegthresh(EEG, 1, 1:EEG.nbchan, -400, 400, EEG.xmin, EEG.xmax, 0, 1);
EEG = pop_jointprob(EEG, 1, 1:EEG.nbchan, 4, 3, 1, 1);
```

### Perform ICA decomposition

Next we performed ICA decomposition using adaptive mixture ICA (AMICA)
(Palmer et al., 2007) of the retained data. During the first 5 training
iterations, optional further data point rejection (based on data
(un)likelihood under the evolving AMICA model) was performed using a
rejection threshold of ±3 SD. This rejected approximately 10% of the
data points, focusing the ICA unmixing on defining maximally independent
processes in the clean data. Here we chose to use AMICA
(https://github.com/japalmer29/amica) for the decomposition as we found
AMICA to produce the most temporally independent and more
physiologically plausible components than any of 21 other ICA and
ICA-like linear data separation approaches (Delorme et al., 2012). In
that study, the second most effective ICA approach was Infomax and
Extended Infomax (Bell & Sejnowksi, 1995; Lee et al., 1997), the default
ICA decomposition approach (runica) for which very fast GPU-enabled
versions, beamica (Christian Kothe) and cudaica ([Raimondo et
al,. 2012](https://www.hindawi.com/journals/cin/2012/206972/)),
respectively, are also available as EEGLAB plug-ins.

``` matlab
EEG = pop_runamica(EEG,'numprocs',4, 'do_reject', 1, 'numrej', 5, 'rejint', 4,'rejsig', 3,'rejstart', 1, 'pcakeep',EEG.nbchan-1); % Computing ICA with AMICA
```

Alternatively, the default ICA decomposition approach (runica) can be
used as follows:

``` matlab
EEG = pop_runica(EEG, 'pca', EEG.nbchan-1); % Computing ICA with Infomax
```

### Select independent components

We selected a subset of the ICs for further processing and analysis as
not all of them accounted for brain activity relevant to the focus of
our analysis. IC selection was performed based on characteristic
features of “brain components” including a dipolar scalp topography and
existence of one or more peaks in the power spectrum between 5 Hz and 30
Hz.

### Fit equivalent current dipole models

After co-registering all channel locations to the MNI head model,
equivalent current dipoles were fit to localize source locations using
the dipfit extension implemented in EEGLAB. A single dipole was fit
first using a Boundary Element Model (BEM) template head model (MNI). IC
candidates for subsequent fitting dual-symmetric equivalent dipoles were
selected by visual inspection of the IC scalp topographies. The
dual-symmetric equivalent dipole model constrained the positions (but
not the orientations) of the two-dipole model to be bilaterally
symmetric, to account for ICs whose scalp topography learned from the
data clearly reflects separable dipolar projections to the two
hemispheres. Dual-symmetric ICs might arise to account for synchronous
activity that is resonant in two coupled cortical source patches densely
and bidirectionally connected by the corpus callosum. For candidate ICs
in which the dual-symmetric equivalent dipole model collapsed to a
single medial equivalent dipole, the unconstrained single equivalent
dipole model was used in further analyses.

``` matlab
dipfitpath = fileparts(which('pop_multifit'));
electemplatepath = fullfile(dipfitpath,'standard_BEM/elec/standard_1005.elc');
[~,coord_transform] = coregister(EEG.chaninfo.nodatchans, electemplatepath, 'warp', 'auto', 'manual', 'off');
EEG = pop_dipfit_settings( EEG, 'hdmfile', fullfile(dipfitpath,'standard_BEM/standard_vol.mat'),...
                                'coordformat', 'MNI', 'chanfile', electemplatepath,'coord_transform', coord_transform,...
                                'mrifile', fullfile(dipfitpath,'standard_BEM/standard_mri.mat'));
EEG = pop_multifit(EEG, 1:EEG.nbchan,'threshold', 100, 'dipplot','off','plotopt',{'normlen' 'on'});
```

The following sample code referer to computing dual dipoles. For this,
the indices of the components fitting dual-symmetric equivalent dipoles
were selected by visual inspection and stored in the variable *matchic*.

``` matlab
EEG = pop_multifit(EEG, matchic, 'threshold', 100, 'dipoles', 2, 'plotopt', {'normlen' 'on'});
```

After this, the data can be saved by using the EEGLAB function
*pop_saveset.m*.

EEGLAB sample code (e.g., for subject 11):

``` matlab
EEG = pop_saveset( EEG, 'filename', subj11_proc.set', 'filepath', path2save); % path2save is variable with the path to save the data
```

## Single subject analysis

To illustrate the process of exploring event-related brain dynamics in
data from hitherto unexplored paradigms, we begin by visualizing
source-resolved EEG dynamics in data from one participant (S11) whose
decomposition produced unusually many well localizable brain source IC
processes. The scripts for the generation of the visualization showed
here can be accessed at
<https://bitbucket.org/sccn_eeglab/wh_eeglabcodes/src/master/figures_code/>,
specifically the script *s11_figures_masterscrip.m*.

### Visualizing IC brain sources

The figure below shows the scalp maps for the 35 IC processes that
contributed most variance to the scalp EEG data of participant S11, plus
the residual variance of their scalp maps not explained by the indicated
cortical source model involving either a single equivalent dipole or two
equivalent dipoles constrained to have bilaterally symmetric positions
(though not orientations) (e.g., ICs 6, 7, 8, 10, 24, 31). By their
scalp maps and properties, we can recognize IC1 as accounting for
potential fluctuations arising from eye blinks, 15 ICs (3, 9, 12-15,
20-22, 25, 28, 29 32, 34, 35) accounting for EMG activities of distinct
scalp muscles, and at least 17 ICs ( 3, 4, 6, 7, 8, 10, 11, 17-19, 23,
24, 27, 30, 31, 33, 34) highly compatible with a cortical brain source
consisting of one or of two (bilateral) cortical patches, respectively
(range of residual IC scalp map variances unaccounted for by the
indicated equivalent dipole models, 0.9% - 4.6%).

[center|600px](/Image:Subject_11_ALL_Figures_Figure_1.jpg "wikilink")

``` matlab
pop_topoplot(EEG,0, [1:35] ,' ',[5 7] ,1,'electrodes','on', 'style','both','dipnormmax','on');1);
```

### IC time courses on *eegplot*

The figure below shows the activation time courses of ICs 1-31 in two
consecutive event-related trial epochs time locked to successive face
stimulus presentations (each trace normed to equal variance). (EEGLAB
function, eegplot())

[center|600px](/Image:Subject_11_ALL_Figures_Figure_2.jpg "wikilink")

``` matlab
 EEG.icaact = eeg_getdatact(EEG);
eegplot(reshape(EEG.icaact(opt.icoi(1:31),:,:),[length(opt.icoi(1:31)) size(EEG.data,2) size(EEG.data,3)]),...
                'srate', EEG.srate,...
                'winlength',2,...
                'events',EEG.event);
```

### Envtopo plots

Envelope (envtopo) plot superimposing the envelopes (colored trace
pairs) of the portions of the (all scalp channels) ERP accounted for by
the six IC processes contributing most strongly to the trial-averaged
ERP to Familiar Face presentation for participant S11. The black trace
pair again shows the envelope of the cleaned scalp-channel ERP. The
colored trace pairs show the envelopes of the component projections. The
gray shaded area in the figure in the bottom is bounded by the envelope
of the summed projections of all 6 ICs. Note the dominance of IC6 and
IC10 in accounting for the ‘N170’ negative-going activation (near 0.18
s) and the dominance of IC8 and IC19 for the positive-going activation
(near 130ms).

[center|700px](/Image:Subject_11_ALL_Figures_Figure_4.jpg "wikilink")

### Plotting dipoles in head model

EEGLAB equivalent-dipole position browser showing symmetrical
dual-dipole models for right-dominant effective source IC6 and
left-dominant effective source IC10. The dominant source dipole for IC6
(green, right) is in right fusiform gyrus as indicated by an online
Talairach atlas given the Talairach XYZ coordinates. The dominant source
equivalent dipole for (red, left) IC10 is a few mm above left fusiform
gyrus (Talairach coordinates not shown). The residual variance (RV) in
the IC5 scalp map not accounted for by the projection of the
dual-symmetric equivalent dipole model is only 1.6% across all scalp
channels. (EEGLAB functions, dipfit() and dipplot()). Because of
individual differences in head shape, cortical surface physiognomy, and
skull conductivity, we cannot expect mm-scale accuracy in dipole
localization to a Talairach atlas.

[center|400px](/Image:Subject_11_ALL_Figures_Figure_5.jpg "wikilink")

### ERP Image plots

To explore the consistency of the N170 ERP feature, we plotted several
ERP-images of the trial-by-trial IC6 activation differences for epochs
time-locked to familiar face presentations. The ERP-image plot in the
figure below shows the trials sorted by time-on-task (i.e., in their
original recording order, here plotted bottom to top). The N170
phenomenon dominates the ERP of this IC process and does not exhibit any
clear change in amplitude or peak latency over time on task (i.e., from
first to last trials), although at about trial 50 the duration of the
negativity does appear to increase. For clearer visualization of trends,
the ERP-images in the figure are smoothed vertically by averaging across
a 10-trial moving window. Three lower traces in the panel A show
(topmost) the mean ERP time course, (middle) latency-varying mean power
at the strongest alpha-band peak in the power spectrum of activity in
these trials (near 9.3 Hz, see spectrum in upper inset), and
(bottommost) latency-varying intertrial phase coherence (ITC) at the
same frequency. Blue shaded areas indicate preliminary significance
boundaries (here p\<0.01, estimated non-parametrically without
correction for multiple comparisons). Note (middle trace) the decline in
mean alpha power following the N170 feature, and the strong ITC value
(maximum ITC is 1) during the N170 latency interval, reflecting a very
consistent tendency for a negative-going activation to appear in this
latency range. In the panel B top, the same trial epochs are sorted by
their mean activation value in the \[146 260\] msec latency window. This
plot shows there was actually some large trial-to-trial variability in
the amplitude of the N170 evoked response feature across single trials.
Note that the single-trial activation data in both panels are always the
same, merely presented (and somewhat smoothed) in differing trial orders
according to various sorting variables. Panel B middle shows the same
trial data effectively sorted by the latency of the N170 peak (here
estimated using the local phase of the single-trial data at the dominant
alpha frequency). Though this was not apparent in the earlier ERP-image
plots (and certainly not in the ERP itself), the peak latency of the
N170 response by this source process varied across trials. In the mean
ERP (upper trace below the ERP-image), the N170 is widened by averaging
across trials in which the response has widely varying response
latencies. In panel B bottom, the same trials are time-aligned to the
most negative-valued latency in the (wider) N170 latency range. The
trial order is the same as in panel B bottom. Note that ERP now exhibits
the true mean width of the N170 deflection. (Note: This plot could not
be produced from the pop_erpimage() gui, but required a command line
call to enter the separately computed N170 peak latencies as the
trial-sorting value).

[center|600px](/Image:Subject_11_ALL_Figures_Figure_6.jpg "wikilink")

## Multiple subjects analysis: STUDY

In this section, we explain the group level analysis performed and shown
some results obtained. The script for processing performed here can be
accessed at
<https://bitbucket.org/sccn_eeglab/wh_eeglabcodes/src/master/wh_study.m>

### Creating the STUDY

The datasets of the 18 subject preprocessed were loaded into EEGLAB and
a STUDY was created. In the example here we used a programmatic way to
generate the STUDY from the command line of MATLAB. For this (see code
below), we first generate a set of commands to be passed to EEGLAB which
will basically tell EEGLAB: Load the set in
*fullfile(path2data,datInfo(i).name, \[datInfo(i).name '_proc.set'\])*,
assign to it a number (counter), a short name (\['subj00' num2str(i)\]),
a group and session (here the same for all subjects) as well as define
that only dipoles located inside the brain and with residual variance
lower than 0.15 must be selected for further processing.

``` matlab
commands = {}; counter = 1;
for i = 2:length(datInfo)
    commands{counter}   = {'index' counter...
                           'load' fullfile(path2data,datInfo(i).name, [datInfo(i).name '_proc.set'])...
                           'subject' ['subj00' num2str(i)]...
                           'group' '1'...
                           'session' 1 ...
                           'inbrain' 'on'...
                           'dipselect' 0.15};
    counter = counter + 1;
end
```

In the sample code above, a structure (datInfo) was previously created
for the easy handling of the examples as well to ensure reproducibility
in the teaching process. This structure contains the following fields

``` matlab
datInfo =

  1×19 struct array with fields:

    name
    event256
    event4096
    edgelenval
    twoDipoleList
    fid
    bad_channels
    bad_regions
    bad_epochs
    bad_comps
    twoDipoleIC
```

After generating the *commands* we can proceed to create the STUDY. For
this, the sample code below can be used. Here, the STUDY is first
generated by using the function *std_editset*. Then the consistency of
the STUDY can be check with the function *std_checkset* before being
saved with *pop_savestudy*.

``` matlab
% Creating the STUDY
[STUDY ALLEEG] = std_editset([], [], 'name','henson_study',...
                                             'task','ScrambledVsNormalFace',...
                                             'commands',commands,...
                                             'updatedat','off',...
                                             'savedat','on',...
                                             'rmclust','on' );

[STUDY ALLEEG] = std_checkset(STUDY, ALLEEG); % Checking all is fine in the STUDY
CURRENTSTUDY   = 1; EEG = ALLEEG; CURRENTSET = [1:length(EEG)];

% Saving the STUDY
[STUDY EEG] = pop_savestudy( STUDY, EEG, 'filename',[studyname '.study'],...
                                         'filepath',studyfolderpath);
```

### Create a statistical design

Here the statistical design is implemented. In this case, the three type
of presentations for each type of stimulus were concatenated, so we can
deal with the marginalized version of the stimulus: Familiar(famous),
unfamiliar and scrambled faces.

``` matlab
STUDY       = std_makedesign(STUDY, ALLEEG, 1, 'name','STUDY.design 1',...
                                               'delfiles','off',...
                                               'defaultdesign','off',...
                                               'variable1','type',...
                                               'values1',{ {'famous_new' 'famous_second_early' 'famous_second_late'}...
                                                          {'scrambled_new' 'scrambled_second_early' 'scrambled_second_late'}...
                                                          {'unfamiliar_new' 'unfamiliar_second_early' 'unfamiliar_second_late'} },...
                                               'vartype1','categorical',...
                                               'subjselect',{'subj0010' 'subj0011' 'subj0012' 'subj0013' 'subj0014' 'subj0015'...
                                                             'subj0016' 'subj0017' 'subj0018' 'subj0019' 'subj002' 'subj003'...
                                                             'subj004' 'subj005' 'subj006' 'subj007' 'subj008' 'subj009'}...
                                                );
```

### Generating measures

Before plotting the component measures, you must precompute them. In the
example presented here we did so by using the function std_precomp from
MATLAB's command line. However, this can also be done from the GUI.
Also, teh same procces can be done for channel measures if you are
interested on it (see std_precomp.m help).

``` matlab
[STUDY ALLEEG]  = std_precomp(STUDY, ALLEEG, 'components','savetrials','on','recompute','on','erp','on','scalp','on','erpparams',{'rmbase' [-100 0]});
```

### Clustering components

#### Why cluster? ([from EEGLAB wiki](https://sccn.ucsd.edu/wiki/Chapter_05:_Component_Clustering_Tools))

<u>Is my Cz your Cz?</u> To compare electrophysiological results across
subjects, the usual practice of most researchers has been to identify
scalp channels (for instance, considering recorded channel "Cz" in every
subject's data to be spatially equivalent). Actually, this is an
idealization, since the spatial relationship of any physical electrode
site (for instance, Cz, the vertex in the International 10-20 System
electrode labeling convention) to the underlying cortical areas that
generate the activities summed by the (Cz) channel may be rather
different in different subjects, depending on the physical locations,
extents, and particularly the orientations of the cortical source areas,
both in relation to the 'active' electrode site (e.g., Cz) and/or to its
recorded reference channel (for example, the nose, right mastoid, or
other site).

That is, data recorded from equivalent channel locations (Cz) in
different subjects may sum activity of different mixtures of underlying
cortical EEG sources, no matter how accurately the equivalent electrode
locations were measured on the scalp. This fact is commonly ignored in
EEG research.

<u>Is my IC your IC?</u> Following ICA (or other linear) decomposition,
however, there is no natural and easy way to identify a component from
one subject with one (or more) component(s) from another subject. A pair
of independent components (ICs) from two subjects might resemble and/or
differ from each other in many ways and to different degrees -- by
differences in their scalp maps, power spectra, ERPs, ERSPs, ITCs, or
etc. Thus, there are many possible (distance) measures of similarity,
and many different ways of combining activity measures into a global
distance measure to estimate component pair similarity.

Thus, the problem of identifying equivalent components across subjects
is non-trivial. An attempt at doing this for 31-channel data was
published in [2002](http://sccn.ucsd.edu/science2002.html) and
[2004](http://sccn.ucsd.edu/papers/PLOS04_animation.html) in papers
whose preparation required elaborate custom scripting (by Westerfield,
Makeig, and Delorme). A
[2005](http://sccn.ucsd.edu/papers/OntonTheta05.html) paper by Onton et
al. reported on dynamics of a frontal midline component cluster
identified in 71-channel data. EEGLAB now contains functions and
supporting structures for flexibly and efficiently performing and
evaluating component clustering across subjects and conditions. With its
supporting data structures and stand-alone **'std_**' prefix analysis
functions, EEGLAB makes it possible to summarize results of ICA-based
analysis across more than one condition from a large number of subjects.
This should make more routine use of linear decomposition and ICA
possible to apply to a wide variety of hypothesis testing on datasets
from several to many subjects.

The number of EEGLAB clustering and cluster-based functions will
doubtless continue to grow in number and power in the future versions,
since they allow the realistic use of ICA decomposition in
hypothesis-driven research on large or small subject populations.

NOTE: Independent component clustering (like much other data clustering)
has no single 'correct' solution. Interpreting results of component
clustering, therefore, warrants caution. Claims to discovery of
physiological facts from component clustering should be accompanied by
thoughtful caveat and, preferably, by results of statistical testing
against suitable null hypotheses.

Now, back to our example. Before clustering all the components, it is
necessary to make some sort of processing to ensure that the measures
selected to base the clustering on contributing to the process in a
meaningful way. Se more info \[here
<https://sccn.ucsd.edu/wiki/Chapter_05:_Component_Clustering_Tools#Preparing_to_cluster_.28Pre-clustering.29_with_PCA_.28original.29_method>\].
To do so, the sample code below can be used. In this example, ERPs,
scalp maps (inverse of ICA decomposition) and dipoles were used to
cluster all the ICs.

``` matlab
[STUDY ALLEEG]  = std_preclust(STUDY, ALLEEG, 1,{'erp' 'npca' 10 'weight' 1 'timewindow' [100 800]  'erpfilter' '25'},...
                                                {'scalp' 'npca' 10 'weight' 1 'abso' 1},...
                                                {'dipoles' 'weight' 10});
```

After preclustering the ICs, we can proceed to cluster them by using the
sample code below. Here we used *kmeans* and requested 16 clusters. As a
result, the EEGLAB environment it will displays 17 clusters (one parent
cluster and teh 16 clusters requested)

``` matlab
[STUDY]         = pop_clust(STUDY, ALLEEG, 'algorithm','kmeans','clus_num',  16 , 'outliers',  2.8 );
```

### STUDY results visualization

At this point, we can visualize the results of clustering the ICs from
all subjects included in the STUDY. In the example here, we will look
for signatures on the brain responses that indicate differences in the
responses to the presentation of the tree type of faces (familiar or
famous, unfamiliar and scrambled).

#### Scalp maps and dipoles on clustered ICs

The figure below shows the average scalp maps of each of the clusters
obtained (EEGLAB sample code below). An interesting point here is the
reproducibility of these results. Given the algorithm used (K-means), it
is possible and almost surely, that every time we run the clustering we
will obtain the clusters in a different order (e.g, cluster 2 in one run
can be cluster 5 in the next run). This should not be a point of
conflict in analyzing the results as is a natural result of the method
used.

[center|500px](/Image:WH_STUDY_figures_scalpmaps.jpeg "wikilink")

``` matlab
STUDY = std_topoplot(STUDY,ALLEEG,'clusters',2:17, 'design', 1);
```

The next figure shows the clustered ICs laying on a head template. In
this visualization, we can asses the relative location in the brain of
the cluster centroids. This may lead to further analysis, by elaborating
results based on the anatomical location and the dynamics of the brain
response itself.

[center|500px](/Image:WH_STUDY_figures_dipoles.jpeg "wikilink")

``` matlab
STUDY = std_dipplot(STUDY,ALLEEG,'clusters',2:17, 'design', 1);
```

#### ERPs on clustered ICs

In the same way that we were able to plot the mean scalp map and dipoles
associated to each cluster, the rest of measures associated(e.g., ERPs,
ERSP, ITC) can also be displayed. The figure below shows the mean IC
time courses associated with the presentation of the three type of faces
on each cluster. In the sample code below, the parameters for the plots
are first defined with *pop_erpparams* (low pass filtering and time
range).

``` matlab
STUDY = pop_erpparams(STUDY, 'filter',15,'timerange',[-100 500], 'ylim', opt.ylimval);
STUDY = std_erpplot(STUDY,ALLEEG,'clusters',2:17, 'design', 1);
```

[center|500px](/Image:WH_STUDY_figures_erps.jpeg "wikilink")

With these results in hand, one might continue the analysis by
assessing, for example, the dynamics in cluster 8 (as shown in the
figure below). In this figure, it can be seen that brain responses
around the right fusiform gyrus, as indicated by an online Talairach
atlas given the Talairach XYZ coordinates, appear to be stronger for the
presentation of scrambled faces. Responses to presentations of familiar
and unfamiliar faces appear to be similar. The affinity of the fusiform
gyrus to the presentation of faces has been well described. This
explains why the responses to the presentation of familiar and
unfamiliar faces appear similar. It may also explain the difference
between the responses to scrambled faces since this is a deviant
stimulus. However, we can not explicitly put forwards these conclusions
without a proper statistical analysis of our results.

[center|600px](/Image:WH_STUDY_figures_cls8.jpeg "wikilink")

Indeed, EEGLAB provides a great framework for the statistical analysis
of electrophysiological data. EEGLAB allows users to use either
parametric or non-parametric statistics to compute and estimate the
reliability of these differences across conditions and/or groups (see
<https://sccn.ucsd.edu/wiki/Chapter_06:_Study_Statistics_and_Visualization_Options>).

#### Statistical Analysis

In the near future, statistical analysis based on hierarchical general
linear models (within subjects, between subjects) will be the default
approach supported by EEGLAB. In this approach, model parameters are
estimated for any selected data measures (ERP, ERSP, power spectra,
etc.) independently at each time (or time/frequency) point for each
subject and each source process (or other spatial channel combination).
Parameters estimated in these first-level (within-subject) analyses are
then integrated across subjects into a second-level GLM, similar to the
approach used to analyze fMRI data. Analysis of data following
decomposition into independent component source processes (or other
decomposition) is supported. To effect this integration and the
consequent extension of statistical analysis available in EEGLAB, we
have developed functions to define and test statistical contrasts, to
visualize their results, and to interact with the user via intuitive
graphical user interfaces (GUIs). EEGLAB internal data and file
structures have been modified to improve computation speed while bearing
the burden of increased data storage required for more complete single
trial-based data analysis. This wiki will be updated soon to show
results and demos on this regard. Meanwhile, take a look [at this
poster](/Media:RMC_postersfn_2016.pdf‎ "wikilink") on the LIMO-EEGLAB
integration and the application to the Wakeman-Henson set of data.