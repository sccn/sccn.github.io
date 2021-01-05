---
layout: default
title: a. Continuous data
parent: 4. Import data
grand_parent: Tutorials
---
Importing continuous and epoched data
=======
{: .no_toc }

Refer to the [quickstart guide](/Tutorials/quickstart.html) to load an EEG data file, and scroll data. This section of the tutorial deals with importing raw data files in different formats, some of them only available through EEGLAB plugins. 

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

Four steps to easily import continuous raw data files
------------------

First, if you have a raw EEG data file, determine the file format (for files with extension .cnt might be Neuroscan or ANT raw files, which are two different formats). Then follow these four steps.
1. Look if a menu item is available in <span style="color: brown">File → Using EEGLAB functions and plugins</span>. If it does, select the menu and import the file.

2. Use menu item <span style="color: brown">File → Using the File-IO interface</span>. EEGLAB might install the File-IO plugin if you do not have it installed already. If the function does not return an error, your file will be imported. File-IO is a Fieldtrip module that imports a variety of data formats. Refer to the [File-IO documentation](https://www.fieldtriptoolbox.org/development/module/fileio/) for more information. 

3. Use menu item <span style="color: brown">File → Using the BIOSIG interface</span>. The Biosig toolbox ([biosig.sf.net](http://biosig.sf.net)) contains
links to functions to read other EEG data formats in Matlab. EEGLAB might install the BIOSIG plugin if you do not have it installed already. If the function does not return an error, your file will be imported.

4. Use menu item <span style="color: brown">File → Manage EEGLAB extensions</span> and search for plugins (use the magnifier on the top right corner). Use the name of the amplifier you are using, for example. Once the plugin is installed, call the newly created sub-menu item in <span style="color: brown">File → Using EEGLAB functions and plugins</span>.

In 90% of the cases, the solution above will import the EEG data file. If it does not work, then the rest of this page contains documentation on importing other file formats.

Acquiring EEG data from within EEGLAB
--------------------

EEGLAB and LabStreamingLayer (LSL) are tightly tied as they both originated at the SCCN laboratory at UCSD. By installing the [*lsl_app_MatlabViewer*](https://github.com/labstreaminglayer/App-MATLABViewer/) extension, a menu item <span style="color: brown">File → Matlab LSL Viewer</span>, not only allows visualizing EEG LSL streams available on the network (Mac and Windows) but also to record them as EEGLAB .set data files. Note that this extension only allows recording one stream at a time. To fuse streams, record data as XDF using the LabRecorder python application, and import the XDF file in EEGLAB using the Mobilab plugin.

List of supported Data Formats
--------------------

The [plugin](https://sccn.ucsd.edu/eeglab/plugin_uploader/plugin_list_all.php) page contains all import plugin. Search for a given file extension or amplifier name. The same list of plugins is available through the EEGLAB plugin manager by invoking the <span style="color: brown">File → Manage EEGLAB extensions</span> menu item. If you encounter any problem with a plugin, we suggest you contact the plugin authors. Plugins also often have their own documentation.

Some rare EEGLAB plugins might not be available on the EEGLAB plugin manager and might be instead distributed as zip file by amplifier manufacturers. If you do not see a plugin for your data format, ask your EEG amplifier manufacturer.

Data import plugins and custom import
--------------------

### Importing data using command line mexSload of BIOSIG

Note that BIOSIG has separate C functions to import data. These functions can be interfaced in Matlab through the *mexSload* function. There is no graphic interface for that function. However, you may use the *mexSload* function to import data on the Matlab command line, and then use the documentation in the next section to import the Matlab array into EEGLAB.

### Importing a Matlab array

We first construct a 2-D Matlab array 'eegdata' containing simulated EEG
data in which rows are channels and columns are data points:

``` matlab
eegdata = rand(32, 256*100);
% build a matrix of random test data (32 channels, 100 seconds at 256 Hz)
```


To import these data, select the menu item <font color=brown>File →
Import data → from ASCII/float file or Matlab array</font>. Click on option Matlab variable from the list and set the
name to *eegdata*. Set the sampling frequency to 256 Hz, press *OK*. Other
dataset parameters will be automatically adjusted.


![700px](/assets/images/pop_importdata12.png)



Note on importing data from other file formats: To import continuous
data from a Matlab *.mat* file instead of a Matlab array, scroll the
list of choices in the box above that shows Matlab *.mat* file.

Note: When reading a Matlab *.mat* file, EEGLAB assumes it contains only
one Matlab variable. For reading a (32-bit) binary float-format data
file, two choices are available: *float le* (little-endian) and *float
be* (big-endian) The correct choice here depends on the operating system. In
case the bit ordering is unknown, try each of them. Note that the
toolbox command line function [shortread.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=shortread.m) can also be used
to read data from a (16-bit) short-integer file. The resulting Matlab
array may then be imported into EEGLAB, as shown above.

Once the data is imported, refer to the [quickstart guide](/Tutorials/quickstart.html) to scroll the data.

### Importing a file containing a Matlab structure

Matlab files may have many different formats. They are simply containers
(like Excel files may contain data organized in many different ways in
different tabs). EEGLAB cannot guess the Matlab file's internal format, so you need to do this step yourself. Matlab files are best
imported on the Matlab command line

``` matlab
mydata = load(‘-mat’, ‘your_file.mat’)
```

Then see where the data is in the “mydata” structure, for example 
*mydata.eeg* might contain an array that contains raw EEG data (channels
by samples). Put this data in a Matlab variable.

``` matlab
myeeg = mydata.eeg; % This is an example, the name of the field "eeg" might differ for you
```

Then select EEGLAB the <font color=brown>File → Import data →
from ASCII/float file or Matlab array</font> menu item and enter “myeeg” in the
first edit box (the previous section has more details on importing
Matlab arrays).

### Importing sets of data averages

EEGLAB was made to process and visualize single-trial data. <b>Despite this section in the tutorial, we strongly advise against processing and importing data averages</b>. Instead, one should import single-trial data from which event averages may be extracted.
Event-related potential (ERP) averages can also be processed and
visualized, but they should not be imported directly.

However, for old data, only data averages might be available. It is possible to process the three average-ERP epochs as if they were
single-trial epochs (although in this case, some EEGLAB functions may not
be meaningful). To import grand-average epochs into EEGLAB, stack the different conditions in
a single array as explained below.

First, the data averages for different conditions must be imported to
Matlab. For example, one may export these averages in text format and
then use the standard Matlab function

```matlab
>> load -ascii filename.txt
```

Note that to import ASCII files to Matlab, all column names and row
names must be removed.

Then you will need to concatenate data averages. For example, from a
three-condition experiment, we may derive three ERP averages with a
sampling rate of 1000 Hz, covering from -100 to 600 ms with respect to
stimulus onsets (Note that we always process each subject individually
and then compare the results across subjects at the end of the
analysis).

For instance typing *>> whos* under Matlab might return:

``` matlab
Name                       Size               Bytes                 Class
avgcond1                   31x600             14880                 double array
avgcond2                   31x600             14880                 double array
avgcond3                   31x600             14880                 double array

Grand total is 55800 elements using 446400 bytes
```

Note: If necessary, transpose the arrays (so rows=channels,
colunmns=data samples, i.e. chan\*samp) like this (not required for
this example). Then concatenate the arrays.

```matlab
>> allcond = [ avgcond1 avgcond2 avgcond3 ];
```

Finally, you will need to import concatenated data averages into EEGLAB as Matlab arrays.
Select menu item <font color=brown>File → Importing data → From
ascii/float file or Matlab array</font> as shown in one of the previous sections.

### Other data formats

We are eager to add
other data importing functions to EEGLAB, so please write a plugin and submit it on this [page](http://sccn.ucsd.edu/eeglab/plugin_uploader/upload_form.php).

The EEGLAB discussion list archive also contains messages from users for
importing specific data formats. You may search the list archive (and
the rest of the EEGLAB web site) archive using Google and adding the keyword *eeglablist*.