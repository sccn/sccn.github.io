---
layout: default
title: EEGLAB functions
parent: Concepts guide
grand_parent: Tutorials
---
EEGLAB functions
=======
{: .no_toc }

This section is intended for users who have learned at least the basics
of MATLAB scriptwriting and wish to use EEGLAB and its many functions
to automate and/or customize data analyses.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

EEGLAB was designed for use by both novice and expert MATLAB users.
Depending on their level of MATLAB expertise, users can either interact
only with the EEGLAB graphic interface (GUI), else they can call EEGLAB
functions directly from the MATLAB command line or write their own
MATLAB scripts using EEGLAB functions and structures.

There are 3 types of EEGLAB functions:

1.  EEGLAB function that manage or check EEGLAB structures. For example
    [eeglab.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeglab.m), [eeg_checkset.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_checkset.m), [eeg_store.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_store.m), [pop_newset.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_newset.m), [std_checkset.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_checkset.m), [eeg_checkchanlocs.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_checkchanlocs.m), [eeglab_error.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeglab_error.m), [eeg_retrieve.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_retrieve.m), etc...


2.  Pop_functions: MATLAB functions with their own graphic interfaces.
    Called with no (or few) arguments (as from the EEGLAB user
    interface), these functions pop up a query window to gather
    additional parameter choices from users. They then generally call
    one or more of the EEGLAB toolbox signal processing functions. The
    pop_functions can also be called from the MATLAB command line or
    from MATLAB scripts. For example
    [pop_erpimage.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_erpimage.m), [pop_newtimef.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_newtimef.m), [pop_topoplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_topoplot.m), etc...

3.  Signal processing functions: The experienced MATLAB user can call
    the EEGLAB signal processing functions directly from the MATLAB command line or
    from their own analysis scripts. For example,
    [erpimage.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=erpimage.m), [newtimef.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=newtimef.m), [topoplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=topoplot.m), etc...

We will first see how *pop_* functions work.

EEGLAB pop_ functions
----------------------

Functions with the prefix *pop_* or *eeg_* are functions that take the
EEG structure as their first input argument. Functions with the prefix
*pop_* can be called either from the EEGLAB menu or from the MATLAB
command line, while functions with the prefix *eeg_* can only be called
from the MATLAB command line. When you select a menu entry in the EEGLAB
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
and paste it onto the MATLAB command line, the processing will be
performed directly, without popping up an interactive query window.
However, try removing all the input parameters to the function call
except the first, naming the EEG structure, and the pop_function will now
pop up a query window before performing any processing.
For example, open a new MATLAB session and try (you may have to type
*\>\> eeglab* to add access paths to the functions below)

``` matlab
EEG = pop_loadset;
```

An interactive window will pop up to ask for the dataset name, just as iT would do if the [pop_loadset.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_loadset.m) command were issued from
the EEGLAB menu via <span style="color: brown">File → Load dataset</span>. 

![Image:Pop_loadset.png](/assets/images/Pop_loadset2.png)

If,
on the other hand, the user provides two string arguments to the [pop_loadset.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_loadset.m) function, the first containing the filename and
the second the file path, no interactive window appears, and the dataset
is loaded directly.

``` matlab
EEG = pop_loadset('myfile.set', 'myfilepath')
```

Try another example:

``` matlab
EEG = pop_eegfilt(EEG);
```

This will pop up an interactive window allowing you to filter the data
according to the parameters you enter in the window. If you wish to
filter the EEG dataset without involving this graphic interface, type:

``` matlab
EEG = pop_eegfilt( EEG, 1, 0);
```

