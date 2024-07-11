---
layout: default
title: Creating-and-managing-a-job-from-pop_nsg-GUI
long_title: Creating-and-managing-a-job-from-pop_nsg-GUI
parent: nsgportal
grand_parent: Plugins
---
# Creating and managing a job from pop_nsg GUI
In this tutorial we will address the creation and managing of NSG jobs from EEGLAB by using the plugin *nsgportal*. Specifically, the tutorial will focus on performing these tasks from the pop_nsg GUI.
Across the tutorial we will use a sample job distributed with the plug-in files. This job was previously used in the section [*Using the Open EEGLAB Portal*](https://github.com/sccn/nsgportal/wiki/Using-the-Open-EEGLAB-Portal).

To start the tutorial, launch the *pop_nsg* GUI by clicking **Tools > NSG Tools > Manage NSG jobs** as in the figure below:

<!-- EEGLAB GUI to launch pop_nsg-->

<center>
<img src="https://github.com/sccn/nsgportal/blob/master/docs/img/eeglab_nsgtools_menus.jpg" alt="drawing" width="400"/>
</center>


The GUI depicted below will pop up. The GUI can also be invoked from the MATLAB command windows by typing *pop_nsg*.

<center>
<img src="https://github.com/sccn/nsgportal/blob/master/docs/img/pop_nsgguineu.jpg" alt="drawing" width="600"/>
</center>

## Submitting a job to NSG
To submit a job from the pop_nsg GUI, go to the GUI section **Submit new NSG job**  and click the button **Browse...**. A window will pop up requesting the type of file to be open, a zip file or a folder. To follow this tutorial, select **Zip file** and then navigate to the folder *.../nsgportal/demos/demo_jobs/* and select the zip file *TestingEEGLABNSG.zip*. Although we use the zip file option in this demo, a folder containing the job files may be selected similarly. The 'job' file must consist of the data to be used for the computation and a MATLAB script (.m) to execute. If functions that do not belong to MATLAB or EEGLAB are used in your script, you should add them to the file as well.

 Once selected the job file, the list of *.m* files in the job zip file will appear in the list of **Matlab scripts to execute**. From here, select the file that must be executed in NSG. In this tutorial, we will select 'run_ica_nsg.m'. 
Notice in the edit ***Job ID (default or custom)*** that a Job ID has been assigned to the job. This job ID is a unique identifier provided to NSG to locate your job. The default job ID assigned is the combination of the job file name and a random number. We encourage users to change this field and set a more meaningful name. Recall, this is a unique ID, so do not use one ID that was used before! In this tutorial we will identify our job as *nsgtutorial*.

Additional options, e.g. running time allocated in NSG, can be defined in the edit **NSG run options**, in this tutorial we will set the running time to 0.5 Hrs by entering the option:  *'runtime' 0.5*.
With the exception of the path to the job file, the GUI at this point of the tutorial should look like the following:

 <!-- Defining JOB ID -->
<center>
<img src="https://github.com/sccn/nsgportal/blob/master/docs/img/pop_nsg_job2send.jpg" alt="drawing" width="600"/>
</center>

After this, you may click the button **Run job on NSG** to submit the job to NSG. But don't do this yet! You may want to test your job submission before that, right?

## Testing your job locally
A job can be tested locally on your computer before being submitted to NSG. For this, a downscaled version of the job should be used (otherwise will deceive the purpose of using HPC). For example, if your NSG job runs a loop several times, you may in your local test perform only one iteration of the loop. The purpose of this test is to check the script you want to execute in NSG. The downscaling should not affect the ability of the script to run. In this tutorial, we will use a script ('*run_ica_nsg_downscaled.m*') similar to the one to be executed in NSG but without actually computing ICA. 
 For this,  under  **Matlab scripts to execute**, select '*run_ica_nsg_downscaled.m*' and click the button **Test job locally**. The script should take just a few seconds to run without issues. Notice that testing your job is not a requirement necessary for job submission, this is just a tool for self-assessment of your job.
 
 Once the testing is done, you can change back the script selected under  **Matlab scripts to execute** to the one defined in the previous section and then submit your job to NSG. After successful submission of the job, the Job ID assigned previously will be shown in the list of jobs under your credentials in NSG. At the same time, the status of the job will be displayed in **NSG job status**.
 
 <!-- Job submited -->
<center>
<img src="https://github.com/sccn/nsgportal/blob/master/docs/img/pop_nsg_jobsubmitted.jpg" alt="drawing" width="600"/>
</center>

## Checking job status periodically
 Once the job is submitted (see **NSG job status**) you can ask *pop_nsg* to check periodically the status of the jobs on your list. For this, check the checkbox **Auto-refresh job list**.  Messages with the job status will start being issued at the MATLAB command windows. To continue with the tutorial you may uncheck this option if desired.

## Retrieving job information: Intermediate messages, files and error logs
Intermediate messages issued in the NSG MATLAB session can be checked from *pop_nsg*. To retrieve this information, click the button **Matlab output log**.  The information will be displayed in a MATLAB browser. The same button can be used at the end of the processing in order to retrieve the MATLAB log for the session corresponding to the processing of the job selected in *pop_nsg*.
If any error has happened during the processing of your job, the font color of the job on the job list will change (red in case of Matlab error or orange for NSG errors) and the button **Matlab error log** will be enabled, from where you can retrieve the information log.

## Retrieving and loading results
Once your job is completed, proceed to download the results by clicking on the button **Download job results'**. A message similar to the one below will be displayed in the command windows. The list of the result files downloaded can be seen in lines 2 to 12. Notice that both, results and files submitted are in the downloaded file. The results will be saved in the path defined in *pop_nsginfo*.

```
1  >> Accessing job: "https://nsgr.sdsc.edu:8443/cipresrest/v1/job/ramonmc/NGBW-JOB-EEGLAB_TG-87B63F47681545A482D010776408F82D/output/33777" on NSG..../TestingEEGLABNSG/
2  >> ./TestingEEGLABNSG/IC_scalp_maps.jpg
3  >> ./TestingEEGLABNSG/eeglab_data_epochs_ica.set
4  >> ./TestingEEGLABNSG/run_ica_nsg.m
5  >> ./TestingEEGLABNSG/eeglab_data_ICA_output.set
6  >> ./TestingEEGLABNSG/run_ica_jader_nsg.m
7  >> ./TestingEEGLABNSG/eeglab_data_ICA_output.fdt
8  >> ./TestingEEGLABNSG/eeglab_data_epochs_ica.fdt
9  >> ./scheduler_stderr.txt
10  >> ./scheduler_stdout.txt
11  >> ./stderr.txt
12  >> ./stdout.txt
13  >> Done.
14  >> File downloaded and decompressed in the
15  >> output folder specified in the settings
16  >> 1  >> Accessing job: "https://nsgr.sdsc.edu:8443/cipresrest/v1/job/ramonmc/NGBW-JOB-EEGLAB_TG-87B63F47681545A482D010776408F82D" on NSG...Done.
17  >> Accessing jobs on NSG...Done
```
EEG files and a wide range of image formats generated as a result of a NSG job can be loaded from the *pop_nsg* GUI. For this click in the button **Load/plot results**. The following file explorer will pop up with the current path being the one where the selected job results were downloaded.

 <!-- Job submited -->
<center>
<img src="https://github.com/sccn/nsgportal/blob/master/docs/img/result_explorer1.jpg" alt="drawing" width="700"/>
</center>

From this file explorer, navigate (by clicking into) to the folder *TestingEEGLABNSG* to acces the result files.
Then, select e.g. the file *IC_scalp_maps.jpg* and then click the button **Load/plot**. The figure below will pop up. This figure was actually generated as part of our NSG job results (see script *run_ica_nsg.m*).

<!-- topos -->
<center>
<img src="https://github.com/sccn/nsgportal/blob/master/docs/img/results_topos.jpg" alt="drawing" width="400"/>
</center>

In a similar way, a *.set* file can be selected and loaded from this interface.

## Deleting a job
After retrieving the results, proceed to delete the job by selecting the job in the job list and clicking the button **Delete this NSG job**. Then the job ID will be removed from the interface.