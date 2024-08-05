---
layout: default
parent: nsgportal
grand_parent: Plugins

title: Nsgportal command line tools
long_title: Nsgportal command line tools
nav_order: 6
---
Just like many other EEGLAB functions, users can interact with *nsgportal* through either the graphic user interface or using command line tools. The command line tools allow users to largely automate their analysis and make the process easy to reproduce. In this section, we introduce the *nsgportal* command line tools to NSG.

# Using EEGLAB command line tools to NSG
Command line access to NSG from EEGLAB is mainly performed through two functions: *pop_nsginfo()* and *pop_nsg()*. The first function (*pop_nsginfo*) is used to setup your NSG credential, while *pop_nsg* will allow you to manage your NSG jobs. These functions are introduced in more detail in the next sections.

## Setting credentials - *pop_nsginfo*
Use function *pop_nsginfo* to specify your NSG credentials. The function accepts key-value pair inputs, allowing users to specify their NSG user name (option ***'nsgusername'***), user password (option ***'nsgpassword'***), and path to folder where NSG data will be downloaded (option ***'outputfolder'***). NSG key and NSG url are acceptable keys but need not be changed. See code snippet below for an example of *pop_nsginfo* command line call:  
```
pop_nsginfo('nsgusername', 'your_username', 'nsgpassword', 'your_password', 'outputfolder', '/path/to/output/folder');
```
Running *pop_nsginfo* without any arguments will bring up its GUI interface.

## Managing your NSG jobs - *pop_nsg*
The function *pop_nsg*  is the workhorse of the EEGLAB command line tools to NSG. Different ways to call the function allows you to:

1. Create and run NSG job (*pop_nsg* option ***'run'***)
2. Test the job on your local computer (*pop_nsg* option ***'test'***)
3. Retrieve its result (*pop_nsg* option ***'output'***)
4. Delete the job (*pop_nsg* option ***'delete'***)

In general, calling *pop_nsg* with these options should be done following the scheme:

```
[NSGJobStructure, AllNSGJobStructure] = pop_nsg('option_name', 'option_value');
```
In the case of using the options ***'run'*** or ***'test'***, the second argument mut be always the path to the zip file or folder containing the job to be submitted or tested. Using these options also require a second pair of arguments defining the script (.m) to be run in your test or NSG run (option ***'filename'***). For instance:

```
[NSGJobStructure, AllNSGJobStructure] = pop_nsg('test', 'path/to/my/job/folder', 'filename', 'my_job_script.m');
```

The two outputs of *pop_nsg* above are (1) *NSGJobStructure*: the NSG job structure containing all relevant information of the submitted job (not available for option ***'test'***) and (2) *AllNSGJobStructure* : array of all NSG jobs currently in your account (available from all *pop_nsg* options).
 
To call *pop_nsg* with options ***'output'*** or ***'delete'*** simply pass the job ID (ID can be assigned by user during job submission), the NSG job structure (see above) or the job URL (unique NSG identifier for a job. see *NSGJobStructure.jobstatus.selfUri.url*). For instance:

```
[NSGJobStructure, AllNSGJobStructure] = pop_nsg('output', 'My_Job_ID'); % Using job id
[NSGJobStructure, AllNSGJobStructure] = pop_nsg('output', NSGJobStructure.jobstatus.selfUri.url); % Using job URL
[NSGJobStructure, AllNSGJobStructure] = pop_nsg('output', NSGJobStructure); % Using job structure
```
Note that for running *pop_nsg* with options ***'output'*** or ***'delete'*** , a job has to be previosly submitted to NSG. The use of ***'output'*** is restricted to jobs already completed.

Running *pop_nsg* without any arguments will bring up the graphic interface.

## Other useful functions
Here a list of other useful EEGLAB command line tools to NSG.

### Request list of NSG jobs - *nsg_jobs*
Return cell array of all NSG jobs under your credentials.

Usage example:

```
alljobs = nsg_jobs;
```

### Recursive checking of job status - *nsg_recurspoll*
Recursive check on the status of a job running on NSG. A mandatory first argument is required to be a single job ID, NSG job structure or job URL. A pair of parameters ('pollinterval', time_in_seconds) can be added to specify the time between polls.

Usage example:

```
NSGJobStructure = nsg_recurspoll('My_Job_ID', 'pollinterval', 120 );
```

# Summary
This article introduced you to the command line tools of EEGLAB plug-in to NSG. To see a detailed explanation and examples of how to use EEGLAB to NSG command line tool, check out [this tutorial](https://github.com/sccn/nsgportal/wiki/Creating-and-managing-an-NSG-job-using-pop_nsg-from-the-command-line).
 Note that any function of EEGLAB plug-in to NSG, you can type "help *function_name*" to read its full documentation. The documentation is a great source explaining what the function does, examples of how to use it, what inputs are allowed, and what outputs it produces. It should always be your go-to when you're unsure about how to use the function.