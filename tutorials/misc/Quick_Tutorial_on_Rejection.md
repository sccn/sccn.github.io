---
layout: default
title: Quick rejection tutorial
parent: Reference Topics
grand_parent: Tutorials
nav_order: 12
---
A quick tutorial on ICA artifact rejection <span style="color: green">- DONE</span>
====================
{: .no_toc }

EEGLAB is a powerful tool for eliminating
several important types of non-brain artifacts from EEG data. EEGLAB allows the user to reject many such artifacts in an efficient and
user-friendly manner. This minimalist guide is for non-EEGLAB users to import their EEG data, reject artifacts, then export the data back to a software package of their choice. For more comprehensive documentation on using EEGLAB, refer to the main sections of the EEGLAB tutorial.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>


## 1. Start MATLAB and EEGLAB, then import your data
Type \>\> eeglab to start EEGLAB under MATLAB. 

Select menu item
<span style="color: brown">File → Import data</span> to import your data file
in any of a variety of file formats. See the [Import data](/tutorials/04_Import/Importing_Continuous_and_Epoched_Data) section for
more details.

Scroll and check data using menu item <span style="color: brown">Plot → Channel data (scroll)</span>.

## 2. Import a channel location file

Importing a channel location file is critical for visualizing the
independent components of your data. Select <span style="color: brown">Edit → Channel locations</span> menu item.

- Solution 1. If channel labels are present in your dataset, EEGLAB will try to look up channel locations based on their labels. Simply press *Ok* to look up locations.

- Solution 2. If channel labels are not present, press the button *Read locations* in the bottom right corner of the channel edit window.
Press *Ok* after selecting the file and
then press *Ok* to have EEGLAB recognize the file format automatically
from the file extension. 

Press *Ok* in
the channel edit window to import the channel locations into EEGLAB.

To check that your channel locations have been imported correctly, use
menu item <span style="color: brown">Plot → Channel locations → By name</span>

## 3. Reject artifact-laden data

The quality of the data is critical for obtaining a good ICA
decomposition. ICA can separate out certain types of artifacts -- only
those associated with fixed scalp-map projections. 

These include eye
movements and eye blinks, temporal muscle activity, and line noise. ICA
may not be used to efficiently reject other types of artifacts -- those
associated with a series of one-of-a-kind scalp maps.

For example, if
the subject were to scratch their EEG cap for several seconds, the
result would be a long series of slightly different scalp maps
associated with the channel and wire movements, etc. Therefore, such
types of "non-stereotyped" or "paroxysmal" noise need to be removed by
the user before performing ICA decomposition.

You have two solutions to reject bad data:

- Automated solution: Select menu item <span style="color: brown">Tools → Reject data using Clean Rawdata and ASR</span>. Press the first checkbox to high pass filter the data and press *Ok*. A new window pops up to ask for a name
for the new dataset. Press *Ok*.

- Manual solution: 
> - To reject “noisy channels“ of either continuous or epoched data, select
menu item <span style="color: brown">Edit → select data</span>. 

> - To reject noisy portions of “continuous data”, select menu item
<span style="color: brown">Tools → Inspect/Reject data by eye</span>.
 Then mark noisy portions of continuous data for
rejection by dragging the mouse horizontally with the left button held
down. Press *Reject* when done. A new window pops up to ask for a name
for the new dataset. Press *Ok*.

## 4. Run ICA and reject artifactual components

Although optional, we advise re-referencing the data to average reference using the <span style="color: brown">Tools → Re-reference the data</span> menu item.

Use menu <span style="color: brown">Tools → Decompose data by ICA</span> to run the ICA
algorithm. To accept the default options, press *Ok*.

You then have two solutions to reject bad ICA components:

- Automated solution: 
> - Label components using the <span style="color: brown">Tools → Classify components using IClabel → Label components</span> menu item.
> - Classify components using the <span style="color: brown">Tools → Classify components using IClabel → Flag components as artifact</span> menu item.
> - Select menu item <span style="color: brown">Tools → Remove components</span>
to actually remove the selected component from the data.

- Manual solution:
> - Use menu <span style="color: brown">Tools → Reject data using ICA → reject component by maps</span> to select artifactual components. See the [Data
analysis (running
ICA)](/tutorials/06_RejectArtifacts/RunICA.html) tutorial for
more details.
> - Select menu item <span style="color: brown">Tools → Remove components</span>
to actually remove the selected component from the data.

See the [Data analysis (running
ICA)](/tutorials/06_RejectArtifacts/RunICA.html) tutorial for
more details and some hints on how to select artifactual components.

## 5. Further processing of and/or exporting the cleaned data

You may also apply a similar procedure to groups of datasets from the EEGLAB GUI, as explained in [this tutorial](/tutorials/10_Group_analysis/multiple_subject_proccessing_overview.html).

Your data has now hopefully been pruned of its major artifacts. You may now proceed with further EEGLAB processing. You may also choose to [export your data](/tutorials/misc/Exporting_Data.html) to the format of your choice.

