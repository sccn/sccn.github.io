---
layout: default
title: III.3 Event Processing
parent: III.Advanced topics
grand_parent: Tutorials
---
This tutorial complements information about EEGLAB event handling covered in other
parts of the EEGLAB tutorial. It first describe how to import, modify,
select, and visualize EEGLAB events, within the EEGLAB graphic
interface. It then describes in more details the *EEG.event*,
*EEG.urevent*, and related *EEG.epoch* structures, and discusses
importing, editing, and using event information in EEGLAB scripts. We
assume that readers are already familiar with the [single subject
tutorial](/I.Single_subject_data_processing_tutorial "wikilink") as well
as with the [EEGLAB script
tutorial](/Chapter_02:_Writing_EEGLAB_Scripts "wikilink").

<u>Important Note:</u> The EEGLAB event structure has evolved through
EEGLAB Version 4.4, after which we hope it may remain stable (note that
functions processing events are backward compatible with old event
structures).

Event Processing in the EEGLAB GUI
----------------------------------

### Getting started

The current section should help familiarize yourself with event handling
in EEGLAB. First start EEGLAB, and load dataset *eeglab_data.set* in the
*sample_data* folder using menu item <font color=brown>File \> Load
dataset</font>. Then use menu item <font color=brown>Plot \> Scroll
data</font> to visualize the data and associated events.


![575px](/assets/images/Scroll_raw_data.png)


Events are shown as vertical lines. Different event types are shown in
different colors. The button "Event types" will show the list of event
types for this dataset.

### Event fields

