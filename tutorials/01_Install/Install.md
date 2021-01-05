---
layout: default
title: 1. Installing EEGLAB
categories: tutorial
parent: Tutorials
nav_order: 1
---
Installing and starting EEGLAB
================

First, download [EEGLAB](http://sccn.ucsd.edu/eeglab/install.html),
which contains the tutorial dataset in the _sample_data_ subfolder of the EEGLAB distribution.
When you uncompress EEGLAB you will obtain a folder named "eeglabxxxx"
(note: current version number 'xxxx' will vary).

Under Windows, Matlab
usually recommends but does not require that you place toolboxes
in the *Application/MatlabRxxxx/toolbox/* folder (note: this name should
vary with the Matlab version 'xxxx'). In Linux, the Matlab toolbox
folder is typically located at */usr/local/pkgs/Matlab-rxxxx/toolbox/*. In MacOS it is in "/Application/MATLAB_Rxxxx". You may also place the folder anywhere else on your path.

Now, we will start Matlab and EEGLAB.

Start Matlab
------

- Windows: Go to Start, find Matlab, and run it.
- MacOS: Start from the Matlab icon in the dock or the
    application folder.
- Linux: Open a terminal window and type *matlab* and hit enter.

Switch to the EEGLAB directory (folder)
------

You may browse for the directory by clicking on the button marked *"…"* in the upper right of the screen.


![](/assets/images/Matlab_main_screen.png)


 This opens the window below. Double-click on a directory to enter it.
 Double-clicking on ".." in the folder list takes you up one level. Hit
 *Ok* once you find the folder or directory you wish to be in.
 Alternatively, from the command line, use *cd* (change directory) to
 get to the desired directory.

Start EEGLAB
------

Type *eeglab* at the Matlab command line and hit enter. EEGLAB will
automatically add itself to the Matlab path.


![](/assets/images/Matlab_Command_Line.png)


 The blue main EEGLAB window below should pop up,  with its seven menu
 headings: <span style= "color:brown">File, Edit, Tools, Plot, Study, Datasets, Help </span> arranged in typical (left-to-right) order of use.

![](/assets/images/Eeglab20191.png)


Adding EEGLAB to the Matlab path
------

You may want to add the EEGLAB folder to the Matlab search path so the
next time you start Matlab, you will be able to directly open EEGLAB.

If you started Matlab through its graphical interface, go to the
<span style="color: brown">file</span> menu item and select <font color=brown>set
path</font>. This will open the following window.


![Matlab set path gui](/assets/images/Matlab_set_path_gui.png)

Or, if you are running Matlab from the command line, type *pathtool*
and hit return; this will also call up this window.

Click on the button marked *Add folder* and select the folder
"eeglabxxxxx", then hit *OK* (EEGLAB will take care of adding its
subfolder itself).

Hit *save* in the *pathtool* window. This will make the EEGLAB call-up
function *eeglab* available in future Matlab sessions. Note that if
you are installing a more recent version of EEGLAB, it is best to
remove the old version from the Matlab path (select, then hit
*Remove*) to avoid the possibility of calling up outdated routines. It
is preferable NOT to add the *eeglab* path with its subfolder and let
EEGLAB manage paths (when you start EEGLAB, it automatically adds
the path it needs).
