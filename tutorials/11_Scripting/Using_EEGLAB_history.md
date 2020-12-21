---
layout: default
title: c. Using EEGLAB history
parent: 11. Write scripts
grand_parent: Tutorials
---
This section is intended for users who have learned at least the basics
of Matlab script writing and wish to use EEGLAB and its many functions
to automate and/or customize data analyses.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

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

You may refer at any time to [EEGLAB Data Structures](/tutorials/ConceptsGuide/Data_Structures.html) for a more complete
description of the EEG structure, and the [EEGLAB functions](/tutorials/ConceptsGuide/EEGLAB_functions.html) documentation to learn about the different types of EEGLAB functions, and how to use them.

EEGLAB session history
---------------------------------------------

This section explains how to take advantage of the history of
modifications of the current dataset for writing scripts.

Let's start EEGLAB, load a dataset, and simply call the data scrolling window.
- Call <span style="color: brown">File → Load dataset</span>. Select the tutorial file "eeglab_data.set" in the "sample_data" folder of the EEGLAB distribution. Then press *Open*.
- Use menu item <span style="color: brown">Plot → Channel data (scroll)</span>. This pops up
the [eegplot](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eegplot.m)
scrolling data display below.
- Use menu item <span style="color: brown">File → History script → Save session history script</span> and save the history as file *doitagain.m*.

![Image:Scrollchannelactivities1.png]({{ site.baseurl }}/assets/images/Scrollchannelactivities1.png)

Now open the script *doitagain.m* in the Matlab editor using the <span style="color: brown">Open</span> button on the Matlab graphical interface. The script should look like this.

```matlab
% EEGLAB history file generated on the 20-Dec-2020
% ------------------------------------------------
[ALLEEG EEG CURRENTSET ALLCOM] = eeglab;
EEG = pop_loadset('filename','eeglab_data.set','filepath','/data/matlab/eeglab/sample_data/');
[ALLEEG, EEG, CURRENTSET] = eeg_store( ALLEEG, EEG, 0 );
EEG = eeg_checkset( EEG );
pop_eegplot( EEG, 1, 1, 1);
eeglab redraw;
```

The first two lines are comments. They are followed by 6 commands:
- The first command starts EEGLAB
- The second command loads the tutorial dataset
- The third command saves the dataset in EEGLAB memory
- The fourth command check the dataset consistency
- The fith command plots the data
- The seventh command refresh the EEGLAB graphical interface (in case the current dataset was modified)

Note: When the file was saved, an extra command, *\>\> eeglab redraw*
was added at the end to insure that the main graphic interface would be
updated after the dataset was processed. 

Now press the <span style="color: brown">Run</span> button in the Matlab editor. The script is being executed and the data scrolling window pops up. Alternatively, you may use EEGLAB menu item <span style="color: brown">File → History script → Run script</span> to execute the script (this menu item is most relevant for compiled versions of EEGLAB for which the Matlab graphical interface is not accessible). You may also type the name of the script on the Matlab command line to execute it (assuming the folder in which you saved it is in your path).

``` matlab
doitagain
```

The script may be modified as needed and executed again. Using EEGLAB graphical interface and saving command history is a simple way to learn to write EEG analysis scripts. Now, to process another dataset
using the same commands you used for processing the current dataset, try
closing the current Matlab session. Then restart Matlab, load the script
*doitagain.m*, modify the name of the dataset (use one of your own for example)
and run the script again.

Most of the commands in the history field call EEGLAB *pop_* functions.
These are functions that take as input the EEG structure. The [EEGLAB functions](/tutorials/ConceptsGuide/EEGLAB_functions.html) documentation discusses how to use these functions in EEGLAB scripts.

Dataset history and the EEG.history field
---------------------------------------------

In EEGLAB, the data structure describing the current dataset can be
accessed at all times from the Matlab command line by typing *\>\> EEG*.
The variable *EEG* is a Matlab structure used by EEGLAB to store all the
information about a dataset. This includes the dataset name and
filename, the number of channels and their locations, the data sampling
rate, the number of trials, information about events in each of the
trials/epochs, the data itself, and much more. For a more complete
description of the *EEG* fields along with examples on sample data, see
[EEGLAB Data Structures](/tutorials/ConceptsGuide/Data_Structures.html). The contents of any
field of the *EEG* structure may be accessed by typing *EEG.fieldname*.
For instance, typing *\>\> EEG.nbchan* on the Matlab command line
returns the number of channels in the current dataset.

