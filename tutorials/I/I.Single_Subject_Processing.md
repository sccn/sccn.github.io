---
layout: default
title: I.Single subject data processing tutorial
permalink: /tutorials/single-subject
parent: Tutorials
has_children: true
has_toc: false
---

Single subject data processing
================================
This part of the tutorial is an introduction to basic EEGLAB functions and processing at the single-subject level. 

In addition to the tutorial sections below, you may want to watch these series of short videos (hosted on Youtube):
- [a general introduction to EEG signal processing and EEGLAB](https://www.youtube.com/playlist?list=PLXc9qfVbMMN2NksmDeqizCI1z5DJBlqC6)


<img align="center" width="200" height="200" src= "{{ site.baseurl }}/assets/images/ICAintro2.png">

 
- [an introduction to preprocessing EEG data](https://www.youtube.com/playlist?list=PLXc9qfVbMMN1ZS3sU2xT2hhfB5PAmuNae)

<img align="center" width="200" height="200" src= "{{ site.baseurl }}/assets/images/ICApreproc.png">


Here are the most common steps you might want to take when processing EEG data at the single subject level:

### Importing your data and associated events and channel location information:

- [Load data in EEGLAB](/tutorials/single-subject/loading-data-in-EEGLAB)
- [Import or check events data]()
- [Importe channel location](/tutorials/single-subject/channel-locations)

### Pre-processing data
- [Re-referencing](/tutorials/single-subject/preprocessing-tools.html#re-referencing-the-data)
- [Re-sampling](/tutorials/single-subject/preprocessing-tools.html#changing-the-data-sampling-rate)
- [Filtering](/tutorials/single-subject/preprocessing-tools.html#filtering-the-data)

### Visually rejecting bad channels and portions of data
- [Visually rejecting bad portion of data](/tutorials/single-subject/loading-data-in-EEGLAB#rejecting-data)
- [Inspecting channel spectra and scalp maps](/tutorials/single-subject/plotting-channel-spectra-and-maps)

### Epoch data 
- [Extracting data epochs](/tutorials/single-subject/extracting-data-epochs) 
- [Rejecting artefactual epochs]()
- [Selecting and comparing epochs for a single dataset](/tutorials/single-subject/selecting-data-epochs-and-comparing)

### Visualize epoch data measures (for a single data set)
- [plot ERPs](/tutorials/single-subject/data-averaging)
- [plot ERP image](/tutorials/single-subject/plotting-erp-images)

### Working with ICA decompistion
- [Running ICA decomposition](/tutorials/single-subject/decomposing-data-using-ICA)
- [Visually inspecting and removing ICA components](/tutorials/single-subject/inspecting-ica-comp.html)
-[Plotting components contribution to EEG data]( /tutorials/single-subject/working-with-ICA-components)

### Time-Frequency decomposition
- [Computing ERSP and ITC for channel and component data](/tutorials/single-subject/time-frequency-decomposition)