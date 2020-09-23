---
layout: default
title: A13 Compiled EEGLAB
permalink: /docs/A13_Compiled_EEGLAB
parent: Docs
---

EEGLAB now exist as a compiled binary for Mac, Windows and Ubuntu and
may be downloaded on the [EEGLAB download
page](https://sccn.ucsd.edu/eeglab/download.php).

## Video

![400px|center|link=<https://www.youtube.com/watch?v=_F-5spN1FL4>](/assets/images/eeglab_compile.png)

## Installation

  - Download the ZIP file for the EEGLAB compiled version on the
    [download page](http://sccn.ucsd.edu/eeglab/download.php) and
    uncompress it
  - Each zip file contains 2 folders "for_redistribution" and
    "for_redistribution_files_only." Start by starting the installer
    in "for_redistribution" folder. If all goes well, this is the only
    thing you have to do to install EEGLAB.
  - If for some reason the installation process fails (permission issue
    for example), you may use the files in the folder
    "for_redistribution_files_only." Note that these files requires
    that the Matlab runtime engine be installed on your system - this
    step should have been done automatically above but we will assume
    here that this step fails. These are available as separate download
    [here](https://www.mathworks.com/products/compiler/matlab-runtime.html)
    (the version needed should appear when you start EEGLAB).
  - Notes for MacOS and Linux users: Apparently the compiled version of
    EEGLAB need to be installed using root user credentials. If you
    experience problems during the installation process on Mac, after
    downloading the zip file, open a terminal, go to the folder
    *for_redistribution/MyAppInstaller_web.app/Contents/MacOS* and
    type in sudo ./setup. This will start the installation as root. Once
    installed, you can run EEGLAB under your non-root account.

## Starting EEGLAB

  - Click "EEGLAB" to start EEGLAB (however see below)
  - Create shortcuts if necessary on the Desktop and in the "Start" menu
  - It is often preferable to have the command line output of EEGLAB as
    it contains relevant information. On windows, start EEGLAB using the
    file "eeglab_run_this_one_on_windows.bat." On OSx and Ubuntu,
    use the file run_EEGLAB.sh (might require to have it permission
    changed to be executable otherwise the content of the script will be
    shown).

## Similarity between the compiled and the Matlab version

  - Both version graphical interface are identical
  - There is nothing in the graphic interface that you can do under
    Matlab that is not possible to do in the compiled version. This
    includes using all the plugins and all the external modules attached
    to EEGLAB, saving scripts and running Matlab scripts.

## What is not possible to do using the compiled version

  - It is not possible to add new plugins or download and install third
    party plugins. To do so EEGLAB needs to be recompiled with the
    additional plugins.
  - When using scripts, is not possible to use external custom Matlab
    functions or to define new functions
  - When using scripts, the range of possible Matlab command usable is
    limited to the Matlab core commands, all EEGLAB commands and a few
    commands from the signal processing, the statistics and the
    optimization toolbox (commands which are included in the compiled
    code).
  - It is not possible to modify EEGLAB source code.

## Can I compile EEGLAB myself?

Compiling EEGLAB usually consist in opening the "eeglab.prj" file (in
the root EEGLAB folder) using the Matlab Compiler Graphical App, then
pressing the package button. However, there might be some path issue
that require fixing on your system. This
[page](/Compiling_EEGLAB:_Technical_note_for_developers "wikilink")
contains notes we use to compile EEGLAB in our lab (it is relatively
complex because we have automated nightly build for 3 operating
systems). More notes on compiling are available on this
[page](/Compiling_EEGLAB:_Technical_note_for_developers "wikilink").

## How to check the integrity of the compiled version

Differences between the Matlab and the compiled EEGLAB version mostly
arise because of the way external data files are handled. This is how we
check the integrity of the compiled version (since it is not possible to
automate this process yet). You may run the script
**test_compiled_version.m** in the folder functions/support_files
(you might have to change the path to the data files).

1.  Start EEGLAB
2.  Edit options and change them; go back to option and make sure they
    have changed
3.  Load continuous dataset. Look up electrodes, run clean raw data, Run
    ICA, run IClabel
4.  Perform source localization of ICA components using Dipfit
5.  Plot 3-D ERP after coregistering
6.  Load Stern study, precompute_ERP and plot them. Try using
    statistics.
7.  Check that the help menus are functional

If all of the above checks, then the compiled EEGLAB version is
considered checked. We check the version separately on Windows and
Unix/MacOS (Unix and MacOS are not checked independently since MacOS is
a version of Unix).

## Frequently asked questions

  - Can I run some of my own Matlab scripts using the EEGLAB compiled
    version? Yes as long as they use standard Matlab functions or EEGLAB
    functions.
  - Is the compiled code faster than the non compiled one? No, it is the
    same speed as it is still interpreted by the Matlab runtime engine.
  - What version of Matlab was used to compile the code? As of 2019, we
    provide a compiled version for every released EEGLAB version.
  - Is it legal since I do not own Matlab? Yes, it is perfectly legal.
    Although it is illegal to run cracked version of Matlab, it is
    perfectly legal to distribute the Matlab Runtime Engine and compiled
    Matlab code.
  - Can I use this program for commercial applications such as my
    clinical private practice? EEGLAB is a research software not a
    clinical software. The program is provided as is with no warrantee
    of any kind. Although the EEGLAB core code is released under a BSD
    2.0 license that allows for commercial use, some of the plugins
    included in the compiled version are not (this includes plugins
    handling source reconstruction for example).
  - Trouble shooting\! Do not hesitate to submit a bug or comment on the
    [EEGLAB Gihub issue tracker](https://github.com/sccn/eeglab/issues)
    if you encounter a problem running a compiled version of EEGLAB.

{ {Backward_Forward|A12:_Quick_Tutorial_on_Rejection|A12: Quick
Tutorial on Rejection|EEGLAB| Return to the EEGLAB Wiki Home} }
[Category:IV. Appendix](/Category:IV._Appendix "wikilink")
[Category:EEGLAB](/Category:EEGLAB "wikilink")