EEGLAB commands issued through the EEGLAB menu that have affected the
current EEG dataset are preserved in the *EEG.history* field. The
contents of the history field includes those function calls that
modified the current dataset, as well as calls to plotting functions. 

Making use of the *EEG.history* is the easiest way to start learning
about EEGLAB scripting. For example, import a binary dataset (for
instance [**TEST.CNT**](http://sccn.ucsd.edu/eeglab/download/TEST.CNT)).

We used the following menu items:
1. Use menu item <font color=brown>File → Import data → Using EEGLAB functions and plugins → From Neuroscan .CNT file</font> to import the file (use all  defaults)
2. Use menu item <font color=brown>Tools → Change sampling rate</font> and change the sampling rate to 250 Hz, keep all defaults to create a new dataset
3. Use menu item <font color=brown>Tools → Filter the data → Basic FIR filter</font> and high pass filter at 1 Hz (first edit box), keep all defaults to create a new dataset
4. Use menu item <font color=brown>Plot → Channel data (scroll)</font> to vizualise the data

Then type *\>\> EEG.history* on the
command line. You should obtain the following text:

```matlab
EEG.history

ans =
     EEG.etc.eeglabvers = '2020.0'; % this tracks which version of EEGLAB is being used, you may ignore it
     EEG = pop_loadcnt('/Users/arno/Downloads/TEST.CNT' , 'dataformat', 'auto', 'memmapfile', '');
     EEG = eeg_checkset( EEG );
     EEG = pop_resample( EEG, 250);
     EEG = eeg_checkset( EEG );
     EEG = pop_eegfiltnew(EEG, 'locutoff',1,'plotfreqz',1);
     EEG = eeg_checkset( EEG )
```

Alternatively, you can save the current dataset history by selecting menu
item <font color=brown>File → Save history → Save dataset history script</font>.

These are all the commands executed in EEGLAB after importing the raw data file.
Note that the *session* history we saved in the previous section is the history
since EEGLAB was last started, and contains modification of multiple datasets.
The *EEG.history* field only contains the modification to the current dataset.

In this case, we should have three datasets in EEGLAB and this is the history field of dataset three. If you
switch to dataset one (the original continuous dataset), by selecting menu
item <font color=brown>Datasets → Dataset 1</font>, and then type *\>\>
EEG.history* on the command line (as shown below), you will retrieve the same list of
commands as above except for the last four. Dataset one is a copy saved in memory just
after the dataset was loaded and it has not been modified yet. Dataset three
is derived from dataset one, so it inherits all the history of
modifications that were applied to it.

```matlab
EEG.history

ans =
     EEG.etc.eeglabvers = '2020.0'; % this tracks which version of EEGLAB is being used, you may ignore it
     EEG = pop_loadcnt('/Users/arno/Downloads/TEST.CNT' , 'dataformat', 'auto', 'memmapfile', '');
     EEG = eeg_checkset( EEG );
```

Repeating the process after selecting <font color=brown>Datasets → Dataset 2</font>, we obtain

```matlab
EEG.history

ans =
     EEG.etc.eeglabvers = '2020.0'; % this tracks which version of EEGLAB is being used, you may ignore it
     EEG = pop_loadcnt('/Users/arno/Downloads/TEST.CNT' , 'dataformat', 'auto', 'memmapfile', '');
     EEG = eeg_checkset( EEG );
     EEG = pop_resample( EEG, 250);
     EEG = eeg_checkset( EEG );
```

Note: EEGLAB loading (and saving) dataset commands are not stored in the dataset history. The reason
for this is that if you were to load a dataset repeatedly, you would not
want the repeated load command to be in your dataset history.

The *EEG.history* command can be very useful when you have several
datasets (for example, from several subjects) and wish to apply the same
processing to all of them. The *EEG.history* field is a part of the
dataset EEG structure, so you can use it in any EEGLAB session. For
example, when you have new dataset you wish to process the same way as a
previous dataset, just load the old dataset into EEGLAB and type *\>\>
EEG.history* to see the list of commands to execute on the new dataset.
A basic method for writing EEGLAB scripts is simply to save or copy and paste these
history commands into a Matlab script file.

More specifically, to process the first
dataset, you can use EEGLAB graphic interface. To process subsequent
similar datasets, you may simply copy or save the history from the first
dataset into a script file (a text file with the extension "*.m*", for
example, *doitagain.m*), load a different dataset, and then run the
script from the Matlab command line. Note that the script file
*doitagain.m* must be in your current Matlab path, which normally
includes the present working directory. Read the help messages for
Matlab functions *path()* and *addpath()* to learn more about the Matlab
path. Step by step instructions are provided below:

1.  Load all the datasets you wish to process into EEGLAB.
2.  Perform the processing you wish from the Matlab menu on the first
    dataset.
3.  Ask for the command history (type *\>\> EEG.history*) and copy the
    data processing commands.
4.  Switch (via the EEGLAB menu) to the second dataset and paste the
    buffered commands onto the Matlab command line to execute them again
    on the new dataset.
5.  Go on like this till the last dataset is processed.

More advanced scripting examples will be presented in the following
sections.

Dataset history is often more convinient to use than session history
because it does not contain all the commands to manipulate datasets.

### Updating the EEGLAB window

![px](/assets/images/Eeglab.jpg)



Whenever you wish to switch back from interacting with the EEG dataset
on the command line to working with the EEGLAB graphic interface, you
should perform one of the two commands below:


1.  If no EEGLAB window is running in the background, type:
``` matlab
eeglab redraw;
```
2.  If there is an open EEGLAB session, first type:
``` matlab
[ALLEEG EEG CURRENTSET\] = eeg_store(ALLEEG, EEG);
```
    to save the modified information, and then:
``` matlab
eeglab redraw;
```
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

``` matlab
eegh
```

under Matlab prints the EEGLAB session history in the Matlab command
line window. For instance, after performing the first step of the main
tutorial (simply opening an existing dataset), typing *eegh* on the
command line should return the following text:

``` matlab
[ALLEEG EEG CURRENTSET ALLCOM\] = eeglab;
EEG = pop_loadset( 'eeglab_data.set', '/home/Matlab/eeglab/script/');
[ALLEEG EEG CURRENTSET\] = eeg_store(ALLEEG, EEG);
```
The first command ([eeglab.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeglab.m)) runs EEGLAB and initializes

several EEGLAB variables listed in the function output. Except for
modifying these variables and adding the path to EEGLAB functions (ifnecessary), the [eeglab.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeglab.m) call will not modify anything else

in the Matlab workspace (there is no global variable in EEGLAB). Thesecond command ([pop_loadset.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_loadset.m)) loads the dataset into the
*EEG* structure, and the last ([eeg_store.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_store.m)) stores the

dataset in the *ALLEEG* structure. For more detailed information, you
must study the Matlab help messages for these functions as explained
below:

Either (1) via the EEGLAB menu selections:
For [pop_loadset.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_loadset.m)\]: via <font color=brown> Help → EEGLAB

functions → Interactive pop_functions</font> or via
<font color=brown> Help → EEGLAB menus</font>For [eeg_store.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_store.m): via <font color=brown> Help → EEGLAB

advanced → Admin functions</font>

Or (2) using Matlab command line help

``` matlab
help \[functioname\]
```

Now use menu item <font color=brown>File → Save history → Session
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

``` matlab
eeglabhist
```

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
tutorial, the command ''\>\> eegh'' would return (with Matlab-style
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
from the main EEGLAB interactive window display the name of theunderlying pop_function in the window title bar. For instance, selecting <font color=brown>File → Load an existing dataset</font> to read in an existing dataset uses EEGLAB function [pop_loadset.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_loadset.m).



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

**1)** If the EEGLAB option to store more than one dataset may in memory is selected, selected via the <font color=brown>File → Preferences</font> menu item (first checkbox), then all current EEGLAB datasets are
stored in the structure array *ALLEEG,*. If you modify a dataset, you
should take care to copy the modified EEG dataset into *ALLEEG*.

Thus, after loading and then modifying an *EEG* structure to create a
new dataset, one might simply type:

``` matlab
ALLEEG(2) = EEG;
CURRENTSET = 2;
```

This command 'might' work as expected (if the new dataset is
internally consistent with the previous one). However, it is better touse the command [eeg_store.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_store.m)' which performs extensive

dataset consistency checking before storing the modified dataset.
Either use the following command to set the new dataset to be dataset
number 2,

``` matlab
[ALLEEG EEG] = eeg_store(ALLEEG, EEG, 2);
```

or

``` matlab
[ALLEEG EEG CURRENTSET] = eeg_store(ALLEEG, EEG);
```

to create a new dataset at the next available free space in the
*ALLEEG* variable. The dataset number will then be available in the
variable *CURRENTSET*. Note that if a previous dataset is already
assigned as dataset 2, then only the last command (above) will not
overwrite it. To view the changes in the main EEGLAB window, use the
command: *\>\> eeglab redraw;*
Another command that can be used to modify the *ALLEEG* structure is [pop_newset.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_newset.m). This command, which also performs extensive

dataset consistency checks, has more useful advanced options. To
modify the current dataset with its accumulated changes type:

``` matlab
[ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET,'overwrite', 'on');
```

If you wish to create a new dataset to hold the modified structure
use:

``` matlab
[ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET);
``` 

The returned argument *CURRENTSET* holds the set number of the new
dataset stored in EEGLAB.
Note: the *EEG* contains only the current dataset, so you must use
extra caution whenever updating this structure. e.g., Be sure it
contains the dataset you actually want to process!
The functions above call the function [eeg_checkset.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_checkset.m) to

check the internal consistency of the modified dataset.

``` matlab
EEG = eeg_checkset(EEG);
```

or

``` matlab
EEG = eeg_checkset(EEG, 'eventconsistency');
```

The second command above runs extra checks for event consistency
(possibly taking some time to complete) and regenerates the
*EEG.epoch* structures from the *EEG.event* information. This command
is only used when the event structure is being altered. See the [Event
tutorial](/Chapter_03:_Event_Processing "wikilink") to learn how to
work with EEG events.

The commands above are very useful if the option to maintain multiple
datasets is on. If the option to maintain multiple datasets is off
(via the <font color=brown>File → Preferences</font> menu item),
the *ALLEEG* variable is not used and *EEG* is the only variable that
contains dataset information. When using this option you can only
process one dataset at a time (the goal here is to use less memory and
being able to process bigger datasets). Any changes made by the user
to the *EEG* structure are thus applied instantaneously and are
irreversible. For consistency, all the commands above will work,
however the *ALLEEG* variable will be empty.

**2)** New fields added to the *EEG* structure by users will not be
removed by EEGLAB functions. Any additional information about a dataset
might be stored in the user-added field:

