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
also support importing BIDS formated MEG data. You may install plugins from the EEGLAB plugin manager (menu item <span style="color: brown">File > Manage EEGLAB extensions</span>). 

For example, after installing the MEF3 and BIDS-matlab-tools plugins, you may import the 
[ds003708 BIDS dataset]([https://openneuro.org/datasets/ds003708](https://nemar.org/dataexplorer/detail?dataset_id=ds003708&processed=0)). 
First download the data. Second, use menu item <span style="color: brown">File > BIDS Tools > Import BIDS folder to STUDY</span>. 
Leave all defaults and press OK (you may also select the column of interest for event types). Alternatively, use
menu item <span style="color: brown">File > Import data > Using EEGLAB functions and plugins > Import MEF3 folder</span> to import the <i>mefd</i> 
folder located in the <i>ds003708/sub-01/ses-ieeg01/ieeg/</i> folder of the BIDS dataset.

When importing with BIDS, the advantage is that you will likely have access the iEEG electrode locations. 
Below the raw sEEG and the channel location are shown for the dataset above.

