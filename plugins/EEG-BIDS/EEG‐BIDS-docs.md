---
layout: default
title: EEG-BIDS
long_title: EEG-BIDS
parent: EEG-BIDS
grand_parent: Plugins
---
# Documentation and tutorial videos

<img width="1680" alt="BIDS_doc1play" src="https://github.com/sccn/bids-matlab-tools/assets/1872705/643cc06a-90b5-4697-b1f8-7769dc937bfb">

[link to video](https://www.youtube.com/watch?v=EClpeP7WREw)

# Import datasets from BIDS to EEGLAB study

The EEGLAB menu to import a BIDS dataset into an EEGLAB study is fully functional. Screen capture is shown below.

![pop_importbids.m interface](pop_importbids.png)

Raw EEG data file often has events. However, BIDS also define events in dedicated event files. Sometimes the BIDS event files contain more information than the raw EEG data file. In that case, users may choose to overwrite raw EEG data events with the event information contained in the BIDS event files.

Similarly, raw EEG data files often define channel labels. However, BIDS also defines channel labels and channel locations in dedicated event files. By pressing the second checkbox, users may choose to use the channel label and location information contained in the BIDS channel definition files.

Finally, users may select an output folder for storing their EEGLAB STUDY. If a folder is not selected, EEGLAB will store STUDY files ''in place'' which means in the BIDS folder structure - resulting in the BIDS folder becoming non-BIDS compliant and failing to pass BIDS validation because of the additional EEGLAB files.

# Export datasets to BIDS from the graphic interface

After installing the bids-matlab-tools plugin, the BIDS menu should appear in the EEGLAB File menu item as shown below.

![](eeglab_menu_bids.png)

We will go through the menus one by one. First the task menu. This is where you enter all the information about the task and amplifier information.

![](bids_task.png)

Once you are done entering task information, you can select the participant menu. There are as many rows as subjects. For each subject, you can specify age, gender, group, etc... Only the participant_id column is mandatory and other columns are optional.

![](participant.png)

Note that it is also possible to define custom columns. To do this, you can click on the "import column(s)" push button. Upon doing so, you are prompted to select a text or Excel file. Note that the first row must contain column names. After selecting the file, the following interface pops up.

![](import_column.png)

You must indicate which column contains participant ID. You can also select columns for the pre-defined BIDS participant information, such as age, gender, etc... Finally, it is possible to select columns which will be added to the BIDS participant file, in this case "ethnicity" and "income".

Lastly, we fill out information about events. The GUI displays default BIDS event fields to which you can associate the corresponding EEGLAB event field in your data. *onset*, *value*, and *sample* are mapped to their corresponding EEGLAB field by default. *duration* and *HED* will also be automatically mapped if their corresponding EEGLAB field (*duration* and *usertags* respectively) exist. Custom fields can be added via the "Add BIDS field" button. Fields can also be removed via the "Remove BIDS field" button. Note that any BIDS field not mapped to EEGLAB event field will not be saved for later export.
![](pop_eventinfo.png)

# Export datasets to BIDS from the command line

Exporting a collection of datasets to BIDS can also conveniently be done from the command line. A documented example script [bids_export_example.m](https://github.com/sccn/bids-matlab-tools/blob/master/bids_export_example.m) and [bids_export_example2.m](https://github.com/sccn/bids-matlab-tools/blob/master/bids_export_example2.m) (more recent) are provided. You may modify these scripts for your own purpose. The help message of the function [bids_export.m](https://github.com/sccn/bids-matlab-tools/blob/master/bids_export.m) also contains information on how to export data in BIDS format. 

Note for exporting:
* Several tasks may be included in a single BIDS container. In this case, the name of the main task can be "mixed tasks" and multiple EEG datasets for different tasks can be contained in a single subject/eeg/ folder.
* Channel electrodes should not be exported by default if they are template electrode positions. This is because BIDS is about raw data. Electrode positions based on templates (averages) should therefore not be included.

# EEG and eye-tracking alignment

In the testing folder, use the **test_smi.m** function to look at EEG and eye-tracking synchronization. The plot below shows the original eye-tracking data (along with the events plotted as black vertical traces) and on top the joint EEG and eye-tracking data (only the eye-tracking data is shown for comparison). The alignment is near perfect despite the different sampling rates. 

![Screen Shot 2023-12-12 at 5 37 25 PM](https://github.com/sccn/bids-matlab-tools/assets/1872705/f2d9f851-b6d9-4e7c-9360-1d7e6880e6b3)

See the function [bids_export_example5_eye.m](https://github.com/sccn/bids-matlab-tools/blob/master/bids_export_eye_tracking_example5.m) for how to export joint EEG and eye-tracking data.