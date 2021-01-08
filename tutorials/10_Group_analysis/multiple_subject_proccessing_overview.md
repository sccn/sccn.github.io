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
To explore the multiple-dataset processing functionality of EEGLAB, you must first load and select several datasets.

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
When there are multiple current datasets, menu items unable to
process multiple datasets are disabled. All available tools process data in a similar way. Upon menu selection,
a menu window pops up (identical to the single dataset window) in which
you may select processing parameters that are then applied to all the
datasets. 

Note that the behavior of EEGLAB will differ depending on your optional settings under
<span style="color: brown">File → Preferences</span>.

- If you allow only one
dataset to be present in memory at a time (see the [dataset management](/tutorials/03_Dataset_management/datasets.html) section of the tutorial sfor more details), existing
datasets will be automatically overwritten *on disk* (a warning window will appear).

- However, suppose you allow all datasets to be present in memory simultaneously. In that case, only the
datasets in memory will be overwritten, and their copies in disk files
will not be affected (you may then select menu item
<span style="color: brown">File → Save current dataset(s)</span> to save all the
currently selected datasets).

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

### Filter the datasets

The selected datasets are already processed and do not require additional processing. Nevertheless, we will simply filter them for illustrative purposes. Select the <span style="color: brown">Tools → Filter the data → Basic FIR filter</span> menu item. The following interface pops up. Enter *100* in the second edit box to low-pass filter the data below 100 Hz (this is half the 200 Hz sampling frequency and will not affect subsequent processing). Press *Ok*.

![](/assets/images/multisub5.png)

EEGLAB asks for confirmation, warning that the datasets will be automatically overwritten on disk. Select *Proceed*.

![](/assets/images/multisub4.png)

The datasets are filtered one by one and resaved on disk. All menu items mentioned previously work similarly.

### Apply ICA

Running ICA on multiple datasets is useful when you have two EEGLAB datasets for
two conditions from a subject that were collected in the same session
and want to perform ICA decomposition on their combined data. Using this
option, you do not have to concatenate the datasets yourself; EEGLAB
will detect that these two datasets belong to the same subject, merge them, run ICA, and save the (same) decomposition in each of the subject's datasets.

The graphic interface for running ICA is a bit more elaborate. Select
menu item <span style="color: brown">Tools \"> Run ICA</span>. The following
window will appear.


![](/assets/images/pop_runica_multiple.png)

By default, 
[pop_runica.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_runica.m)
 will concatenate datasets from the same
subject and session. For example, you may have several datasets time-locked to different classes of events, constituting several experimental
conditions per subject, all collected in the same session with the same
electrode montage. 
By default (leaving the lowest checkbox checked), 
[pop_runica.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_runica.m)  will perform ICA decomposition on the
concatenated data trials from these datasets, and will then attach the
same ICA unmixing weights and sphere matrices to each dataset.
Information about the datasets selected for concatenation will be
provided on the MATLAB command line before beginning the decomposition. Note that to apply [pop_runica.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_runica.m) to
concatenated datasets, the datasets' epoch lengths are
assumed to be equal.

If you wish (and have enough computer RAM), you may also ask 
[pop_runica.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_runica.m) to load and concatenate all datasets before
running ICA. We do not recommend this approach since it tacitly
(and unreasonably) assumes that the very same brain and non-brain
sources and the very same
electrode positions exist in each session and/or subject.

Multiple-subject selection and EEGLAB studies
---

After processing of all selected datasets, you may use menu item
<span style="color:brown">File → Create Study → Using all loaded datasets</span> to create a study using all loaded datasets (if you only
want to use the dataset you selected, you will have to remove the other
datasets from the list of datasets to include in the STUDY). See the [group analysis tutorial](/tutorials/10_Group_analysis/) for more details.

Note that you may also create a *STUDY* before processing datasets and then proceed to batch process them. Once a *STUDY* is created, all  *STUDY* datasets remain selected, and multi-subject processing menu items become available. See the [STUDY creation tutorial](/tutorials/10_Group_analysis/study_creation.html) on how to create a *STUDY*.

