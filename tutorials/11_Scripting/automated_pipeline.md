---
layout: default
title: c. Automated pipeline
parent: 11. Write scripts
grand_parent: Tutorials 
position: 4
---
Automated processing pipelines using EEGLAB
=====
{: .no_toc }

You do not have to write script to process all datasets at the same in a STUDY. This [video](https://www.youtube.com/watch?v=-jL3PuHD3aY) describe how to perform batch processing from the EEGLAB graphic interface. In this section, we run a similar pipeline using a script.

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

Alternatively use one of the available [EEGLAB studies](tutorials/tutorial_data.html). Note that some of these studies already have their data preprocessed and may not be suitable for automated processing.

Run the pipeline
----------------

First the data is imported. Then it is cleaned with clean_rawdata (default paramters are used here but may need adjustment based on data quality). ICA is then run on all datasets, and ICLabel is used to flag bad channels. 

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
STUDY = std_erpplot(STUDY,ALLEEG,'channels',{'AF7','AF3','F1','F3','F5','F7','FT7','FC5','FC3','FC1','C1','C3','C5','T7','CP5','CP3','CP1','P5','P7','P9','PO7','PO3','O1','Iz','Oz','POz','Pz','CPz','Fpz','Fp2','AF8','AF4','AFz','Fz','F2','F4','F6','F8','FT8','FC6','FC4','FC2','FCz','Cz','C2','C4','C6','T8','TP8','CP6','CP4','CP2','P2','P4','P6','P8','P10','PO8','PO4','O2','EXG1','EXG2','EXG3','EXG4','EXG5','EXG8','Resp'}, 'design', 1);
```

A figure similar to the one below will be plotted


Other EEGLAB pipelines
----------------------

There are other EEGLAB pipelines. 

* [The PREP pipeline](https://vislab.github.io/EEG-Clean-Tools/) is an EEGLAB plugin. It is an outdated pipeline (as of 2022) because automated artifact detection is suboptimal, but it was a relevant pipeline from 2014 to 2020 and there is nothing fundamentally wrong with it.
* [Makoto's processing pipeline](https://sccn.ucsd.edu/wiki/Makoto's_preprocessing_pipeline) is another relevant reference. It is not recommended for beginner. Nevertheless it contains important information about EEG processing and it is a worthwhile read.
* [Danielle Gruber's pipeline](https://medium.datadriveninvestor.com/streamline-your-eeglab-experience-8803c805c5a7). Danielle Gruber is an EEGLAB user who shared her pipeline. It is long and detailed and also outdated (as of 2022). We did not spot any fundamental errors in the pipeline though. It is a single subject pipeline.
* [The BIDS data script](tutorials/11_Scripting/Analyzing_EEG_BIDS_data_in_EEGLAB.html) is part of this tutorial, and it is a similar pipeline (although more complex) compared to the one presented on this page for processing data.
* [The HAPPE pipeline](https://www.frontiersin.org/articles/10.3389/fnins.2018.00097/full). We have not evaluated this EEGLAB-based pipeline but it is a popular one.

