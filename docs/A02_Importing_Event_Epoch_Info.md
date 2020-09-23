---
layout: default
title: A02 Importing Event Epoch Info
permalink: /docs/A02_Importing_Event_Epoch_Info
parent: Docs
---

{ {Backward_Forward|A01:_Importing_Continuous_Epoched_Data|A01:
Importing Continuous Epoched
Data|A03:_Importing_Channel_Locations|A03: Importing Channel
Locations} }

## Importing event and epoch information

#### Supported Data Formats

| File Format                                                            | File Extension   | File type | Events | Channel Labels | EEGLAB                                | Biosig                                | File IO | Support                             |
| ---------------------------------------------------------------------- | ---------------- | --------- | ------ | -------------- | ------------------------------------- | ------------------------------------- | ------- | ----------------------------------- |
| [Presentation](/#Importing_events_from_a_Presentation_file "wikilink") | .LOG             | _        | _     | _             | { {table|status=y|color=lightgreen} } | { {table|status=y|color=lightgreen} } | _      | [Comments](/Talk:log "wikilink")    |
| [Neuroscan](/#Importing_Neuroscan_.DAT_information_files "wikilink")   | .DAT             | _        | _     | _             | { {table|status=y|color=lightgreen} } | { {table|status=y|color=lightgreen} } | _      | [Comments](/Talk:dat "wikilink")    |
| Eprime                                                                 | .TXT (not .EDAT) | _        | _     | _             | { {table|status=y|color=lightgreen} } | _                                    | _      | [Comments](/Talk:eprime "wikilink") |
| Custom text                                                            | _               | _        | _     | _             | { {table|status=y|color=lightgreen} } | _                                    | _      | [Comments](/Talk:txt "wikilink")    |
|                                                                        |                  |           |        |                |                                       |                                       |         |                                     |
|                                                                        |                  |           |        |                |                                       |                                       |         |                                     |
|                                                                        |                  |           |        |                |                                       |                                       |         |                                     |
|                                                                        |                  |           |        |                |                                       |                                       |         |                                     |


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



EEGLAB counts records of the time and nature of experimental events to
analyze the EEG data. This section details how to load in event
information which coded in one of the data channels, stored in a Matlab
array or separate ascii file. When event information is read in, (as of
v4.2) EEGLAB copies the resulting EEG.event structure to a back-up
(*ur*) copy, EEG.urevent and creates links from each event to the
corresponding urevent. This allows the user to select events based on
the previous (or future) event *context*, even *after* data containing
some events has been rejected from the data (see the [event
tutorial](/Chapter_03:_Event_Processing "wikilink") for more
information).

#### Importing events from a data channel

Often, information about experimental events are recorded onto one of
the rows (channels) of the EEG data matrix. Once more we create
simulated data to illustrate how to import events from a data channel.
Assuming an EEG dataset with 33 rows (channels), out of which the first
32 are channels and the last (33) is an event channel with values 1
(stimulus onset), 2 (subject response), and 0 (other), Matlab code for
generating such data follows (to test, copy and paste the code to the
Matlab command line):

>
> \>\> eegdata = rand(32, 256\*100); % 32 channels of random activity
> (100 s sampled at 256 Hz).
> \>\> eegdata(33,\[10:256:256\*100\]) = 1; % simulating a stimulus
> onset every second
> \>\> eegdata(33,\[100:256:256\*100\]+round(rand\*128)) = 2; %
> simulating reaction times about 500 ms after stimulus onsets


After copying the code above to Matlab and importing the array *eegdata*
into EEGLAB as a test dataset (see [Matlab
arrays](/#Importing_a_Matlab_array "wikilink") in this section), select
menu item <font color=brown>File \> Import event info \> from data
channel</font> to call function { {File|pop_chanevent.m} } .



![Image:II21pop_chanevent.jpg](/assets/images/II21pop_chanevent.jpg)



Enter *33* as the event channel and set the edge-extract type to *up
(leading)* (Note: place the mouse over the text *Transitions to extract*
to see contextual help).

Press *OK*. Now, the event information will have been imported into the
test EEGLAB dataset. At the same time, channel 33 will have been deleted
from the test data. Select menu item <font color=brown>Edit \> Event
values</font> to inspect the imported event types and latencies.

#### Importing events from a Matlab array or text file

Using the random EEG dataset created above, we import event information
stored in an ASCII text file,
[tutorial_eventtable.txt](http://sccn.ucsd.edu/eeglab/download/tutorial_eventtable.txt).
This text file is composed of three columns, the first containing the
latency of the event (in seconds), the second the type of the event, and
the third a parameter describing the event (for example, the position of
the stimulus). For example, the top lines of such a file might be:

<table>
<tbody>
<tr class="odd">
<td><p><font color=green><strong>Latency</strong></p></td>
<td><p><font color=green><strong>Type</strong></p></td>
<td><p><font color=green><strong>Position</strong></p></td>
</tr>
<tr class="even">
<td><p><font color=green>1</p></td>
<td><p><font color=green>target</p></td>
<td><p><font color=green>1</p></td>
</tr>
<tr class="odd">
<td><p><font color=green>2.3047</p></td>
<td><p><font color=green>response</p></td>
<td><p><font color=green>1</p></td>
</tr>
<tr class="even">
<td><p><font color=green>3</p></td>
<td><p><font color=green>target</p></td>
<td><p><font color=green>2</p></td>
</tr>
<tr class="odd">
<td><p><font color=green>4.7707</p></td>
<td><p><font color=green>response</p></td>
<td><p><font color=green>2</p></td>
</tr>
<tr class="even">
<td><p><font color=green>5</p></td>
<td><p><font color=green>target</p></td>
<td><p><font color=green>1</p></td>
</tr>
<tr class="odd">
<td><p><font color=green>6.5979</p></td>
<td><p><font color=green>response</p></td>
<td><p><font color=green>1</p></td>
</tr>
<tr class="even">
<td><p><font color=green>...</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
</tr>
</tbody>
</table>

Select menu item <font color=brown>File \> Import event info \> Import
Matlab array or ASCII file</font>



![Image:pop_importevent.jpg](/assets/images/pop_importevent.jpg)



Browse for the tutorial text file, set the number of header lines to 1
(for the first line of the file, which gives the column field names) and
set the input fields (i.e., the names associated with the columns in the
array) to *latency type position*. If these field names are quoted or
separated by commas, these extra characters are ignored. (NOTE: It is
NECESSARY to use the names *latency* and *type* for two of the fields.
These two field names are used by EEGLAB to extract, sort and display
events. These fields must be lowercase since Matlab is case sensitive.)
In this interactive window the input *Event indices* and checkbox
*Append events?* can be used to insert new events or replace a subset of
events with new events (for instance for large EEG files which may have
several event files).

##### Important note about aligning events

An essential input above is *Align event latencies to data events* which
aligns the first event latency to the existing event latency and checks
latency consistency. A value of *NaN* (Matlab for not-a-number)
indicates that this option is ignored (as in the example above).
However, for most EEG data, the EEG is recorded with basic events stored
in an event channel (see Import events from a data channel above) for
instance. Detailed event information is recorded separately in a text
file: as a consequence the events recorded in the text file have to be
aligned with the events recorded in the EEG.

To do so, set the input for *Align event latencies to data events* to 0
if the first event in the text file correspond to the first event
recorded in the EEG (i.e., if the offset between the two is 0). Setting
this value to 1 indicates that event 1 in the event text file
corresponds to event number 2 in the EEG data. Here, negative values can
also be used to indicate that events in text file start before those
recorded in the EEG).

When aligning events, as shown in the following section, the function
displays the latencies of the two event types, so the user can check
that they are aligned based on his knowledge of the experiment (for
instance, there may be more events in the text file than recorded in the
EEG).
The last checkbox allow to automatically adjust the sampling rate of the
new events so they best align with the closest old event. This may take
into account small differences in sampling rates that could lead to big
differences by the end of the experiment (e.g., a 0.01% clock difference
during would lead to a 360-ms difference after one hour if not
corrected).

#### Importing events from a Presentation file

EEGLAB can also import events saved using the Presentation software.
Sample files are available for download here:
[TEST.SMA](http://sccn.ucsd.edu/eeglab/download/TEST.SMA)(a SnapMaster
.SMA file) and [TEST.LOG](http://sccn.ucsd.edu/eeglab/download/TEST.LOG)
(a Presentation event log file).</font>

To test the use of these sample files, first import the .SMA data file
using menu item <font color=brown>File \> Import data \> From .SMA data
file</font>. Then select <font color=brown>File \> Import event info \>
from Presentation LOG. file</font> to import events from the
Presentation log file as shown below</font>



![Image:pop_importpres.jpg](/assets/images/pop_importpres.jpg)



Then the following window pops-up</font>


![Image:pop_importpres2.jpg](/assets/images/pop_importpres2.jpg)



Scroll file fields to select which field (i.e., file column) contain the
event type and which column contain the event latency. The default is
fine with this specific file, so simply press *OK*. Matlab then returns:

` Replacing field 'Event Type' by 'type' for EEGLAB compatibility`
` Replacing field 'Time' by 'latency' for EEGLAB compatibility`
` Renaming second 'Uncertainty' field`
` Reading file (lines): 6`
` Check alignment between pre-existing (old) and loaded event latencies:`
` Old event latencies (10 first): 10789 21315 31375 41902 51962 62489 …`
` New event latencies (10 first): 10789 21315 31376 41902 51963 62489 …`
` Best sampling rate ratio found is 0.9999895. Below latencies after adjustment`
` Old event latencies (10 first): 10789 21315 31376 41902 51963 62488 …`
` New event latencies (10 first): 10789 21315 31375 41902 51962 62489 …`
` Pop_importevent warning: 0/6 have no latency and were removed`
` eeg_checkset: value format of event field 'Duration' made uniform`
` eeg_checkset: value format of event field 'Uncertainty2' made uniform`
` eeg_checkset note: creating the original event table (EEG.urevent)`
` Done.`

The function aligns the first event latency recorded in the Presentation
file to the first event latency recorded in the EEG in the SnapMaster
file. Check that the events recorded in the SnapMaster file have the
same latencies as the ones recorded in the .LOG presentation file. The
function then computes the best sampling rate ratio: this may account
for small differences in sampling rate that could lead to big
differences at the end of the experiment (e.g., 0.01% clock difference
during half an hour would lead to a 360-ms difference after one hour if
not corrected). Note that if the events are shifted (with respect to
events from the binary EEG file), it is always possible to suppress
events manually or to import the presentation file as a text file, as
described in the previous section. Note that some Presentation files
that contain comments at the end of the file may not be supported. If
you are not able to import a Presentation file, try removing any
comments from the end of the file. If it still does not work, try
importing the Presentation file as a text file as described in the
previous section.

Note: the presentation file contains more events (such as reaction time)
compared to the raw EEG data file (this is actually why we are importing
such file). The function will automatically ignore additional events
when events are aligned.

#### Importing E-Prime information files

The E-prime format is highly configurable, so you may use the ASCII
importer to import data files. Usually, we would use EEGLAB's
<font color=brown>Import data -\> From ASCII/float file or Matlab
array</font> functionality to import the data file and configure the
interface with the name of the E-Prime columns. It might be necessary in
some cases to export the E-Prime to a tab-delimited file first (for
example in a spreadsheet application) and edit some of the columns
information that might not be read correctly under Matlab. Send us your
E-Prime files (at eeglab at sccn.ucsd.edu) so we may tailor the ASCII
import menu for E-Prime files.

#### Importing Neuroscan .DAT information files

To import the .DAT file linked to a previously loaded .CNT file, select
menu item <font color=brown>File \> Import epoch info \> From Neuroscan
.DAT info file</font> (calling function { {File|pop_loaddat.m}
}).</font> The sample .DAT file associated with the continuous .CNT file
we used above is available for download --
[TEST.DAT](http://sccn.ucsd.edu/eeglab/download/TEST.DAT) (both the .DAT
file and the .CNT contains 100 epoch events).
Select the file to import in the resulting window. A second window will
then appear:



![Image:pop_loaddat.gif](/assets/images/pop_loaddat.gif)



In .DAT files, there must be a reaction time (in milliseconds) for each
epoch. However, depending on experiment design there may be no reaction
time in a given epoch. Then one has to use a code value for reaction
time latencies in these epochs. For instance, you might decide that a
value of *1000* (ms) would indicate that the subject did not respond.
(If all the epochs of the experiment already have a reaction time, do
not enter anything here.)

#### Importing epoch info Matlab array or text file into EEGLAB

Importing epoch information means that data epochs have already been
extracted from the continuous EEG data, and that the Matlab array or
text epoch information file has one entry per epoch. To illustrate how
to import such a file or array, we will once more create some simulated
EEG data.

` >>eegdata = rand(32, 256, 10); % 32 channels, 256 time points per epoch, 10 epochs`


Select menu item <font color=brown>File \> Import data \> From
ascii/float data file or Matlab array</font>.



![784px|Importing data averages](/assets/images/pop_importdata3.gif)



Press *OK* in this window (Note: If you select a data importing format
different from *Matlab variable*, be sure to click on it to actually
select the option.) Then, a second window will pop up.



![Image:pop_importdatanewset.jpg](/assets/images/pop_importdatanewset.jpg)



Press *OK* in this window (see [how to
import](/#Importing_a_Matlab_array "wikilink") at the beginning of this
page for more information). Note that the Matlab array, being 3-D, is
automatically imported as data epochs: the first dimension is
interpreted as data channels, the second as data points and the third as
data epochs or trials (e.g., our sample data matrix above contains 10
epochs). Let us imagine that our simulated EEG data came from a simple
stimulus/response task, with subject responses being either 'correct' or
'wrong' and response latencies recorded in milliseconds. Then the epoch
event file might look something like this:

|                             |                                |                                         |
| :-------------------------- | :----------------------------: | --------------------------------------: |
| <font color=green>**Epoch** | <font color=green>**Response** | <font color=green>**Response_latency** |
| <font color=green>1         |   <font color=green>Correct    |                   <font color=green>502 |
| <font color=green>2         |   <font color=green>Correct    |                   <font color=green>477 |
| <font color=green>3         |   <font color=green>Correct    |                   <font color=green>553 |
| <font color=green>4         |   <font color=green>Correct    |                   <font color=green>612 |
| <font color=green>5         |    <font color=green>Wrong     |                   <font color=green>430 |
| <font color=green>6         |   <font color=green>Correct    |                   <font color=green>525 |
| <font color=green>7         |   <font color=green>Correct    |                   <font color=green>498 |
| <font color=green>8         |   <font color=green>Correct    |                   <font color=green>601 |
| <font color=green>9         |   <font color=green>Correct    |                   <font color=green>398 |
| <font color=green>10        |   <font color=green>Correct    |                   <font color=green>573 |


This file
[tutorial_epoch.txt](http://sccn.ucsd.edu/eeglab/download/tutorial_epoch.txt)can
be downloaded or copied from the array above in a text file. Then select
menu item <font color=brown>File \> Import epoch info \> from Matlab
array or ascii file</font>, bringing up the following window:



![Image:II33pop_inportepoch.jpg](/assets/images/II33pop_inportepoch.jpg)



Above, browse for the *tutorial_epoch.txt* file, set the input fields
to *epoch response rt* (where rt is an acronym for 'reaction time'). The
only one of these fields that contains latency information is *rt*, so
it is entered to the as input to the *Field name(s) containing
latencies* query box. This file (see above) has 1 header line, as we
need to specify in the *Number of file header lines to ignore* box.
Finally the reaction times are recorded in milliseconds, which we
indicate as *1E-3* (i.e., one-thousandth of a second). Note that the
last entry, *Remove old epoch ...*, allows the user to import other
information later if it is unset. Press *OK* when done. Now select
<font color=brown>Edit \> Event fields</font>.




![Image:II33pop_editeventfield.jpg](/assets/images/II33pop_editeventfield.jpg)



It is a good idea to click each of the *Field description* buttons above
to add detailed descriptions of the meaning of each of the fields and
the coding of the field values (for example: 1 = correct, 2 = wrong,
etc.). This information is stored along with the event field values when
the dataset is saved (very useful for later analysis by you or
others\!).


Above, there are now five fields, not three as for the file data. Also
note that the field *rt* is not present. All of this is normal because
EEGLAB does not store epoch information as such, but converts it into
fields in its events structure. Though this seems a bit complicated in
the beginning, it helps avoid redundancy and inconsistencies between
epoch and event information. It also means that new data epochs can be
re-extracted from data epochs based on the stored events. Now select
menu item <font color=brown> Edit \> Event values</font> to inspect what
happened to the reaction time information (use the arrow to move to the
second event):



![Image:II33pop_editeventvals.jpg](/assets/images/II33pop_editeventvals.jpg)




As shown above, when epoch information was imported, events with type
named *rt* were created and assigned a latency. If we had had several
columns containing latency information, the function would have created
several types.
<u>Programming note:</u> For convenience, standard epoch information is
available from the command line in the variable *EEG.epoch*. Also, event
information available in *EEG.event* can be used for script or command
line data processing. See the [script writing
tutorial](/Chapter_02:_Writing_EEGLAB_Scripts "wikilink") for more
information.


## Exporting event information

Event information can also be exported to a .csv file (a plain text file
containing comma-separated values; a tab is used as delimiter). This
file can be opened with any text editor, OpenOffice Calc, or Microsoft
Excel, for example. To export all events of the currently loaded EEG
file, select File \> Export \> Events to text file. A dialog window pops
up asking for the name and location of the .csv file. The first row of
the file contains the names of the event fields. Note that there is
additional column "number", which is not an event field.

If you want more control over export options, you should use the command
line version of this tool. In the MATLAB command window, enter the
following code to achieve the same result as before with the GUI:

` events = eeg_eventtable(EEG, 'exportFile', 'test.csv');`
` `

In addition, a table with all events is displayed in the command window
by default. The additional index column can be disabled, and the time
unit of the latency and duration event fields can be set to seconds or
samples (default). The event structure is stored in a cell array for
convenient access. Type `help eeg_eventtable` to get more help on this
command.

[Category:IV. Appendix](/Category:IV._Appendix "wikilink") {
{Backward_Forward|A01:_Importing_Continuous_Epoched_Data|A01:
Importing Continuous Epoched
Data|A03:_Importing_Channel_Locations|A03: Importing Channel
Locations} }