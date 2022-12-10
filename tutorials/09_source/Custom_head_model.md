---
layout: default
title: d. Custom head model
long_title: d. Using a custom head model
parent: 9. Source analysis
grand_parent: Tutorials
---
Better electrode location
===========================
The use of a custom head model may improve source localization. It is most important for MEG because 
MEG can usually not adapt a custom head model to match the individual subject head geometry. By contrast with
EEG, if we have scanned electrode position, these contain information about the subject's head geometry
and may be used to deform/adapt a template head model.

Therefore one should consider first to scan EEG electrode positions. Even without the subject's MRI, this
will greatly improve the accuracy of source localization because:
- We may deform the template head model to adapt to the subject head geometry
- The template electrode location (in the 10-20 system) differ greatly between manufacturers. My Fz may not be your Fz.
- Scanning electrode position has become easy and innexpensive with modern smartphone that contains 3-D scanners
(iPhone 13 pro, Samsung Galaxy S20 Ultra, etc...).  

We are actively developping solution to assist in 3-D scanning of electrode position, and improve our 
[get_chanlocs plugin](https://github.com/sccn/get_chanlocs/wiki), itself based on a solution 
developped in [Fieldtrip](https://www.fieldtriptoolbox.org/tutorial/electrode/). Our goal is to provide
automated alignment solutions to simplify the identification of electrodes in 3-D scans.

![Screen Shot 2022-12-10 at 12 26 58 PM](https://user-images.githubusercontent.com/1872705/206874056-8a2e646e-aff5-4a8b-b342-292725f6ae88.png)

If you have scanned electrode position and wish to use them for source localization, you may follow the [DIPFIT settings](Model_Settings.md) tutorial.

Custom head model
=================
If you have the scanned electrode positions, and also happen to have the subjects' MRI, then you may build a custom head model. It is important to use the non-defaced MRI. Sometimes, the face of the subject will be removed from the MRI for privacy purposes. Such MRI may not be used to build a head model. The first reason is that it will not be possible to precisely select fiducials in the MRI as the nazion is often missing. The second reason is that you will not be able to extrac the surface for the face of the subject. These surfaces influence volume conduction. 

In this tutorial, we will use the popular Henson Wakeman dataset. The dataset is available [here](https://zenodo.org/record/7410278). It contains a single subject (even though it looks like the file for other subjects are present, they are empty). The head model generation 



The use of a custom head model may improve source localization. It is most important for MEG because 
MEG can usually not adapt a custom head model to match the individual subject head geometry. By contrast with
EEG, if we have scanned electrode position, these contain information about the subject's head geometry
and may be used to deform/adapt a template head model.

Therefore one should consider first to scan EEG electrode positions. Even without the subject's MRI, this
will greatly improve the accuracy of source localization because:
- We may deform the template head model to adapt to the subject head geometry
- The template electrode location (in the 10-20 system) differ greatly between manufacturers. My Fz may not be your Fz.
- Scanning electrode position has become easy and innexpensive with modern smartphone that contains 3-D scanners
(iPhone 13 pro, Samsung Galaxy S20 Ultra, etc...).  

We are actively developping solution to assist in 3-D scanning of electrode position, and improve our 
[get_chanlocs plugin](https://github.com/sccn/get_chanlocs/wiki), itself based on a solution 
developped in [Fieldtrip](https://www.fieldtriptoolbox.org/tutorial/electrode/). Our goal is to provide
automated alignment solutions to simplify the identification of electrodes in 3-D scans.
