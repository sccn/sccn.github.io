---
layout: default
title: EEGLAB data structures
parent: Concepts guide
grand_parent: Tutorials
nav_order: 5
---
EEGLAB Data Structures
=======================

This section is intended for users who wish to [use EEGLAB and its
functions in Matlab scripts](tutorials/III.2 Writing EEGLAB Scripts). We have tried
to make EEG structures as simple and as transparent as possible so that
advanced users can use them to efficiently process their data.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

EEG and ALLEEG
---------------
EEGLAB variable *EEG* is a Matlab structure that contains all the
information about the current EEGLAB dataset. For instance, following
the [single subject tutorial documentation](/I.Single_subject_data_processing_tutorial "wikilink")
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
dataset. See the [Script Tutorial](/Chapter_02:_Writing_EEGLAB_Scripts "wikilink") for more
information on manipulating these structures.
Most fields of the *EEG* structure contain single values (as detailed in
[eeg_checkset.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_checkset.m)). However some important fields of the *EEG*
structure contain sub-structures. We will describe briefly three of
those below: *EEG.chanlocs*, *EEG.event*, and *EEG.epoch*.

### EEG.chanlocs

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
each of the 32 channels in this dataset). 

Typing *\>\>EEG.chanlocs*
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
function or menu item <span style="color: brown">Edit → Channel locations</span>
to edit or recompute the channel location information. The value of any
EEG structure field may also be modified manually from the Matlab
command line. See also the [EEGLAB channel location file database
page](http://sccn.ucsd.edu/eeglab/channellocation.html) and the main
tutorial section regarding ['Using channel
locations'](/Chapter_02:_Channel_Locations "wikilink").

### EEG.event

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
in the event structure:

- *type* contains the event type
- *latency* contains the event latency in data point unit
- *urevent* contains the
index of the event in the original (= "ur") urevent table (see below).

Other fields like *position* are user defined and are specific to the
experiment. 

The user may also define a field called *duration*
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

<u>**WARNING:** </u>

Datasets created under EEGLAB 4.1 and loaded into
4.2 had an *EEG.urevent* structure created automatically. If some data
containing events had been rejected BEFORE this time, then the urevent
structure information IS INCOMPLETE (i.e. to some degree wrong!). Most
new datasets created under 4.2 had the urevent structure saved correctly
when the event information was first added. Be cautious about using
urevent information from legacy 4.1 datasets.

You may refer to the [Event Processing Tutorial](/Chapter_03:_Event_Processing "wikilink") for more details on
the event and urevent stuctures.

### EEG.epoch

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
all dataset events that occurred during this epoch. 

The fields
*EEG.epoch.eventtype*, *EEG.epoch.eventposition* and
*EEG.epoch.eventlatency* are cell arrays containing values for each of
the events (*EEG.epoch.event*) that occurred during the epoch. Note that
the latencies in *EEG.epoch.eventlatency* have been recomputed in units
of milliseconds with respect to the epoch time-locking event. 

When there
is only one event in an epoch, the epoch table is more readable.

You may refer to the [Event Processing Tutorial](/Chapter_03:_Event_Processing "wikilink") for more details.

The STUDY structure
---------
This section gives details of EEGLAB structures necessary for writing
custom Matlab scripts, functions, and plug-ins that operate on EEGLAB
STUDY structures and studysets.

The *STUDY* structure contains information for each of its datasets,
plus additional information to allow processing of all datasets
sequentially. After clustering the independent components identified for
clustering in each of the datasets, each of the identified components in
each dataset is assigned to one component cluster (in addition to
Cluster 1 that contains all components identified for clustering). The
*STUDY* structure also contains the details of the component clusters.

Below is a prototypical *STUDY* structure. In this tutorial, the
examples shown were collected from analysis of a small sample studyset
comprising ten datasets, two conditions from each of five subjects.
After loading a studyset (see previous sections, or as described below)
using the function { {File\|pop_loadstudy.m} }, typing *STUDY* on Matlab
command line will produce results like this:

``` matlab
>> STUDY

STUDY =

    name:       'N400STUDY'
    filename:   'OctN400ClustEditHier.study'
    filepath:   '/eeglab/data/N400/'
    datasetinfo:    [1x10 struct]
    session:    []
    subject:    {1x5 cell}
    group:      {'old' 'young'}
    condition:  {'non-synonyms' 'synonyms'}
    setind:     [2x5 double]
    cluster:    [1x40 struct]
    notes:      ' '
    task:       'Auditory task: Synonyms Vs. Non-synonyms, N400'
    history:    [1x4154 char]
    etc:        [1x1 struct]
```

The field *STUDY.datasetinfo* is an array of structures whose length is
the number of datasets in the *STUDY*. Each structure stores information
about one of the datasets, including its subject, condition, session,
and group labels. It also includes a pointer to the dataset file itself
(*as explained below in more detail*).

*STUDY.datasetinfo* sub-fields *subject*, *group*, *session* and
*condition* label the subject, subject group, session, and condition
associated with each dataset in the study. This information must be
provided by the user when the *STUDY* structure is created. Otherwise,
default values are assumed.

The *STUDY.cluster* field is an array of cluster structures, initialized
when the *STUDY* is created and updated after clustering is performed
(*as explained below in more detail*).

The *STUDY.history* field is equivalent to the *history* field of the
*EEG* structure. It stores all the command line calls to the functions
from the gui. For basic script writing using command history
information, see the [EEGLAB script writing tutorial](/tutorials//III/III.2_Writing_EEGLAB_Scripts).

The *STUDY.etc* field contains internal information that helps manage
the use of the *STUDY* structure by the clustering functions. In
particular, pre-clustering data are stored there before clustering is
performed.

### The STUDY.datasetinfo sub-structure
The *STUDY.datasetinfo* field is used for holding information on the
datasets that are part of the study. Below is an example *datasetinfo*
structure, one that holds information about the first dataset in the
*STUDY* :

``` matlab
>> STUDY.datasetinfo(1)

    ans =

        filepath:   '/eeglab/data/N400/S01/'
        filename:   'syn01-S253-clean.set'
        subject:    'S01'
        group:      'young'
        condition:  'synonyms'
        session:    1
        trialinfo:  [1×426 struct]
        comps:      [3 5 6 7 8 9 11 13 14 15 16 17 19 20 21 24 25 28 29 34 35 44 52]
        index:      1
```

This information was posted when the *STUDY* was created by the user.

The *datasetinfo.filepath* and *datasetinfo.filename* fields give the
location of the dataset on disk.

The *datasetinfo.subject* field attaches a subject code to the dataset.
Note: Multiple datasets from the same subject belonging to a *STUDY* are
stored under different datasetinfo entries and are usually distinguished
as being in different experimental conditions and/or as representing
different experimental sessions.

The *datasetinfo.group* field attaches a subject group label to the
dataset.

The *datasetinfo.condition* and *datasetinfo.session* fields hold
dataset condition and session labels. If the *condition* field is empty,
all datasets are assumed to represent the same condition. If the
*session* field is empty, all datasets in the same condition are assumed
to have been recorded in different sessions.

The *datasetinfo.index* field holds the dataset index in the *ALLEEG*
vector of currently-loaded dataset structures. It is redundant but
useful when the the substructure is used as input to another function
(i.e.: *datasetinfo.index = 1* must correspond to *ALLEEG(1)*
(typically, the first dataset loaded into EEGLAB), *datasetinfo.index =
2* to *ALLEEG(2)*, etc).

The *datasetinfo.comps* field holds indices of the components of the
dataset that have been designated for clustering. When it is empty, all
of its components are to be clustered.

The *datasetinfo.trialinfo* field holds information about each data
trial. It is empty for continuous data. This field allow to create
contrast between trials within a given dataset and is described below.

``` matlab
STUDY.datasetinfo(1).trialinfo(1)

ans =

  struct with fields:

           chan: 0
    description: 'syn'
       duration: 128
         points: 1
           type: 'S253'
```

The fields in the trialinfo data structure mirror the field in the event
structure of the datasets (the fields are the same as in EEG.event). The
field "type" contains the type of stimulus. The fields "duration"
indicates the duration of presentation of the stimulus in samples. Other
fields ("chan", "description", "points") contain information specific to
a given dataset. In general, a different dataset will contain different
fields. 

See
[Definition_of_STUDY_design_independent_variables](/Chapter_07:_EEGLAB_Study_Data_Structures#Definition_of_STUDY_design_independent_variables "wikilink")
for additional information on how this structure is created and how to
create custom field.

### The STUDY.design sub-structure
For the purpose of performing inference testing, any (m x n) design is
possible (including choosing independent variables from among
conditions, groups, sessions, particular stimulus-related trials, or
other trial subsets). Below is a description of the STUDY design fields.

This is the current (v2019) STUDY.design sub-structure:

``` matlab
  STUDY.design(1)

  ans =

             name: 'Design 1 - compare letter types'
         variable: [1x2 struct]
            cases: [1x1 struct]
         filepath: ''
          include: {}
```

Exploding the contents of each of these sub-structures, we obtain

``` matlab
             name: 'Design 1 - light and audio all subjects'

         variable: [1x2 struct]
                 label: 'condition'
               pairing: 'on'
                 value: {'ignore'  'memorize'  'probe'}
               vartype: 'categorical'

           cases: [1x1 struct]
              label: 'subject'
              value: {'S01'  'S02'  'S03'  'S04'  'S05'  'S06' }

         include: {}
```

-   The "variable" field stands for "independent variable." Currently,
    up to two independent variables may be defined when using EEGLAB
    standard plotting functions (when using the LIMO extension to EEGLAB
    for calculating statistics and plotting results, an arbitrary number
    of independent variables may be used). STUDY.design(x).variable(1)
    contains the description of the first independent variable for STUDY
    design number x, and STUDY.design(x).variable(2) contains the
    description of the second independent variable (if any). Each
    independent variable has a 'label', a pairing status ('on', for
    paired data and 'off' for unpaired data), associated values, and a
    type (categorical or continuous - note that continuous variable are
    only relevant when using the LIMO extension to EEGLAB). For
    instance, in this specific example the independent variable
    'condition' may take the values 'ignore', 'memorize' and 'probe'. As
    detailed in the graphic interface STUDY.design section, values may
    be combined by concatenating the value labels and separating them
    with a '-' character. For instance 'memorize - probe' is a new value
    for the variable 'condition' and it points to datasets containing
    either the 'memorize' or the 'probe' stimuli.


-   The "cases" field contains the descriptions of the single 'cases' (a
    term adopted in statistics from clinical studies). Using the current
    interface, it is not possible to define "cases" other than subjects
    (although when plotting single subjects, selecting the option to use
    single trials for statistics automatically makes 'cases equivalent
    to 'trials'). In future versions, it will be possible to use an
    arbitrary variable for case.


-   The "filepath" field is the path where the data files are being
    stored.

<!-- -->

-   The "include" field is a list of independent variables and values to
    include in the design - for instance, to include "memorize" stimuli
    only (and ignore all subject datasets (or, for single-trial
    statistics, all trials) that do not have this independent variable
    value.

#### Definition of STUDY design independent variables

Most independent variables are defined in the main STUDY interface when
creating a STUDY. "condition", "group" and "session" are independent
variables defined in the first STUDY editing GUI. In addition to these
variables, EEGLAB extracts independent variables for each subset of data
epochs based on epoch field information for the time-locking event in
each dataset. The function <i>std_maketrialinfo</i> creates the
"trialinfo" substructure in STUDY.datasetinfo. For instance, the first
dataset in the STUDY may have the properties:

``` matlab
  STUDY.datasetinfo(1).condition = 'a';
  STUDY.datasetinfo(1).group = 'g1';
  STUDY.datasetinfo(1).trialinfo(1).presentation = 'evoked';
  STUDY.datasetinfo(1).trialinfo(2).presentation = 'evoked';
  STUDY.datasetinfo(1).trialinfo(3).presentation = 'evoked';
  STUDY.datasetinfo(1).trialinfo(4).presentation = 'spontaneous1';
  STUDY.datasetinfo(1).trialinfo(5).presentation = 'spontaneous1';
  STUDY.datasetinfo(1).trialinfo(6).presentation = 'spontaneous1';
  STUDY.datasetinfo(1).trialinfo(7).presentation = 'spontaneous2';
  STUDY.datasetinfo(1).trialinfo(8).presentation = 'spontaneous2';
  STUDY.datasetinfo(1).trialinfo(9).presentation = 'spontaneous2';
```

The "trialinfo" structure describes the property of each trial for
dataset number 1. Trial number 1,2,3 are trials of presentation type
"evoked", whereas trials 4,5,6 are trials of presentation type
"spontaneous1" and trials 7,8,9 are trials of presentation type
"spontaneous2".

For a given trial, only the information of the time-locking event is
reported. If there is other information of interest in other events of a
given trial (like reaction time for example), it needs to be added as a
field to the time locking event (for example EEG.events(1).rt = 1231
indicating a reaction time of 1231 ms for that trial). This has to be
performed using a script and cannot be performed yet on the graphic
interface.

If you want to add an independent variable, simply write a script that
scans the EEG.event structure for each dataset and add a relevant field
for the time locking event (event at time 0) of each data trial. For
example, you may add the field "previous_event_type" that would contain
the type of previous event. Once you create the STUDY, this field will
automatically taken into account and appears in the STUDY design
interface. Below is an example of a simple script performing that
function on a *STUDY* containing datasets in which trials have been
extracted. All the datasets are assumed to contain multiple trials and
have only two event types (TLE for time locking events usually
immediately followed by RT for reaction time). Note that when a reaction
time is missing for a given trial, it will be dealt with appropriately
at the *STUDY* level.

``` matlab
% Scan all datasets in the study
for iDat = 1:length(ALLEEG)

     for iEvent = 1:length(ALLEEG(iDat).event)-1

           curEvent = ALLEEG(iDat).event(iEvent)
           nextEvent = ALLEEG(iDat).event(iEvent+1)

           % only find reaction time event following time-locking events (TLE) within the same epoch
           if strcmpi( curEvent.type, 'TLE') && strcmpi( nextEvent.type, 'RT') && nextEvent.epoch == curEvent.epoch

                   ALLEEG(iDat).event(iEvent).rt = (nextEvent.latency - curEvent.latency)/ALLEEG(iDat).srate * 1000; % latency of reaction time in ms

           end

           % resave dataset
           ALLEEG(iDat).saved = 'no';
           ALLEEG(iDat) = pop_saveset(ALLEEG(iDat), 'savemode', 'resave');
     end
end

STUDY = std_maketrialinfo(STUDY, ALLEEG); % update STUDY structure with the new information
```

The function <i>std_makedesign</i> (or its GUI equivalent
<i>pop_studydesign</i>) uses the information defined above to create
STUDY designs. The content for 'variable1' entry of the
<i>std_makedesign</i> function can be either a field of 'datasetinfo' or
a field of 'datasetinfo.trialinfo'. Fields from 'trialinfo' are used in
a similar way to fields of STUDY.datasetinfo structure. For instance if
the STUDY.datasetinfo is defined as above.

To call std_makestudy(), simply say

``` matlab
  STUDY = std_makedesign(STUDY, ALLEEG, 1, 'variable1', 'condition');
```

This will create

``` matlab
  STUDY = std_makedesign(STUDY, ALLEEG, 1, 'variable1', 'presentation');
```

To select specific values for 'presentation'

``` matlab
  STUDY = std_makedesign(STUDY, ALLEEG, 1, 'variable1', 'presentation', 'values1', { 'spontaneous1' 'spontaneous2' } );
```

### The STUDY.changrp sub-structure

The *STUDY.changrp* sub-structure is the equivalent of the the
*STUDY.cluster* structure for data channels. There is usually as many
element in *STUDY.changrp* as there are data channels. Each element of
*STUDY.changrp* contains one data channels and regroup information for
this data channel accross all subjects. For instance, after precomputing
channel measures, typing *STUDY.changrp(1)* may return

``` matlab
>> STUDY.changrp

    ans =

    1x14 struct array with fields:
        name
        channels
        chaninds
```

The *changrp.name* field contains the name of the channel (i.e. 'FP1').
The *changrp.channels* field contains the name of the channels in this
group. This is because a group may contain several channels (for
instance for computing measures like ERP across a group of channels, or
for instance for computing the RMS across all data channels; note that
these features are not yet completely supported in the GUI).

### The STUDY.cluster sub-structure

The *STUDY.cluster* sub-structure stores information about the
clustering methods applied to the *STUDY* and the results of clustering.
Components identified for clustering in each *STUDY* dataset are each
assigned to one of the several resulting component clusters. Hopefully,
different clusters may have spatially and/or functionally distinct
origins and dynamics in the recorded data. For instance, one component
cluster may account for eye blinks, another for eye movements, a third
for central posterior alpha band activities, etc. Each of the clusters
is stored in a separate *STUDY.cluster* field, namely,
*STUDY.cluster(2)*, *STUDY.cluster(3)*, etc...

The first cluster, *STUDY.cluster(1)* , is composed of all components
from all datasets that were identified for clustering. It was created
when the STUDY was created and is not a result of clustering; it is the
*ParentCluster*. This cluster does not contain those components whose
equivalent dipole model exhibit a high percent variance from the
component's scalp map. These components have been excluded from
clustering (see
[Chapter_02:_STUDY_Creation\#Editing_STUDY_datasets](/Chapter_02:_STUDY_Creation#Editing_STUDY_datasets "wikilink")
for more information on how to exclude components from clustering.
Typing *STUDY.cluster* at the Matlab command line returns

``` matlab
>> STUDY.cluster

    ans =

    1x23 struct array with fields:
        name [string]
        parent [integer]
        child [cell]
        comps [array]
        sets [array]
        algorithm [cell]
        preclust [struct]
        topo [2-D array]
        topox [array]
        topoy [array]
        topoall [cell]
        topopol [array]
        dipole [struct]
```

All this information (including the clustering results) may be accessed
from the Matlab command line, or by using the interactive function {
{File\|pop_clustedit.m} }.
 
 Use of this function is explained at [Editing
clusters](/Chapter_05:_Component_Clustering_Tools#Editing_clusters "wikilink").

EEGLAB version 14 use to contain more information pertaining to each
cluster (such as the ERP, Spectrum and time-frequency data for a given
cluster) and this information would be made available in this structure
when a given cluster was plotted. These arrays were accessible to users
but were mostly cached values used for plotting purposes (so EEGLAB
would not have to reload them every time they were being plotted).

EEGLAB 2019 and later version have adopted a simpler cache approach
where all the plotted data is stored in the STUDY.cache structure. To
access this information, it is now recommended to use the return values
of the plotting functions std_erpplot, std_specplot, and std_erspplot -
if necessary disabling plotting. If the data is available in the STUDY
cache, then the cached values are automatically returned.

The *cluster.name* sub-field of each cluster is initialized according to
the cluster number, e.g. its index in the cluster array (for example:
'cls 2', 'cls 3', etc.). These cluster names may be changed to any
(e.g., more meaningful) names by the user via the command line or via
the { {File\|pop_clustedit.m} } interface.

The *cluster.comps* and *cluster.sets* fields describe which components
belong to the current cluster: *cluster.comps* holds the component
indices and *cluster.sets* the indices of their respective datasets.
(Note that this did not change in EEGLAB v9 that added STUDY.design
capabilities). Note also that several datasets may use the same
component weights and scalp maps -- for instance two datasets containing
data from different experimental conditions for the same subject and
collected in the same session, therefore using the same ICA
decomposition.

The *cluster.preclust* sub-field is a sub-structure holding
pre-clustering information for the component contained in the cluster.
This sub-structure includes the pre-clustering method(s), their
respective parameters, and the resulting pre-clustering PCA data
matrices (for example, mean component ERPs, ERSPs, and/or ITCs in each
condition). Additional information about the *preclust* sub-structure is
given in the following section in which its use in further (hierarchic)
sub-clustering is explained.

The *cluster.centroid* field holds the cluster measure centroids for
each measure used to cluster the components (e.g., the mean or centroid
of the cluster component ERSPs, ERPs, ITCs, power spectra, etc. for each
*STUDY* condition), plus measures not employed in clustering but
available for plotting in the interactive cluster visualization and
editing function, { {File\|pop_clustedit.m} }.

The *cluster.algorithm* sub-field holds the clustering algorithm chosen
(for example *kmeans*) and the input parameters that were used in
clustering the pre-clustering data.

The *cluster.parent* and *cluster.child* sub-fields are used in
hierarchical clustering (see [Hierarchic
Clustering](/Chapter_05:_Component_Clustering_Tools#Hierarchic_sub-clustering_.28PCA_method_only.29 "wikilink")).

The *cluster.child* sub-field contains indices of any clusters that were
created by clustering on components from this cluster (possibly,
together with additional cluster components). The *cluster.parent* field
contains the index of the parent cluster.

The *cluster.topo* field contains the average topography of a component
cluster. Its size is 67x67 and the coordinate of the pixels are given by
*cluster.topox* and *cluster.topoy* (both of them of size \[1x67\]).
This contains the interpolated activity on the scalp so different
subjects having scanned electrode positions may be visualized on the
same topographic plot. The *cluster.topoall* cell array contains one
element for each component and condition. The *cluster.topopol* is an
array of -1s and 1s indicating the polarity for each component.
Component polarities are not fixed, in the sense that inverting both one
component activity and its scalp map does not modify the back-projection
of the component to the data channels). The true scalp polarity is taken
into account when displaying component ERPs.

Finally, the *cluster.dipole* structure contains the centroid equivalent
dipole location of the component cluster. This structure is the same as
for a single component dipole ([see DIPFIT2
tutorial](/A08:_DIPFIT#DIPFIT_structure_and_functions "wikilink")).

Continuing with the hierarchical design introduced briefly above (in
[Hierarchic
Clustering](/Chapter_05:_Component_Clustering_Tools#Hierarchic_sub-clustering_.28PCA_method_only.29 "wikilink")),
suppose that Cluster 2 (*artifacts*) comprises 15 components from four
of the datasets. The *cluster* structure will have the following
values:

``` matlab
>> STUDY.cluster(2)

    ans =

        name:       'artifacts'
        parent:     {'ParentCluster 1'}
        child:      {'muscle 4' 'eye 5' 'heart 6'}
        comps:      [6 10 15 23 1 5 20 4 8 11 17 25 3 4 12]
        sets:       [1 1 1 1 2 2 2 3 3 3 3 3 4 4 4]
        algorithm:  {'Kmeans' [2]}
        preclust:   [1x1 struct]
```

This structure field information says that this cluster has no other
*parent* cluster than the *ParentCluster* (as always, Cluster 1), but
has three *child* clusters (Clusters 4, 5, and 6). It was created by the
'Kmeans' *algorithm* and the requested number of clusters was '2'. Note
that as of EEGLAB 2019, we do not recommend using hierarchical
clustering. Often simple cluster can achieve similar or better results.

Preclustering details are stored in the *STUDY.cluster(2).preclust*
sub-structure (not shown above but detailed below). For instance, in
this case, the *cluster.preclust* sub-structure may contain the
PCA-reduced mean activity spectra (in each of the two conditions) for
all 15 components in the cluster.

The *cluster.preclust* sub-structure contains several fields, for
example:

``` matlab
>> STUDY.cluster(2).preclust

    ans =

        preclustdata:   [15x10 double]
        preclustparams: { {1x9 cell} }
        preclustcomps:  {1x4 cell}
```

The *preclustparams* field holds an array of cell arrays. Each cell
array contains a string that indicates what component measures were used
in the clustering (e.g., component spectra (*spec*), component ersps
(*ersp*), etc...), as well as parameters relevant to the measure. In
this example there is only one cell array, since only one measure (the
power spectrum) was used in the clustering.


For example:

``` matlab
>> STUDY.cluster(1).preclust.preclustparams

    ans =

        'spec' 'npca' [10] 'norm' [1] 'weight' [1] 'freqrange' [3 25]
```

The data measures used in the clustering were the component spectra in a
given frequency range ('' ‘freqrange' \[3 25\]*), the spectra were
reduced to 10 principal dimensions (* 'npca' \[10\]*), normalized (*
'norm' \[1\]*), and each given a weight of 1 (* 'weight' \[1\]''). When
more than one method is used for clustering, then *preclustparams* will
contain several cell arrays.
The *preclust.preclustdata* field contains the data given to the
clustering algorithm (*Kmeans*). The data size width is the number of
ICA components (15) by the number of retained principal components of
the spectra (10) shown above. To prevent redundancy, only the measure
values of the 15 components in the cluster were left in the data. The
other components' measure data was retained in the other clusters.

The *preclust.preclustcomps* field is a cell array of size (nsubjects x
nsessions) in which each cell holds the components clustered (i.e., all
the components of the parent cluster).

#### Understanding the .sets, .comps substructures for STUDY clusters

In this part, *clust* will indicate the current cluster of interest.
STUDY.cluster(clust).sets and STUDY.cluster(clust).comps fields contain
the list of component included in a given cluster.
STUDY.cluster(clust).sets is a \[datasets_with_same_ica x ncomps\]
matrix giving the index of the corresponding dataset in
STUDY.datasetinfo and corresponds to the components listed in
STUDY.cluster(clust).comps. STUDY.cluster(clust).sets and
STUDY.cluster(clust).comps have the same number of columns. However,
STUDY.cluster(clust).sets may have several rows if some datasets (from
the same subject) have the same ICA decomposition - an example is given
below of a cluster when each component is contained in two datasets (2
rows for the .sets field) containing identical ICA decompositions.

``` matlab
>> STUDY.cluster(clust)
ans =
         name: 'Cls 3'
         sets: [2x13 double]
        comps: [23 5 13 47 38 3 50 5 12 4 11 3 5]
       parent: {'Parentcluster 1'}
```

If, for some reasons, the STUDY.cluster(clust).sets in not homogeneous –
some subjects have several datasets with the same decompositions and
other subjects have a different number of datasets with the same
decompositions, NaN are inserted for the missing datasets. However, the
presence of these missing datasets may break some analysis (warning
messages are displayed when relevant).

### STUDY data files

When pre-computing measures for a specific STUDY design, some files are
saved on disk. These files have names such as

``` matlab
  S01.daterp  % ERP data for data channels
  S01.icaerp  % ERP data for ICA components
  S01.datspec % Spetrum data for data channels
  S01.icaspec % Spetrum data for ICA components
  S01.dattimef % Single-trial time-frequency data for data channels
  S01.icatimef % Single-trial time-frequency data for ICA components
  S01.daterpim % ERPIMAGE data for data channels
  S01.icaerpim % ERPIMAGE data for ICA components
  S01.icatopo  % ICA component topographies
```

<b>S01</b> indicate that these files are for subject 1. The name of the
file is based on the naming convention in your *STUDY*. If the first
subject is named "xx01" then the file name will start with "xx01". This
is also why subject should not simply be numbers (1, 2, 3, etc...) as
most operating systems will not allow saving files that start with a
number.

Note that the file naming convention for version of EEGLAB older than
2019 (EEGLAB 12, 13 and 14) was slightly different, and that the files
needed to be recomputed for each study design (which is not the case for
EEGLAB 2019 and later versions). Also in old versions of EEGLAB, there
were two additional files xxxx.datersp and xxxx.datitc that contained
average time-frequency decompositions - since all files now contain
single trial data, these files have been removed.

The file structure is similar for all file types listed below.

``` matlab
>> fileContent = load('-mat', 'S01.daterp');
>> fileContent

         chan1: [750×784 single]
         chan2: [750×784 single]
         chan3: [750×784 single]
         chan4: [750×784 single]
         chan5: [750×784 single]
         ...
        chan70: [750×784 single]
        chan71: [750×784 single]
        labels: {1×71 cell}
         times: [1×750 double]
      datatype: 'ERP'
    parameters: {'rmcomps'  {1×3 cell}  'interp'  [1×71 struct]}
     datafiles: {'/data/data/STUDIES/STERN/S01/Memorize.set'  '/data/data/STUDIES/STERN/S01/Ignore.set'  '/data/data/STUDIES/STERN/S01/Probe.set'}
     trialinfo: [1×784 struct]
```

The fields chan<b>x</b> represent ERP data for these channels. For ICA
components, the prefix is <i>comp</i> instead of <i>chan</i>. Each
channel data will contain an array for time x trials. Below a
description of the additional fields:

-   <b>labels</b>: the cell array contain the channel labels { 'Cz' 'Pz'
    ... }. This field is only present for data channels and is not
    present for ICA components.
-   <b>datatype</b>: contains the type of data saved in the file. More
    details are provided below.
-   <b>parameters</b>: the list of parameters that was used to compute
    this file.
-   <b>datafile</b>: the list of files used to compute this file.
-   <b>trialinfo</b>: information about each data trial. This is similar
    to the list of information in the field "trialinfo" of
    *STUDY.dataset* (however it also includes information about
    condition, group and session which is stored separately in the
    *STUDY.dataset* structure).

The field datatype can take several values:

-   <b>ERP</b>: ERP data.
-   <b>SPECTRUM</b>: SPECTRUM data (legacy).
-   <b>TIMEF</b>: time-frequency data.
-   <b>ERPIMAGE</b>: ERPIMAGE data.

Note that for ERPIMAGE data, the <i>comp</i> and <i>chan</i> fields may
contain a string of character. If this is the case, the string is
executed when loading the file. This avoids storing the single-trial
data multiple times if this is not necessary.
