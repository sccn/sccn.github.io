---
layout: default
parent: NSGportal
grand_parent: Plugins
render_with_liquid: false

title: Using-pop_nsg-command-line-tools-in-your-EEGLAB-plug-in
long_title: Using-pop_nsg-command-line-tools-in-your-EEGLAB-plug-in
---
# Using pop_nsg command line tools in your EEGLAB plug-in

 The goal of this tutorial is to demonstrate the use of *pop_nsg* command line tools (see [Tutorial 2](https://github.com/sccn/nsgportal/wiki/Creating-and-managing-an-NSG-job-using-pop_nsg-from-the-command-line)) to implement EEGLAB plug-ins equiped with NSG capabilities. This is demonstrated here by implementing a sample plug-in using *pop_nsg* command line tools. The plug-in implemented for this purpose (*pop_icansg*)  is a light-weight version of *pop_runica* implemented to compute ICA (using a method selected from two options) on a loaded EEG dataset. However here, instead of showing the many options and parameters available in *pop_runica*, *pop_icansg* focuses on enabling some standard *pop_nsg* command line options to run via NSG, thereby potentially reducing compute time. Below we discuss each of the steps involved in this process.
  
   First, you will need to specify your NSG credential using *pop_nsginfo*, either via the EEGLAB menu selection **Tools > Send to NSG portal > Change NSG portal settings and credentials** or by calling the function *pop_nsginfo* on the command line. Make sure also that you have the *nsgportal* plug-in folder under *../eeglab/plugins*.

## The sample plug-in *pop_icansg*
  
The example plug-in (*pop_icansg*) implemented for this tutorial is distributed with the *nsgportal* plug-in files and can be found in *nsgportal/demos/demo_plugin/icansg/*. To install the plug-in, move the folder containing the plug-in (*icansg*) to *../eeglab/plugins* and restart EEGLAB.

In the plug-in folder you will find two  files, [eegplugin_icansg.m](https://github.com/sccn/nsgportal/blob/master/demos/demo_plugin/icansg/eegplugin_icansg.m) and [pop_icansg.m](https://github.com/sccn/nsgportal/blob/master/demos/demo_plugin/icansg/pop_icansg.m).
 The first function enables the user to launch the plug-in from the EEGLAB menu and provides the current EEG dataset structure (the dataset currently loaded in EEGLAB) as an input to *pop_icansg.m*. An explanation of the syntax used in this function can be found in [this EEGLAB wiki section](https://sccn.ucsd.edu/wiki/A07:_Contributing_to_EEGLAB#How_to_write_an_EEGLAB_extension)  
 
The second function will be the focus of this tutorial. The aim of the plug-in is to perform ICA decomposition via NSG using one of two implemented decomposition approaches, 'runica' or 'jader', that performs Infomax or JADE ICA decomposition, respectively. If called from the EEGLAB menu by manually selecting the EEGLAB GUI menu item specified in the *eegplugin_icansg* function (see figure below), the plug-in will use the current EEG dataset structure loaded into EEGLAB, and will pop up an option entry window asking which ICA method to use. The figure below shows the *eegplugin_icansg* menu item selected and the *pop_icansg* window popped up as a result. 

<center>
<img src="https://github.com/sccn/nsgportal/blob/master/docs/img/plugin_runicansg.jpg?raw=true" alt="drawing" width="600"/>
</center>

The plug-in pop-function (*pop_icansp*)can also be called from the MATLAB command line; in this case, you may pass as input the EEG dataset structure you want to decompose as well as the decomposition method to apply to the data. The sample code below specifies both the EEG dataset structure to operate on and the ICA decomposition type to apply; it thus will perform ICA decomposition via NSG on the currently loaded (EEG structure) dataset (using *'runica'*) *without* popping up a parameter input window:

`OUT_EEG = pop_icansg(EEG,'icatype','runica')`

After calling and executing the plug-in, the function *pop_icansg* will have created a folder containing the data and scripts required to submit an NSG job. The plug-in will then submit that job to NSG, and when the job finishes, will retrieve and return the EEG dataset plus its ICA decomposition. This processing proceeds in the following steps:

1.  Manage the inputs
2.  Create a temporary folder and save the input data to it 
3.  Compose the m-file MATLAB script to be executed via NSG
4.  Submit the job to NSG
5.  Optionally activate periodic NSG polling for job completion 
6.  Download the input data and job results
7.  Delete the job from your NSG job list
8.  Load the results into EEGLAB and return them in the plug-in command output.

The following subsections explain these steps in detail. The subsection headings are direct references to comment headings in [pop_icansg.m](https://github.com/sccn/nsgportal/blob/master/demos/demo_plugin/icansg/pop_icansg.m).  
 
### Section 1: Manage the plug-in inputs 
```
if nargin < 1   
    help pop_icansg;
    return;
end

allalgs   = { 'runica' 'jader' }; 

if nargin < 2  % Pop up window call: No ICA method specified; 
               %           pop up the parameter input window.
   
    cb_ica = 'close(gcbo);';        
    promptstr    = { { 'style' 'text'    'string' 'ICA algorithm to use (click to select)' } ...
                     { 'style' 'listbox' 'string' char(allalgs{:}) 'callback', cb_ica }};
    geometry = { [2 1.5]};  geomvert = 1.5;                        
    result       = inputgui( 'geometry', geometry,'geomvert', geomvert, ...
                             'uilist', promptstr,'helpcom', 'pophelp(''pop_icansg'')', ...
                             'title', 'Run ICA decomposition in NSG -- pop_icansg()');
    if ~isempty(result)
        options = { 'icatype' allalgs{result{1}}};
    else
        return;
    end
else % Command line call specifying the ICA decomposition method;
     %  in this case no pop-up parameter input window is created.
    options = varargin;   
end
```

In the code subsection above, the plug-in handles the *pop_icansg* function inputs. The code supports the two ways of invoking the plug-in, from the EEGLAB menu (see the **Pop-up window call** code section above) and by a MATLAB command line call (see the **Command line call** code section above). If the function is called with only one argument (specifying the EEG set to decompose), the code pops up a parameter input window asking which ICA algorithm to use. The selected option is stored in the variable *options*. If the command line call provides the ICA algorithm to use (using the optional input '*icatype*'), then the function will assign its argument to the variable *options*.

### Section 2: Create a temporary folder and save the input data to it. 

In the first part of this section, your NSG credentials and options (including the location of the output folder to receive the results) are retrieved by invoking *nsg_info.m*. These options, of course, must already have been set by using *pop_nsginfo.m* as [explained here](https://github.com/sccn/nsgportal/wiki/Setting-up-the-plug-in). 
This information is used to create a temporary folder (here *icansgtmp*) in the NSG output folder (as defined in *pop_nsginfo.m*).
The location of the temporary output folder is freely selectable. Here we use the output folder defined in the NSG options, as we assume the user has permissions to write and modify files in this location (since that option was previously defined by the user).

```
nsg_info;                   % Get the name and path of the temporary folder
jobID = 'icansg_tmpjob';    % Specified job ID (must be a string)

% Create a temporary folder

foldername = 'icansgtmp';                        % Temporary folder name
tmpJobPath = fullfile(outputfolder,'icansgtmp');
if exist(tmpJobPath,'dir'), 
      rmdir(tmpJobPath,'s'); 
end
mkdir(tmpJobPath);                               % Make the temporary folder
```
For the sake of simplicity, in our example we use a hard-coded job ID (string variable *jobID* in code section above). This may be sufficient *if* no other job is submitted (by anyone) via this plug-in while a earlier *pop_icansg* job is still in the NSG processing queue, and if previous NSG job records have been deleted (as demonstrated below) after retrieving their results. However, if you want to allow multiple concurrent job submissions to be active in the NSG job queue, we encourage you to generate individual job IDs, so that NSG job label confounds do not arise. For instance, you may create a job ID by attaching a three digits random number to the current name ( MATLAB code: jobID = ['icansg_tmpjob' num2str(floor(rand(1)*1000))]).

Next, save the input data in the temporary folder via the following code:

```
% Save data in the folder previously created. 
% Here you may change the filename to match the one
% in the script to be executed via NSG

pop_saveset(EEG,'filename', EEG.filename, 'filepath',tmpJobPath);
```
Here, the name of the data file was not changed, but it might be modified to make it consistent with its treatment in the next section.

### Section 3: Manage the m-file script to be executed via NSG

The MATLAB script to be executed via NSG (code Section 3) is written so as to allow the script to flexibly adapt to different input options. In our example, the name of the dataset and the ICA algorithm to use are provided as inputs, either through the pop-up parameter input window or the command line. These values are used then to compose the script to be executed via NSG:

```
fid = fopen( fullfile(tmpJobPath,'icansg_job.m'), 'w');
fprintf(fid, 'eeglab;\n');
fprintf(fid, 'EEG = pop_loadset(''%s'');\n', EEG.filename);
fprintf(fid, 'EEG = pop_ica(EEG, ''%s'',''%s'');\n', options{1},options{2});
fprintf(fid, 'pop_saveset(EEG, ''filename'', ''%s'');\n',EEG.filename);
fclose(fid);
```
If, as here, the *icatype* is 'runica' and the EEG file name is *tempdatafile.set*, the script to be run via NSG will then read as follows:
```
eeglab;                                     % The composed script to be run via NSG 
EEG = pop_loadset('tempdatafile.set');
EEG = pop_ica(EEG, 'icatype','runica');
pop_saveset(EEG, 'filename', 'tempdatafile.set');
```

### Section 4: Submit the job to NSG

In Sections 2 and 3, the job files were created in the folder *icansgtmp*. In this section, the job will be submitted to NSG. (This part of the code may look similar the one used in the [Tutorial 2](https://github.com/sccn/nsgportal/wiki/Creating-and-managing-an-NSG-job-using-pop_nsg-from-the-command-line)).

```
MAX_RUN_HOURS = 0.5;
jobstruct = pop_nsg('run',tmpJobPath,'filename', 'icansg_job.m', ...
                    'jobid', jobID,'runtime', MAX_RUN_HOURS);  % run the job via NSG; here 
                                                               % ask for up to 30 min runtime
```
Observe here that although some default NSG options are hard-coded in the *pop_nsg* code, it is possible for the programmer to allow users to specify some or all of these options using, for instance, a parameter input edit in the main GUI of the plug-in (not shown in this tutorial). 

Alternatively, the plug-in function may end here (Section 4); in this case the user can be directed to manage the job through the *pop_nsg* pop-up window (see [Tutorial 1](https://github.com/sccn/nsgportal/wiki/Creating-and-managing-a-job-from-pop_nsg-GUI)). The rationale for this is that jobs may remain for some time in the NSG job queue waiting to be processed. Thus, you may not want the plug-in function and window to remain active until the job finishes. Due to this, you may want to direct the user to manage the job through *pop_nsg*, so as to wait for job completion, or the user can choose to log back into *pop_nsg*  to check on the NSG job status at some later time. If you *do* want the plug-in to hang until the NSG job is finished, then continue the function code as below:

### Section 5: Activate periodical job status polling from NSG

Next, we perform periodic job status polling using *nsg_recurspoll.m*.
 
```
POLL_INTERVAL = 60;  % use a (default) 60-second polling interval value
jobstructout = nsg_recurspoll(jobstruct,...
                  'pollinterval', POLL_INTERVAL); % recursively poll for NSG job status 
                                                  % and display latest results
```
The function will now retrieve the status of the submitted NSG job every 60 seconds (via the argument to option *'pollinterval'*), continuing to run until the job is completed. **Note**: We advise making this polling mode optional, as the user may rather wish to perform other work in EEGLAB and check the status of the job later (See comments at the end of Section 4).

### Section 6: Download the NSG job data and results

After the function *nsg_recurspoll.m* exits, download the NSG job results using another call to *pop_nsg*:
```
pop_nsg('output',jobstructout); 
```

### Section 7: Delete the job from the user's NSG job list

You can then again call *pop_nsg* to remove the NSG job record from the user's NSG job list. 

```
pop_nsg('delete',jobstructout);
```
In general, it is good practice to remove the job record once its results are retrieved. This will avoid cluttering your NSG account with jobs that are no longer active.

### Section 8: Load the NSG job results into EEGLAB and return the results from the calling function

Here, the EEG data *and* its computed ICA decomposition are loaded into EEGLAB and returned in the function output. Here, we use the default output folder path defined in *nsg_info.m*.

```
OUT_EEG = pop_loadset(EEG.filename, fullfile(outputfolder, ['nsgresults_' jobID],foldername));
```

## Example of executing *pop_icansg*

In this example, we apply the completed plug-in *pop_icansg* to a sample EEG dataset.

### Load data

 Here we use the EEG sample data, *eeglab_data_epochs_ica.set*, distributed with EEGLAB, which is located in *../eeglab/sample_data/* . To load the data, either use the EEGLAB menu (by selecting menu item **File > Load existing dataset**) or use a command line call to *pop_loadset* (as in the example below).
 
 `EEG = pop_loadset('filename','eeglab_data_epochs_ica.set','filepath','/eeglab/sample_data/');`


### Call the plug-in *pop_icansg*

We now compute the ICA decomposition of the loaded EEG dataset using *pop_icansg*, selecting the 'runica' method. To perform this, select EEGLAB menu item **Tools > Run ICA via NSG** and then select the ICA method 'runica' in the pop up parameter selection window. Press 'Ok', after the selection.
Else, to execute the same process but from the command line, use the following command:
 
 ```
 OUT_EEG = pop_icansg(EEG,'icatype','runica');
 ```
 
### While waiting for the NSG job to complete

After *pop_icansg* executes,  you will see in the MATLAB command line window accumulating messages similar to these:
```
1  >> Scaling components to RMS microvolt
2  >> Saving dataset...
3  >> Job has been submitted!
4  >> Accessing jobs on NSG...Done.
5  >> Accessing job: "https://nsgr.sdsc.edu:8443/cipresrest/v1/job/ramonmc/NGBW-JOB-1 >> EEGLAB_TG-291E9AF9FAB64B918C07259E310A3A78" on NSG...Done.
6  >> Accessing jobs on NSG...Done.
7  >> Accessing job: "https://nsgr.sdsc.edu:8443/cipresrest/v1/job/ramonmc/NGBW-JOB-EEGLAB_TG-291E9AF9FAB64B918C07259E310A3A78" on NSG...Done.
8  >> Job status on 6-10-2019 15:10:3 : QUEUE
9  >> Accessing job: "https://nsgr.sdsc.edu:8443/cipresrest/v1/job/ramonmc/NGBW-JOB-EEGLAB_TG-291E9AF9FAB64B918C07259E310A3A78" on NSG...Done.
10 >> Job status on 6-10-2019 15:11:3 : SUBMITTED
11 >> Accessing job: "https://nsgr.sdsc.edu:8443/cipresrest/v1/job/ramonmc/NGBW-JOB-EEGLAB_TG-291E9AF9FAB64B918C07259E310A3A78" on NSG...Done.
12 >> Job status on 6-10-2019 15:12:3 : LOAD_RESULTS
13 >> Accessing job: "https://nsgr.sdsc.edu:8443/cipresrest/v1/job/ramonmc/NGBW-JOB-EEGLAB_TG-291E9AF9FAB64B918C07259E310A3A78" on NSG...Done.
14 >> Job status on 6-10-2019 15:13:3 : COMPLETED
15 >> Accessing job: "https://nsgr.sdsc.edu:8443/cipresrest/v1/job/ramonmc/NGBW-JOB-EEGLAB_TG-291E9AF9FAB64B918C07259E310A3A78" on NSG...Done.
16 >> ./icansgtmp/
17 >> ./icansgtmp/eeglab_data_epochs_ica.set
18 >> ./icansgtmp/tempdatafile.fdt
19 >> ./icansgtmp/icansg_job.m
20 >> ./icansgtmp/tempdatafile.set
21 >> ./icansgtmp/eeglab_data_epochs_ica.fdt
22 >> ./scheduler_stderr.txt
23 >> ./scheduler_stdout.txt
24 >> ./stderr.txt
25 >> ./stdout.txt
26 >> Done.
27 >> File downloaded and decompressed in the
28 >> output folder specified in the settings
29 >> Accessing job: "https://nsgr.sdsc.edu:8443/cipresrest/v1/job/ramonmc/NGBW-JOB-EEGLAB_TG-291E9AF9FAB64B918C07259E310A3A78" on NSG...Done.
30 >> Accessing jobs on NSG...Done.
31 >> Accessing job: "https://nsgr.sdsc.edu:8443/cipresrest/v1/job/ramonmc/NGBW-JOB-EEGLAB_TG-291E9AF9FAB64B918C07259E310A3A78" on NSG...Done.
32 >> Accessing jobs on NSG...Done.
33 >> pop_loadset(): loading file /Users/amon-ra/Downloads/nsgtmp/nsgresults_icansg_tmpjob/icansgtmp/eeglab_data_epochs_ica.set ...
34 >> Reading float file '/Users/amon-ra/Downloads/nsgtmp/nsgresults_icansg_tmpjob/icansgtmp/eeglab_data_epochs_ica.fdt'...
35 >> Scaling components to RMS microvolt
```

The first and second lines indicate that the dataset provided as an input was saved in the temporary folder *icansgtmp*. Lines 3 and 4 confirm that the job was submitted to NSG. Lines 5 to 14 provide periodic updates on the job status (dated 60 seconds apart). Lines 15 to 32 detail the process of downloading the job's results. The final lines 33-35 document loading the function output.
Note that this is the whole output print of the job; to generate all these messages, the job must complete successfully. Be aware this may take some time.

If you are curious about the job generated by calling *pop_icansg*, check the folder you indicated should receive the output of the NSG job, and list the sub-folder '*icansgtmp*'. This will contain the data submitted to the NSG job and its output file(s).
 
##  Summary

Here we showed, via a simple example, how high-performance computing (HPC) resources at the San Diego Supercomputer Center (SDSC), accessible via NSG, can be integrated seamlessly into an EEGLAB plug-in using the flexible *pop_nsg* command line tool.
Note that this example is intended only a proof-of-concept example. Feel free to explore other implementation variations in your plug-ins. Note also that your plug-in should in nearly all cases give the user the option of computing on the local machine *else* via NSG. You should consider allowing the user to specify further NSG launch variables, and might also urge the NSG user to test the performance of the plug-in on a small subset of their data before launching a lengthy NSG computation. 