``` matlab
EEG.analysis_priority = 1;
```

**3)** The following are the reserved variable names used by EEGLAB:

         EEG        - the current EEG dataset
         ALLEEG     - array of all loaded EEG datasets   (Thus >> EEG = ALLEEG(CURRENTSET);)
         CURRENTSET - the index of the current dataset
         LASTCOM    - the last command issued from the EEGLAB menu
         ALLCOM     - all the commands issued from the EEGLAB menu during this EEGLAB session

Note: that EEGLAB does not use global variables (the variables above are
accessible from the command line but they are not used as global
variables within EEGLAB). The above variables are ordinary variables in
the global Matlab workspace. All EEGLAB functions except the maininteractive window function [eeglab.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeglab.m) (and a few other

display functions) process one or more of these variables explicitly as
input parameters and do not access or modify any global variable. This
insures that they have a minimum chance of producing unwanted 'side
effects' on the dataset.

Basic scripting examples
------------------------
Below is an example of Matlab script copied from the history that includes some of the
first basic manipulations that must be performed on a dataset. This
example works with the tutorial dataset *eeglab_data.set* and the
corresponding channel location file *eeglab_chan32.locs*. We have added a
few lines of code to locate the data files on your computer, and added comments, but otherwise
the script is directly copied from the EEGLAB history. The script in this section is available [here](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeglab_history.m)

