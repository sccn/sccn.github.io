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

If you have scanned electrode position and wish to use them for source localization, you may follow the [DIPFIT settings](Model_Settings.md) tutorial.
