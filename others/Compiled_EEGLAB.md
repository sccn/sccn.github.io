---
layout: default
title: Download EEGLAB compiled
long_title: Download the compiled of EEGLAB 
parent: Download EEGLAB
---

The compiled version of EEGLAB
=========================
{: .no_toc }

EEGLAB exists as a compiled binary for Mac, Windows, and Ubuntu and
may be downloaded on the [EEGLAB download
page](https://sccn.ucsd.edu/eeglab/download.php). The video below shows how to install the compiled version of EEGLAB.

<center> <iframe width="560" height="315" src="https://www.youtube.com/embed/_F-5spN1FL4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center> 

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

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

Troubleshooting the compiled version of EEGLAB
-----------------------------------------------
On MAC OSX, you might get a message that your operating system is too old, so you should try an older version of the compiled EEGLAB version.

Starting EEGLAB usually means opening your *Application* (Mac) or *Program files* folder, opening the EEGLAB folder, and clicking on the EEGLAB application. There are some caveat though:
- If this does not work, try running EEGLAB as an administrator
- On MAC, if clicking the App does not work, try invoking a terminal, go to the folder containing EEGLAB, and type in

```
./run_EEGLAB.sh /Applications/MATLAB_R2022b.app
```

If you call *run_EEGLAB.sh* without argument, it will tell you that you need to point to the MATLAB runtime engine. Above, we pointed to */Applications/MATLAB_R2022b.app*, but the folder might be different on your computer. Note that the runtime engine must correspond to the MATLAB version with which EEGLAB was compiled. The runtime engine is installed with EEGLAB, so it should already be on your computer, but you might still need to point to it.

- On MAC, the EEGLAB terminal does not show by default. Instead, it would be best if you used the solution above from the terminal. Alternatively, you click on the program named *eeglab_run_this_one_on_osx_or_linux*, which is an executable. This does not always work due to permission problems.

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
    [EEGLAB GitHub issue tracker](https://github.com/sccn/eeglab/issues)
    if you encounter a problem running a compiled version of EEGLAB.

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


Can I compile EEGLAB myself?
----------------------------

Compiling EEGLAB usually consists of opening the "eeglab.prj" file (in
the root EEGLAB folder) using the MATLAB Compiler Graphical App, and
pressing the *package* button. However, there might be some path issues
that require fixing on your system. See detailed instructions below.

### Manual compilation notes

1. Clone EEGLAB with default plugins

``` Matlab 
git clone --recurse-submodules https://github.com/sccn/eeglab.git
```

2. Install additional plugins (plugins that are already installed will
be skipped). Some folders from the plugins clean_rawdata
and Fieldtrip should
be removed to avoid compilation issues. Use the
following script to install plugins and remove these folders:

```matlab
eeglab  % restart the fleshly installed eeglab

% Installing plugins
plugin_askinstall('ANTeepimport', 'eegplugin_eepimport', true);
plugin_askinstall('Fieldtrip-lite', 'ft_defaults', true);
plugin_askinstall('Fileio', 'ft_read_data', true);
plugin_askinstall('IClabel', 'eegplugin_iclabel', true);
plugin_askinstall('PICARD', 'picard', true);
plugin_askinstall('vised', 'vised', true);
plugin_askinstall('bids-matlab-tools', 'bids_export', true);
plugin_askinstall('bids-validator', 'pop_validatebids', true);
plugin_askinstall('bva-io', 'eegplugin_bva_io', true);
plugin_askinstall('clean_rawdata', 'eegplugin_clean_rawdata', true);
plugin_askinstall('dipfit', 'eegplugin_dipfit', true);
plugin_askinstall('egilegacy', 'eegplugin_egilegacy', true);
plugin_askinstall('firfilt', 'eegplugin_firfilt', true);
plugin_askinstall('irrfilt', 'eegplugin_iirfilt', true);
plugin_askinstall('musedirect', 'eegplugin_musedirect', true);
plugin_askinstall('musemonitor', 'eegplugin_musemonitor', true);
plugin_askinstall('neuroscanio', 'eegplugin_neuroscanio', true);
plugin_askinstall('xdfimport', 'eegplugin_xdfimport', true);

% Removing clean_rawdata files
% For clean_rawdata, remove folder manopt/reference/m2html.
CleanRawData_folder = fileparts(which('clean_rawdata.m'));
rmdir(fullfile(CleanRawData_folder,'manopt','reference','m2html'), 's');
rmdir(fullfile(CleanRawData_folder,'manopt','tests'), 's');

% Removing ICLabel files
iclabel_folder = fileparts(which('iclabel.m'));
% rmdir(fullfile(iclabel_folder,'matconvnet','examples'), 's'); % not there any more?

% Removing FieldTrip files
% For Fieldtrip remove folders compat, external/afni, external/spm8, external/spm12, external/gifti, external/eeglab, external/bemcp and external/npmk
FieldTrip_folder = fileparts(which('ft_defaults.m'));
rmdir(fullfile(FieldTrip_folder,'compat'), 's');
rmdir(fullfile(FieldTrip_folder,'external','afni'), 's');
rmdir(fullfile(FieldTrip_folder,'external','spm8'), 's');
rmdir(fullfile(FieldTrip_folder,'external','spm12'), 's');
rmdir(fullfile(FieldTrip_folder,'external','gifti'), 's');
rmdir(fullfile(FieldTrip_folder,'external','eeglab'), 's');
rmdir(fullfile(FieldTrip_folder,'external','bemcp'), 's');
rmdir(fullfile(FieldTrip_folder,'external','npmk'), 's');
rmdir(fullfile(FieldTrip_folder,'external','signal'), 's');
rmdir(fullfile(FieldTrip_folder,'external','mffmatlabio'), 's');
rmdir(fullfile(FieldTrip_folder,'external','egi_mff_v2'), 's');
```

3. Optional: Edit the eeglab.m file and add new plugins to the compiled version of EEGLAB (line 900). Change the version of EEGLAB in the prj file.

3. Open the "eeglab.prj" file in the Matlab editor. Check the path for plugins. If a new version is available, rename the version in the eeglab.prj file.

3. Change the EEGLAB version in the eeg_getversion.m and in the eeglab.prj files.

3. Open the Application compiler (Matlab tab "Apps" and button
"Application compiler") and open the "eeglab.prj" file. DO NOT RESAVE THE PROJECT IN THE APPLICATION COMPILER AS IT TENDS TO MESS UP PATHS FOR CROSS PLATFORM COMPILATION.

4. On the command line, type "setenv('MCC_USE_DEPFUN','1')". There will still be class errors when checking dependencies, but the EEGLAB will compile anyway.

4. Press "Package" and wait (usually 30 minutes or so)

4. If successful, 3 folders are created. You may test the compiled
EEGLAB version by running the program in the "for_testing" folder.

4. Test the compiled version for potential runtime errors (see notes on
testing
[here](https://sccn.github.io/others/Compiled_EEGLAB.html#how-to-check-the-integrity-of-the-compiled-version)).
On Mac and OSX use ./run_eeglab.sh MATLAB_PATH.

> <span style="color: red">Known problem: check documentation in compiled version</span>

> <span style="color: red">Known error: mex files not included for ANT plugin (ASR test file present)</span>

### Plugins selected for future inclusion

Selected for future inclusion but require testing. If you have a plugin
you want to include, please try compiling with the plugin and testing
the plugin in the compiled EEGLAB version. If all is functional, email
us at eeglab_at_sccn.ucsd.edu and your plugin will be included in the
next release.

Adding new plugins

-   Download or clone plugin
-   Add to eeglab.m
-   Compile
-   Update this page (create a pull request)

| Plugin name       | Comment                                                                                               |
|-------------------|-------------------------------------------------------------------------------------------------------|
| Biosig            | Path issue for compiler. Using the version included in Fieldtrip                                                           |
| MFFMatlabIO       | Issue with finding the JAR file at execution time; more debugging necessary before inclusion possible |
| bids-matlab-tools | Not tested                                                                                            |
