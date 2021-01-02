---
layout: default
title: a. Batch processing
parent: 10. Group analysis
grand_parent: Tutorials 
---
Batch processing of subjects' data
====
{: .no_toc }

In this tutorial, we introduce advanced elements of EEGLAB focused on processing multiple subjects. These topics
are recommended to successfully analyze large-scale
experiments, which go beyond single-subject analysis. 

In addition to reading this tutorial, you may want to watch the short video below on multiple subjects processing in EEGLAB:

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/-jL3PuHD3aY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

Load multiple datasets
----
In this tutorial, we will use a [5-subject experiment](http://sccn.ucsd.edu/eeglab/download/STUDY5subjects.zip) (450Mb). See the [STUDY creation tutorial](/tutorials/10_Group_analysis/study_creation.html) for more information on this data. 

After uncompressing the data archive, load one by one all the datasets in EEGLAB using the <span style="color: brown">File → Load existing dataset</span> menu item. When several datasets are in the same folder, they may be all selected and loaded in EEGLAB simultaneously, as shown below.

![](/assets/images/multisub1.png)

Select multiple datasets for processing
----

After importing all ten datasets, select the <span style="color: brown">Datasets → Select multiple datasets</span> menu item, as shown below.

![](/assets/images/multisub2.png)

The following GUI will pop up. Select all ten datasets and press *Ok*.

![](/assets/images/multisub3.png)

Perform batch processing
----
EEGLAB allows processing a collection of datasets, whether these datasets are organized in a *STUDY* or not.

You may now select any available menu item to process the selected datasets. A standard sequence to process raw datasets could be:
1. Remove unwanted channels using the <span style="color: brown">Edit → Select data</span> menu item.
1. Look up channel locations using the <span style="color: brown">Edit → Channel locations</span> menu item.
1. High-pass filter the data using the <span style="color: brown">Tools → Filter the data → Basic FIR filter</span> menu item.
1. Perform automated artifact rejection using the <span style="color: brown">Tools → Reject data using Clean Rawdata and ASR</span> menu item.
1. Re-reference the data using the <span style="color: brown">Tools → Re-reference the data</span> menu item.
1. Run independent component analysis using the <span style="color: brown">Tools → Decompose data by ICA</span> menu item.
1. Label components using the <span style="color: brown">Tools → Classify components using IClabel → Label components</span> menu item.
1. Classify components using the <span style="color: brown">Tools → Classify components using IClabel → Flag components as artifact</span> menu item.
1. Locate component equivalent dipoles using the <span style="color: brown">Tools → Locate dipoles using DIPFIT -> Head model and settings</span> menu item, and then the <span style="color: brown">Tools → Locate dipoles using DIPFIT -> Autofit</span> menu item.
1. Extract data epochs using the <span style="color: brown">Tools → Extract epochs</span> menu item.

The selected datasets are already processed and do not require additional processing. Nevertheless, we will simply filter them for illustrative purposes. Select the <span style="color: brown">Tools → Filter the data → Basic FIR filter</span> menu item. The following interface pops up. Enter *100* in the second edit box to low-pass filter the data below 100 Hz (this is half the 200 Hz sampling frequency and will not affect subsequent processing). Press *Ok*.

![](/assets/images/multisub5.png)

EEGLAB asks for confirmation, warning that the datasets will be automatically overwritten on disk. Select *Proceed*.

![](/assets/images/multisub4.png)

The datasets are filtered one by one and resaved on disk. All menu items mentioned previously work similarly.

For example, this is useful when you have two datasets for
two conditions from a subject that were collected in the same session,
and want to perform ICA decomposition on their combined data. Using this
option, you do not have to concatenate the datasets yourself; EEGLAB
will detect that these two datasets belong to the same subject, merge them, run ICA, and save the (same) decomposition in each of the subject's datasets.

Note that you may also create a *STUDY* and then proceed to batch process datasets. Once a *STUDY* is created, all  *STUDY* datasets remain selected and multi-subject processing menu items become available. See the [STUDY creation tutorial](/tutorials/10_Group_analysis/study_creation.html) on how to create a *STUDY*.