``` matlab
%% Getting started with EEGLAB history
% The line below was added by us to locate data files
eeglab_path = fileparts(which('eeglab.m'));

% Start eeglab
[ALLEEG EEG CURRENTSET ALLCOM] = eeglab;

% Change option to process multiple datasets
pop_editoptions( 'option_storedisk', 0);

% Load the dataset (We modified the path manually here)
EEG = pop_loadset( 'eeglab_data.set', fullfile(eeglab_path, 'sample_data'));

% Load the channel location file, enabling automatic detection of channel file format'; We modified the path manually here
EEG.chanlocs=pop_chanedit(EEG.chanlocs, 'load',{ fullfile(eeglab_path, 'sample_data', 'eeglab_chan32.locs'), 'filetype', 'autodetect'});

% Store the dataset into EEGLAB
[ALLEEG EEG CURRENTSET ] = eeg_store(ALLEEG, EEG);

% High pass filter the data with cutoff frequency of 1 Hz.
EEG = pop_eegfilt( EEG, 1, 0, [], [0]); 

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

Note that some commands such as *eeg_store* and *pop_newset* are meant to manage multiple datasets.
If you are simply interested in processing the current dataset, they can be safely ignored. Below, is the same script
compactified, without the comments and the additional data managing commands.

```matlab
eeglab_path = fileparts(which('eeglab.m'));
[ALLEEG EEG CURRENTSET ALLCOM] = eeglab;
pop_editoptions( 'option_storedisk', 0);
EEG = pop_loadset( 'eeglab_data.set', fullfile(eeglab_path, 'sample_data')); % We modified the path manually here
EEG.chanlocs=pop_chanedit(EEG.chanlocs, 'load',{ fullfile(eeglab_path, 'sample_data', 'eeglab_chan32.locs'), 'filetype', 'autodetect'});
EEG = pop_eegfilt( EEG, 1, 0, [], [0]); 
EEG = pop_reref( EEG, [], 'refstate',0);
EEG.comments = pop_comments(EEG.comments,'','Dataset was highpass filtered at 1 Hz and rereferenced.',1);
EEG = pop_epoch( EEG, { 'square' }, [-1 2], 'newname', 'Continuous EEG Data epochs', 'epochinfo', 'yes');
EEG = pop_rmbase( EEG, [-1000 0]);
EEG.comments = pop_comments(EEG.comments,'','Extracted ''square'' epochs [-1 2] sec, and removed baseline.',1);
[ALLEEG EEG CURRENTSET] = eeg_store(ALLEEG, EEG, 1);
eeglab redraw 
```

Some other useful scripting examples copied from the EEGLAB history with added comments (see the function help messages for
more details):

1. Reduce sampling rate

``` matlab
%% Reduce sampling rate
% Reduce the sampling rate to 128 Hz (the above example was already sampled at 128 Hz'')
EEG = pop_resample( EEG, 128);

