---
layout: default
title: EEGLAB and iEEG data
long_title: EEGLAB and MEG data
parent: Reference Topics
grand_parent: Tutorials
---
EEGLAB and iEEG/sEEG/ECoG data
====================

EEGLAB supports reading most iEEG data formats (EDF, MEF3) through native code 
or plugins. The BIDS-matlab-tools EEGLAB plugin
also support importing BIDS formatted MEG data. You may install plugins from the EEGLAB plugin manager (menu item <span style="color: brown">File > Manage EEGLAB extensions</span>). 

For example, after installing the MEF3 and BIDS-matlab-tools plugins, you may import the 
[ds003708 BIDS dataset](https://nemar.org/dataexplorer/detail?dataset_id=ds003708&processed=0). 
First, download the data. Second, use menu item <span style="color: brown">File > BIDS Tools > Import BIDS folder to STUDY</span>. 
Leave all defaults and press OK (you may also select the column of interest for event types). Alternatively, use
menu item <span style="color: brown">File > Import data > Using EEGLAB functions and plugins > Import MEF3 folder</span> to import the <i>mefd</i> 
folder located in the <i>ds003708/sub-01/ses-ieeg01/ieeg/</i> folder of the BIDS dataset.

When importing with BIDS, the advantage is that, along with the data, you will likely have access the iEEG electrode locations and relevant events. We show below the raw sEEG data for the unique subject in BIDS dataset <i>ds003708</i>.

![Screen Shot 2022-09-09 at 3 16 34 PM](https://user-images.githubusercontent.com/1872705/189453192-66169ca9-174b-419c-ba7b-2bada4cbda91.png)

Below the channel locations for the same dataset above are shown.

![Screen Shot 2022-09-09 at 3 16 56 PM](https://user-images.githubusercontent.com/1872705/189453262-e942a285-b19f-455e-aad0-b38bbc62d0dd.png)

Even if you are not planning to use EEGLAB to process iEEG data, importing your iEEG data into EEGLAB and resaving it into an EEGLAB dataset may be useful to process it in other software.

Other relevant resources for processing iEEG data:
- [Fieldtrip sEEG tutorial](https://www.fieldtriptoolbox.org/tutorial/human_ecog/)
- [MIA](http://www.neurotrack.fr/mia/) toolbox. Also accessible as a Brainstorm plugin.
