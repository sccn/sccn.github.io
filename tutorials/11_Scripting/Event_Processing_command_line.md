---
layout: default
title: Event Processing from the command line
parent: 11. Scripting
grand_parent: Tutorials
---

his tutorial first describe how to import, modify,
select, and visualize EEGLAB events, within the EEGLAB graphic
interface. It then describes in more details the *EEG.event*,
*EEG.urevent*, and related *EEG.epoch* structures, and discusses
importing, editing, and using event information in EEGLAB scripts.

Event processing from the Matlab command line
---------------------------------------------

This section is essential for users who want to write EEGLAB/Matlab
scripts that select and/or process data time-locked to given types or
combinations of events. It is also important for any EEGLAB user who
wants to know how EEGLAB data and events are actually stored and
manipulated.

### Accessing events from the command line

#### Event types

Event fields of the current data structure can be displayed by typing
''\>\> EEG.event '' on the Matlab command line. For instance, using the
unprocessed tutorial dataset,

> \>\> EEG.event

returns,

``` matlab
ans =

    1x157 struct array with fields:
        type
        position
        latency
        urevent
```

To display the field values for the first event, type:

> \>\> EEG.event(1)

This will return,

``` matlab
ans =
    type: 'square'
    position: 2
    latency: 129.087
    urevent: 1
```

Remember that custom event fields can be added to the event structure
and will thereafter be imported with the event information whenever the
dataset is loaded. Therefore, the names of some event fields may differ
in different datasets. Note that event field information can be easily
retrieved using commands such as *\>\> {EEG.event.fieldname}*. For
example,

> \>\> {EEG.event(1:5).type}

returns the contents of the *type* field for the first 5 events:

``` matlab
ans =
    'square' 'square' 'rt' 'square' 'rt'
```

Use the following commands to list the different event types in the
unprocessed tutorial dataset:

``` matlab
>> unique({EEG.event.type});

ans=
    'rt' 'square'
```

The command above assumes that event types are recorded as strings. Use
*\>\> unique(cell2mat({EEG.event.type}));* for event types stored as
numbers.

You may then use the recovered event type names to extract epochs. Below
is the command-line equivalent of the epoch extraction procedure
presented above in section [“I.5 Extracting data
epochs”](/Chapter_05:_Extracting_Data_Epochs "wikilink").

> \>\>EEG = pop_epoch( EEG, { 'square' }, \[-1 2\], 'epochinfo', 'yes');

If you decide to process data from the command-line directly, do not
forget to first remove baseline activity,

> \>\> EEG = pop_rmbase( EEG, \[-1000 0\]);

See the [Script
tutorial](/Chapter_02:_Writing_EEGLAB_Scripts "wikilink") for more
details on how to write Matlab scripts using EEGLAB.

#### Event latencies

We may use the same command as in the section above to display the
contents of the event latency field. Event latencies are stored in units
of data sample points relative to (0) the beginning of the continuous
data matrix (EEG.data). For the tutorial dataset (before any
processing), typing:

> \>\>{EEG.event(1:5).latency}

returns the first 5 event latencies,

> ans =
>
> \[129.0087\] \[218.0087\] \[267.5481\] \[603.0087\] \[659.9726\]

To see these latencies in seconds (instead of sample points above), you
need first to convert this cell array to an ordinary numeric array
(using EEGLAB { {File\|cell2mat.m} } function), then subtract 1 (because
the first sample point corresponds to time 0) and divide by the sampling
rate. Therefore,

> \>\>(cell2mat({EEG.event(1:5).latency})-1)/EEG.srate

returns the same event latencies in seconds,

> ans =
>
> 1.0001 1.6954 2.0824 4.7032 5.1482

