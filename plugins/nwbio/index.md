---
layout: default
title: nwbio
long_title: nwbio
parent: Plugins
has_children: true
nav_order: 12
---
To view the plugin source code, please visit the plugin's [GitHub repository](https://github.com/sccn/nwbio).

![NWBio](https://github.com/sccn/nwbio/assets/1872705/c7f70411-9d86-4df5-8de4-6e0a69594785)

# NWBio EEGLAB plugin

This plugin imports data from the Neurodata Without Borders
data format. Time series, channel information, and 
event information are imported. Use the EEGLAB import/export menus to
import/export files, or use the command line function pop_nwbimport.m
or pop_nwbexport.m

# Example

Export the tutorial EEGLAB data.

```matlab
pop_nwbexport(EEG, 'test.nwb');
```

Import the file exported above.

```matlab
EEG = pop_nwbimport('test.nwb');
```

# Use with EEGLAB

Use menu item **File > EEGLAB extensions** and search for the "nwbio" plugin. Once you have found it
install it. Then, use the menu item **File > Import data > From NWB file** to import a file. Once you
have selected a file, the following graphical interface will pop up.

![Screenshot 2024-04-13 at 3 12 11 PM](https://github.com/sccn/nwbio/assets/1872705/a25b146c-f235-4e39-ac7d-979a29e45796)

It lets you decide which event information you want to use as the primary information for EEGLAB (EEGLAB event type). 
EEGLAB perform most operations on event types, although it is also possible to use other fields. Note that all fields
will be imported in EEGLAB, but the primary field will be duplicated and in the event type field.

The checkbox allows importing neurons' spikes as EEGLAB event when they are present in the data file (when greyed out,
spikes are not present). Note that EEGLAB will not import all NWB information (such as spacial movement, calcium imaging, etc...).
This EEGLAB plugin only import electrophysiology data.

To export EEG or iEEG data, use the menu item **File > Export > Data to NWB file**. The following graphical interface
will pop up, allowing you to enter NWB-specific information. 

![Screenshot 2024-04-13 at 3 25 03 PM](https://github.com/sccn/nwbio/assets/1872705/aa287c74-0e2e-4576-89ea-ccabc939ab21)

Most entries are NWB-specific, so you may refer to the [NWB documentation](https://www.nwb.org/) for more information. The last two 
entries are specific to EEGLAB. "Event fields to export" lists the EEGLAB event fields available to export. Event onset and duration
are exported by default and are not listed. "Export channel (x, y, z) locations" allow exporting channel locations. If you use 
the template channel location, you may leave this option unchecked. 

# Version history

1.0 - import, and export, tested on multiple files
