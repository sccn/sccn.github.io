---
layout: default
title: nsgportal-graphical-user-interface:-pop_nsg
long_title: nsgportal-graphical-user-interface:-pop_nsg
parent: nsgportal
grand_parent: Plugins
---

# *nsgportal* graphical user interface: pop_nsg

Interaction with key function in EEGLAB is mostly supported through both, command line and graphical user interface (GUI). The plugin *nsgportal* also follows this philosophy. In this section, we introduce the GUI supporting the plugin *nsgportal* through its main function, *pop_nsg*. A more advanced tutorial on using the plugin from its GUI will be addressed in the next sections (see [here](https://github.com/sccn/nsgportal/wiki/Creating-and-managing-a-job-from-pop_nsg-GUI)).

## The *pop_nsg* GUI
To call the *pop_nsg* GUI, simply type *pop_nsg* from the MATLAB command windows. The GUI depicted below will pop up. the GUI can also be invoked from the EEGLAB main GUI by clicking ***Tools > NSG Tools > Manage NSG jobs***. For this, the plugin *nsgportal*  has to be installed before (see [this](https://github.com/sccn/nsgportal/wiki/Registering-on-NSG-R) section). 

<center>
<img src="https://github.com/sccn/nsgportal/blob/master/docs/img/pop_nsgguineu.jpg?raw=true" alt="drawing" width="800"/>
</center>

The main functionalities supported from the pop_nsg GUI are listed below:

1. Submit an EEGLAB job to NSG. See GUI section "Submit new NSG job"
2. Test NSG jobs locally on your computer.
3. Delete jobs from your NSG account
4. Download NSG job results.
5. Load results from a completed and downloaded NSG job.
6. Visualize error and intermediate logs
7. Access *pop_nsg* help.

## GUI main sections
### Submitting new NSG job
From this section of the GUI you will be able to test and submit a job for processing in NSG.

Component list:

 1. Edit **Job folder or zip file** : Full path to the zip file or folder for a job to submit to NSG
 2. Button **Browse**: Browse a zip file or folder for a job to submit to NSG
 3. Edit **Matlab script to execute**: Matlab script for NSG to execute upon job submission
 4. Button **Test job locally**:  Test job locally on this computer. A downscaled version of the job MUST be used.
 5. Edit **Job ID (default or custom)**: Unique identifier for the NSG job. Modify this field at your convenience.   
 6. Edit **NSG run options (see Help)**: NSG options for the job to be submitted. See *>> pop_nsg help* for the list of all options.
 7. Button **Run job on NSG**: Submit the job to run on NSG                
                                  
### Interacting with your jobs
 From this section of the GUI, you will be able to interact with the jobs submitted to NSG under your credentials.
 This section is comprised of the following components:
 
 1. Button **Refresh job list**: Refresh the list of all of your NSG jobs.
 2. Checkbox **Auto-refresh job list**: Automatically refresh the list of all of your NSG jobs.
 3. Button **Delete this NSG job**: Delete the currently selected job
 4. List box **Select job**: List of all jobs under your credentials in NSG. A color code is used here to inform on the status of the jobs in this list. The legend can be found below the list box.
 5. Button **Matlab output log**: Download and display MATLAB command line output for the currently selected job. Intermediate job logs can be also visualized from here. In the figure above, this option appears disabled since there is no current job on the list.
 6. Button **Matlab error log**: Download and display the MATLAB error log for the currently selected job. In the figure above, this option appears disabled since there is no current job on the list.
 7. Button **Download job result**: Download result files from the currently selected job
 8. Button **Load/plot results**: Launch a GUI for loading and displaying results of the currently selected job
    
### Checking your NSG job status
In this section are displayed the messages issued by NSG during the submission and processing of the job currently selected from the list box **Select job**.