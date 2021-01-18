---
layout: default
title: b. Event Processing
long_title: b. Event Processing
parent: 11. Write scripts
grand_parent: Tutorials

---
Event processing scripts
=====
{: .no_toc }

This section is essential for users who want to write EEGLAB/MATLAB
scripts that select and/or process data time-locked to given types or
combinations of events. It is also important for any EEGLAB user who
wants to know how EEGLAB data and events are actually stored and
manipulated. First, you might want to read the section of the tutorial describing the [EEGLAB event structure](/tutorials/ConceptsGuide/Data_Structures.html#eegevent).

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>


Scripts for creating or modifying events
---------------------------
<button onclick="showModal(this)" data-command="eeglabp = fileparts(which('eeglab.m')); open(fullfile(eeglabp, 'tutorial_scripts', 'event_processing_single_dataset.m'));">Show MATLAB command</button>

The scripts below are relatively advanced EEGLAB/MATLAB scripts. The
[EEGLAB script tutorial](/tutorials/11_Scripting/Using_EEGLAB_history.html)
contains basic details on how to write MATLAB scripts using EEGLAB. 
First, we will import the continuous tutorial dataset. The code below
detects the EEGLAB path automatically, so you may copy and paste it to your MATLAB
command window.

``` matlab
%% Working with events
eeglab_path = fileparts(which('eeglab.m')); % get EEGLAB path
[ALLEEG EEG CURRENTSET ALLCOM] = eeglab; % start EEGLAB
pop_editoptions( 'option_storedisk', 0); % Change option to process multiple datasets
EEG = pop_loadset( 'eeglab_data.set', fullfile(eeglab_path, 'sample_data')); % load data
```

A
simple script below shift event latencies by 10 samples. Such manipulation are sometimes necessary because of delays introducted by the amplifier or computer collecting behavioral events. Alternatively, you may use the [pop_adjustevents.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_adjustevents.m) function. The script 
from this section is available [here](http://sccn.ucsd.edu/eeglab/locatefile.php?file=event_processing_single_dataset.m).

``` matlab
%% Adjust event latency
for iEvent=1:length(EEG.event)
     EEG.event(iEvent).latency = EEG.event(iEvent).latency + 10;
end
[ALLEEG EEG CURRENTSET] = eeg_store(ALLEEG, EEG, CURRENTSET); % Store dataset
```

The following script illustrates how to manipulate a dataset event list
using the tutorial dataset by adding a new class of (pseudo)
events to the existing dataset. Here, we want to add new events whose
latencies are 100 ms before existing 'square'-type events. (Note: Say we
might want to do this to allow epoching of the data relative to the
new events).

``` matlab
%% Add new cue events to a loaded dataset 0.1 second before time-locking event
nevents = length(EEG.event);
for index = 1 : nevents
    if ischar(EEG.event(index).type) && strcmpi(EEG.event(index).type, 'square')
    % Add events relative to existing events
        EEG.event(end+1) = EEG.event(index); % Add event to end of event list
        % Specifying the event latency to be 0.1 sec before the referent event (in real data points)
        EEG.event(end).latency = EEG.event(index).latency - 0.1*EEG.srate;
        EEG.event(end).type = 'cue'; % Make the type of the new event cue
    end
end

EEG = eeg_checkset(EEG, 'eventconsistency'); % Check all events for consistency
[ALLEEG EEG CURRENTSET] = eeg_store(ALLEEG, EEG, CURRENTSET); % Store dataset
eeglab redraw % Redraw the main EEGLAB window
```

The EEGLAB 'urevent' structure allows researchers to explore the point
of view that *no two events* during an experiment are actually
equivalent since each event occurs in a different *context*. Although
hard to dispute, insights into brain function to be gleaned from this
point of view are sacrificed when dynamics time-locked to all events of
a certain type are simply *averaged* together. In particular, the EEGLAB [erpimage.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=erpimage.m) and [pop_erpimage.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_erpimage.m)
functions allow users to visualize differences in potential time course or spectral
amplitudes in epochs time-locked to events sorted by some feature of
their context. A simple example is sorting stimulus-locked epoch by
subsequent response time ('rt'), though this is only a simple and straightforward example.
The function [eeg_urlatency.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_urlatency.m)
is useful for obtaining the latency of events in the original data. 

Adding event information for group analysis
--------------
<button onclick="showModal(this)" data-command="eeglabp = fileparts(which('eeglab.m')); open(fullfile(eeglabp, 'tutorial_scripts', 'event_processing_study.m'));">Show MATLAB command</button>

The EEGLAB [data structure](/tutorials/ConceptsGuide/Data_Structures.html) section of the tutorial indicates how events are
processed for group analysis. Event information is pulled from all datasets
and stored in the *STUDY.datasetinfo.trialinfo* structure.

For a given trial, only the information of the time-locking event is
stored. If there is other information of interest in other events of a
given trial (like reaction time for example), it needs to be added as a
field to the time locking event (for example, EEG.events(1).rt = 1231
indicating a reaction time of 1231 ms for that trial). This has to be
performed using a script and cannot be performed yet on the graphic
interface.

If you want to add an independent variable, simply write a script that
scans the EEG.event structure for each dataset and add a relevant field
for the time locking event (event at time 0) of each data trial. For
example, you may add the field 'previous_event_type' that would contain
the type of the previous event. Once you create the *STUDY*, this field will
automatically be taken into account and appears in the *STUDY* design
interface. Below is an example of a simple script scanning events and adding
the reaction as a new field to the 'square' time-locking events. This way
it will become visible at the STUDY level.
Note that when a reaction
time is missing for a given trial, it will be dealt with appropriately
at the *STUDY* level. Here, a *STUDY* is created with a single dataset, but
in the general case, it would be created from multiple datasets. The script 
below is available [here](http://sccn.ucsd.edu/eeglab/locatefile.php?file=event_processing_study.m).

``` matlab
%% Modify the events of datasets for creating STUDY designs

% load the epoched tutorial dataset
eeglab_path = fileparts(which('eeglab.m')); % get EEGLAB path
[ALLEEG, EEG, CURRENTSET, ALLCOM] = eeglab; % start EEGLAB
pop_editoptions( 'option_storedisk', 0); % Change option to process multiple datasets
EEG = pop_loadset( 'eeglab_data_epochs_ica.set', fullfile(eeglab_path, 'sample_data')); % load data
[ALLEEG, EEG, CURRENTSET] = eeg_store(ALLEEG, EEG);

% scan all datasets and modify events
% there is only one here so it is for illustration purpose
commands = {}; % for building the STUDY
for iDat = 1:length(ALLEEG)
     for iEvent = 1:length(ALLEEG(iDat).event)-1
           curEvent  = ALLEEG(iDat).event(iEvent); % current event
           nextEvent = ALLEEG(iDat).event(iEvent+1); % next event

           % only find reaction time event following time-locking events (TLE) within the same epoch
           if strcmpi( curEvent.type, 'square') && strcmpi( nextEvent.type, 'rt') && nextEvent.epoch == curEvent.epoch
                ALLEEG(iDat).event(iEvent).rt = (nextEvent.latency - curEvent.latency)/ALLEEG(iDat).srate * 1000; % latency of reaction time in ms
           end

     end
     % save dataset
     fileName = fullfile( ALLEEG(iDat).filepath, [ ALLEEG(iDat).setname(1:end-4) '_rtevents.set' ]);
     ALLEEG(iDat).saved = 'no';
     ALLEEG(iDat) = pop_saveset(ALLEEG, fileName);
     
     % add to list of dataset to build STUDY
     if isempty( ALLEEG(iDat).subject),  ALLEEG(iDat).subject = sprintf('S%2.2d', iDat); end % create subject name
     commands = { commands{:} 'index' iDat 'load' fileName 'subject' ALLEEG(iDat).subject }; 
end

% create study
[STUDY, ALLEEG] = std_editset( [], [], 'commands', commands,'updatedat','off' );
CURRENTSTUDY = true;
eeglab redraw

% Use menu item STUDY -> Select/Edit STUDY design then 
% under "Edit the independent variables for this design", press "New"
% You should be able to select event field 'rt' for creating designs
```

After running the script above, using the menu item <span style="color: brown">Study → Select/Edit STUDY design</span>, press the *New* button under the section *Edit the independent variables for this design*. You should be able to select *rt* to create new statistical designs (since this is a continuous variable, you would need to use the LIMO EEGLAB plugin to regress single-trial EEG activities on reaction times). Note that if you already have a *STUDY*, you will need to reload it from disk to update trial information (or call the function [std_maketrialinfo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_maketrialinfo.m from the MATLAB command line)).

Note that you may be tempted to modify the *STUDY.datasetinfo.trialinfo* field instead of modifying events for each dataset. However, even if you have saved the STUDY, every time you restart EEGLAB and reload the STUDY, your modifications will be erased. This is because EEGLAB keeps consistent the content of the *STUDY.datasetinfo.trialinfo* structures with the events in the individual datasets.