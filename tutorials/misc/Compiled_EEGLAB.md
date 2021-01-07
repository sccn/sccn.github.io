---
layout: default
title: compiled EEGLAB
parent: Reference Topics
grand_parent: Tutorials
---

The compiled version of EEGLAB <span style="color: green">- DONE</span>
=========================

EEGLAB exists as a compiled binary for Mac, Windows, and Ubuntu and
may be downloaded on the [EEGLAB download
page](https://sccn.ucsd.edu/eeglab/download.php). The video below shows how to install the compiled version of EEGLAB.

<center> <iframe width="560" height="315" src="https://www.youtube.com/embed/_F-5spN1FL4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center> 

Installation
------------

-   Download the ZIP file for the EEGLAB compiled version on the
    [download page](http://sccn.ucsd.edu/eeglab/download.php) and
    uncompress it
-   Each zip file contains 2 folders "for_redistribution" and
    "for_redistribution_files_only." Start by starting the installer in
    "for_redistribution" folder. If all goes well, this is the only
    thing you have to do to install EEGLAB.
-   If for some reason, the installation process fails (permission issue,
    for example), you may use the files in the folder
    "for_redistribution_files_only." Note that these files require that
    the MATLAB runtime engine be installed on your system - this step
    should have been done automatically above but we will assume here
    that this step fails. These are available as separate download
    [here](https://www.mathworks.com/products/compiler/matlab-runtime.html)
    (the Runtime version you need should appear when you attempt to start EEGLAB).
-   Notes for MacOS and Linux users: Apparently, the compiled version of
    EEGLAB needs to be installed using root user credentials. If you
    experience problems during the installation process on Mac, after
    downloading the zip file, open a terminal, go to the folder
    *for_redistribution/MyAppInstaller_web.app/Contents/MacOS* and type
    in *sudo ./setup*. This will start the installation as root. Once
    installed, you may use EEGLAB under your user (non-root) account.

Starting EEGLAB
---------------

-   Click "EEGLAB" to start EEGLAB (however, see below)
-   Create shortcuts if necessary on the Desktop and in the "Start" menu
-   It is often preferable to have the command line output of EEGLAB as
    it contains relevant information. On Windows, start EEGLAB using the
    file "eeglab_run_this_one_on_windows.bat." On OSx and Ubuntu, use
    the file run_EEGLAB.sh (might require to have its permission changed
    to be executable; otherwise, the content of the script will be shown).

Similarity between the compiled and the MATLAB version of EEGLAB
------------------------------------------------------

-   Both version graphical interface are identical
-   There is nothing in the EEGLAB graphic interface that you can do under
    MATLAB that is not possible to do in the compiled version of EEGLAB. This
    includes using all the plugins and all the external modules attached
    to EEGLAB, saving scripts, and running MATLAB scripts.

### What is not possible to do using the compiled version

-   It is not possible to add new plugins or download and install third-party 
    plugins. To do so, EEGLAB needs to be recompiled with the
    additional plugins.
-   When using scripts, it is not possible to use external custom MATLAB
    functions or to define new functions
-   When using scripts, the range of possible MATLAB commands is
    limited to the MATLAB core commands, all EEGLAB commands and a few
    commands from the signal processing, the statistics and the
    optimization toolbox (commands which are included in the compiled
    code).
-   It is not possible to modify EEGLAB source code.

Can I compile EEGLAB myself?
----------------------------

Compiling EEGLAB usually consists of opening the "eeglab.prj" file (in
the root EEGLAB folder) using the MATLAB Compiler Graphical App, and
pressing the *package* button. However, there might be some path issues
that require fixing on your system. Ask us for detailed instructions.

How to check the integrity of the compiled version
--------------------------------------------------

Differences between the MATLAB and the compiled EEGLAB version mostly
arise because of the way external data files are handled. This is how we
check the  compiled version's integrity (since it is not possible to
automate this process yet). You may run the script
*test_compiled_version.m* in the folder functions/support_files (you
might have to change the path to the data files). For testing, we use the [STERN STUDY](https://sccn.ucsd.edu/eeglab/download/STUDYstern_125hz.zip) (0.9 Gb). Please download the data on your computer.

1.  Start EEGLAB
2.  Edit options and change them; go back to option and make sure they
    have changed
3.  Load the continuous tutorial dataset "eeglab_data.set". Look up electrodes, run clean raw data, Run
    ICA, run IClabel
4.  Perform source localization of ICA components using Dipfit
5.  Plot 3-D ERP after coregistering
6.  Load Stern study, precompute ERPs and plot them. Try using statistics.
7.  Check that the help menus are functional

If all of the above checks, then the compiled EEGLAB version is
considered verified. We check the version separately on Windows and
Unix/MacOS.

Frequently asked questions
--------------------------

-   Can I run some of my MATLAB scripts on the EEGLAB compiled
    version? Yes, as long as they use standard MATLAB functions or EEGLAB
    functions.

-   Is the compiled code faster than the non compiled one? No, it is the same speed as the MATLAB runtime engine still interprets it.
-   Is it legal since I do not own MATLAB? Yes, it is perfectly legal.
    Although it is illegal to run a pirated version of MATLAB, it is
    perfectly legal to distribute the MATLAB Runtime Engine and compiled
    MATLAB code.
-   Can I use this program for commercial applications such as my
    private clinical practice? EEGLAB is a research software package, not a clinical software package. The program is provided as-is with no warranty
    of any kind. Although the EEGLAB core code is released under a BSD
    2.0 license that allows for commercial use, some of the plugins
    included in the compiled version are not (this includes plugins
    handling source reconstruction, for example).
-   Trouble shooting! Do not hesitate to submit bug reports on the
    [EEGLAB Gihub issue tracker](https://github.com/sccn/eeglab/issues)
    if you encounter a problem running a compiled version of EEGLAB.