For consistency, for epoched datasets the event latencies are also
encoded in sample points with respect to the beginning of the data (as
if the data were continuous). Thus, after extracting epoch from the
tutorial dataset (["Data
Epochs"](/Chapter_05:_Extracting_Data_Epochs "wikilink"))

> \>\>{EEG.event(1:5).latency}

returns the first 5 event latencies,

> ans =
>
> ``
>
> `[129][218.00][267.5394][424][513]`

Note that for an epoched dataset this information has no direct meaning.
Instead, select menu item <font color=brown>Edit \> Event values</font>
(calling function { {File\|pop_editeventvals.m} }) to display the
latency of this event in seconds relative to the epoch time-locking
event. From the command-line, you may use the eeg_function {
{File\|eeg_point2lat.m} } to convert the given latencies from data
points relative to the beginning of the data to latencies in seconds
relative to the epoch time-locking event. For example:

``` matlab
>> eeg_point2lat(cell2mat({EEG.event(1:5).latency}), ...
        cell2mat({EEG.event(1:5).epoch}), EEG.srate, [EEG.xmin EEG.xmax])

ans =

    0 0.6953 1.0823 -0.6953 0
```

(The reverse conversion can be accomplished using function {
{File\|eeg_lat2point.m} })

The most useful function for obtaining event information from the
command-line is EEGLAB function { {File\|eeg_getepochevent.m} }. This
function may be used for both continuous and epoch data to retrieve any
event field for any event type. For example, using the tutorial data
(after epoch extraction), type in

> \>\> \[rt_lat all_rt_lat\] = eeg_getepochevent(EEG, 'rt', \[\],
> 'latency');

to obtain the latency of events of type *rt*. The first output is an
array containing one value per data epoch (the *first* event of the
specified type in each data epoch). The second output is a cell array
containing the field values for *all* the relevant events in each data
epoch. Latency information is returned in milliseconds. (Note: The third
input allows searching for events in a specific time window within each
epoch. An empty value indicates that the whole epoch time range should
be used).

Similarly to obtain the value of the event 'position' field for 'square'
events in each epoch, type:

> \>\> \[rt_lat all_rt_lat\] = eeg_getepochevent(EEG, 'square', \[\],
> 'position');

Continuous data behave as a single data epoch, so type:

> \>\> \[tmp all_sq_lat\] = eeg_getepochevent(EEG, 'square');

to obtain the latencies of all 'square' events in the continuous data
(via the second output).

#### Urevents

In EEGLAB v4.2 and above, a separate "ur" (German for "original") event
structure, *EEG.urevent*, holds all the event information originally
loaded into the dataset. If some events or data regions containing
events are removed from the data, this should not affect the
*EEG.urevent* structure. If some new events are inserted into the
dataset, the urevent structure is automatically updated. This is useful
to obtain information on the *context* of events in the original
experiment. Even after extracting data epochs, the prior *context* of
each event in a continuous or epoched dataset is still available.
Currently the *EEG.urevent* structure can only be examined from the
command line.

The *EEG.urevent* structure has the same format as the *'EEG.event*
structure. The *urevent* field in the event structure (e.g.,
*EEG.event(n).urevent*) contains the index of the corresponding event in
the urevent structure array -- thereby 'pointing' from the event to its
corresponding urevent, e.g., its "original event" number in the
continuous data event stream. For example, if a portion of data
containing the second event is removed from a continuous dataset during
artifact rejection, the second event will not remain in the *EEG.event*
structure. It *will* remain, however, in the *EEG.urevent* structure.
e.g. the second *EEG.event* might now point to the third *EEG.urevent*:

``` matlab
>> EEG.event(2).urevent

ans =
    3
```

Note that 'urevent' indices in the *EEG.event* structure do not have to
increase linearly. For example after epochs were extracted from the
tutorial dataset,

``` matlab
>> {EEG.event(1:5).urevent}

ans =

    [1] [2] [3] [1] [2]
```

This means that events 1 and 2 (in the first data epoch) and events 4
and 5 (in the second data epoch) are actually the same original
events.

At present (v4.4), a few EEGLAB command-line functions use the urevent
structure: { {File\|eeg_time2prev.m} }, { {File\|eeg_urlatency.m} } and
{ {File\|eeg_context.m} }. We will use the important {
{File\|eeg_context.m} } function in a script example below. The next
section provides more insight into the relation between the *EEG.event*
and *EEG.urevent* structures.

#### Boundary events

Events of reserved type 'boundary' are created automatically by EEGLAB
when portions of the data are rejected from continuous data or when
continuous datasets are concatenated. These events indicate the
latencies and (when possible) the durations of the discontinuities these
operations introduce in the data. In the image below, a portion of data
that included event \#2 was rejected, and a type 'boundary' event was
added to the event structure. Its index became 2, since events are
sorted by their latencies. The urevent structure continues to hold the
original event information, with no added 'boundary' event.


![Image:Eventcontinuous.gif](/assets/images/Eventcontinuous.gif)



Boundary events are standard event structures with *event.type* =
'boundary'. They also have an *event.duration* field that holds the
duration of the rejected data portion (in data samples). (Note: Since
all events in a dataset must have the same set of fields, in datasets
containing boundary events every event will have a 'duration' field --
set by default to 0 except for true boundary type events. Boundary
events are used by several signal processing functions that process
continuous data. For example, calculating the data spectrum in the {
{File\|pop_spectopo.m} } function operates only on continuous portions
of the data (between boundary events). Also, data epoching functions
will (rightly!) not extract epochs that contain a boundary event.

*Epoched* datasets do not have boundary events between data epochs.
Instead of being stored in a 2-D array of size (channels, sample_points)
like continuous data, epoched data is stored in a 3-D array of size
(channels, sample_points, trials). Events in data epochs are stored as
if the data were continuous, in effect treating the data as a 2-D array
of size (channels, (sample_points\*trials)). This format makes handling
events from the command-line more convenient.

The purpose of the *EEG.urevent* structure is to retain the full record
of experimental events from the original continuous data, as shown in
the image below. Function { {File\|eeg_context.m} } uses 'urevent'
information to find events defined by their neighboring event 'context'
in the experiment (and original data).


![Image:Eventepoch.gif](/assets/images/Eventepoch.gif)


#### 'Hard' boundaries between datasets

When continuous datasets are concatenated, a 'harder' type of boundary
event must be inserted, this time into both the *EEG.event* and
*EEG.urevent* structures. In particular, if the first urevent in the
pair was the last event in one dataset, and the next urevent was the
first event in the next concatenated dataset (which need not have been
recorded at the same time), the latencies of the neighboring pair of
urevents cannot be compared directly. Such so-called "hard" boundary
events marking the joint between concatenated datasets have the usual
type "boundary" but a special "duration" value, *NaN* (Matlab numeric
value "not-a-number"). They are the only "boundary" events present in
*EEG.urevent* and are the only type "boundary" events in *EEG.event*
with a "duration" of "NaN" and an *EEG.event.urevent* pointer to an
urevent. Hard "boundary" events are important for functions such as {
{File\|eeg_context.m} } that are concerned with temporal relationships
among events in the original experiment (i.e., among urevents).

### The 'epoch' structure

The *EEG.epoch* structure is empty in continuous datasets, but is
automatically filled during epoch extraction. It is computed from the
*EEG.event*structure by the function { {File\|eeg_checkset.m} } (with
flag 'eventconsistency') as a convenience for users who may want to use
it in writing EEGLAB scripts. One of the few EEGLAB functions that use
the *EEG.epoch* structure (all 'eeg_' command-line functions) is {
{File\|eeg_context.m} }. Each *EEG.epoch* entry lists the type and
*epoch* latency (in msec) of every event that occurred during the epoch.
The following example was run on the tutorial set after it was converted
to data epochs.

``` matlab
>> EEG.epoch

ans =
    1x80 struct array with fields:
        event
        eventlatency
        eventposition
        eventtype
        eventurevent
```

Note that this dataset contains 80 epochs (or trials). Now type

``` matlab
>> EEG.epoch(1)

ans =

    event: [1 2 3]
    eventlatency: {[0] [695.3125] [1.0823e+03]}
    eventposition: {[2] [2] [2]}
    eventtype: {'square' 'square' 'rt'}
    eventurevent: {[1] [2] [3]}
```

The first field *EEG.epoch(1).event* contains the indices of all events
that occurred during this epoch. The fields *EEG.epoch(1).eventtype*,
*EEG.epoch(1).eventposition* and *EEG.epoch(1).eventlatency* are cell
arrays containing the event field values of each of the events in that
epoch. Note that the latencies in *EEG.epoch(1).eventlatency* are in
milliseconds with respect to the epoch time-locking event.

When extracting epochs, it is possible to remove all but a selected set
of events from the data. For example, if there is only one event in an
epoch, the epoch table may look more readable. Using the tutorial
dataset after extracting data epochs, select item <font color=brown>Edit
\> Select epoch/event</font> in the menu, and then enter (in the pop-up
window below) "rt" in the *Event type* field, then select *Keep only
selected events and remove all other events* instead of *Remove epochs
not referenced by any event*. Press *OK* to create a new data set. Note:
This daughter (and its future child datasets, if any) contains no trace
(except in *EEG.urevent*) of all the events that actually occurred
during the experiment but were erased by this process. <u>Therefore, we
strongly recommend against using this option!</u>


![Image:Pop_selectevent.jpg](/assets/images/Pop_selectevent.jpg)


then typing

``` matlab
>> EEG.epoch(1)
```

returns

``` matlab

ans =

    event: 1
    eventlatency: 1.0823e+03
    eventposition: 2
    eventtype: 'rt'
    eventurevent: 3
```

This means that epoch number "1" contains a single event of type "rt" at
latency 1082.3 ms, it also indicates that this is the first event in the
dataset (i.e. *event: 1*), but note that it was the third event in the
original dataset, since its corresponding urevent (stored in
*EEG.event.urevent*) is "3".

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
using the (epoched) tutorial dataset, by adding a new class of (pseudo)
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
eeglab redraw % Redraw the main eeglab window
```

Event context (as more reliably retrieved from the 'EEG.urevent' table)
can be valuable in data analysis. For example, one may want to study all
events of a certain type (or set of types) that precede or follow events
of some other types by delays within a given range. A classic ERP
example was the demonstration by [Squires et
al.](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=pubmed&dopt=Abstract&list_uids=64341)
that the P300 peak was larger when a rare stimulus followed a string of
standard stimuli than when it followed other rare stimuli. The (v4.4)
command-line function { {File\|eeg_context.m} } looks for events of
specified *target* type(s), then for preceding and/or succeeding events
of specified *neighbor* type(s).

The script below is a simple demonstration script using {
{File\|eeg_context.m} } that finds target events in the sample dataset
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
equivalent, since each event occurs in a different *context*. Although
hard to dispute, insights into brain function to be gleaned from this
point of view are sacrificed when dynamics time-locked to all events of
a certain type are simply *averaged* together. In particular, the EEGLAB
{ {File\|erpimage.m} } and { {File\|pop_erpimage.m} } functions allow
users to visualize differences in potential time course or spectral
amplitudes in epochs time-locked to events sorted by some feature of
their context. A simple example is sorting stimulus-locked epoch by
subsequent response time ('rt'), though this is only a simple and
straightforward example. Using the { {File\|eeg_context.m} } function,
one might also sort stimulus event-locked epochs by the amount of time
since the *previous* button press, or by the fraction of 'position'=1
events in the last minute, etc. Some future EEGLAB functions (and many
user scripts) will no doubt exploit such possibilities in many ways.

