---
layout: default
title: III.2 Writing EEGLAB Scripts
parent: III.Advanced topics
grand_parent: Tutorials
---
This section is intended for users who have learned at least the basics
of Matlab script writing and wish to use EEGLAB and its many functions
to automate and/or customize data analyses. This section mainly uses the
same sample EEG dataset as the [single subject data analysis
tutorial](/I.Single_subject_data_processing_tutorial "wikilink").

Why write EEGLAB Matlab scripts?
--------------------------------

EEGLAB is a collection of Matlab functions many of which can be called
from a main graphic interface. Writing EEGLAB Matlab scripts simply
involves calling these functions from a script file or from the command
line instead of calling them interactively from the EEGLAB gui. EEGLAB's
history mechanism keeps track of all operations performed on datasets
from the EEGLAB graphic interface and eases the transition from
menu-based to script-based computing. It allows the user to perform
exploratory signal processing on a sample dataset, then use the
accumulated commands issued from the EEGLAB window in a script file,
which can then be modified using any text editor.

Writing Matlab scripts to perform EEGLAB analyses allows the user to
largely automate the processing of one or more datasets. Because
advanced analyses may involve many parameter choices and require fairly
lengthy computations, it is often more convenient to write a custom
script, particularly to process multiple datasets in the same way or to
process one dataset in several ways.

Note: Writing EEGLAB Matlab scripts requires some understanding of the
EEGLAB data structure (EEG) and its substructures (principally
*EEG.data*, *EEG.event*, *EEG.urevent*, *EEG.epoch*, *EEG.chanlocs* and
*EEG.history*). We will introduce these data structures as needed for
the tutorial examples and will discuss the five reserved variable names
used by EEGLAB and their uses:

         EEG        - the current EEG dataset
         ALLEEG     - array of all loaded EEG datasets
         CURRENTSET - the index of the current dataset
         LASTCOM    - the last command issued from the EEGLAB menu
         ALLCOM     - all the commands issued from the EEGLAB menu

You may refer at any time to [Appendix A5. EEGLAB Data
Structures](/A05:_Data_Structures "wikilink") for a more complete
description of the EEG structure.

Using dataset history to write EEGLAB scripts
---------------------------------------------

This section begins with a basic explanation of the EEG Matlab structure
used by EEGLAB. It then explains how to take advantage of the history of
modifications of the current dataset for writing scripts. Finally we
describe how EEGLAB functions are organized and how to use these
functions in Matlab scripts. Following sections describe how to take
advantage of EEGLAB structures to process multiple datasets.

In EEGLAB, the data structure describing the current dataset can be
accessed at all times from the Matlab command line by typing *\>\> EEG*.
The variable *EEG* is a Matlab structure used by EEGLAB to store all the
information about a dataset. This includes the dataset name and
filename, the number of channels and their locations, the data sampling
rate, the number of trials, information about events in each of the
trials/epochs, the data itself, and much more. For a more complete
description of the *EEG* fields along with examples on sample data, see
[Appendix A2](/A2:_Data_Structures "wikilink"). The contents of any
field of the *EEG* structure may be accessed by typing *EEG.fieldname*.
For instance, typing *\>\> EEG.nbchans* on the Matlab command line
returns the number of channels in the current dataset.

### Dataset history: the EEG.history field

