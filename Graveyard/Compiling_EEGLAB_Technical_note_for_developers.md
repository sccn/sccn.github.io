---
layout: default
---

In this page, we address how to set up computational resources at SCCN
to compile EEGLAB nightly. Notes and instructions are provided for three
different OS: macOS, Ubuntu, and Windows. In the current setup, we are
using a Mac computer (*delorming.ucsd.edu*) to host two virtual machines
(VM). VMWare Fusion is used in the host machine to run Windows (Windows
10 x64) and Linux (Ubuntu 64-bit 18.04). The compiled EEGLAB files for
macOS and Windows are stored in a common folder synchronized through
Google Drive. The compiled files in the Ubuntu VM are transferred to the
Google Drive file in the host machine, where they are uploaded and
synchronized. Compilation of EEGLAB in the three OS is performed
nightly. For this, a system daemon
([cron](https://help.ubuntu.com/community/CronHowto)) is used to execute
the task in the Mac (host) and Ubuntu (VM) machines. To automate the
compilation in the Windows VM, a job was set up in Task Scheduler. In
the following section, details for each specific OS are provided. Before
beginning, make sure the host Mac is connected to the Internet, and that
you have access to the Google account used in the Google Drive app.

Automated compilation notes
===========================

Automated compilation setup on macOS (Host machine: delorming)
--------------------------------------------------------------

-   Start by installing MATLAB on the host machine. In the current setup
    (10/18), MATLAB 2018a is installed. It is important to check and
    install any updates released by Mathworks for the version installed.
    E.g., for the 2018a version, the update
    [here](https://www.mathworks.com/downloads/web_downloads/download_update?release=R2018a&s_tid=ebrg_R2018a_2_1757132)
    is necessary for proper operation of the compiled EEGLAB.

<!-- -->

-   Set up the [EEGLAB git](https://github.com/sccn/eeglab.git)
    repository. To be consistent across all three OS, the repository
    should be created in *\~/program_files/eeglab*. The following code
    can be used on the terminal to create the folder and set up the
    repository.

``` powershell
cd ~
mkdir program_files
git clone https://github.com/eeglabdevelopers/eeglab.git
git pull
git submodule update --init --recursive
git pull --recurse-submodules
```

-   Add EEGLAB to the MATLAB path. You may run into issues with
    permissions. To fix this. Locate the *pathdef.m* file and change the
    permissions. To locate the file, type in MATLAB command window:
    *which('pathdef.m')*. Use the output to locate the file in the
    terminal to change the permission using: *chmod 777 path2pathdef*

``` powershell
chmod 777 path2pathdef.m
```

-   Download and install the Google Drive App for Mac. The default name
    of the Google Drive folder is *Google Drive*. Since in a Unix-based
    system spaces in pathnames may raise issues (and are also
    aesthetically dubious), the folder is renamed as *Google Drive*.
    After renaming the folder, you need to make sure to update the link
    to the new folder in the Google Drive App. It is probable you will
    receive a notification from the application regarding the lost of
    the link to the file. This is a reminder of what to do in this step.

<!-- -->

-   Copy the folder *eeglab_comp_daily*, located in
    *.../program_files/eeglab/functions/adminfunc/*, to the *Google
    Drive* folder. This folder contains three subfolders:
    *compile_tools*, *macos*, *ubuntu* and *windows*. The folder
    *compile_tools* contains the scripts necessary for the compilation
    and setup of [crontab
    job](https://help.ubuntu.com/community/CronHowto). The folders
    *macos*, *ubuntu* and *windows* will be initially empty, but will be
    populated with the compilation files for each OS.

<!-- -->

-   Setup a *crontab* job to automatize the daily compilation. For this,
    create a *crontab* job from the terminal, as indicated here;

``` powershell
crontab –e
```

This will open a text editor (e.g., vim), then use the content of the
file *crontab_task_mack_bckup.txt* in the folder *compile_tools* to
create the job:

``` powershell
# ┌───────────── minute (0 - 59)
# │ ┌───────────── hour (0 - 23)
# │ │ ┌───────────── day of month (1 - 31)
# │ │ │ ┌───────────── month (1 - 12)
# │ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday;
# │ │ │ │ │                                   7 is also Sunday on some systems)
# │ │ │ │ │
# │ │ │ │ │
# * * * * * command to execute
59 23 * * * /Users/eeglab/Google_Drive/eeglab_comp_daily/compile_tools/cronjob_eeglab_mac.sh
```

Notice this crontab job is pointing to the execution of the file
*cronjob_eeglab_mac.sh* located on the same folder, which triggers the
update of the EEGLAB repository and then starts the compilation,
implemented in the file *eeglab_compile.m*.

Automated compilation setup in Ubuntu (Virtual machine: delorming)
------------------------------------------------------------------

Start by installing Ubuntu in the host machine using VMWare Fusion. Once
installed:

-   Install MATLAB in the Ubuntu VM. In the current setup we have
    installed MATLAB 2018a. The MATLAB update indicated in the MAC setup
    need to be installed as well (See section \#\#).
-   Setup up the [EEGLAB
    git](https://github.com/eeglabdevelopers/eeglab.git) repository. The
    repository should be created in */home/delorming/program_files*. For
    this, the same code used in the MAC setup can be used.

``` powershell
cd ~
mkdir program_files
git clone https://github.com/sccn/eeglab.git
git pull
git submodule update --init --recursive
git pull --recurse-submodules
```

-   Add EEGLAB to the MATLAB path. You may run into issues with
    permissions. See details on the same step in the Mac configuration.

<!-- -->

-   Install *open-vmware-tools* and start service. This is necessary to
    ensure the sharing of files across the *host* and virtual Ubuntu
    machine.

``` powershell
sudo apt-get install open-vm-tools
sudo /etc/init.d/vmware-tools start
```

-   Mount *delorming*, the host machine, over the network. To do this,
    open *Files* and click in *Other locations* (see step 1 in the
    figure below), then double-click in the *delorming* icon (see step 2
    in the figure below).

![](/assets/images/Mount_delorming_network1.jpg)

After doing this, the link showing the local connection to the host
machine has been established (see the figure below).

![](/assets/images/Mount_delorming_network2.jpg)

Once the connection is established, the folder *compile_tools* in the
*Google_Drive* folder of the host machine can be accessed as:

``` powershell
cd /run/user/1000/gvfs/sftp:host=delorming.local/Users/eeglab/Google_Drive/eeglab_comp_daily/compile_tools
```

-   Before creating the crontab job, make sure the file
    *cronjob_eeglab_ubuntu.sh* is executable (change file permissions if
    necessary). For this you can use the following code (assuming as
    your current directory *compile_tools*):

``` powershell

sudo chmod 777 cronjob_eeglab_ubuntu.sh
sudo chmod +x cronjob_eeglab_ubuntu.sh
```

-   Then, a *crontab* needs to be created to perform the compilation
    daily. For this, the code in the file
    *crontab_task_ubuntu_bckup.txt* should be used (see code below).

``` powershell
# ┌───────────── minute (0 - 59)
# │ ┌───────────── hour (0 - 23)
# │ │ ┌───────────── day of month (1 - 31)
# │ │ │ ┌───────────── month (1 - 12)
# │ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday;
# │ │ │ │ │                                   7 is also Sunday on some systems)
# │ │ │ │ │
# │ │ │ │ │
# * * * * * command to execute
1 1 * * * /run/user/1000/gvfs/sftp:host=delorming.local/Users/eeglab/Google_Drive/eeglab_comp_daily/compile_tools/cronjob_eeglab_ubuntu.sh
```

After setting up the *crontab*, the compilation will be done by the
execution of the very same file used in the compilation on the host
machine *delorming*. Remember that this file is located in the host
machine and is accessed through a local sharing of its folder. After
running the compilation, performed in the local *eeglab* folder, the
compilation files are transferred to the host machine and stored in
*\~/Google_Drive/eeglab_comp_daily/ubuntu/*.

### Network issues experienced in the Ubuntu VM

It is possible the Ubuntu VM lose network access at some point while
Windows VM is up and running. While the reason for this behavior is
still unknown, a temporary solution has been to: 1-Identify the
interface that is disconnected (down) (use command: ip a) 2-Start the
service manually using the id for the interface, 'ens33' in this case (
use command: sudo ifup ens33)

After this, the host machine should be mounted over the network again
(see previous steps).

Automated compilation setup in Windows (Virtual Machine)
--------------------------------------------------------

Compilation setup in the Windows VM will repeat some of the steps for
the host and Ubuntu VM compilations. However, some different steps are
required, to automate the compilation process and install the git
management software.

-   Start by installing MATLAB and the updates indicated for the MATLAB
    version. As for the host and Ubuntu virtual machine, in the current
    setup we use MATLAB 2018a with the updates indicated \[here\].
-   Download and install Google Drive, then log into it. In this VM, the
    name of the *Google Drive* folder is not modified.
-   Download and install git and git manager software. In the current
    setup, [Git for Windows](https://gitforwindows.org/) has been used.
-   Setup the EEGLAB git repository in the git bash. For this use, the
    same code used as in the Mac and Ubuntu compliations -- but from the
    Git Bash terminal.

``` powershell
cd ~
mkdir program_files
git clone https://github.com/eeglabdevelopers/eeglab.git
git pull
git submodule update --init --recursive
git pull --recurse-submodules
```

-   Add EEGLAB to the MATLAB path.
-   To automatize the daily compilation, the *Task Scheduler* in Windows
    is used. Follow the instructions below to create a new task.

* From the *Start Menu*, open the *Task Scheduler*. if the program is
not listed directly in the menu, you can type **scheduler** in the
search bar in the same menu to look for it.

* Once you have opened the Task Scheduler (see figure below), click on
**'Create task**' in the right menu (highlighted with a red dotted box).
![](/assets/images/Task_scheduler_main_interface_f1.jpg )

* Enter the name of the task (see Step 1 in the figure below) and a
short description (see Step 2 in the figure below). Check the options to
allow the task to run whether the users are logged in or not (see Step 3
in the figure below) and to give the task the highest privileges (see
Step 4 in the figure below).
![](/assets/images/Task_scheduler_create_task_f2.jpg )

* Set up the *Triggers* of the task. For this, click *Triggers* in the
upper menu (see 1 in the figure below). Then set the option for running
the task daily (see 2 in the figure below) and specify when the task
should run (see 3 in the figure below). Click *OK*. The time to run the
task should be set so as to not overlap the compilations on the host and
Ubuntu machines.

![](/assets/images/Task_sheduler_create_task_trigger_f3.jpg )

After setting the triggers, the graphics interface will display the task
as follows.

![](/assets/images/Task_scheduler_create_task_trigger_f3b.jpg )

* Now setup the menu *Action* to indicate the script that will run
every day. We have created a *.bat* file (*batchjob_eeglab_win.bat*)
that basically perform the same functions as the crontab jobs
implemented in the Mac (host) and the virtual Linux machine: updating
the git repository and then running the compilation file. To set up this
option, click 'Actions'' in the upper menu ' (see 1 in the figure
below). Then add a new action by clicking on the *New* button (see 2 in
the figure below). A new window (*New action*) will pop up allowing you
to specify the file to run. Look for and select the file
*batchjob_eeglab_win.bat* located in *..\\Google
Drive\\eeglab_comp_daily\\compile_tools* by clicking in the *Browse..*
button (see 3 in the figure below). Click *OK*.
![](/assets/images/Task_scheduler_create_task_actions_f4.jpg )

* Finally, to create the task go back to the upper menu *General* and
click *OK*. Now the task has been created and the compilation is ready
to run daily.

Manual compilation notes - common to all platforms
==================================================

1\. Clone EEGLAB with default plugins

``` Matlab
git clone --recurse-submodules https://github.com/sccn/eeglab.git
```

2\. Install additional plugins (plugins that are already installed will
be skipped). Some folders from the plug-ins clean_rawdata
(**manopt/reference/m2html**) and Fieldtrip (**compat**,
**external/afni**, **external/spm8**, **external/spm12**,
**external/gifti**, **external/eeglab** and **external/bemcp**) should
be removed to avoid compilation issues. Do not use the GIT repo to
remove these folders, it will creates many more problems. Use the
following script to do so:

``` Matlab
eeglab  % restart the fleshly installed eeglab

% Installing plugins
plugin_askinstall('ANTeepimport', 'eegplugin_eepimport', true);
plugin_askinstall('bva-io', 'eegplugin_bva_io', true);
plugin_askinstall('clean_rawdata', 'eegplugin_clean_rawdata', true);
plugin_askinstall('dipfit', 'eegplugin_dipfit', true);
plugin_askinstall('egilegacy', 'eegplugin_egilegacy', true);
plugin_askinstall('Fieldtrip-lite', 'ft_defaults', true);
plugin_askinstall('Fileio', 'ft_read_data', true);
plugin_askinstall('firfilt', 'eegplugin_firfilt', true);
plugin_askinstall('IClabel', 'eegplugin_iclabel', true);
plugin_askinstall('Picard', 'picard_standard', true);
plugin_askinstall('musemonitor', 'eegplugin_musemonitor', true);
plugin_askinstall('neuroscanio', 'eegplugin_neuroscanio', true);
plugin_askinstall('xdfimport', 'eegplugin_xdfimport', true);
plugin_askinstall('iirfilt', 'iirfilt', true);
plugin_askinstall('vised', 'vised', true);

% Removing clean_rawdata files
% For clean_rawdata, remove folder manopt/reference/m2html.
CleanRawData_folder = fileparts(which('clean_rawdata.m'));
rmdir(fullfile(CleanRawData_folder,'manopt','reference','m2html'), 's');

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
```

3\. Open the Application compiler (Matlab tab "Apps" and button
"Application compiler")
4. Open the "eeglab.prj" file.
5. Check the path for plugins. If a new version is available, rename the
version in the eeglab.prj file. NEVER RESAVE THE PROJECT IN THE
APPLICATION COMPILER.
9. Press "Package" and wait (usually 30 minutes or so)
10. If successful, 3 folders are created. You may test the compiled
EEGLAB version by running the program in the "for_testing" folder.
11. Test the compiled version for potential runtime errors (see notes on
testing
[here](https://sccn.github.io/others/Compiled_EEGLAB.html#how-to-check-the-integrity-of-the-compiled-version)).
On Mac and OSX use ./run_eeglab.sh MATLAB_PATH.

<font color=red>Known error: running eLoreta from DIPFIT, cannot find
precompute_dpss</font>. We need to look into it.

Selected for future inclusion but require testing. If you have a plugin
you want to include, please try compiling with the plugin and testing
the plugin in the compiled EEGLAB version. If all is functional, email
us at eeglab_at_sccn.ucsd.edu and your plugin will be included in the
next release.

12\. Adding new plugins

-   Download or clone plugin
-   Add to eeglab.m
-   Compile
-   Update this page

| Plugin name       | Comment                                                                                               |
|-------------------|-------------------------------------------------------------------------------------------------------|
| Biosig            | Not necessary because included in Fieldtrip                                                           |
| MFFMatlabIO       | Issue with finding the JAR file at execution time; more debugging necessary before inclusion possible |
| bids-matlab-tools | Not tested                                                                                            |