This command will highpass filter the data above 1 Hz. To see which parameter this function takes as argument, see [pop_eegfilt.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_eegfilt.m)
help. Keep in mind that all the interactive EEGLAB pop_ functions work
this way. You may copy commands from the EEG history fields and modify
the function input as desired. Function help messages are available
either from the EEGLAB graphic interface <span style="color: brown">Help →
EEGLAB functions → Interactive pop_ functions</span>, from the
[Internet](http://sccn.ucsd.edu/eeglab/allfunctions/), or from the
command line (type *\>\> help pop_xxx*).

Note: Only *pop_xxx* functions or *eeg_xxx*
functions process the EEG dataset structure; *eeg_xxx* functions
take the EEG data structure as an argument but do not pop up
interactive windows. Thus, they are typically not available from the
EEGLAB menu but only from the command line.

pop_ function vs signal processing functions
----------------------

As mentioned *pop_funcname.m* function is
a graphic user interface (gui) function that operates on the *EEG* data
structure using the stand-alone processing function *funcname.m*. The
stand-alone processing function, which has no knowledge of the dataset
structure, can process any suitable data matrix, whether it is an EEGLAB
data matrix or not.
For instance, [pop_erpimage.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_erpimage.m) calls the data processing and
plotting function [erpimage.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=erpimage.m). To review the input parameters
to these functions, either use the EEGLAB help menu (from the EEGLAB
window) or the MATLAB function help (from the MATLAB command line). For
example:

``` matlab
help pop_erpimage
help erpimage
```

As mentioned earlier, the two following function calls are equivalent:

``` matlab
eeglab; close; % add path
eeglabp = fileparts(which('eeglab.m'));
EEG = pop_loadset(fullfile(eeglabp, 'sample_data', 'eeglab_data_epochs_ica.set'));

figure; 
subplot(1,2,1); [outdata, outvar, outtrials] = pop_erpimage(EEG,1,12);
subplot(1,2,2); [outdata, outvar, outtrials] = erpimage( mean(EEG.data([12], :),1), ...
ones(1, EEG.trials)*EEG.xmax*1000, linspace(EEG.xmin*1000, EEG.xmax*1000, EEG.pnts), 'C3', 5, 0 );
```

![](/assets/images/erpimage_same.png)

**What do pop_ functions return?**

When called from the EEGLAB interface, pop_ functions do not return
variables. Instead, they may alter (when called for) the EEG data
structure itself. However, when called from the command line, many of
the visualization functions in the EEGLAB toolbox do return variables
when useful (e.g., the results plotted). To determine which variables
are returned by a function, it is important to understand how they work.
To carry out their required data processing, most of the pop_ functions
(each named *pop_xxx*) call a similarly named processing
function (*xxxx*). You may directly call these functions to
perform more advanced scripting. The important thing
is that both the pop_ function and its corresponding processing
function return the same variables (usually, the pop_ function help
messages refer the user to the processing function help message, which
describes the output variables). For example, the [pop_erpimage.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_erpimage.m) function returns the same outputs as the [erpimage.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=erpimage.m) function:

``` matlab
figure; [outdata1, outvar, outtrials] = pop_erpimage(EEG,1,12);
```

or the equivalent non-pop function call

``` matlab
figure; [outdata2, outvar, outtrials] = erpimage( mean(EEG.data([12], :),1), ...
ones(1, EEG.trials)*EEG.xmax*1000, linspace(EEG.xmin*1000, EEG.xmax*1000, EEG.pnts), 'C3', 5, 0 ); close
```

*Note:* If *pop_xxx* is a plotting function, then a
new figure is created automatically only when the function is called in
pop-up window mode. Otherwise, *pop_xxx* plotting commands,
as well as all non-pop plotting commands, should be
preceded by a MATLAB *figure* command, as in the example above. Note that
*figure* is added before the command by the EEGLAB history
mechanism. This feature allows you to create compound figures using
MATLAB *subplot* or the more flexible EEGLAB version [sbplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=sbplot.m).


Using EEGLAB data processing functions may require understanding some
subtleties of how they work and how they are called. Users should read
carefully the documentation provided with each function. Though for most
functions, the function documentation is supposed to describe function
output in all possible situations, occasionally, users may need to look in
the function script files themselves to see exactly how data processing
is performed. Since EEGLAB functions are open source, this is always
possible.

