---
layout: default
title: c. Automated pipeline
parent: 11. Write scripts
grand_parent: Tutorials 
position: 6
---
Automated processing pipelines using EEGLAB
=====
{: .no_toc }

You do not need to write a script to process all datasets simultaneously in a STUDY. This [video](https://www.youtube.com/watch?v=-jL3PuHD3aY) describes how to perform batch processing from the EEGLAB graphic interface. In this section, we run a similar pipeline using a script.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

<button onclick="showModal(this)" data-command="eeglabp = fileparts(which('eeglab.m')); open(fullfile(eeglabp, 'tutorial_scripts', 'simple_study_pipeline.m'));">Show MATLAB command</button>

Creating a STUDY or import from BIDS
------------------------------------

Download the data from https://openneuro.org/datasets/ds003061/ and go to this folder then run the script in the next section.

Alternatively, use one of the available [EEGLAB studies](tutorial_data.html). Note that some of these studies already have their data preprocessed and may not be suitable for automated processing.

Running the pipeline
----------------

The pipeline below takes the raw data from all subjects, clean the data, extracts epochs of interest, and plots the grand average ERP.

First, the data is imported. Then it is cleaned with clean_rawdata (default parameters are used here but may need adjustment based on data quality). ICA is then run on all datasets, and ICLabel is used to flag bad channels. 

Then oddball and standard stimuli epochs are extracted, the baseline is removed (from -1000 to 0 millisecond before the stimulus onset), and ERPs are computed and plotted. If you want to run this pipeline on your own EEGLAB study, then you will need to modify the line for extracting data epochs (as the name of your events will likely differ).

``` matlab
% check folder
eeglab
if ~exist('task-P300_events.json', 'file')
    error('Download the data from https://openneuro.org/datasets/ds003061/ and go to the downloaded folder');
else
    filepath = fileparts(which('task-P300_events.json'));
end

% import data
[STUDY, ALLEEG] = pop_importbids(filepath, 'studyName','Oddball');
EEG = ALLEEG; CURRENTSET = 1:length(EEG); CURRENTSTUDY = 1; eeglab redraw; % redraw EEGLAB interface (optional)

% compute average reference
EEG = pop_reref( EEG,[]);

% clean data using the clean_rawdata plugin
EEG = clean_artifacts( EEG,'FlatlineCriterion',5,'ChannelCriterion',0.8, ...
    'LineNoiseCriterion',4,'Highpass',[0.25 0.75] ,'BurstCriterion',20, ...
    'WindowCriterion',0.25,'BurstRejection','on','Distance','Euclidian', ...
    'WindowCriterionTolerances',[-Inf 7] ,'fusechanrej',1);

% recompute average reference interpolating missing channels (and removing
% them again after average reference - STUDY functions handle them automatically)
EEG = pop_reref( EEG,[],'interpchan',[]);

% run ICA reducing the dimention by 1 to account for average reference 
EEG = pop_runica(EEG, 'icatype','runica','concatcond','on','options',{'pca',-1});

% run ICLabel and flag artifactual components
EEG = pop_iclabel(EEG, 'default');
EEG = pop_icflag( EEG,[NaN NaN;0.9 1;0.9 1;NaN NaN;NaN NaN;NaN NaN;NaN NaN]);

% extract data epochs
EEG = pop_epoch( EEG,{'oddball_with_reponse','standard'},[-1 2] ,'epochinfo','yes');
EEG = eeg_checkset( EEG );
EEG = pop_rmbase( EEG,[-1000 0] ,[]);

% create STUDY design
ALLEEG = EEG;
STUDY = std_makedesign(STUDY, ALLEEG, 1, 'name','STUDY.design 1','delfiles','off', ...
    'defaultdesign','off','variable1','type','values1',{'oddball_with_reponse','standard'},...
    'vartype1','categorical','subjselect',{'sub-001'});

% precompute ERPs at the STUDY level
[STUDY, ALLEEG] = std_precomp(STUDY, ALLEEG, {},'savetrials','on','rmicacomps','on','interp','on','recompute','on','erp','on');

% plot ERPS for the P300 
STUDY = pop_erpparams(STUDY, 'topotime',350);
chanlocs = eeg_mergelocs(ALLEEG.chanlocs); % get all channels from all datasets
STUDY = std_erpplot(STUDY,ALLEEG,'channels', {chanlocs.labels}, 'design', 1);
```

A figure similar to the one below will be plotted. The figure may differ as some of the artifact and rejection steps above involve choosing data randomly. To make the pipeline reproducible, add "rng(1)" at the beginning of the script above.

Optimizing the pipeline for your data
-------------------------------------

### Filtering

You might want to apply a different filter than the filter applied by the *clean_rawdata* plugin (which is an elipic filter). For example, to apply a standard FIR filter, you would need to replace the call to the *clean_artifacts* function by:

``` matlab
EEG = pop_eegfiltnew( EEG,'locutoff',0.5);
EEG = clean_artifacts( EEG,'FlatlineCriterion',5,'ChannelCriterion',0.8, ...
    'LineNoiseCriterion',4,'Highpass','off' ,'BurstCriterion',20, ...
    'WindowCriterion',0.25,'BurstRejection','on','Distance','Euclidian', ...
    'WindowCriterionTolerances',[-Inf 7] ,'fusechanrej',1);
```

Note that when calling the function to clean artifacts from the *clean_rawdata* plugin, the *highpass* argument is set to *off* to disable filtering.

### Why do we rereference twice?

Artifact cleaning using *clean_rawdata* usually works better on averaged reference data. We have made this observation when processing data, although there is no published article on this topic. After bad channels have been removed, then we need to compute the average reference again. The second average reference computation undoes the first one, as explained on this [page](05_Preprocess/rereferencing.html).

### Automated cleaning parameter

The call to *clean_artifacts* uses the default EEGLAB parameters. However, these are not always optimal. In particular, *'ChannelCriterion'* may be modified to reject more or fewer channels. *'BurstCriterion'* is another important parameter. Increase it to 40, for example (or some people recommend 100) if you feel too many data regions are rejected. More information is available on the plugin [wiki page](https://github.com/sccn/clean_rawdata).

Finding optimal parameters for cleaning your data is essential to designing your pipeline. It would be best if you experimented with a couple of subjects. Also, once you run your pipeline on all subjects, you should check how much data was removed for each subject. Sometimes, 80% of the data is removed for some subjects, which is not acceptable.

An alternative solution for cleaning data is also to run data cleaning multiple times. Your run artifact rejection once to remove bad channels and large artifacts. Then after running ICA, you can run it again to remove smaller artifacts. The advantage of this approach is that the first data cleaning will not remove eye blinks (which ICA can subtract from your data allowing you to keep these regions of data). An example of this approach is shown in [this section of the tutorial](11_Scripting/Analyzing_EEG_BIDS_data_in_EEGLAB.html).

### Which ICA to use

The script above uses *runica* (Infomax) which is the default in EEGLAB. Other popular choices which require to install the relevant plugins are *Amica*, *Picard*, and *FastICA*. We compared different ICA solutions in this [paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0030135). In short, there is no ideal algorithm:
- *Runica* has been used the most. It is robust but slow.
- *picard* optimizes the same objective function as *runica*. It converges faster and with lower residuals. It was also designed by one of the ICA pioners Jean-Francois Cardoso. Nevertheless, it is still a new algorithm (as of 2022) that has not been thoroughly compared with others on EEG data.
- *FastICA* is an ICA algorithm widely used on EEG data. The author of the algorithm advise to use the symmetric approach instead of the iterative one (which is the default).
- *Amica* is the best ICA algorithm based on our [comparison](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0030135). Nevertheless it is slow. Also it can only be applied to single EEG datasets.

### What algorithm for automated ICA artifact rejection?

We used *ICLabel* in the script above. They are others. For example *MARA* is another popular one. 

For *ICLabel*, you may set threshold to detect artifactual components. In the script above, we set the threshold to 90% for the likelyhood to be an eye movement artifact (blink or lateral eye movement) and 90% for the likelyhood to be a muscle. This is quite conservative, and will only reject 1 to 5 component per subject. Some researchers are less conservative and would set threshold lower. The [ICLabel](https://github.com/sccn/ICLabel) page contains more information on this subject.

### More advanced pipelines

* What if I want to plot the spectrum instead of ERPs? The example above was for ERPs. However, it is easy to plot other measures as described in this [page](command_line_study_functions.html).
* Can I use LIMO in my pipeline. Yes, of course. See [this paper](https://www.frontiersin.org/articles/10.3389/fnins.2020.610388/full) and the [LIMO wiki](https://github.com/LIMO-EEG-Toolbox/limo_meeg/wiki) for reference. 
* Can I do source localization of ICA components and cluster components. Yes, all 

Other EEGLAB pipelines
----------------------

Below are other EEGLAB pipelines. 

* [The PREP pipeline](https://vislab.github.io/EEG-Clean-Tools/) is an EEGLAB plugin. It is an outdated pipeline (as of 2022) because automated artifact detection is suboptimal, but it was a relevant pipeline from 2014 to 2020, and there is nothing fundamentally wrong with it.
* [Makoto's processing pipeline](https://sccn.ucsd.edu/wiki/Makoto's_preprocessing_pipeline) is another relevant reference. It is not recommended for beginners. Nevertheless, it contains important information about EEG processing, and it is a worthwhile read.
* [Danielle Gruber's pipeline](https://medium.datadriveninvestor.com/streamline-your-eeglab-experience-8803c805c5a7). Danielle Gruber is an EEGLAB user who shared her pipeline. It is long and detailed and also outdated (as of 2022). We did not spot any fundamental errors in the pipeline, though. It is a single-subject pipeline.
* [The BIDS data script](Analyzing_EEG_BIDS_data_in_EEGLAB.html) is part of this tutorial, and it is a similar pipeline (although more complex) compared to the one presented on this page for processing data.
* [The HAPPE pipeline](https://www.frontiersin.org/articles/10.3389/fnins.2018.00097/full). We have not evaluated this EEGLAB-based pipeline but it is a popular one.