EEGLAB commands issued through the EEGLAB menu that have affected the
current EEG dataset are preserved in the *EEG.history* field. The
contents of the history field includes those function calls that
modified the current dataset, as well as calls to plotting functions.
For instance, following the [single subject
tutorial](/I.Single_subject_data_processing_tutorial "wikilink") to the
end of section ["Importing channel
locations"](/Chapter_02:_Channel_Locations "wikilink") and then typing
*\>\> EEG.history* on the command line would return the following text:

``` matlab
pop_eegplot( EEG, 1, 1, 1);
EEG.setname='Continuous EEG Data';
EEG = eeg_eegrej( EEG, [295 512] );
EEG.chanlocs=pop_chanedit(EEG.chanlocs, 'load',{ '/matlab/eeglab/sample_data/eeglab_chan32.locs', 'filetype', 'autodetect'});
figure;
topoplot([],EEG.chanlocs, 'style', 'blank', 'electrodes', 'labelpoint');
```


The first command *pop_eegplot( EEG, 1, 1, 1);* plotted the data. The
second and the third commands removed portions of the data. These three
commands were inherited from the parent dataset. The last command
plotted the channel locations by name. As we will see, a basic method
for writing EEGLAB scripts is simply to save or copy and paste these
history commands into a Matlab script file.

Processing multiple datasets: One typical use of dataset history for
writing scripts is to process several datasets. To process the first
dataset, you can use EEGLAB graphic interface. To process subsequent
similar datasets, you may simply copy or save the history from the first
dataset into a script file (a text file with the extension "*.m*", for
example, *doitagain.m*), load a different dataset, and then run the
script from the Matlab command line. Note that the script file
*doitagain.m* must be in your current Matlab path, which normally
includes the present working directory. Read the help messages for
Matlab functions *path()* and *addpath()* to learn more about the Matlab
path. For instance, to repeat the processing applied to your current
dataset onto another dataset, use menu <font color=brown>File \> Save
history \> Dataset history</font> to save the history of your current
dataset as file *doitagain.m* as shown below.


![275px](/assets/images/Iv21history.jpg)



Clicking “Save” in the window above will cause the command history to be
saved into the Matlab script file *doitagain.m* (you can choose any name
for this file, as long as it ends in the standard Matlab script file
extension, "*.m*").
Note: When the file was saved, an extra command, *\>\> eeglab redraw*
was added at the end to insure that the main graphic interface would be
updated after the dataset was processed. Now, to process another dataset
using the same commands you used for processing the current dataset, try
closing the current Matlab session, restart Matlab then EEGLAB, reload a
different dataset and run the script saved above by typing

> \>\> doitagain

Most of the commands in the history field call EEGLAB *pop_* functions.
These are functions that take as input the EEG structure. The next
sub-section discusses how to use these functions in EEGLAB scripts.

### EEGLAB Function Architecture

EEGLAB was designed for use by both novice and expert Matlab users.
Depending on their level of Matlab expertise, users can either interact
only with the EEGLAB graphic interface (GUI), else they can call EEGLAB
functions directly from the Matlab command line or write their own
Matlab scripts using EEGLAB functions and structures.

EEGLAB functions are grouped in three layers:

1.  The main eeglab function and its menu handlers: EEGLAB users
    typically call these functions by selecting menu items from the main
    EEGLAB window menu.

<!-- -->

1.  Pop_functions: Matlab functions with their own graphic interfaces.
    Called with no (or few) arguments (as from the EEGLAB user
    interface), these functions pop up a query window to gather
    additional parameter choices from users. They then generally call
    one or more of the EEGLAB toolbox signal processing functions. The
    pop_functions can also be called from the Matlab command line or
    from Matlab scripts.

<!-- -->

1.  Signal processing functions: The experienced Matlab user can call
    the ICA toolbox functions directly from the Matlab command line or
    from their own analysis scripts. Some EEGLAB helper functions are
    also in this layer.


We will first see how pop_function work.

### EEGLAB pop_ functions

Functions with the prefix *pop_* or *eeg_* are functions that take the
EEG structure as their first input argument. Functions with the prefix
*pop_* can be called either from the EEGLAB menu or from the Matlab
command line, while functions with the prefix *eeg_* can only be called
from the Matlab command line. When you select a menu entry in the EEGLAB
main window, EEGLAB calls a *pop_* function, usually providing it with
one parameter only, the EEG structure containing the current dataset
(when selecting a menu item, the pop_ function it calls is listed in
the title bar of the pop-up window). Since the pop_ function is not
given enough parameters to actually perform any processing, it pops up a
window to ask the user to provide additional parameters. When you have
entered the required parameters into the pop_ window, the data
processing is performed. EEGLAB then adds the complete function call to
the dataset history, including the parameters you have entered in the
pop-up window. If you later copy this command from the dataset history
and paste it onto the Matlab command line, the processing will be
performed directly, without popping up an interactive query window.
However, try removing all the input parameters to the function call
except the first, naming the EEG structure and the pop_function will now
pop up a query window before performing any processing.
For example, open a new Matlab session and try (you may have to type
*\>\> eeglab* to add access paths to the functions below)

> \>\> EEG = pop_loadset;

An interactive window will pop up to ask for the dataset name, just as
it would do if the { {File\|pop_loadset.m} } command were issued from
the EEGLAB menu via <font color=brown>File \> Load dataset</font>. If,
on the other hand, the user provides two string arguments to the {
{File\|pop_loadset.m} } function, the first containing the filename and
the second the file path, no interactive window appears and the dataset
is loaded directly.
Try another example:

> \>\> EEG = pop_eegfilt(EEG);

This will pop up an interactive window allowing you to filter the data
according to the parameters you enter in the window. If you wish to
filter the EEG dataset without involving this graphic interface, type:

> \>\> EEG = pop_eegfilt( EEG, 1, 0);

This command will highpass filter the data above 1 Hz. To see which
parameter this function takes as argument see { {File\|pop_eegfilt.m} }
help. Keep in mind that all the interactive EEGLAB pop_ functions work
this way. You may copy commands from the EEG history fields and modify
the function input as desired. Function help messages are available
either from the EEGLAB graphic interface <font color=brown>Help \>
EEGLAB functions \> Interactive pop_ function</font>, from the
[Internet](http://sccn.ucsd.edu/eeglab/allfunctions/), or from the
command line (type *\>\> help pop_*functioname).
Note: Only *pop_\[funcname\]()* functions or *eeg_\[funcname\]()*
functions process the EEG dataset structure; *eeg_funcname()* functions
take the EEG data structure as an argument, but do not pop up
interactive windows. Thus, they are typically not available from the
EEGLAB menu, but only from the command line.

**What do pop_ functions return?**

When called from the EEGLAB interface, pop_ functions do not return
variables. Instead, they may alter (when called for) the EEG data
structure itself. However, when called from the command line, many of
the visualization functions in the EEGLAB toolbox do return variables
when useful (e.g., the results plotted). To determine which variables
are returned by a function, it is important to understand how they work.
To carry out their required data processing, most of the pop_ functions
(each named *pop_\[funcname\]()*) call a similarly named processing
function (*\[funcname\]*). You may directly call these functions to
perform more advanced scripting (see [low level
scripting](/#Low_level_scripting "wikilink") below). The important thing
is that both the pop_ function and its corresponding processing
function return the same variables (usually the pop_ function help
messages refer the user to the processing function help message which
describes the output variables). For example, the {
{File\|pop_erpimage.m} } function returns the same outputs as the {
{File\|erpimage.m} } function:

> figure; \[outdata, outvar, outtrials\] = pop_erpimage(EEG,1,12); %
> ERP-image plot of channel 12
>
> % or the equivalent non-pop function call
> figure; \[outdata, outvar, outtrials\] = erpimage( EEG.data(12,:),
> zeros(1,EEG.trials), EEG.times, '', 10, 1, 'nosort');


Important note: If *pop_\[funcname\]()* is a plotting function, then a
new figure is created automatically only when the function is called in
pop-up window mode. Otherwise, *pop_\[funcname\]()* plotting commands
(as well as all non-pop plotting commands, except *eegplot()*) should be
preceded by a Matlab *figure;* command, as in the example above (Note:
the *figure;* is added before the command by the EEGLAB history
mechanism). This feature allows you to create compound figures using
Matlab *subplot()*or the more flexible EEGLAB version { {File\|sbplot.m}
}.

### Script examples using dataset history

Making use of the *EEG.history* is the easiest way to start learning
about EEGLAB scripting. For example, import a binary dataset (for
instance [**TEST.CNT**](http://sccn.ucsd.edu/eeglab/download/TEST.CNT)),
then follow the [single subject
tutorial](/I.Single_subject_data_processing_tutorial "wikilink") until
the end of Section ["Extracting data
epochs"](/Chapter_05:_Extracting_Data_Epochs "wikilink") (in this
section, do not enter any event type name for epoch extraction; the
function will use all events). Then type *\>\> EEG.history* on the
command line. You should obtain the following text:

``` matlab
  EEG = pop_loadcnt('/home/arno/temp/TEST.CNT' , 'dataformat', 'int16');
  EEG.setname='CNT file';
  pop_eegplot( EEG, 1, 1, 1);
  EEG.setname='Continuous EEG Data';
  EEG = eeg_eegrej( EEG, [295 512] );
  EEG.chanlocs=pop_chanedit(EEG.chanlocs, 'load',{ '/matlab/eeglab/sample_data/eeglab_chan32.locs', 'filetype',  autodetect'});
  figure; topoplot([],EEG.chanlocs, 'style', 'blank', 'electrodes', 'labelpoint');
  figure; pop_spectopo(EEG, 1, [0 238304.6875], 'EEG' , 'percent', 15, 'freq', [6 10 22], 'freqrange',[2   25],'electrodes','off');
  EEG = pop_eegfilt( EEG, 1, 0, [], [0]);
  EEG.setname='Continuous EEG Data';
  EEG = pop_epoch( EEG, { 'square' }, [-1 2], 'newname', 'Continuous EEG Data epochs', 'epochinfo', 'yes');
  EEG.setname='Continuous EEG Data epochs';
  EEG = pop_rmbase( EEG, [-1000 0]);
```

This is the history field of dataset 2 (the epoched dataset), if you
switch to dataset 1 (the original continuous dataset), by selecting menu
item <font color=brown>Datasets \> dataset 1</font>, and then type *\>\>
EEG.history* on the command line, you will retrieve the same list of
commands as above except for the last three. This is because dataset 2
is derived from dataset 1, so it inherits all the history of
modifications that were applied to dataset 1 up to the time dataset 2
was created from it.

The *EEG.history* command can be very useful when you have several
datasets (for example, from several subjects) and wish to apply the same
processing to all of them. The *EEG.history* field is a part of the
dataset EEG structure, so you can use it in any EEGLAB session. For
example, when you have new dataset you wish to process the same way as a
previous dataset, just load the old dataset into EEGLAB and type *\>\>
EEG.history* to see the list of commands to execute on the new dataset.
More specifically,

1.  Load all the datasets you wish to process into EEGLAB.
2.  Perform the processing you wish from the Matlab menu on the first
    dataset.
3.  Ask for the command history (type *\>\> EEG.history*) and copy the
    data processing commands.
4.  Switch (via the EEGLAB menu) to the second dataset and paste the
    buffered commands onto the Matlab command line to execute them again
    on the new dataset.
5.  Go on like this till the last dataset is processed.


At this point you may want to save all the modified datasets to the
computer. You may also use menu <font color = brown>File \> Save history
\> Dataset history</font> to save the current dataset history
(*EEG.history* field) into a Matlab script file and recall this Matlab
script from the command line as described in the previous sub-section.

Note: EEGLAB loading dataset commands (menus <font color=brown>File \>
Load dataset</font>) are not stored in the dataset history. The reason
for this is that if you were to load a dataset repeatedly, you would not
want the repeated load command to be in your dataset history.

More advanced scripting examples will be presented in the following
sections.

### Updating the EEGLAB window



![px](/assets/images/Eeglab.jpg)



Whenever you wish to switch back from interacting with the EEG dataset
on the command line to working with the EEGLAB graphic interface, you
should perform one of the two commands below:


1.  If no EEGLAB window is running in the background, type:
    > \>\> eeglab redraw;
2.  If there is an open EEGLAB session, first type:
    > \>\> \[ALLEEG EEG CURRENTSET\] = eeg_store(ALLEEG, EEG);

    to save the modified information, and then:

    > \>\> eeglab redraw;

    to see the changes reflected in the EEGLAB window.

To learn more about scripting and EEGLAB data structures see the next
section [Scripting at the EEGLAB Structure
Level](/#Scripting_at_the_EEGLAB_structure_level "wikilink")


Using EEGLAB session history to perform basic EEGLAB script writing
-------------------------------------------------------------------

There are two main EEGLAB Matlab data structures, *EEG* and *ALLEEG*.
The *ALLEEG* array contains all the dataset structures that currently
loaded in the EEGLAB session. The *EEG* structures contains all the
information about the current dataset being processed.

There are two main differences between EEGLAB “dataset history” and
“session history”. As the names imply, “session history” saves all the
function calls issued for all the datasets in the current EEGLAB
session, while “dataset history” saves only the function calls that
modified the current dataset. Session history is available only during
the current session of EEGLAB -- starting a new EEGLAB session will
create a new session history -- whereas dataset history is saved in the
*EEG.history* field of the EEG dataset structure when you save the
dataset at the end of the session. It therefore will be retrieved when
the dataset is re-loaded in future EEGLAB sessions (assuming, of course,
that you save the dataset at the end of the current session!).

EEGLAB session history allows you to manipulate and process several
datasets simultaneously. Thus, its use can be considered the next level
of EEGLAB scripting.

### The eegh command

To view the session history for the current EEGLAB session, use the
*eegh* (history) command. Typing:

> \>\> eegh

under Matlab prints the EEGLAB session history in the Matlab command
line window. For instance, after performing the first step of the main
tutorial (simply opening an existing dataset), typing *eegh* on the
command line should return the following text:

>
> \>\>\[ALLEEG EEG CURRENTSET ALLCOM\] = eeglab;
> \>\>EEG = pop_loadset( 'eeglab_data.set',
> '/home/Matlab/eeglab/script/');
> \>\>\[ALLEEG EEG CURRENTSET\] = eeg_store(ALLEEG, EEG);

The first command ({ {File\|eeglab.m} }) runs EEGLAB and initializes
several EEGLAB variables listed in the function output. Except for
modifying these variables and adding the path to EEGLAB functions (if
necessary), the { {File\|eeglab.m} } call will not modify anything else
in the Matlab workspace (there is no global variable in EEGLAB). The
second command ({ {File\|pop_loadset.m} }) loads the dataset into the
*EEG* structure, and the last ({ {File\|eeg_store.m} }) stores the
dataset in the *ALLEEG* structure. For more detailed information, you
must study the Matlab help messages for these functions as explained
below:

Either (1) via the EEGLAB menu selections:

> For { {File\|pop_loadset.m} }\]: via <font color=brown> Help \> EEGLAB
> functions \> Interactive pop_functions</font> or via
> <font color=brown> Help \> EEGLAB menus</font>
>
> For { {File\|eeg_store.m} }: via <font color=brown> Help \> EEGLAB
> advanced \> Admin functions</font>

Or (2) using Matlab command line help

> \>\> help \[functioname\]

Now use menu item <font color=brown>File \> Save history \> Session
history</font> to save the command history into an ascii-text Matlab
script file. Save the file into the current directory, or into a
directory in the Matlab command path (i.e., in the list returned by
*\>\> path*). Selecting the “Save session history” menu item above will
pop up the window below:


![275px](/assets/images/Scripthist.jpg)


Clicking “Save” in the window above will cause the session command
history to be saved into the Matlab script file *eeglabhist.m* (you can
choose any name for this file, as long as it ends in the standard Matlab
script file extension, “.m”). Now try closing the current Matlab
session, restarting Matlab, and running the script saved above by typing

> \>\> eeglabhist

The main EEGLAB window is created and the same dataset is loaded.

Now open the script file *eeglabhist.m* in any text editor so you may
modify function calls.
Note: as for the dataset history, when the file was saved, an extra
command, *\>\> eeglab redraw* was added at the end to insure that the
main graphic interface would be updated after the dataset was
(re)loaded.

### Script example using session history

Building and running short or long EEGLAB Matlab scripts saved by EEGLAB
history can be that simple. Simply perform any EEGLAB processing desired
via the EEGLAB menu, save the EEGLAB command history, and re-run the
saved script file. Matlab will repeat all the steps you performed
manually. For instance, following the first several steps of the main
tutorial, the command ''\>\> h '' would return (with Matlab-style
comments in black italic format added for clarity):

``` matlab
 [ALLEEG EEG CURRENTSET ALLCOM] = eeglab; % start EEGLAB under Matlab
EEG = pop_loadset( 'ee114squares.set', '/home/payton/ee114/'); % read in the dataset
[ALLEEG EEG CURRENTSET] = eeg_store(ALLEEG, EEG); % copy it to ALLEEG

EEG = pop_editeventfield( EEG, 'indices', '1:155', 'typeinfo', 'Type of the event'); % edit the dataset event field
[ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET); % copy changes to ALLEEG

% update the dataset comments field
EEG.comments = pop_comments('', '', strvcat( 'In this experiment, stimuli can appear at 5 locations ',
'One of them is marked by a green box ', 'If a square appears in this box, the subject must respond, otherwise
he must ignore the stimulus.', ' ', 'These data contain responses to (non-target) circles appearing in the attended
box in the left visual field '));

[ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);% copy changes to ALLEEG
pop_eegplot( EEG, 1, 0, 1); % pop up a scrolling window showing the component activations

EEG.chanlocs=pop_chanedit(EEG.chanlocs, { 'load', '/home/payton/ee114/chan32.locs'},{ 'convert',{ 'topo2sph', 'gui'} },{ 'convert',{ 'sph2cart', 'gui'} });
% read the channel location file and edit the channel location information ''

figure; pop_spectopo(EEG, 0, [-1000 237288.3983] , 'percent', 20, 'freq', [10], 'icacomps', [1:0],'electrodes','off');
% plot RMS power spectra of the ICA component activations;
% show a scalp map of total power at 10 Hz plus maps of the components contributing most power at the same frequency''
```

<u>Important note:</u> As briefly mentioned previously, functions called
from the main EEGLAB interactive window display the name of the
underlying pop_function in the window title bar. For instance, selecting
<font color=brown>File \> Load an existing dataset</font> to read in an
existing dataset uses EEGLAB function { {File\|pop_loadset.m} }.


![275px](/assets/images/Pop_loadset.gif)


The next steps in learning to write EEGLAB Matlab scripts involve
learning to change EEGLAB function parameters and adding loops to
perform multiple analyses.

### Scripting at the EEGLAB structure level

The type of scripting illustrated above might involve going back and
forth between EEGLAB graphic interface and the Matlab command line. To
maintain consistency between the two main EEGLAB structure (*EEG* and
*ALLEEG*), you need to update the *ALLEEG* every time you modify the
*EEG* structure (see exception below in (1)). To add or directly modify
*EEG* structure values from a script or the Matlab command line, one
must respect some simple rules:

**1)** If the EEGLAB option to “Retain parent dataset”, selected via the
<font color=brown>File \> Maximize Memory</font> menu item (for details,
see [Appendix A3.](/A3:_Maximizing_Memory "wikilink") for the maximizing
memory menu), is set (default), then all current EEGLAB datasets are
stored in the structure array *ALLEEG,*. If you modify a dataset, you
should take care to copy the modified EEG dataset into *ALLEEG*.

> Thus, after loading and then modifying an *EEG* structure to create a
> new dataset, one might simply type:
>
> > \>\>ALLEEG(2) = EEG;
> > \>\>CURRENTSET = 2;
>
> This command 'might' work as expected (if the new dataset is
> internally consistent with the previous one). However, it is better to
> use the command { {File\|eeg_store.m} }' which performs extensive
> dataset consistency checking before storing the modified dataset.
> Either use the following command to set the new dataset to be dataset
> number 2,
>
> > \>\> \[ALLEEG EEG\] = eeg_store(ALLEEG, EEG, 2);
>
> or
>
> > \>\>\[ALLEEG EEG CURRENTSET\] = eeg_store(ALLEEG, EEG);
>
> to create a new dataset at the next available free space in the
> *ALLEEG* variable. The dataset number will then be available in the
> variable *CURRENTSET*. Note that if a previous dataset is already
> assigned as dataset 2, then only the last command (above) will not
> overwrite it. To view the changes in the main EEGLAB window, use the
> command: *\>\> eeglab redraw;*
> Another command that can be used to modify the *ALLEEG* structure is {
> {File\|pop_newset.m} }. This command, which also performs extensive
> dataset consistency checks, has more useful advanced options. To
> modify the current dataset with its accumulated changes type:
>
> > \[ALLEEG EEG CURRENTSET\] = pop_newset(ALLEEG, EEG, CURRENTSET,
> > 'overwrite', 'on');
>
> If you wish to create a new dataset to hold the modified structure
> use:
>
> > \>\>\[ALLEEG EEG CURRENTSET\] = pop_newset(ALLEEG, EEG, CURRENTSET);
>
> The returned argument *CURRENTSET* holds the set number of the new
> dataset stored in EEGLAB.
> Note: the *EEG* contains only the current dataset, so you must use
> extra caution whenever updating this structure. e.g., Be sure it
> contains the dataset you actually want to process!
>
> The functions above call the function { {File\|eeg_checkset.m} } to
> check the internal consistency of the modified dataset.
>
> > \>\> EEG = eeg_checkset(EEG);
>
> or
>
> > \>\> EEG = eeg_checkset(EEG, 'eventconsistency');
>
> The second command above runs extra checks for event consistency
> (possibly taking some time to complete) and regenerates the
> *EEG.epoch* structures from the *EEG.event* information. This command
> is only used when the event structure is being altered. See the [Event
> tutorial](/Chapter_03:_Event_Processing "wikilink") to learn how to
> work with EEG events.
>
> The commands above are very useful if the option to maintain multiple
> datasets is on. If the option to maintain multiple datasets is off
> (via the <font color=brown>File \> Maximize Memory</font> menu item),
> the *ALLEEG* variable is not used and *EEG* is the only variable that
> contains dataset information. When using this option you can only
> process one dataset at a time (the goal here is to use less memory and
> being able to process bigger datasets). Any changes made by the user
> to the *EEG* structure are thus applied instantaneously and are
> irreversible. For consistency, all the commands above will work,
> however the *ALLEEG* variable will be empty.

**2)** New fields added to the *EEG* structure by users will not be
removed by EEGLAB functions. Any additional information about a dataset
might be stored in the user-added field:

> \>\>EEG.analysis_priority = 1;

**3)** The following are the reserved variable names used by EEGLAB:

         EEG        - the current EEG dataset
         ALLEEG     - array of all loaded EEG datasets   (Thus >> EEG = ALLEEG(CURRENTSET);)
         CURRENTSET - the index of the current dataset
         LASTCOM    - the last command issued from the EEGLAB menu
         ALLCOM     - all the commands issued from the EEGLAB menu during this EEGLAB session

Note: that EEGLAB does not use global variables (the variables above are
accessible from the command line but they are not used as global
variables within EEGLAB). The above variables are ordinary variables in
the global Matlab workspace. All EEGLAB functions except the main
interactive window function { {File\|eeglab.m} } (and a few other
display functions) process one or more of these variables explicitly as
input parameters and do not access or modify any global variable. This
insures that they have a minimum chance of producing unwanted 'side
effects' on the dataset.

Basic scripting examples
------------------------

Below is a simple example of a Matlab script that includes some of the
first basic manipulations that must be performed on a dataset. This
example works with the tutorial dataset *eeglab_data.set* and the
corresponding channel location file *eeglab_chan32.locs*, which are
assumed to be located on your computer in the following directory:
*/home/Matlab/eeglab/script/*.

``` matlab
[ALLEEG EEG CURRENTSET ALLCOM] = eeglab;
% Load eeglab
EEG = pop_loadset( 'eeglab_data.set', '/home/Matlab/eeglab/script/');
% Load the dataset
EEG.chanlocs=pop_chanedit(EEG.chanlocs, 'load',{ '/home/Matlab/eeglab/script/eeglab_chan32.locs', 'filetype', 'autodetect'});
% Load the channel location file, enabling automatic detection of channel file format'
[ALLEEG EEG CURRENTSET ] = eeg_store(ALLEEG, EEG);% Store the dataset into EEGLAB
EEG = pop_eegfilt( EEG, 1, 0, [], [0]);''''' % High pass filter the data with cutoff frequency of 1 Hz.
% Below, create a new dataset with the name filtered Continuous EEG Data
[ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET, 'setname', 'filtered Continuous EEG Data');% Now CURRENTSET= 2
EEG = pop_reref( EEG, [], 'refstate',0); % Re-refrence the new dataset
% This might be a good time to add a comment to the dataset.
EEG.comments = pop_comments(EEG.comments,'','Dataset was highpass filtered at 1 Hz and rereferenced.',1);
% You can see the comments stored with the dataset either by typing >> EEG.comments or selecting the menu option Edit->About this dataset.
EEG = pop_epoch( EEG, { 'square' }, [-1 2], 'newname', 'Continuous EEG Data epochs', 'epochinfo', 'yes');
% Extract epochs time locked to the event - 'square', from 1 second before to 2 seconds after those time-locking events.
% Now, either overwrite the parent dataset, if you don't need the continuous version any longer, or create a new dataset
%(by removing the 'overwrite', 'on' option in the function call below).
[ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET, 'setname', 'Continuous EEG Data epochs', 'overwrite', 'on');
EEG = pop_rmbase( EEG, [-1000 0]); % Remove baseline
% Add a description of the epoch extraction to EEG.comments.
EEG.comments = pop_comments(EEG.comments,'','Extracted ''square'' epochs [-1 2] sec, and removed baseline.',1);
[ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);  %Modify the dataset in the EEGLAB main window
eeglab redraw % Update the EEGLAB window to view changes
```

Some other useful scripting examples (see the function help messages for
more details):

**1.** Reduce sampling rate

``` matlab
% Reduce the sampling rate to 128 Hz (the above example was already sampled at 128 Hz'')
EEG = pop_resample( EEG, 128);
% Save it as a new dataset with the name Continuous EEG Data resampled
[ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET, 'setname', 'Continuous EEG Data resampled');
% If you wish to return to the previous dataset (before downsampling), type
'EEG = eeg_retrieve(ALLEEG, 1); CURRENTSET = 1;
```


**2.** Print a series of ERP scalp maps

``` matlab
% Plot ERP maps (via the second argument choice 1), every 100 ms from 0 ms to 500 ms [0:100:500]
% with the plot title - 'ERP image', in 2 rows and 3 columns. Below, the 0 means do not plot dipoles.
% Plot marks showing the locations of the electrodes on the scalp maps.
pop_topoplot(EEG,1, [0:100:500] , 'ERP image',[2:3] ,0, 'electrodes', 'on');
```


In the next section, we will directly call some lower-level EEGLAB data
processing functions. For instance, the command above can be executed by
directly calling the signal processing function { {File\|topoplot.m} }
as shown below:

``` matlab
times = [0:100:500];
% Define variables:
pos = eeg_lat2point(times/1000, 1, EEG.srate, [EEG.xmin EEG.xmax]);
% Convert times to points (or >pos = round( (times/1000-EEG.xmin)/(EEG.xmax-EEG.xmin) * (EEG.pnts-1))+1;)
% See the event tutorial for more information on processing latencies
mean_data = mean(EEG.data(:,pos,:),3);
% Average over all trials in the desired time window (the third dimension of EEG.data allows to access different data trials).
% See appendix A1 for more information
maxlim = max(mean_data(:));
minlim = min(mean_data(:));
% Get the data range for scaling the map colors.
maplimits = [ -max(maxlim, -minlim) max(maxlim, -minlim)];
% Plot the scalp map series.
figure
for k = 1:6
sbplot(2,3,k);
% A more flexible version of subplot.
topoplot( mean_data(:,k), EEG.chanlocs, 'maplimits', maplimits, 'electrodes', 'on', 'style', 'both');
title([ num2str(times(k)) ' ms']);
end
cbar; % A more flexible version of colorbar.
```

Low level scripting
-------------------

As mentionned at the end of section IV.2.3, *pop_funcname()* function is
a graphic-user interface (gui) function that operates on the *EEG* data
structure using the stand-alone processing function *funcname()*. The
stand-alone processing function, which has no knowledge of the dataset
structure, can process any suitable data matrix, whether it is an EEGLAB
data matrix or not.

For instance, { {File\|pop_erpimage.m} } calls the data processing and
plotting function { {File\|erpimage.m} }. To review the input parameters
to these functions, either use the EEGLAB help menu (from the EEGLAB
window) or the Matlab function help (from the Matlab command line). For
example:

>
> \>\> help pop_erpimage
> \>\> help erpimage


As mentioned earlier, the two following function calls are equivalent:

>
> \>\> figure; \[outdata, outvar, outtrials\] =
> pop_erpimage(EEG,1,12);
> \>\> figure; \[outdata, outvar, outtrials\] = erpimage(
> EEG.data(12,:), zeros(1,EEG.trials), EEG.times, '', 10, 1, 'nosort')


Using EEGLAB data processing functions may require understanding some
subtleties of how they work and how they are called. Users should read
carefully the documentation provided with each function. Though for most
functions, the function documentation is supposed to describe function
output in all possible situation, occasionally users may need to look in
the function script files themselves to see exactly how data processing
is performed. Since EEGLAB functions are open source, this is always
possible.

### Example script for processing multiple datasets

For example, when computing event-related spectral power (ERSP)
transforms for sets of data epochs from two or more experimental
conditions, the user may want to subtract the same (log) power baseline
vector from all conditions. Both the { {File\|pop_timef.m} } function
and the { {File\|timef.m} } function it calls return spectral baseline
values that can be used in subsequent ''timef() '' computations. For
instance, assuming that three sets of data epochs from three
experimental conditions have been stored for 10 subjects in EEGLAB
dataset files named *subj\[1:10\]data\[1:3\].set* in directory
*/home/user/eeglab*, and that the three datasets for each subject
contain the same ICA weights, the following Matlab code would plot the
ICA component-1 ERSPs for the three conditions using a common spectral
baseline for each of the 10 subjects:

``` matlab
eeglab; % Start eeglab
Ns = 10; Nc = 3; % Ns - number of subjects; Nc - Number of conditions;'
for S = 1:Ns  % For each of the subjects
    mean_powbase = []; % Initialize the baseline spectra average over all conditions for each subject
    for s =1:Nc  % Read in existing EEGLAB datasets for all three conditions
        setname = ['subj' int2str(S) 'data' int2str(s) '.set'];  % Build dataset name
        EEG = pop_loadset(setname,'/home/user/eeglab/'); % Load the dataset
        [ALLEEG EEG] = eeg_store(ALLEEG, EEG, Nc*(S-1) + s);  % Store the dataset in ALLEEG
        [ersp,itc,powbase{s}] =pop_timef( ALLEEG(s),0, 1, [-100 600], 0, 'plotitc', 'off', 'plotersp', 'off' );
        % Run simple timef() for each dataset, No figure is created because of options 'plotitc', 'off', 'plotersp', 'off'
        mean_powbase = [mean_powbase; powbase{s}];  % Note: curly braces
    end % condition
    % Below, average the baseline spectra from all conditions
    mean_powbase = mean(mean_powbase, 1);

    % Now recompute and plot the ERSP transforms using the same baseline
    figure;  % Create a new figure (optional figure('visible', 'off'); would create an invisible figure)
    for s = 1:Nc; % For each of the three conditions
        sbplot(1,3,s); % Select a plotting region
        pop_timef( ALLEEG(s), 0, 1, [-100 600], 0, 'powbase', mean_powbase, ...
        title', ['Subject ' int2str(S)]);''''' % Compute ERSP using mean_powbase''
    end % End condition plot
    plotname = ['subj' int2str(S) 'ersp' ];  % Build plot name
    eval(['print -depsc ' plotname]); % Save plot as a color .eps (postcript) vector file
end % End subject
eeglab redraw  % Update the main EEGLAB window
```

Repetitive processes, such as the computation performed above, may be
time consuming to perform by hand if there are many epochs in each
dataset and many datasets. Therefore it may be best performed by an
EEGLAB Matlab script that is left to run until finished in a Matlab
session. Writing scripts using EEGLAB functions makes keeping track of
data parameters and events relatively easy, while maintaining access to
the flexibility and power of the Matlab signal processing and graphics
environment.

<u>Notes: </u>

-   Normally, the user might want to accumulate and save the ERSPs and
    other output variables returned by *timef()* above to make possible
    further quantitative comparisons between subjects. The function
    described in the next paragraph { {File\|tftopo.m} } allows the user
    to combine ERSP outputs from different subjects and apply binary
    statistics.
-   In the current version of EEGLAB, the cross-coherence function {
    {File\|crossf.m} } can calculate significance of differences between
    coherences in two conditions.
-   In the future, { {File\|timef.m} } will be extended to allow
    comparisons between multiple ERSP and ITC transforms directly.
-   The same type of iterative normalization (illustrated above) may be
    applied for the "baseamp" parameter returned by {
    {File\|pop_erpimage.m} }

### Example script performing time-frequency decompositions on all electrodes

This more advanced example demonstrates some of the power of low-level
scripting that goes beyond the scope of functions currently available
through the graphical interface. You can run this script on any epoched
dataset including the tutorial dataset.

``` matlab
% Compute a time-frequency decomposition for every electrode
for elec = 1:EEG.nbchan
    [ersp,itc,powbase,times,freqs,erspboot,itcboot] = pop_newtimef(EEG, …
    1, elec, [EEG.xmin EEG.xmax]*1000, [3 0.5], 'maxfreq', 50, 'padratio', 16, ...
    'plotphase', 'off', 'timesout', 60, 'alpha', .05, 'plotersp','off', 'plotitc','off');
    if elec == 1  % create empty arrays if first electrode
        allersp = zeros([ size(ersp) EEG.nbchan]);
        allitc = zeros([ size(itc) EEG.nbchan]);
        allpowbase = zeros([ size(powbase) EEG.nbchan]);
        alltimes = zeros([ size(times) EEG.nbchan]);
        allfreqs = zeros([ size(freqs) EEG.nbchan]);
        allerspboot = zeros([ size(erspboot) EEG.nbchan]);
        allitcboot = zeros([ size(itcboot) EEG.nbchan]);
    end;
    allersp (:,:,elec) = ersp;
    allitc (:,:,elec) = itc;
    allpowbase (:,:,elec) = powbase;
    alltimes (:,:,elec) = times;
    allfreqs (:,:,elec) = freqs;
    allerspboot (:,:,elec) = erspboot;
    allitcboot (:,:,elec) = itcboot;
end;
% Plot a tftopo() figure summarizing all the time/frequency transforms
figure;
tftopo(allersp,alltimes(:,:,1),allfreqs(:,:,1),'mode','ave','limits', …
[nan nan nan 35 -1.5 1.5],'signifs', allerspboot, 'sigthresh', [6], 'timefreqs', ...
[400 8; 350 14; 500 24; 1050 11], 'chanlocs', EEG.chanlocs);
```

Executing the following code on the tutorial dataset (after highpass
filtering it above 1 Hz, extracted data epochs, and removing baseline),
produces the following figure.




![375px](/assets/images/Iv512timefreq_plot.jpg)


### Creating a scalp map animation

A simple way to create scalp map animations is to use the (limited)
EEGLAB function { {File\|eegmovie.m} } from the command line. For
instance, to make a movie of the latency range -100 ms to 600 ms, type:

``` matlab
pnts = eeg_lat2point([-100:10:600]/1000, 1, EEG.srate, [EEG.xmin EEG.xmax]);
% Above, convert latencies in ms to data point indices
figure; [Movie,Colormap] = eegmovie(mean(EEG.data(:,128:2:192),3), EEG.srate, EEG.chanlocs, 0, 0);
seemovie(Movie,-5,Colormap);
```

A second solution here is to dump a series of images of your choice to
disk, then to assemble them into a movie using another program. For
instance, type

``` matlab
counter = 0;
for latency = -100:10:600 %-100 ms to 1000 ms with 10 time steps
    figure; pop_topoplot(EEG,1,latency, 'My movie', [] ,'electrodes', 'off'); % plot'
    print('-djpeg', sprintf('movieframe%3d.jpg', counter)); %save as jpg
    close;  % close current figure
    counter = counter + 1;
end;
```

Then, for example in Unix, use *% convert movieframe\*.jpg mymovie.mpg*
to assemble the images into a movie.

Refer to the event scripting tutorial for more script and command line
examples (see next tutorial regarding [accessing events from the command
line](/Chapter_03:_Event_Processing#Accessing_events_from_the_command_line "wikilink")).

### Plotting measures in scalp topography

The { {File\|metaplottopo.m} } function is a powerful function that
allows plotting any measure for all channels and components. For
example, the code below allow plotting time-frequency decompositions for
all data channels.

``` matlab
figure; metaplottopo( EEG.data, 'plotfunc', 'newtimef', 'chanlocs', EEG.chanlocs, 'plotargs', ...
                   {EEG.pnts, [EEG.xmin EEG.xmax]*1000, EEG.srate, [0], 'plotitc', 'off', 'ntimesout', 50, 'padratio', 1});
```




![400px](/assets/images/Newtimeftopo.png)


Another example below allows plotting ERPimage for all data channels.
Note that for ERPimage, the function does not plot the axis for each
plot making it convinient to plot huundreds of channels if necessary. It
is also possible to plot ICA components in this way by replacing
EEG.data by EEG.icaact and removing the 'chanlocs' argument.

``` matlab
figure; metaplottopo( EEG.data, 'plotfunc', 'erpimage', 'chanlocs', EEG.chanlocs, 'plotargs', ...
         { eeg_getepochevent( EEG, {'rt'},[],'latency') linspace(EEG.xmin*1000, EEG.xmax*1000, EEG.pnts) '' 10 0 });
```




![400px](/assets/images/Erpimagetopo.png)


*(More example scripts would be useful here. Send us your own commented
script).*
