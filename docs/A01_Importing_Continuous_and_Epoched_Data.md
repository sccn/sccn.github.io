---
layout: default
title: A01 Importing Continuous and Epoched Data
permalink: /docs/A01_Importing_Continuous_and_Epoched_Data
parent: Docs
---

{ {Backward_Forward|IV.Appendix|IV. Appendix|A02: Importing Event Epoch
Info|A02: Importing Event Epoch Info} }

## Importing continuous and epoched data

#### Supported Data Formats

| File Format                                                                             | File Extension | File type              | Events                  | Channel Labels | EEGLAB                                               | Biosig                                               | File IO                                              | Support                                    |
| --------------------------------------------------------------------------------------- | -------------- | ---------------------- | ----------------------- | -------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------ |
| ANT EEProbe                                                                             | .avr           | _                     | _                      | _             | _                                                   | _                                                   | _                                                   | [Comments](/Talk:avr "wikilink")           |
| ANT EEProbe                                                                             | .cnt           | _                     | _                      | _             | { {table|status=y|color=green} }                     | { {table|status=y|color=green} }                     | { {table|status=y|color=green} }                     | [Comments](/Talk:EEProbe_cnt "wikilink")   |
| [ASCII](/#Importing_sets_of_data_averages_into_EEGLAB "wikilink")                       | .txt           | _                     | _                      | _             | { {table|status=y|color=lightgreen} }                | { {table|status=y|color=lightgreen} }                | _                                                   | [Comments](/Talk:txt "wikilink")           |
| BCI2000                                                                                 | .bci2000       | continuous             | _                      | _             | { {table|status=p|color=yellow} }                    | _                                                   | _                                                   | [Comments](/Talk:bci2000 "wikilink")       |
| BCI2000                                                                                 | .gdf           | continuous             | _                      | _             | { {table|status=p|color=yellow} }                    | _                                                   | _                                                   | [Comments](/Talk:gdf "wikilink")           |
| Biologic                                                                                | .eeg           | _                     | _                      | _             | _                                                   | _                                                   | _                                                   | [Comments](/Talk:biologic_eeg "wikilink")  |
| Biopac                                                                                  | .mat/.acq      | _                     | _                      | _             | { {table|status=p (see comments)|color=yellow} }     | _                                                   | _                                                   | [Comments](/Talk:biopac_eeg "wikilink")    |
| [Biosemi](/#Importing_Biosemi_.BDF_files "wikilink")                                    | .bdf           | continuous             | Channel                 | _             | { {table|status=y|color=lightgreen} }                | { {table|status=y|color=lightgreen} }                | { {table|status=y|color=lightgreen} }                | [Comments](/Talk:bdf "wikilink")           |
| Blackrock                                                                               | .NEV .NSx      | _                     | _                      | _             | { {table|status=see comments|color=yellow} }         | _                                                   | _                                                   | [Comments](/Talk:Blackrock_eeg "wikilink") |
| [Brain Vision Analyzer](/#Importing_Brain_Vision_Analyser_Matlab_files "wikilink")      | .mat           | continuous & segmented | Embedded                | _             | { {table|status=y|color=lightgreen} }                | { {table|status=y|color=lightgreen} }                | { {table|status=n|color=red} }                       | [Comments](/Talk:bva_mat "wikilink")       |
| Brain Vision Analyzer                                                                   | .vhdr          | _                     | file                    | _             | { {table|status=y|color=lightgreen} }                | { {table|status=y|color=lightgreen} }                | { {table|status=n|color=red} }                       | [Comments](/Talk:vhdr "wikilink")          |
| BrainStorm                                                                              | .vsm           | _                     | _                      | _             | _                                                   | _                                                   | _                                                   | [Comments](/Talk:vsm "wikilink")           |
| [Cogniscan](/EEGLAB_Plugins "wikilink")                                                 | _             | _                     | _                      | _             | { {table|status=p|color=yellow} }                    | _                                                   | _                                                   | [Comments](/Talk:cogniscan "wikilink")     |
| Compumedics Profusion                                                                   | .raw           | _                     | _                      | _             | { {table|status=see comments|color=yellow} }         | _                                                   | _                                                   | [Comments](/Talk:compumedics "wikilink")   |
| CTF/BrainStorm                                                                          | .ctf           | _                     | _                      | _             | { {table|status=y|color=lightgreen} }                | { {table|status=y|color=lightgreen} }                | { {table|status=y|color=lightgreen} }                | [Comments](/Talk:ctf "wikilink")           |
| [EGI/Netstation](/#Importing_EGI_.RAW_continuous_files "wikilink")                      | .RAW           | continuous & segmented | Channel                 | _             | { {table|status=y|color=lightgreen} }                | { {table|status=y|color=lightgreen} }                | { {table|status=y|color=lightgreen} }                | [Comments](/Talk:raw "wikilink")           |
| Elektra (MEG)                                                                           | .fif           | _                     | _                      | _             | { {table|status=n (see comments)|color=yellow} }     | { {table|status=y|color=lightgreen} }                | { {table|status=n|color=red} }                       | [Comments](/Talk:elktra_meg "wikilink")    |
| Emotiv                                                                                  | .edf           | _                     | _                      | _             | { {table|status=y (see comments)|color=lightgreen} } | { {table|status=y (see comments)|color=lightgreen} } | { {table|status=y (see comments)|color=lightgreen} } | [Comments](/Talk:emotiv_eeg "wikilink")    |
| ERPSS                                                                                   | .raw           | _                     | _                      | _             | { {table|status=y|color=lightgreen} }                | { {table|status=n|color=red} }                       | { {table|status=n|color=red} }                       | [Comments](/Talk:erpss_eeg "wikilink")     |
| ERPSS                                                                                   | .rdf           | _                     | _                      | _             | { {table|status=y|color=lightgreen} }                | { {table|status=n|color=red} }                       | { {table|status=n|color=red} }                       | [Comments](/Talk:rdf "wikilink")           |
| [European Data Format (16-bit)](/#Importing_European_data_format_.EDF_files "wikilink") | .edf           | _                     | Channel                 | _             | { {table|status=y|color=lightgreen} }                | { {table|status=y|color=lightgreen} }                | { {table|status=n|color=red} }                       | [Comments](/Talk:edf "wikilink")           |
| EDF+                                                                                    | .edf           | _                     | Channel                 | _             | { {table|status=y|color=lightgreen} }                | { {table|status=y|color=lightgreen} }                | { {table|status=n|color=red} }                       | [Comments](/Talk:edfplus "wikilink")       |
| INSTEP                                                                                  | .asc           | _                     | _                      | _             | { {table|status=y|color=lightgreen} }                | { {table|status=n|color=red} }                       | { {table|status=n|color=red} }                       | [Comments](/Talk:asc "wikilink")           |
| [Matlab Array](/#Importing_a_Matlab_array "wikilink")                                   | .mat           | _                     | Channel                 | _             | { {table|status=y|color=lightgreen} }                | { {table|status=y|color=lightgreen} }                | { {table|status=n|color=red} }                       | [Comments](/Talk:mat "wikilink")           |
| [Micromed](/EEGLAB_Plugins "wikilink")                                                  | _             | _                     | _                      | _             | { {table|status=p|color=yellow} }                    | _                                                   | _                                                   | [Comments](/Talk:micromed "wikilink")      |
| Neuroimaging4D                                                                          | .m4d           | _                     | _                      | _             | { {table|status=y|color=lightgreen} }                | { {table|status=n|color=red} }                       | { {table|status=n|color=red} }                       | [Comments](/Talk:m4d "wikilink")           |
| Neuromag                                                                                | .fif           | _                     | _                      | _             | { {table|status=see comments|color=red} }            | { {table|status=n|color=red} }                       | { {table|status=see comments|color=yellow} }         | [Comments](/Talk:m4d "wikilink")           |
| Neuroscan                                                                               | .avg           | _                     | _                      | _             | _                                                   | _                                                   | _                                                   | [Comments](/Talk:avg "wikilink")           |
| [Neuroscan](/#Importing_Neuroscan_.CNT_continuous_files "wikilink")                     | .CNT           | _                     | Embedded (see comments) | _             | { {table|status=y|color=lightgreen} }                | { {table|status=y|color=lightgreen} }                | { {table|status=y|color=lightgreen} }                | [Comments](/Talk:cnt "wikilink")           |
| [Neuroscan](/#Importing_Neuroscan_.EEG_data_epoch_files "wikilink")                     | .eeg           | continuous             | _                      | _             | { {table|status=y|color=lightgreen} }                | { {table|status=y|color=lightgreen} }                | { {table|status=y|color=lightgreen} }                | [Comments](/Talk:eeg "wikilink")           |
| [Nihon Kodhen](/#Importing_NihonKohden "wikilink")                                      | .eeg           | continuous             | _                      | _             |                                                      | { {table|status=y (see comments)|color=lightgreen} } |                                                      | [Comments](/Talk:nk "wikilink")            |
| Profusion                                                                               | .slp           | _                     | _                      | _             | _                                                   | _                                                   | _                                                   | [Comments](/Talk:slp "wikilink")           |
| [Snapmaster](/#Importing_Snapmaster_.SMA_files "wikilink")                              | .SMA           | _                     | Channel                 | _             | { {table|status=y|color=lightgreen} }                | { {table|status=y|color=lightgreen} }                | { {table|status=n|color=red} }                       | [Comments](/Talk:sma "wikilink")           |
| Spike2                                                                                  | .mat           | _                     | _                      | _             | { {table|status=y (see comments)|color=yellow} }     | { {table|status=n|color=red} }                       | { {table|status=n|color=red} }                       | [Comments](/Talk:spike2 "wikilink")        |
| [Tucker-Davis Technology](/EEGLAB_Plugins "wikilink")                                   | .tdt           | _                     | _                      | _             | { {table|status=p|color=yellow} }                    | _                                                   | _                                                   | [Comments](/Talk:tdt "wikilink")           |


**Please upload test files at <ftp://sccn.ucsd.edu/incoming> to help us
fill the table.**
File Format Compatibility is noted by the following:

|                                                                             |                                       |
| --------------------------------------------------------------------------- | ------------------------------------- |
| Supported Formats                                                           | { {table|status=y|color=lightgreen} } |
| Supported but requires MEX file                                             | { {table|status=y|color=green} }      |
| Unverified                                                                  | _                                    |
| Currently unsupported formats or not working                                | { {table|status = n|color=red} }      |
| Functionality via third-party [EEGLAB Plug-Ins](/EEGLAB_Plugins "wikilink") | { {table|status=p|color=yellow} }     |


See also [Electrode Data
Formats](/A03:_Importing_Channel_Locations#Supported_Electrode_Data_Formats "wikilink")
and how to work with [Other
Formats](/#Importing_data_in_other_data_formats "wikilink")


#### Importing a Matlab array or file

We first construct a 2-D Matlab array 'eegdata' containing simulated EEG
data in which rows are channels and columns are data points:

``` matlab
eegdata = rand(32, 256*100);
% build a matrix of random test data (32 channels, 100 seconds at 256 Hz)
```


To import these data, select the menu item <font color=brown>File \>
Import data \> from ASCII/float file or Matlab array</font>. At the Data
file/array click on option Matlab variable from the list and set the
name to eegdata. Set the sampling frequency to 256 Hz, press *OK*. Other
dataset parameters will be automatically adjusted.


![700px](/assets/images/II11pop_editset.jpg)



Note on importing data from other file formats: To import continuous
data from a Matlab *.mat* file instead from a Matlab array, scroll the
list of choices in the box above that shows Matlab *.mat* file.

Note: When reading a Matlab *.mat* file, EEGLAB assumes it contains only
one Matlab variable. For reading a (32-bit) binary float-format data
file, two choices are available: *float le* (little-endian) and *float
be* (big-endian) The correct choice here depends on operating system. In
case the bit ordering is unknown, try each of them. Note that the
toolbox command line function { {File|shortread.m} } can also be used to
read data from a (16-bit) short-integer file. The resulting Matlab array
may then be imported into EEGLAB as shown above.

Now is a good time to add a *Description* about the dataset. A window
will pop up containing a text box for this purpose. Enter as much
information about the dataset as possible. The information you enter
will be saved with the dataset for future reference by you or by others
who may load the data. You can add to or revise these comments later by
selecting menu item <font color=brown>Edit \> Dataset info</font>. It is
also possible to save the newly created data into a new dataset, either
retaining or overwriting (in Matlab process memory) the old dataset. To
also save the new dataset (with all its accompanying information fields)
to disk, enter a filename in the lower edit field. Press *OK* to
accept.


![Image:II11pop_newset.jpg](/assets/images/II11pop_newset.jpg)



Then use menu item <font color=brown>Plot \> Channel data
(scroll)</font> to visualize the imported data.

#### Importing a random Matlab file

Matlab files may have many different formats. They are simply containers
(like Excel files may contain data organized in many different ways in
different tabs). EEGLAB cannot guess the internal format of the Matlab
file, so you need to do this step yourself. Matlab files are best
imported on the Matlab command line

``` matlab
mydata = load(‘-mat’, ‘your_file.mat’)
```

Then see where is the data in the “mydata” structure, for example in
mydata.eeg might contain an array that contains raw EEG data (channels
by samples). Put this data in a Matlab variable.

``` matlab
myeeg = mydata.eeg; % This is an example, the name of the field "eeg" might differ for you
```

Then select EEGLAB menu item <font color=brown>File \> Import data \>
from ASCII/float file or Matlab array</font> and enter “myeeg” in the
first edit box (the previous section has more details on importing
Matlab arrays).

#### Importing Biosemi .BDF files

[Biosemi](http://www.biosemi.com) has extended the 16-bit European
standard "EDF" (European Data Format) to their 24-bit data format, BDF
(Biosemi Data Format). Select menu item <font color=brown>File \> Import
data \> From Biosemi .BDF file</font> (calling function {
{File|pop_readbdf.m} }). A window will pop up to ask for a file name.


![275px](/assets/images/pop_readbdf.gif)



Press *OPEN* to import a file.

Then a second window pops up, press *Ok*.



![Image:II12pop_readbdf.jpg](/assets/images/II12pop_readbdf.jpg)



The third window to pop up ask for a new dataset name.



![Image:pop_readbdf2.gif](/assets/images/pop_readbdf2.gif)



Press *OK*, then select menu item <font color=brown>Plot \> Channel data
(scroll)</font> to inspect the data. A sample .BDF file is available --
[TEST_256.BDF](http://sccn.ucsd.edu/eeglab/download/TEST_256.BDF) (use
*save link as* in your browser). (More sample files and reading
functions are also available from the [Biosemi ftp
site](ftp://194.109.194.84/Biosemi/BDF/)). To extract event records from
.BDF data, select menu item <font color=brown>File \> Import event info
\> From data channel</font> as explained elsewhere in this tutorial.

#### Importing European data format .EDF files

To import data collected in the joint European 16-bit data format (EDF),
select menu item <font color=brown>File \> Import data \> From European
data format .EDF file</font> (calling function { {File|pop_readedf.m}
}). A window will pop up to ask for a file name. Then select menu item
<font color=brown>Plot \> EEG data (scroll)</font> to inspect the data.
A sample .EDF file is available --
[TEST.EDF](http://sccn.ucsd.edu/eeglab/download/TEST.EDF) (use *save
link as* in your browser). To extract event records from .EDF data,
select menu item <font color=brown>File \> Import event info \> From
data channel</font> as explained elsewhere in this tutorial.

#### Importing Netstation/EGI files

The simplest way to read EGI (Electrical Geodesics Incorporated) .RAW
data files is to select menu item <font color=brown>File \> Import data
\> From Netstation binary simple file</font>. Note that native EGI files
in the current 2009 version of the EGI Netstation software are not
EEGLAB compatible and need to be converted to Netstation binary simple.
There are however two solutions to import the most recent files. One is
an EEGLAB plugin and another one is through File-IO. EGI files can also
be converted to EDF and imported into EEGLAB but events may be corrupted
in EDF files so the "Netstation binary simple" format is to be
preferred. Once the EEGLAB menu is selected, the following window will
appear


![290px](/assets/images/pop_readegi.gif)



The function { {File|pop_readegi.m} } should be able to read EGI
Version 2 and Version 3 data files. The presence of events in the EGI
format is recorded in an additional EGI data channel. Information from
this channel is automatically imported into the EEGLAB event table and
this channel is then removed by EEGLAB from the EEGLAB data. (If, for
any reason this fails to occur, extract events using menu item
<font color=brown>File \> Import event info \> From data channel</font>
as explained elsewhere in this tutorial.)

Note that current Native Netstation files cannot be imported in
EEGLAB/Matlab. Only "Netstation binary simple" files can be imported in
EEGLAB (current Netstation files can easily be converted to Netstation
binary simple from the Netstation software itself). EDF files can also
be exported from Netstation and imported in EEGLAB, but the events are
not stored in the last channel by Netstation. Converting data files to
"Netstation binary simple" is the simpliest way to get EGI files under
EEGLAB/Matlab.

When a subject is made of multiple segments (xxx001.raw; xxx002.raw;
xxx003.raw etc...), select <font color=brown>File \> Import data \> From
multiple seg. Netstation files</font>. A window will pop up to ask for
the file name. Then select menu item <font color=brown>Plot \> EEG data
(scroll)</font> to inspect the imported data.
Finally, it is also possible to import Matlab files exported by
Netstation using menu item (<font color=brown>File \> Import data \>
From Netstation epoch Matlab files</font>) - the function can only
import data exported using the "individual fields" option which is the
default. These files contain data epochs but are missing a lot of
information. It is therefore recommended to use the file "Netstation
binary simple" format.

#### Importing Neuroscan .CNT continuous files

Note: In our experience, importing Neuroscan files is not an easy matter
and no universal read function may exist. It seems that the EEGLAB
function works properly in most cases, even for recent (2002) data
files. For more about how to read Neuroscan files under Matlab, see a
[helper
page(obsolete)](http://www.cnl.salk.edu/%7Earno/cntload/index.html). A
stand-alone Matlab function for reading this format is also available on
the function index page as { {File|loadcnt.m} }. You may import the EEG
test file [TEST.CNT](http://sccn.ucsd.edu/eeglab/download/TEST.CNT) and
use it to test the following tutorial steps.


Start by selecting the menu item <font color=brown>File \> Import data
\> From .CNT data file</font>, which calls the { {File|pop_loadcnt.m} }
function. The following window will appear:



![Image:pop_loadcnt2.gif](/assets/images/pop_loadcnt2.gif)



Select the file to input (after changing the filter to the correct
directory if necessary), and press *OPEN*. The following window will pop
up:



![Image:pop_loadcnt.gif](/assets/images/pop_loadcnt.gif)



The first input field concerns the structure of the .CNT file. If the
imported data don't look like continuous EEG, try changing this number.
Most often it should be 1 or 40, but other values may work. Now press
*OK*. A window asking for a new set name will pop up, press OK to save
the new data set.




![Image:II15pop_newset.jpg](/assets/images/II15pop_newset.jpg)



Next, use menu item <font color=brown>Plot \> Channel data
(scroll)</font> to inspect the input data and menu item
<font color=brown> Edit \> Event values</font> to inspect the input
event field latencies. EEGLAB (from version 4.31) automatically reads
channel labels. If you call the menu <font color=brown>Edit \> Channel
locations</font>, EEGLAB will automatically find the location of most
channels (based on channel labels).

We will now illustrate how to import additional epoch event information
contained in an accompanying Neuroscan .DAT file into the EEGLAB
dataset. Before importing the .DAT file, you must first epoch the loaded
data (i.e., you must separate it into data epochs). To epoch the data,
select <font color=brown>Tools \> Extract epochs</font>



![Image:pop_epochcnt.gif](/assets/images/pop_epochcnt.gif)



Simply press *OK* to epoch the data based on the events contained in the
.CNT file (here using a time window extending from -1 s before to 2 s
after events). The following window will appear:



![Image:II15pop_newset2.jpg](/assets/images/II15pop_newset2.jpg)



Use this window to enter description and save the new dataset. For
computers with limited memory (RAM), try overwriting the parent dataset
(here, the continuous dataset we have just imported) by checking the
*Overwrite parent* box in this window. One may also save the dataset to
disk. Press *OK* when done. The following baseline removal window will
pop up:



![Image:II15pop_rmbase.jpg](/assets/images/II15pop_rmbase.jpg)



Simply press *OK* and continue.

#### Importing Neuroscan .EEG data epoch files

Select <font color=brown>File \> Import data \> From .EEG data
file</font>, calling function { {File|pop_loadeeg.m} }. A first window
will pop up to ask for the file name and a second window (below) will
query for data format (16 or 32 bits) and for data range. See the {
{File|pop_loadeeg.m} } function for more details (a 16-bit sample file
is available [here](http://sccn.ucsd.edu/eeglab/download/TESTEEG.EEG)
for testing). Data epochs have now been extracted from the EEG data. See
also the section below about importing DAT file containing epoch
information.



![Image:pop_loadeeg.gif](/assets/images/pop_loadeeg.gif)



Then select menu item <font color=brown>Plot \> EEG data (scroll)</font>
to inspect the imported data. In this case, epoch events have also been
imported from the file and can be visualized using menu item
<font color=brown>Edit \> Event values</font>.

#### Importing Snapmaster .SMA files

Select menu item <font color=brown>File \> Import data \> From
Snapmaster .SMA file</font> (calling function { {File|pop_snapread.m}
}). A window will pop up to ask for a file name. The following window
will pop up to ask for relative gain, leave it on 400 and press *Ok*.



![Image:II16pop_snapread.jpg](/assets/images/II16pop_snapread.jpg)



A window will pop up to ask for a file name. Then select menu item
<font color=brown>Plot \> Channel data (scroll)</font> to inspect the
data and item <font color=brown>Edit \> Event values</font> to inspect
event latencies and types. A sample .SMA data file is available --
[TEST.SMA](http://sccn.ucsd.edu/eeglab/download/TEST.SMA) (use *save
link as* in your browser).

#### Importing ERPSS .RAW or .RDF data files

To read ERPSS files (Event-Related Potential Software System, JS Hansen,
Event-Related Potential Laboratory, University of California San Diego,
La Jolla, CA, 1993), select menu item <font color=brown>File \> Import
data \> From ERPSS .RAW or .RDF file</font> (calling function {
{File|pop_read_erpss.m} }). A window will pop up to ask for a file
name. Then select menu item <font color=brown>Plot \> Channel data
(scroll)</font> to inspect the data and item <font color=brown>Edit \>
Event values</font> to inspect event latencies and types. A sample .RDF
data file is available --
[TEST.RDF](http://sccn.ucsd.edu/eeglab/download/TEST.RDF) (use *Save
link as* in your browser). A header file for the ERPSS format is also
available [here](http://sccn.ucsd.edu/eeglab/download/ERPSS.H).\>

#### Importing Brain Vision Analyser Matlab files

To read Brain Vision Analyser (BVA) Matlab files, first export Matlab
files from the BVA software. Then use menu item <font color=brown>File
\> Import data \> From Brain Vis. Anal. Matlab file</font> (calling
function { {File|pop_loadbva.m} }). A window will pop up asking for a
file name. After reading the data file, select menu item
<font color=brown>Plot \> Channel data (scroll)</font> to inspect the
data and item <font color=brown>Edit \> Event values</font> to inspect
event latencies and types. Channel locations will also be imported and
can be visualized using menu item <font color=brown>Plot \> Channel
locations \> By name</font>. A sample BVA Matlab data file is available
-- { {File|TESTBVA.MAT} } (use *Save link as* in your browser). Note
that you need a
[macro](http://sccn.ucsd.edu/eeglab/testfiles/BVA/CreateMATFile.vabs)
(and Matlab installed) to be able to export Matlab files from Brain
Vision Analyser.

#### Importing sets of data averages into EEGLAB

EEGLAB was made to process and visualize single-trial data.
Event-related potential (ERP) averages can also be processed and
visualized, but they should not be imported directly. Note that in our
current practice, we perform averaging over trials after applying ICA
and not before (see Makeig et al. Science, 2002).

However, an increasing number of ERP researchers find it of interest to
apply ICA to related *sets* of ERP grand averages (see [Makeig et al, J.
Neuroscience, 1999](http://sccn.ucsd.edu/~scott/bib.html#JN1999) and
[Makeig et al., Royal
Society, 1999](http://sccn.ucsd.edu/~scott/bib.html#RoyalSoc1999)). To
import data grand-average epochs into EEGLAB, stack the different
conditions in a single array as explained below.

First, the data averages for different conditions must be imported to
Matlab. For example, one may export these averages in text format and
then use the standard Matlab function

> \>\> load -ascii filename.txt

Note that to import ASCII files to Matlab, all column names and row
names must be removed. For Neuroscan user, we have also programmed the
function { {File|loadavg.m} } which can read most binary .AVG Neuroscan
files.

Then you will need to concatenate data averages. For example, from a
three-condition experiment, we may derive three ERP averages with a
sampling rate of 1000 Hz, covering from -100 to 600 ms with respect to
stimulus onsets (Note that we always process each subject individually
and then compare the results across subjects at the end of the
analysis).

For instance typing *\>\> whos* under Matlab might return:

``` matlab
Name                       Size               Bytes                 Class
avgcond1                   31x600             14880                 double array
avgcond2                   31x600             14880                 double array
avgcond3                   31x600             14880                 double array

Grand total is 55800 elements using 446400 bytes
```


Note: If necessary, transpose the arrays (so rows=channels,
colunmns=data samples, i.e. chan\*samp) like this (not necessary for
this example)

> \>\> avgcond1 = avgcond1';

Then concatenate the arrays

> \>\> allcond = \[ avgcond1 avgcond2 avgcond3 \];


Finaly, you will need to import concatenated data averages into EEGLAB.
First start EEGLAB:

> \>\> eeglab


Select menu item <font color=brown>File \> Importing data \> From
ascii/float file or Matlab array</font>


![Importing data averages](/assets/images/pop_importdata2.gif)



Enter the information as indicated above. The following window pops up
and allows you to add comments and/or save the new dataset immediately.
Press *OK* to create a new dataset.



![Image:pop_newset.jpg](/assets/images/pop_newset.jpg)



Select <font color=brown>Plot \> Channel ERPs\> in rect. array</font>
and set the last option, 'Plot single trials', to *YES* to visualize the
three condition ERPs.



![Image:II43pop_plotdata.jpg](/assets/images/II43pop_plotdata.jpg)



It is possible to process the three average-ERP epochs as if they were
single-trial epochs (although in this case some EEGLAB functions may not
be meaningful). See the [Single subject data analysis
tutorial](/I.Single_subject_data_processing_tutorial "wikilink") for
more information.

#### Importing data in other data formats

The Biosig toolbox ([biosig.sf.net](http://biosig.sf.net)) contains
links to functions to read other EEG data formats in Matlab. You may
download the Biosig plugin for EEGLAB (see the EEGLAB
[plugin](http://sccn.ucsd.edu/eeglab/plugins.html) page).

For other non-suported data format, the home page of [Alois
Schlolg](http://www-dpmi.tu-graz.ac.at/%7Eschloegl/matlab/eeg/) contains
links to other Matlab reading functions. We are also willing to add
other data importing functions to EEGLAB, so please send us a sample raw
data file together with a Matlab function to read it and a README file
describing the origin of the data and its format. We will attempt to
include such functions in future releases of EEGLAB. Contributing
authors will retain all rights to the functions they submit, and the
authors' name(s) will be displayed in the function header. See our page
on how to [contribute](/A4:_Contributing_to_EEGLAB "wikilink") to
EEGLAB.
The EEGLAB discussion list archive also contains messages from users for
importing specific data formats. You may search the list archive (and
the rest of the EEGLAB web site) archive using Google from the bottom of
the main [EEGLAB web page](http://sccn.ucsd.edu/eeglab/).

[Category:IV. Appendix](/Category:IV._Appendix "wikilink") {
{Backward_Forward|IV.Appendix|IV. Appendix|A02: Importing Event Epoch
Info|A02: Importing Event Epoch Info} }