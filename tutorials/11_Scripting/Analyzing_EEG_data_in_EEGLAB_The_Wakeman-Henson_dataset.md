---
layout: default
title: e. BIDS Data script
summary: Analyzing the Wakeman-Henson dataset with EEGLAB
parent: 11. Write scripts
grand_parent: Tutorials 
---

![right\|830px](/assets/images/Rmc_sfn_poster_2018_2print.jpg)

# Analyzing EEG-BIDS data with EEGLAB: The Wakeman-Henson dataset

The EEGLAB architecture makes it suited to data exploration and visualization as
well as to applying customized analysis including general linear model
statistics. 
EEGLAB also has specific functions to import EEG data organized according to the [Brain Imaging Data Structure](https://bids.neuroimaging.io) (BIDS) (see aksi the specific reference for [EEG_BIDS](https://www.nature.com/articles/s41597-019-0104-8))

 Here we demonstrate how to import EEG-BIDS data into EEGLAB and how to use the [EEGLAB STUDY](https://sccn.github.io/tutorials/10_Group_analysis) tool for group analysis on these data to perform some basic EEGLAB methods focusing on ICA
decompositions and on the study of the dynamics of the
resulting effective brain sources.

 The EEG data used in this example comes from [Wakeman and Henson (2015)](https://www.nature.com/articles/sdata20151). In this experiment, MEG-EEG data were collected while subjects  viewed famous, unfamiliar and scrambled faces. Each image was repeated  twice (immediately in 50% of cases and 5–10 stimuli apart for the other  50%) and subjects pressed one of two keys with their left or right index finger indicating how symmetric they regarded each image relative to  the average.

## EEG-BIDS 
The data are organized according to the [BIDS format](https://bids.neuroimaging.io). You can read more on the specificities of the EEG-BIDS format [here](https://www.nature.com/articles/s41597-019-0104-8). EEGLAB  has dedicated BIDS tools called [bids-matlab-tools](https://github.com/sccn/bids-matlab-tools) to create files, export and import BIDS dataset. This is available  using the EEGLAB plugin manager and must be installed before running the code below. It is worthwhile spending a bit of time looking at how files are organized and named in BIDS, as we will follow this convention throughout.
To know more about how EEGLAB interacts with BIDS file you can also watch this serie of short YouTube videos below. Click on the icon on the top right corner to access the list of videos in the playlist.



<center><iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PLXc9qfVbMMN3II4EnVQNjOeVl-UprWlnM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>



## Download the data
The data were prepared (i.e. EEG extracted, timing corrected,  electrode position re-oriented, event recorded) by Dung Truong, Ramon  Martinez & Arnaud Delorme and can be downloaded from [OpenNeuro 10.18112/openneuro.ds002718.v1.0.3.](https://openneuro.org/datasets/ds002718/versions/1.0.3) 

### More about the Wakeman-Henson dataset

Human perception of suddenly presented face images produces a large
negative peak near 170 ms (dubbed ‘the N170’) in averaged event-related
potentials (ERPs) for posterior scalp channels [Bentin et al.,
1996](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2927138/). This
potential has been localized by several methods, including direct
electrocorticographic (ECoG) recording from the cortical surface, to the
bilateral fusiform gyrus. 

Henson and Wakeman (2015) apply joint EEG/MEG
source analysis to the N170 peak scalp maps to estimate the areas of
inferior temporal cortex that produce the response feature. A BOLD
signal increase in the same areas is seen in fMRI studies ([Kanwisher et
al., 1997](https://www.ncbi.nlm.nih.gov/pubmed/9151747)). A long train
of functional imaging and EEG experiments have considered the question
of whether activation of fusiform gyrus by face image presentations
indexes face-specific processing ([Kanwisher & Yovel,
2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1857737/)) or
processing supporting more general expert identification of individuals
or subcategories for any large set of important and long-studied objects
-- for example, automobile grilles by automobile experts ([Gauthier et
al., 1999](https://www.ncbi.nlm.nih.gov/pubmed/10448223)). 

Generally,
face presentations produce much larger ‘N170’ potentials (and ensuing
fusiform BOLD activations) than do presentations of ‘face-like’ images
of houses, etc. 

Wakeman and Henson (2015) developed the paradigm used to
collect the data treated here to determine how repetition (of the same
face image) in a series of tachistoscopically presented ‘face versus
house’ images experiment affected EEG and concurrent MEG responses, and
how responses to well-known, unknown, and scrambled faces in the same
sequence differed. See details of the paradigm in the figure below.

![`center|400px`](/assets/images/Wakeman_henson_eegset.jpg)

## Data pre-processing
Data pre-processing pipeline
Once you have downloaded the data you can run the code below. 

Note that this pre-processing step is also available as a MATLAB Live Script [PATH TO LIVESCRIPT]

### Start EEGLAB 

``` matlab
clear
[ALLEEG, EEG, CURRENTSET, ALLCOM] = eeglab;
eeglabPath = fileparts(which('eeglab'));
```

If you saved the data elsewhere than in the EEGLAB "sample_data" subfolder you will have to adjust the filepath variable in the cell below :

``` matlab
filepath = fullfile(eeglabPath, sample_data, 'WakemanHenson_Faces', filesep, 'eeg');
```

### Import BIDS data
The function pop_importbids() imports a BIDS format folder structure into an EEGLAB study. 
If 'bidsevent' is 'on' then events will be imported from the BIDS .tsv event file and events in the raw binary EEG files will be ignored. Similarly 'bidschanloc', 'on' will import channel locations from BIDS .tsv file and ignore any locations in raw EEG files. The 'studyName' field let you specify the name of the newly created STUDY.

``` matlab
[STUDY, ALLEEG] = pop_importbids(filepath, 'bidsevent','on','bidschanloc','on', ...
    'studyName','Face_detection');

ALLEEG = pop_select( ALLEEG, 'nochannel',{'EEG061','EEG062','EEG063','EEG064'});
CURRENTSTUDY = 1; EEG = ALLEEG; CURRENTSET = [1:length(EEG)];
```

### Remove bad channels
Here we are using the pop_clean_rawdata() function to remove flat line channels and channels with abnormal activity.
The pop_clean_rawdata()  uses the [Artefact Subspace Reconstruction](https://sccn.github.io/tutorials/ConceptsGuide/ASR_background.html) (ASR) module that is integrated into the EEGLAB [clean_rawdata() plugin](https://sccn.github.io/tutorials/ConceptsGuide/ASR_background.html) (already installed by default). 
In a further step below we will again use ASR but to remove portions of data. 

``` matlab
EEG = pop_clean_rawdata( EEG,'FlatlineCriterion',5,'ChannelCriterion',0.8,...
    'LineNoiseCriterion',4,'Highpass',[0.25 0.75] ,...
    'BurstCriterion','off','WindowCriterion','off','BurstRejection','off',...
    'Distance','Euclidian','WindowCriterionTolerances','off' );
``` 

### Re-reference using the average reference

``` matlab

EEG = pop_reref( EEG,[],'interpchan',[]);
```

### Run ICA and flag artefactual components using IClabel
You can find more details on using ICA to remove artefacts embeded in EEG data by reading the [dedicated section](https://github.com/sccn/clean_rawdata) on the EEGLAB tutorial.
IClabel is an EEGLAB plugin developped by Luca Pion-Tonachini and installed by default with EEGLAB.  IClabel provides an estimation of the type of each of the independent components (brain, eye, muscle, line noise, etc.).
ICA components that are flagged as artefactual by IClabel are then subtracted (removed) from the data.
Note that the second argument of the function pop_icflag() 'thresh' is to specify the min and max threshold values used to include for selection of a component as artefact. The thresholds are entered for 6 categories of ICA component that are, in order: Brain, Muscle, Eye, Heart, Line Noise, Channel Noise, Other.
So here you can see that we only remove ICA components if they are classified in the Eye or Heart category with between 80%-100% confidence. 

``` matlab
for s=1:size(EEG,2)
    EEG(s) = pop_runica(EEG(s), 'icatype','runica','concatcond','on',...
                                'options',{'pca',EEG(s).nbchan-1});
    EEG(s) = pop_iclabel(EEG(s),'default');
    EEG(s) = pop_icflag(EEG(s),'thresh', [NaN NaN;0.8 1;0.8 1;NaN NaN;NaN NaN;NaN NaN;NaN NaN]);
    EEG(s) = pop_subcomp(EEG(s), find(EEG(s).reject.gcompreject), 0);
end
```

### Remove portions of data contaminated by artefacts
Again we are using ASR and pop_clean_rawdata() here but this time to remove portions of data containing artefactual activity (not channels as this was done above).
First, ASR finds clean portions of data (calibration data) and  calculates the standard deviation of PCA-extracted components (ignoring  physiological EEG alpha and theta waves by filtering them out). Then, it rejects data regions if they exceeds 20 times (by default) the standard deviation of the calibration data. The lower this threshold, the more  aggressive the rejection is.

``` matlab
EEG = pop_clean_rawdata( EEG,'FlatlineCriterion','off','ChannelCriterion','off',...
    'LineNoiseCriterion','off','Highpass','off','BurstCriterion',20,...
    'WindowCriterion',0.25,'BurstRejection','on','Distance','Euclidian',...
    'WindowCriterionTolerances',[-Inf 7] );
```

You can access the description of each of this function's parameter from within Matalab if you enter:
``` matlab
help clean_artifacts
```

### Extract data epochs 
Here we convert the continuuous EEG datasets of our STUDY to epoched data by extracting data epochs that are time-locked to the event types specified in 'typerange' when calling pop_epoch(). The 'timelim' input defines the epoch latency limits in seconds relative to the time-locking events, here we defined a window from -0.5s before the event to 1s after the event. 
Note that we do not remove a baseline here.

``` matlab
EEG    = pop_epoch( EEG,'typerange', {'famous_new','famous_second_early','famous_second_late',...
    'scrambled_new','scrambled_second_early','scrambled_second_late','unfamiliar_new',...
    'unfamiliar_second_early','unfamiliar_second_late'},'timelim', [-0.5 1] ,'epochinfo','yes');
EEG    = pop_saveset(EEG, 'savemode', 'resave');
ALLEEG = EEG;
```

### Create a STUDY design
STUDY designs let you perform statistical comparisons of a STUDY multiple trial and dataset subsets without having to create and store the STUDY more than once. 
Here, we create a design that we name 'Faces' that takes all values of events type (ie. scramble, familiar and unfamiliar) as first independent variable. 

``` matlab
STUDY  = std_checkset(STUDY, ALLEEG);
STUDY  = std_makedesign(STUDY, EEG, 1, 'name','Faces','delfiles','off',...
                        'defaultdesign','off','variable1','type','values1',{});
```

Update the EEGLAB window
``` matlab
eeglab redraw
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
versions, beamica (Christian Kothe) and cudaica ([Raimondo et al,.
2012](https://www.hindawi.com/journals/cin/2012/206972/)), respectively,
are also available as EEGLAB plugins.

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

