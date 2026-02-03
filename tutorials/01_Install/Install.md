---
layout: default
title: 1. Installing EEGLAB
long_title: 1. Installing EEGLAB
categories: tutorial
parent: Tutorials
nav_order: 1
---

Installing and starting EEGLAB
==============================

First, download [EEGLAB](https://sccn.ucsd.edu/eeglab/download.php),  
which contains the tutorial dataset in the _sample_data_ subfolder of the EEGLAB distribution.  
When you decompress EEGLAB, you will obtain a folder named "eeglabxxxx"  
(note: the current version number 'xxxx' will vary).

Under Windows, MATLAB usually recommends but does not require that you place toolboxes  
in the *Application/MATLABRxxxx/toolbox/* folder (note: this name should  
vary with the MATLAB version 'xxxx'). In Linux, the MATLAB toolbox  
folder is typically located at */usr/local/pkgs/MATLAB-rxxxx/toolbox/*. In **macOS**, it is in */Applications/MATLAB_Rxxxx/*. You may also place the folder anywhere else on your path.

Now, we will start MATLAB and EEGLAB.

Start MATLAB
------------

- **Windows**: Go to Start, find MATLAB, and run it.  
- **macOS**: Start from the MATLAB icon in the Dock or the Applications folder.  
- **Linux**: Open a terminal window and type *matlab*, then hit Enter.

Switch to the EEGLAB directory
------------------------------

You may browse for the directory by clicking on the button marked *"…"* in the upper right of the screen.

![](/assets/images/MATLAB_main_screen.png)

This opens the window below. Double-click on a directory to enter it.  
Double-clicking on ".." in the folder list takes you up one level. Hit *OK* once you find the folder or directory you wish to be in.  
Alternatively, from the command line, use *cd* (change directory) to get to the desired directory.

Start EEGLAB
------------

Type *eeglab* at the MATLAB command line and hit Enter. EEGLAB will  
automatically add itself to the MATLAB path.

![](/assets/images/MATLAB_Command_Line.png)

The blue main EEGLAB window below should pop up, with its seven menu  
headings: <span style="color:brown">File, Edit, Tools, Plot, Study, Datasets, Help</span> arranged in typical (left-to-right) order of use.

![](/assets/images/Eeglab20191.png)

Adding EEGLAB to the MATLAB path
--------------------------------

You may want to add the EEGLAB folder to the MATLAB search path so the  
next time you start MATLAB, you will be able to directly open EEGLAB.

If you started MATLAB through its graphical interface, go to the  
<span style="color: brown">File</span> menu item and select <span style="color: brown">Set Path</span>. This will open the following window.

![MATLAB set path gui](/assets/images/MATLAB_set_path_gui_2.png)

Or, if you are running MATLAB from the command line, type *pathtool* at the command line  
and hit Enter; this will also call up this window.

Click on the button marked *Add Folder* and select the folder  
"eeglabxxxx", then hit *OK* (EEGLAB will take care of adding its  
subfolders itself).

Hit *Save* in the *pathtool* window. This will make the EEGLAB call-up  
function *eeglab* available in future MATLAB sessions. Note that if  
you are installing a more recent version of EEGLAB, it is best to  
remove the old version from the MATLAB path (select it, then hit  
*Remove*) to avoid the possibility of calling up outdated routines. It  
is preferable **not** to add the *eeglab* path with its subfolders manually—let  
EEGLAB manage paths (when you start EEGLAB, it automatically adds  
the paths it needs).