The EEG event structure contains records of the experimental events that
occurred while the data was being recorded, as well as structure
handling events which are automatically inserted by EEGLAB. To view the
information for an event, use menu <font color=brown>Edit \> Event
values\<</font> (see the window below, which shows events of the
tutorial dataset imported in the previous step.


![375px](/assets/images/V1pop_editeventvals.png)



The *type* and *latency* fields are the most important EEGLAB event
fields (see below). Some EEGLAB functions recognize and use these two
fields for plotting events, sorting trials, etc. (Note: One can also
process events lacking these fields, though this strongly limits the
range of event processing possibilities). Other fields, including
*epoch*, *duration*, *urevent*, are also recognized by EEGLAB (they are
created automatically during extracting of epochs, rejecting data, or
storing event data). User-defined fields can have any other name that is
relevant to the data (for example, *position* in the example above).
A short description of recognized event fields is given below. Further
information can be found in the event scripting section in the next
sections.
\*<u>type</u> - specifies the type of the event. For example, 'square'
in the example above is a stimulus type, 'rt' is a subject button-press
(i.e., reaction-time) event, etc... In continuous datasets, EEGLAB may
add events of type 'boundary' to specify data boundaries (breaks in the
continuous data). The next section on event scripting provides more
detailed information about this special event type.

-   <u>latency</u> - contains event latencies. The latency information
    is displayed in seconds for continuous data, or in milliseconds
    relative to the epoch's time-locking event for epoched data. As we
    will see in the event scripting section, the latency information is
    stored internally in data samples (points or EEGLAB 'pnts') relative
    to the beginning of the continuous data matrix (EEG.data).
-   <u>duration</u> - duration of the event. This information is
    displayed in seconds for continuous data, and in milliseconds for
    epoched data. Internally, duration is (also) stored in data samples
    (pnts).
-   <u>urevent</u> - contains indices of events in the original ('ur' in
    German) event structure. The first time events are imported, they
    are copied into a separate structure called the 'urevent' structure.
    This field is hidden in the graphic interface (above) since they
    should not be casually modified.
-   <u>epoch</u> - indices of the data epochs (if any) the event falls
    within. This field is only present for data for which data epochs
    have been extracted (which is not the case here since the data is
    continuous).


Note: all event fields may contain either numbers or strings (except for
*latency*, *duration*, *urevent* and *epoch* which must contain
numbers). For instance, the *type* field can contain a number (i.e. 1,2,
etc.) or a string (i.e. 'square', 'rt', etc.). However, EEGLAB cannot
process a mixture of both formats (numeric and string) for one field. A
function that checks the event structure ({ {File\|eeg_checkset.m} }
with flag *eventconsistency*), called each time a dataset is modified,
enforces each field's contents to remain consistent, automatically
converting numeric values to strings if necessary. This constraint was
imposed to speed up event manipulation by a factor of about 1000X.

### Importing, adding, and modifying events

Events can be imported into EEGLAB by selecting menu item
<font color=brown>File \> Import event info</font>. To find out more
about this option, refer to the [Importing Event and Epoch
Information](/A02:_Importing_Event_Epoch_Info "wikilink") which follows
the ["importing event information for a continuous EEG dataset"
tutorial](/A01:_Importing_Continuous_Epoched_Data "wikilink"). The same
method may also be used to add new events to a pre-existing event
table.

To insert new events manually, select menu item <font color=brown>Edit
\> Event values</font>. Click on the *Insert event* button to add a new
event before the current event. The *Append event* button adds an event
*after* the current event. After a new event has been inserted or
appended, its event-field information can immediately be changed in the
corresponding boxes. For instance, to insert a event of type *new* 500
ms after the onset of the time-locking stimulus, enter *new* in the
event *type* edit box, and 500 in the event *latency* edit box.
Note: If you then click on the *cancel* button, none of the new
information will be saved.


![375px](/assets/images/V121pop_editeventvals_2.png)



After you press *OK*, the events may be resorted (events must always be
in order of increasing latency), and some field contents may be modified
to ensure consistency, as indicated at the end of the previous
section.

In the graphic interface above, all experimental events can be manually
modified by simply typing the new values in the edit window for each
field. Events may also be deleted (*Delete event* button) or resorted
(see the bottom part of the window). Resorting events is only for
viewing purposes (as EEGLAB cannot process an event structure that is
not sorted by increasing event latency).

The [Vised EEGLAB plugin](https://github.com/jadesjardins/vised_marks)
available from the EEGLAB plugin manager allows user to manually add
events directly on the EEG browser and is convenient for marking events
of interest (such as blinks for example).

### Exporting events


Another way to modify new events is to export them, modify them under a
spreadsheet software and then import them back into EEGLAB. You may
import the tutorial data <i>eeglab_data.set</i> in the
<i>sample_data</i> under EEGLAB, then call menu item
<font color=brown>File \> Export \> Events to text file</font> and save
a data file. Using this data file, we show how to rename all events with
type "rt" to events with type "response" under a Spreadsheet software.


![600px](/assets/images/Spreadsheet_event.png)


Then using menu item <font color=brown>File \> Import event info \> From
Matlab array of ASCII file</font> we select the modified file. We enter
the column names, indicate that there is 1 line of header, and set the
unit latency to NaN (which indicate that no conversion is necessary). We
also uncheck the alignment option (although leaving it checked has no
effect). Now all the events have been renamed (note that the interface
to select events presented in a following section also allows to rename
event type values so this is only presented as didactic example).


![600px](/assets/images/Event_reimport.png)


### Selecting events

To select specific events, use menu item <font color=brown>Edit \>
Select epochs/events</font>. This can be exploited to compare different
types of data epochs, as described in the ["Selecting events and epochs
for two
conditions"](/Chapter_07:_Selecting_Data_Epochs_and_Comparing#Selecting_events_and_epochs_for_two_conditions "wikilink")
section of the main tutorial. That section describes a basic event
selection process. However, you can also specify more complex
combinations of event field selections and ranges as the criterion for
selecting trials. For instance, the window below would select epochs
containing events of type *rt*, not following stimuli presented at
'position' 1, in which subject reaction time latency is between 0 ms and
400 ms, from among the 40 first epochs of the parent dataset.
Note: The option set above the *Cancel* button (below): *Remove epochs
not referenced by any selected event*. If this checkbox were left unset
and the checkbox *Keep only selected events and remove all other
events*, the function would simply select the specified events but would
not remove epochs not containing those events.
Note: To select events outside the given range, check the *Select events
NOT selected above* box to the right of the field range entry. It is
possible to rename the type of the selected events (while (optionally)
keeping the old event type name as a new field) using the last two edit
boxes.


![Image:Pop_selectevent.jpg](/assets/images/Pop_selectevent.jpg)


### Using events for data processing

Event information can be used in several EEGLAB processing functions as
listed below.

1.  The event *type* field can be used to extract data epochs, as
    described in section ["I.5 Extracting data
    epochs"](/Chapter_05:_Extracting_Data_Epochs "wikilink"). Select
    menu option <font color=brown>Tools \> extract epochs</font> to open
    the window below.

    ![Image:Pop_epoch.jpg](/assets/images/Pop_epoch.jpg)



    This operation will extract epochs of duration one second before to
    two seconds after all events of type "square".

2.  Events can also be used for making ERP-image plots. Select
    <font color=brown>Plot \> Channel ERP image</font>. This brings up
    the { {File\|pop_erpimage.m} } window (below).

    ![Image:V123pop_erpimag.jpg](/assets/images/V123pop_erpimag.jpg)



    The *Epoch-sorting field* button allows you to choose any of the
    event fields as the sorting criteria. The next button, *Event
    type(s)*, enables you to choose only a subset of events. In this
    example, events of type "square" are sorted by their position field
    value. For more details see the ["Plotting ERP
    images"](/Chapter_08:_Plotting_ERP_images#Plotting_ERP_images_using_pop_erpimage.28.29 "wikilink")
    section of the main tutorial.

3.  Event statistics can be plotted with regard to different event
    fields. For example, selecting menu option <font color=brown>Plot \>
    Data statistic \> Event statistic</font> or in newer versions of
    EEGLAB typing <i>pop_eventstat(EEG);</i> on the Matlab command line,
    the following window pops up.

    ![Image:V14pop_eventstat.jpg](/assets/images/V14pop_eventstat.jpg)



    Entering 'rt' as the event type, and "\[250 500\]" (ms) as the event
    latency range, and pressing *OK* will show the following 'rt' event
    statistics.


    ![Image:V14eventstat.jpg](/assets/images/V14eventstat.jpg)



    See the ([rejection tutorial on data channel
    statistics](/Chapter_01:_Rejecting_Artifacts#Rejecting_data_channels_based_on_channel_statistics "wikilink"))
    for more information on this graphic interface.

4.  Most EEGLAB functions take events into account. For instance,
    functions that remove data ({ {File\|pop_eegplot.m} }, {
    {File\|pop_select.m} }) will also remove events that occur during
    the data removed (though not their corresponding urevents).
    Functions that process continuous data ({ {File\|pop_spectopo.m} },
    { {File\|pop_resample.m} }\], { {File\|pop_mergeset.m} }) will take
    into account 'boundary' events (data events added by EEGLAB to note
    portions of the data that have been removed or at 'hard' boundaries
    between concatenated datasets).

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