% Save it as a new dataset with the name Continuous EEG Data resampled
[ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET, 'setname', 'Continuous EEG Data resampled');

% Now on the GUI we returned to the previous dataset (before downsampling)
EEG = eeg_retrieve(ALLEEG, 1); CURRENTSET = 1;
```

2. Print a series of ERP scalp maps

``` matlab
%% Plot ERP maps 
% Every 100 ms from 0 ms to 500 ms [0:100:500]
% with the plot title - 'ERP image', in 2 rows and 3 columns. Below, the 0 means do not plot dipoles.
% Plot marks showing the locations of the electrodes on the scalp maps.
pop_topoplot(EEG,1, [0:100:500] , 'ERP image',[2:3] ,0, 'electrodes', 'on');
```

![500px]({{ site.baseurl }}/assets/images/topoplot_history2.png)

In the next section, instead of calling a pop_ function we will directly call some lower-level EEGLAB data
processing functions. Note that this script was not generated by EEGLAB and copied from EEGLAB history.
It was written from scratch by us for illustrative purposes. The command above [pop_topoplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=topoplot.m) can be executed bydirectly calling the signal processing function [topoplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=topoplot.m)
as shown below:

``` matlab
%% Topographic plot
% Define variables:
times = [0:100:500];
pos = round(eeg_lat2point(times/1000, 1, EEG.srate, [EEG.xmin EEG.xmax]));

% Convert times to points (or >pos = round( (times/1000-EEG.xmin)/(EEG.xmax-EEG.xmin) * (EEG.pnts-1))+1;)
% See the event tutorial for more information on processing latencies
mean_data = mean(EEG.data(:,pos,:),3);

% Average over all trials in the desired time window (the third dimension of 
% EEG.data allows to access different data trials). See tutorial about data structures
maxlim = max(mean_data(:));
minlim = min(mean_data(:));
maplimits = [ -max(maxlim, -minlim) max(maxlim, -minlim)]; % Get the data range for scaling the map colors

% Plot the scalp map series
figure
for k = 1:6
    sbplot(2,3,k);
    % A more flexible version of subplot
    topoplot( mean_data(:,k), EEG.chanlocs, 'maplimits', maplimits, 'electrodes', 'on', 'style', 'both');
    title([ num2str(times(k)) ' ms']);
end
cbar; % A more flexible version of Matlab colorbar
```

The topographic plot is virtually identical to the previous one, escept for the scale.

![500px]({{ site.baseurl }}/assets/images/topoplot_history1.png)
