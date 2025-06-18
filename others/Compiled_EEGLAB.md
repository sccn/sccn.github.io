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

Below are the instructions to install the MAC version. The Windows version follows the same procedure (although it is somewhat less complex towards the end, which is why we focus on the MAC version). Uncompress the archive and run the installer. 

-   Download the ZIP file for the EEGLAB compiled version on the
    [download page](http://sccn.ucsd.edu/eeglab/download.php) and
    uncompress it
-   Uncompress the zip file and run the installation file.
-   If, for some reason, the installation process fails, you may need to run it as an administrator

The following screen will pop up.

<br/><br/> 

<img width="844" alt="Screen Shot 2023-09-01 at 11 40 52 AM" src="https://github.com/sccn/sccn.github.io/assets/1872705/de3a5a88-8c88-4c72-84ca-5d54bab23cb2">

<br/><br/> 

Simply press next. Press next as well on the next three screens. Do not change the default paths.

<br/><br/> 

<img width="839" alt="Screen Shot 2023-09-01 at 11 40 59 AM" src="https://github.com/sccn/sccn.github.io/assets/1872705/4b291279-5d08-462a-b89f-6b6283b7e6cb">

<br/><br/> 

<img width="841" alt="Screen Shot 2023-09-01 at 11 41 17 AM" src="https://github.com/sccn/sccn.github.io/assets/1872705/1a2b6822-59d6-4e2c-b376-5bdd0d020a0d">

<br/><br/> 

<img width="841" alt="Screen Shot 2023-09-01 at 11 10 54 AM" src="https://github.com/sccn/sccn.github.io/assets/1872705/9c197d8b-d664-4787-a770-634cd36a5b44">

<br/><br/> 

**MAC only**. When the installation is completed, the following message will appear. **YOU CAN IGNORE THE MESSAGE**

<br/><br/> 

<img width="837" alt="Screen Shot 2023-09-01 at 11 54 52 AM" src="https://github.com/sccn/sccn.github.io/assets/1872705/eaee9f29-9875-4b2e-91f6-5e904484278f">

<br/><br/> 

Instead, go to the installed EEGLAB version and select the file **EEGLAB_verbose** on MAC or **EEGLAB.exe** on Windows as shown below. Do not click on **EEGLAB.app** on MAC because you will not have the command prompt and EEGLAB might not start unless you set the path above (the part we mentioned you should ignore). Setting the path is possible, but it is not straightforward. Alternatively, on MAC, use the command  "./run_EEGLAB.sh /Applications/MATLAB/MATLAB_Runtime/R2024a/" (the MATLAB runtime version must match the one used to compile EEGLAB and should be automatically installed with EEGLAB; if not it can be found [here](https://www.mathworks.com/products/compiler/matlab-runtime.html)).

<br/><br/> 

![Screenshot 2024-08-29 at 13 20 25](https://github.com/user-attachments/assets/6757f18f-eb1d-4c4c-8b04-6924bba63275)

<br/><br/> 

It should take about 1 minute for EEGLAB to start.

<br/><br/> 

<img width="844" alt="Screen Shot 2023-09-01 at 11 42 30 AM" src="https://github.com/sccn/sccn.github.io/assets/1872705/8a08b846-a0cb-45b2-9be8-f8732f5a6ecf">

## Troubleshooting

On both MAC and Windows, you might need to run EEGLAB as an administrator to access some folders.

On MAC OSX, you might get a message that your operating system is too old, so you should try an older version of the compiled EEGLAB version.

Let us know if you encounter problems and how you solve them. See also below how 

## Executing code and scripts with the compiled version

Scripts can be executed from the EEGLAB GUI in the compiled version. Note that functions and subscripts cannot be used, although the script can use all MATLAB and EEGLAB functions. If you have a script that calls another script, you must combine both scripts into a single one. If you are calling a user-defined function, you must convert this function into a script and include the code in your script. The menu below may be used to execute scripts.

![Screenshot 2024-07-10 at 16 00 43](https://github.com/sccn/sccn.github.io/assets/1872705/5cfc2ad8-f0fa-4e5b-b866-099370f2f83e)

Scripts and code snippets may also be executed from the command line. Below is an example from the command line on Windows. The same may be done on MAC using the **EEGLAB_verbose** executable. On Windows, on the DOS command line, go to the folder containing the EEGLAB.exe file and type:

```
.\EEGLAB.exe "disp('hello world');"
```

Below is the output.

![Screenshot 2024-07-10 at 15 53 41](https://github.com/sccn/sccn.github.io/assets/1872705/d6192ace-79d0-4741-9c5a-7b9415976c9f)

You may also write a script containing MATLAB and EEGLAB code. For example, save the same text "disp('hello world');" in the file **script.m** then type:

```
.\EEGLAB.exe ".\script.m"
```

Below is the output.

![Screenshot 2024-07-10 at 15 59 15](https://github.com/sccn/sccn.github.io/assets/1872705/8cec47dc-e82f-4012-a646-b968760c7358)

Of course, running the "hello world" examples mentioned above is not particularly interesting. Instead, you might want to execute the EEGLAB scripts provided in the tutorial section.

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

2. Install additional plugins (already installed plugins will
be skipped). Some folders from the plugins clean_rawdata
and Fieldtrip should
be removed to avoid compilation issues. **Do not use the GIT version of Fieldtrip.** as it makes the release 1.5Gb instead of 200Mb. Instead get the latest plugin. Use the
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
plugin_askinstall('iirfilt', 'eegplugin_iirfilt', true);
plugin_askinstall('musedirect', 'eegplugin_musedirect', true);
plugin_askinstall('musemonitor', 'eegplugin_musemonitor', true);
plugin_askinstall('neuroscanio', 'eegplugin_neuroscanio', true);
plugin_askinstall('xdfimport', 'eegplugin_xdfimport', true);
plugin_askinstall('mffmatlabio', 'pop_mffimport', true);
plugin_askinstall('scd', 'eegplugin_scd', true);
plugin_askinstall('snapmaster', 'eegplugin_snapmaster', true);
plugin_askinstall('biosig', 'sread', true);

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

3. Optional: Edit the eeglab.m file and add new plugins to the compiled version of EEGLAB (line 900).

3. Open the "eeglab.prj" file in the Matlab editor. Check the path for plugins. If a new version is available, rename the version in the eeglab.prj file.

3. Change the EEGLAB version in the eeg_getversion.m **and** in the eeglab.prj files.

3. Open the Application compiler (Matlab tab "Apps" and button
"Application compiler") and open the "eeglab.prj" file. DO NOT RESAVE THE PROJECT IN THE APPLICATION COMPILER AS IT TENDS TO MESS UP PATHS FOR CROSS PLATFORM COMPILATION.

4. If there are class errors (and there usuly are), use the command below. There will still be class errors when checking dependencies, but the EEGLAB will compile anyway. On the command line, type

```matlab
setenv('MCC_USE_DEPFUN','1')
```

7. Make sure the file EEGLAB_verbose has the right version of MATLAB listed and change the version number

4. **Windows**. Remove Mac files, check the command line option and Press "Package" and wait (usually 10 minutes or so)

4. **MAC**. Remove Windows file (EEGBIDS.bat) and Press "Package" and wait (usually 30 minutes or so)

4. If successful, 3 folders are created. You may test the compiled
EEGLAB version by running the program in the "for_testing" folder.

4. Test the compiled version for potential runtime errors (see notes on
testing
[here](https://sccn.github.io/others/Compiled_EEGLAB.html#how-to-check-the-integrity-of-the-compiled-version)).
On Mac and OSX use ./run_eeglab.sh MATLAB_PATH.

> <span style="color: red">Known problem: check documentation in compiled version</span>

> <span style="color: red">Known error: mex files not included for ANT plugin (ASR test file present)</span>

4. Distribute the "for redistribution folder"

### Plugins selected for future inclusion

Selected for future inclusion but requires testing. If you have a plugin
you want to include, please try compiling with the plugin and testing
the plugin in the compiled EEGLAB version. If all is functional, email
us at eeglab_at_sccn.ucsd.edu, and your plugin will be included in the
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
