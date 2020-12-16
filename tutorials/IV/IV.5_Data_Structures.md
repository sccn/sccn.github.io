---
layout: default
title: IV.5 Data Structures
parent: IV. Appendix
grand_parent: Tutorials
nav_order: 5
---

{ {Backward_Forward\|A4:_Exporting_Data\|A4: Exporting
Data\|A6:_Maximizing_Memory\|A6: Maximizing Memory} }

EEGLAB Data Structures
----------------------

This section is intended for users who wish to [use EEGLAB and its
functions in Matlab
scripts](/Chapter_02:_Writing_EEGLAB_Scripts "wikilink"). We have tried
to make EEG structures as simple and as transparent as possible so that
advanced users can use them to efficiently process their data.

#### EEG and ALLEEG

EEGLAB variable *EEG* is a Matlab structure that contains all the
information about the current EEGLAB dataset. For instance, following
the [single subject tutorial
documentation](/I.Single_subject_data_processing_tutorial "wikilink")
until data epochs have been extracted and the ICA decomposition
computed, and then typing *\>\>EEG* will produce the following command
line output:

``` matlab
>> EEG

    EEG =
        setname:        'Epoched from "ee114 continuous"'
        filename:       'ee114squaresepochs.set'
        filepath:       '/home/arno/ee114/'
        pnts:           384
        nbchan:             32
        trials:         80
        srate:          128
        xmin:           -1
        xmax:           1.9922
        data:           [32x384x80 double]
        icawinv:        [32x32 double]
        icasphere:      [32x32 double]
        icaweights:     [32x32 double]
        icaact:         []
        event:          [1x157 struct]
        epoch:          [1x80 struct]
        chanlocs:       [1x32 struct]
        comments:       [8x150 char]
        averef:         'no'
        rt:         []
        eventdescription:   {1x5 cell}
        epochdescription:   {}
        specdata:       []
        specicaact:     []
        reject:         [1x1 struct]
        stats:          [1x1 struct]
        splinefile:     []
        ref:            'common'
        history:        [7x138 char]
        urevent:        [1x154 struct]
        times:          [1x384 double]
```

Above, we have italized several important fields. See the help message
of the [eeg_checkset.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_checkset.m) function (which checks the consistency
of EEGLAB datasets) for the meaning of all the fields.

EEGLAB variable *ALLEEG* is a Matlab array that holds all the datasets
in the current EEGLAB/Matlab workspace. In fact *ALLEEG* is a structure
array of *EEG* datasets (described above). If, in the current EEGLAB
session you have two datasets loaded, typing *\>\> ALLEEG* on the Matlab
command line returns:

``` matlab
ALLEEG =
    1x2 struct array with fields:
        setname
        filename
        filepath
        pnts
        nbchan
        trials
        srate
        xmin
        xmax
        data
        icawinv
        icasphere
        icaweights
        icaact
        event
        epoch
        chanlocs
        comments
        averef
        rt
        eventdescription
        epochdescription
        specdata
        specicaact
        reject
        stats
        splinefile
        ref
        history
        urevent
        times
```

Typing *\>\> ALLEEG(1)* returns the structure of the first dataset in
ALLEEG, and typing *\>\> ALLEEG(2)* returns the structure of the second
dataset. See the [Script
Tutorial](/Chapter_02:_Writing_EEGLAB_Scripts "wikilink") for more
information on manipulating these structures.
Most fields of the *EEG* structure contain single values (as detailed in
[eeg_checkset.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_checkset.m)). However some important fields of the *EEG*
structure contain sub-structures. We will describe briefly three of
those below: *EEG.chanlocs*, *EEG.event*, and *EEG.epoch*.

#### EEG.chanlocs

This EEG-structure field stores information about the EEG channel
locations and channel names. For example, loading the tutorial dataset
and typing *\>\> EEG.chanlocs* returns

``` matlab
>> EEG.chanlocs

    ans =

    1x32 struct array with fields:
        theta
        radius
        labels
        sph_theta
        sph_phi
        sph_radius
        X
        Y
        Z
```

Here,*EEG.chanlocs* is a structure array of length 32 (one record for
each of the 32 channels in this dataset). Typing *\>\>EEG.chanlocs*
returns:

``` matlab
>> EEG.chanlocs(1)

    ans =
        theta:      0
        radius:     0.4600
        labels:     'FPz'
        sph_theta:  0
        sph_phi:    7.200
        sph_radius: 1
        X:      0.9921
        Y:      0
        Z:      0.1253
```

