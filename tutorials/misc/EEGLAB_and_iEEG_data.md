---
layout: default
title: EEGLAB and iEEG data
long_title: EEGLAB and MEG data
parent: Reference Topics
grand_parent: Tutorials
---
EEGLAB and iEEG, sEEG, or ECoG data
====================

EEGLAB supports reading most iEEG data formats (EDF, MEF3, NWB) through native code 
or plugins. The BIDS-Matlab-tools EEGLAB plugin
also supports importing BIDS-formatted MEG data. You may install plugins from the EEGLAB plugin manager (menu item <span style="color: brown">File > Manage EEGLAB extensions</span>). 
Gre
## Importing data

For example, after installing the MEF3 and BIDS-Matlab-tools plugins, you may import the 
[ds003708 BIDS dataset](https://nemar.org/dataexplorer/detail?dataset_id=ds003708&processed=0). 
First, download the data. Second, use menu item <span style="color: brown">File > BIDS Tools > Import BIDS folder to STUDY</span>. 
Leave all defaults and press OK (you may also select the column of interest for event types). Alternatively, use
menu item <span style="color: brown">File > Import data > Using EEGLAB functions and plugins > Import MEF3 folder</span> to import the <i>mefd</i> 
folder located in the <i>ds003708/sub-01/ses-ieeg01/ieeg/</i> folder of the BIDS dataset.

When importing with BIDS, the advantage is that, along with the data, you will likely have access to the iEEG electrode locations and relevant events. We show below the raw sEEG data for the unique subject in the BIDS dataset <i>ds003708</i>.

![Screen Shot 2022-09-09 at 3 16 34 PM](https://user-images.githubusercontent.com/1872705/189453192-66169ca9-174b-419c-ba7b-2bada4cbda91.png)

The channel locations for the same dataset are shown below.

![Screen Shot 2022-09-09 at 3 16 56 PM](https://user-images.githubusercontent.com/1872705/189453262-e942a285-b19f-455e-aad0-b38bbc62d0dd.png)

Even if you are not planning to use EEGLAB to process iEEG data, importing your iEEG data into EEGLAB and resaving it into an EEGLAB dataset may be useful for processing it in other software.

## Importing spike information

EEGLAB allows importing spikes as events when using the NWB (Neurodata Without Border). Below, we show an example using the file [sub-01_ses-20140828T132700_ecephys+image.nwb](https://api.dandiarchive.org/api/assets/94ba06fc-c870-4698-9c31-f403ee733887/download/) of this [DandiSet](https://dandiarchive.org/dandiset/000576/). After downloading the file, and after installing the NWB-io EEGLAB plugins (menu item <span style="color: brown">File > EEGLAB extensions</span> then install the NWB-io plugin). After installing the plugin, import the file above in EEGLAB using menu item <span style="color: brown">File > Import data > Using EEGLAB functions and plugins > From NWB file</span>. Make sure to check the checkbox to import spike latencies.

![Screenshot 2024-04-17 at 10 00 59 AM](https://github.com/sccn/sccn.github.io/assets/1872705/88a21917-0b8e-4f1d-a6fa-cae1297994d2)

Once the file has been imported, use menu item <span style="color: brown">Plot > Channel data (scroll)</span>

![Screenshot 2024-04-17 at 10 02 28 AM](https://github.com/sccn/sccn.github.io/assets/1872705/d8ddf709-7963-4f05-adef-8bf4049cc484)

We can then extract data epochs and plot ERPs. For example, to extract data epochs based on the spike of unit #1, use menu item <span style="color: brown">Tools > Extract epochs</span> and select events corresponding to the first unit as shown below.

![Screenshot 2024-04-17 at 11 45 31 AM](https://github.com/sccn/sccn.github.io/assets/1872705/c9b4082c-33c3-4f75-8d0a-522e852a7009)

You can then use menu item <span style="color: brown">Plot > Channel ERPs > with scalp maps</span> to plot the ERP of the two channels recorded in this dataset.

![Screenshot 2024-04-17 at 11 48 32 AM](https://github.com/sccn/sccn.github.io/assets/1872705/a863a7d3-cf51-4e38-b615-44ebc575bd50)

## Additional ressources

Other relevant resources for processing iEEG data:
- [Fieldtrip sEEG tutorial](https://www.fieldtriptoolbox.org/tutorial/human_ecog/)
- [MIA](http://www.neurotrack.fr/mia/) toolbox. Also accessible as a Brainstorm plugin.
- [RAVE](https://rave.wiki/) toolbox (R language).
