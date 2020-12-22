---
layout: default
title: d. Event Processing
parent: 11. Write scripts
grand_parent: Tutorials

---
Event processing scripts
=====
{: .no_toc }

This tutorial first describes how to import, modify,
select, and visualize EEGLAB events within the EEGLAB graphic
interface. It then describes the *EEG.event*,
*EEG.urevent*, and related *EEG.epoch* structures, and discusses
importing, editing, and using event information in EEGLAB scripts.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

Event processing from the Matlab command line
---------------------------------------------

This section is essential for users who want to write EEGLAB/Matlab
scripts that select and/or process data time-locked to given types or
combinations of events. It is also important for any EEGLAB user who
wants to know how EEGLAB data and events are actually stored and
manipulated.

### Accessing events from the command line


### Scripts for creating new events based on context

The scripts below are relatively advanced EEGLAB/Matlab scripts. The
[Script tutorial](/Chapter_02:_Writing_EEGLAB_Scripts "wikilink")
contains basic details on how to write Matlab scripts using EEGLAB. A
simple script below changes the event type by concatenating the event
type of the previous event. It is then possible to extract epochs based
on this information in the EEGLAB graphic interface.

``` matlab
for i=length(EEG.event):-1:2
     EEG.event(i).type = [ EEG.event(i).type ' preceeded by ' EEG.event(i-1).type ];
end;
[ALLEEG EEG CURRENTSET] = eeg_store(ALLEEG, EEG, CURRENTSET); % Store dataset
```

The following script illustrates how to manipulate a dataset event list
using the (epoched) tutorial dataset by adding a new class of (pseudo)
events to the existing dataset. Here, we want to add new events whose
latencies are 100 ms before existing 'square'-type events. (Note: Say we
might want to do this to allow re-epoching of the data relative to the
new events).

``` matlab
% Add new events to a loaded dataset
nevents = length(EEG.event);
for index = 1 : nevents
    if ischar(EEG.event(index).type) && strcmpi(EEG.event(index).type, 'square')
    % Add events relative to existing events
        EEG.event(end+1) = EEG.event(index); % Add event to end of event list
        % Specifying the event latency to be 0.1 sec before the referent event (in real data points)
        EEG.event(end).latency = EEG.event(index).latency - 0.1*EEG.srate;
        EEG.event(end).type = 'cue'; '% Make the type of the new event 'cue
    end;
end;

EEG = eeg_checkset(EEG, 'eventconsistency'); % Check all events for consistency
[ALLEEG EEG CURRENTSET] = eeg_store(ALLEEG, EEG, CURRENTSET); % Store dataset
eeglab redraw % Redraw the main EEGLAB window
```

Event context (as more reliably retrieved from the 'EEG.urevent' table)
can be valuable in data analysis. For example, one may want to study all
events of a certain type (or set of types) that precede or follow events
of some other types by delays within a given range. A classic ERP
example was the demonstration by [Squires et
al.](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=pubmed&dopt=Abstract&list_uids=64341)
that the P300 peak was larger when a rare stimulus followed a string of
standard stimuli than when it followed other rare stimuli. The (v4.4)command-line function [eeg_context.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_context.m) looks for events of

specified *target* type(s), then for preceding and/or succeeding events
of specified *neighbor* type(s).

The script below is a simple demonstration script using [eeg_context.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_context.m) that finds target events in the sample dataset

that are followed by appropriate button press responses. Some response
ambiguity is resolved by making sure the response does not follow a
succeeding target. (In that case, we assume the response is to the
second target). It also finds the responded targets that follow a
non-responded target since, we expect, the EEG dynamics time-locked to
these targets may differ in some way from those not following a 'miss'.

``` matlab
% For each target 'square' event, find the succeeding 'rt' and 'square' events

[targsrt,nextrts,nxtypert,rtlats] = eeg_context(EEG,{'square'},{'rt'},1);  % find succeeding rt events
[targssq,nextsqs,nxtypesq,sqlats] = eeg_context(EEG,{'square'},{'square'},1);  % find succeeding square events

% find target 'square' events with appropriate button-press responses

selev = []; % selected events
rejev = [];  % rejected events
for e=1:length(targsrt) % For each target,
    if rtlats(e) > 200 & rtlats(e) < 1500 ...  % if 'rt' latency in acceptable range
    & (sqlats(e) > rtlats(e) | isnan(sqlats(e))) % and no intervening 'square' event,
        selev = [selev targsrt(e,1)];  % mark target as responded to
    else  % Note: the isnan() test above tests for NaN value
    % of sqlats (when no next "square")
        rejev = [rejev targsrt(e,1)];
    end
end
rts = rtlats(selev); % collect RT latencies of responded targets
whos rtlats sqlats nextrts nextsqs
selev = targs(selev); % selev now holds the selected EEG.event numbers
rejev = targs(rejev);
fprintf(['Of %d "square" events, %d had acceptable "rt" responses ',...
'not following another "square".\n'],length(targsrt),length(selev));

%
% find targets following non-responded targets
%
aftererr = rejev+1;  % find target events following an unresponded target
aftererr(find(ismember(aftererr,selev)==0)) = [];  % remove events themselves
% not responded
whos selev rejev aftererr
fprintf(['Of %d "square" events following non-responded targets, ',...
'%d were themselves responded.\n\n'], length(rejev), length(aftererr));
```

The EEGLAB 'urevent' structure allows researchers to explore the point
of view that *no two events* during an experiment are actually
equivalent since each event occurs in a different *context*. Although
hard to dispute, insights into brain function to be gleaned from this
point of view are sacrificed when dynamics time-locked to all events of
a certain type are simply *averaged* together. In particular, the EEGLAB[erpimage.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=erpimage.m) and { {File\|pop_erpimage.m} } functions allow

users to visualize differences in potential time course or spectral
amplitudes in epochs time-locked to events sorted by some feature of
their context. A simple example is sorting stimulus-locked epoch by
subsequent response time ('rt'), though this is only a simple andstraightforward example. Using the [eeg_context.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_context.m) function,

one might also sort stimulus event-locked epochs by the amount of time
since the *previous* button press, or by the fraction of 'position'=1
events in the last minute, etc. Some future EEGLAB functions (and many
user scripts) will undoubtedly exploit such possibilities in many ways.

