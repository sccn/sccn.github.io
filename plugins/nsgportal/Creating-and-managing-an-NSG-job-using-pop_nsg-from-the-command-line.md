---
layout: default
parent: NSGportal
grand_parent: Plugins
render_with_liquid: false

title: Creating-and-managing-an-NSG-job-using-pop_nsg-from-the-command-line
long_title: Creating-and-managing-an-NSG-job-using-pop_nsg-from-the-command-line
---
This tutorial describes in details the process of submitting and managing a job using the command line options in _pop_nsg_. 

Before following the tutorial, you will need to install the plug-in and set up your NSG credentials. If you haven't done so, refer to [this section](https://github.com/sccn/nsgportal/wiki/Setting-up-the-plug-in) for instructions.

We will use the same job created in section [Preparing your files to submit a job](https://github.com/nucleuscub/pop_nsg_wiki/wiki/Preparing-your-files-to-submit-a-job) and used in the [Demo 1](https://github.com/nucleuscub/pop_nsg_wiki/wiki/Demo-1:-Creating-and-managing-a-job-form-pop_nsg-GUI). You can download the tutorial script [here](https://github.com/sccn/nsgportal/blob/master/demos/demo_command_line_tools.m) to follow along.

## Overview of the _pop_nsg_ command
The **_pop_nsg_** command can be called with no arguments, in which case it will bring up the GUI interface (see [Demo 1](https://github.com/sccn/nsgportal/wiki/Creating-and-managing-a-job-from-pop_nsg-GUI)). Else, the first argument to _pop_nsg_ should specify the action you want to take:
* 'test': Perform a test run on the local computer [argument: the job .zip file or folder]
* 'run': Submit the job to run on NSG [argument: the job .zip file or folder]
* 'output': Retrieve the job output files [argument: job identifier or NSG job structure]
* 'delete': Delete the job record from your NSG account [argument: job identifier or NSG job structure]

## Running an NSG job from the command line
In this example, we will assign the path to the job zip file or folder to a variable, but in general, the path can be passed directly as a string to the function:
```
path2zip = '/Users/amon-ra/program_files/eeglab/plugins/nsgportal/demos/demo_jobs/TestingEEGLABNSG.zip';
```
To run the job using the default options use:
```
[currentjob, alljobs] = pop_nsg('run',path2zip,'filename', 'run_ica_nsg.m');
```
Notice that a second pair of parameters was used here (```'filename', 'run_ica_nsg.m'```). This is necessary when using the option _'run'_ to specify which script should NSG execute in order to run the job. Thus the option 'filename' is mandatory when using the option _'run'_.

The default options will assign a randomly generated ID to the job and will submit the job to run on NSG using default job parameters. 

You may also specify some job parameters by providing Key-Value pair arguments to the function call. Optional arguments include:
* 'jobid'     :   Client job ID string [default value will be the job name trailed by a randon generated number eg: _jobname_1234_]
* 'outfile'   :   Results filename string [default: ['nsgresults_', '_jobid_']]
* 'runtime'   :   Maximum time (in hours) to allocate for running the job on NSG [default: 0.5]
* 'subdirname':   Name of the sub-directory containing the script file (if the script file is not in the top level folder) [default: none]

Example of a 'run' command with optional arguments specified:
```
[NSGjobstruct, alljobs] = pop_nsg('run', path2zip, 'filename', 'run_ica_nsg.m', 'jobid', 'runica_testing', 'runtime', 0.3); 
```

The function returns a MATLAB NSG job structure for the submitted job (_currentjob1_) and a structure containing information about all jobs under your NSG credential (_alljobs_).

## Checking job status periodically
After the job is submitted it will be processed by the NSG server. You can check the status of the job periodically by calling the function _nsg_recurspoll_, providing as arguments either the jobid, job URL or job structure, and (optionally) the polling interval in seconds. Here the jobid is used as the first argument:
```
NSGjobstruct = nsg_recurspoll('runica_testing','pollinterval', 30);
```

The _pollinterval_ should be more than (the default) 30 seconds. Keep the polling interval as long as possible to avoid overloading NSG.

_nsg_recurspoll_ [argument: jobid] returns a structure containing the status of a specified job. After the job completes, you can retrieve its results using _pop_nsg_.

Job results can be retrieved after the job completes. Use _nsg_recurspoll_ to confirm that the job has finished before attempting to access its results.

## Retrieving job results
Access job results by providing either the _jobid_, job URL or job structure to _pop_nsg_:
```
[NSGjobstruct, alljobs] = pop_nsg('output', NSGjobstruct); 
```
The input _NSGjobstruct_ contains the NSG job structure for the job we want to retrieve results from. The output _NSGjobstruct_ also contains the output status of the job. Output variable _alljobs_ contains current status information for all NSG jobs associated with the user credential.

## Deleting an NSG job
To delete a job from the NSG record associated with the user NSG credential, provide either the _jobid_, job URL or job structure as a second argument:
```
[NSGjobstruct, alljobs] = pop_nsg('delete',NSGjobstruct); 
```
Outputs are, as above, the modified NSG job structure and the information for all NSG jobs associated with the user credential. Notice that after this command is executed the job is deleted from your account in NSG. The structure returned as output _NSGjobstruct_ is a reference to the deleted job (as it can be seen in the field ```NSGjobstruct.jobStage``` which is set to 'DELETED') and cannot be used anymore to access the job.