These values store the channel location coordinates and label of the
first channel ('FPz'). You may use the [pop_chanedit.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_chanedit.m)
funciton or menu item <font color=brown>Edit \> Channel locations</font>
to edit or recompute the channel location information. The value of any
EEG structure field may also be modified manually from the Matlab
command line. See also the [EEGLAB channel location file database
page](http://sccn.ucsd.edu/eeglab/channellocation.html) and the main
tutorial section regarding ['Using channel
locations'](/Chapter_02:_Channel_Locations "wikilink").

#### EEG.event

The EEG structure field contains records of the experimental events that
occurred while the data was being recorded, plus possible additional
user-defined events. Loading the tutorial dataset and typing

``` matlab
>> EEG.event

    ans =
        1x157 struct array with fields:
            type
            position
            latency
            urevent
```

In general, fields *type*, *latency*, and *urevent* are always present
in the event structure. *type* contains the event type. *latency*
contains the event latency in data point unit. *urevent* contains the
index of the event in the original (= "ur") urevent table (see below).
Other fields like *position* are user defined and are specific to the
experiment. The user may also define a field called *duration*
(recognized by EEGLAB) for defining the duration of the event (if
portions of the data have been deleted, the field *duration* is added
automatically to store the duration of the break (i.e. boundary) event).
If epochs have been extracted from the dataset, another field, *epoch*,
is added to store the index of the data epoch(s) the event belongs to.
To learn more about the EEGLAB event structure, see the [event
processing tutorial](/Chapter_03:_Event_Processing "wikilink").
There is also a separate "ur" (German for "original") event structure,
*EEG.urevent* (in EEGLAB v4.2 and above), which holds all the event
information that was originally loaded into the dataset plus events that
were manually added by the user. When continuous data is first loaded,
the content of this structure is identical to contents of the
*EEG.event* structure (minus the *urevent* pointer field of
*EEG.event*). However, as users remove events from the dataset through
artifact rejection or extract epochs from the data, some of the original
(ur) events continue to exist only in the urevent structure.

The *urevent* field in the EEG.event structure above contains the index
of the same event in the *EEG.urevent* structure array. For example: If
a portion of the data containing the second urevent were removed from a
dataset during artifact rejection, the second event would <u>not</u>
remain in the *EEG.event* structure -- but would still remain in the
*EEG.urevent* structure. Now, the second event left in the data might be
the original third event, and so will be linked to the third
*EEG.urevent*, i.e. checking

``` matlab
>> EEG.event(2).urevent

    ans =
        3
```

<u>**WARNING:** </u>Datasets created under EEGLAB 4.1 and loaded into
4.2 had an *EEG.urevent* structure created automatically. If some data
containing events had been rejected BEFORE this time, then the urevent
structure information IS INCOMPLETE (i.e. to some degree wrong!). Most
new datasets created under 4.2 had the urevent structure saved correctly
when the event information was first added. Be cautious about using
urevent information from legacy 4.1 datasets.

You may refer to the [Event Processing
Tutorial](/Chapter_03:_Event_Processing "wikilink") for more details on
the event and urevent stuctures.

#### EEG.epoch

In an epoched dataset, this structure is similar to the *EEG.event*
structure, except that there is only one record for each epoch. Note
that EEGLAB functions never use the epoch structure. It is computed from
the *EEG.event* structure by the [eeg_checkset.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_checkset.m) function
(using flag 'eventconsistency') as a convenience for users who may want
to use it to write advanced EEGLAB scripts. For the tutorial dataset,
after extracting data epochs the epoch structure looks like this:

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

        event:      [1 2 3]
            eventlatency:   {[0] [695.2650] [1.0823e+03]}
        eventposition:  {[2] [2] [2]}
        eventtype:  {'square' 'square' 'rt'}
        eventurevent:   {[1] [2] [3]}
```


The first field *EEG.epoch.event* is an array containing the indices of
all dataset events that occurred during this epoch. The fields
*EEG.epoch.eventtype*, *EEG.epoch.eventposition* and
*EEG.epoch.eventlatency* are cell arrays containing values for each of
the events (*EEG.epoch.event*) that occurred during the epoch. Note that
the latencies in *EEG.epoch.eventlatency* have been recomputed in units
of milliseconds with respect to the epoch time-locking event. When there
is only one event in an epoch, the epoch table is more readable.

You may refer to the [Event Processing
Tutorial](/Chapter_03:_Event_Processing "wikilink") for more details.

The next section will cover the supervening data structure, new as of
EEGLAB v5.0b, the *STUDY* or *studyset*.

[Category:IV. Appendix](/Category:IV._Appendix "wikilink") {
{Backward_Forward\|A4:_Exporting_Data\|A4: Exporting
Data\|A6:_Maximizing_Memory\|A6: Maximizing Memory} }
