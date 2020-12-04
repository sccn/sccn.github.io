---
layout: default
title: I.12 Multiple Datasets
permalink: /tutorials/single-subject/multiple-datasets
parent: I.Single subject data processing tutorial
grand_parent: Tutorials
nav_order: 12
---

{ {Backward_Forward\|Chapter_11:_Timefrequency_decomposition\|(MT)
Chapter 11: Timefrequency
decomposition\|II.Multiple_subject_processing_tutorial\|II.Multiple
subject processing tutorial} }

Processing Multiple Datasets
----------------------------

Processing multiple datasets sequentially and automatically is important
for analysing data. While early versions of EEGLAB exclusively relied on
[command line scripting](/Chapter_02:_Writing_EEGLAB_Scripts "wikilink")
for processing multiple datasets, some automated processing is now
available directly from the EEGLAB graphic user interface (gui). To
explore this capability, you must first select several datasets. For
this section, we will use data from the [STUDY
tutorial](/Chapter_02:_STUDY_Creation "wikilink").

To work on multiple datasets at once, it is first necessary to select
them. To do so, use menu item <font color=brown>Dataset \> Select
multiple datasets</font>


![200px]({{ site.baseurl }}/assets/images/Pop_multiple.gif)



As in the screen view above, select a few datasets. Note that the
behavior of EEGLAB will differ depending on your optional settings under
<font color=brown>File \> Save memory</font>. If you allow only one
dataset to be present in memory at a time (see [Memory
options](/A3:_Maximizing_Memory "wikilink") for more details), existing
datasets will be automatically overwritten *on disk*. However, if you
allow all datasets to be present in memory simultaneously, only the
datasets in memory will be overwritten and their copies in disk files
will not be affected (you may then select menu item
<font color=brown>File \> Save current dataset(s)</font> to save all the
currently selected datasets).

EEGLAB functions available through the EEGLAB menu that can process
multiple datasets can be seen in the <font color=brown>Tools</font>
menu. When there are multiple current datasets, menu items unable to
process multiple datasets are disabled. Currently (v6.x-), functions
that can process multiple datasets include functions that resample the
data, filter the data, re-reference the data, remove channel baselines,
and run ICA. If all the datasets have the same channel locations, you
can also locate equivalent dipoles for independent components of
multiple datasets.

All available tools process data in a similar way. Upon menu selection,
a menu window pops up (identical to the single dataset window) in which
you may select processing parameters that are then applied to all the
datasets. If the dataset copies on disk are overwritten (under the
only-one-set-in-memory option), then a warning window will appear. For
example, selecting the <font color=brown>Tools \> Change sampling
rate</font> menu item pops up the following interface.


![150px]({{ site.baseurl }}/assets/images/Pop_resample.gif)



To resample all datasets at 125 Hz, enter 125 then *OK*. If the current
datasets have to be resaved to disk (because at most one dataset can be
present in memory), the following warning window appears:


![375px]({{ site.baseurl }}/assets/images/Confirm_multiple.gif)



The graphic interface for running ICA is a bit more elaborate. Select
menu item <font color=brown>Tools \> Run ICA</font>. The following
window will appear.


![475px]({{ site.baseurl }}/assets/images/Pop_runicamultiple.gif)



The statistical tools in EEGLAB for evaluating STUDY condition, session,
and group measure differences assume that datasets for different
conditions recorded in the same session share the same ICA
decomposition, i.e. the same independent component maps. By default, {
{File\|pop_headplot.m} } will concatenate STUDY datasets from the same
subject and session. For example, you may have several datasets time
locked to different classes of events, constituting several experimental
conditions per subject, all collected in the same session with the same
electrode montage. By default (leaving the lowest check-box checked), {
{File\|pop_headplot.m} } will perform ICA decomposition on the
concatenated data trials from these datasets, and will then attach the
same ICA unmixing weights and sphere matrices to each dataset.
Information about the datasets selected for concatenation will be
provided on the Matlab command line before beginning the decomposition.
</font>

In some cases, concatenating epoched datasets representing multiple
conditions collected in the same session may involve replicating some
portions of the data. For example, the pre-stimulus baseline portion of
an epoch time locked to a target stimulus may contain some portion of an
epoch time locked to a preceding nontarget stimulus event. Infomax ICA
performed by { {File\|pop_headplot.m} } and { {File\|pop_headplot.m} }
does not consider the time order of the data points, but selects time
points in random order during training. Thus, replicated data points in
concatenated datasets will only tend to be used more often during
training. However, this may not bias the forms of the resulting
components in other than unusual circumstances.


Some other blind source decomposition algorithms such as {
{File\|pop_headplot.m} } do consider the time order of points in brief
data windows. The version of the { {File\|pop_headplot.m} } function
used in EEGLAB has been customized to avoid selecting data time windows
that straddle an epoch boundary. To apply { {File\|pop_headplot.m} } to
concatenated datasets, however, the epoch lengths of the datasets are
assumed to be equal.
If you wish (and have enough computer RAM), you may also ask {
{File\|pop_headplot.m} } to load and concatenate all datasets before
running ICA. This will concatenate all the datasets in you computer main
memory, so you actually need to have enough memory to contain all
selected datasets. We do not recommend this approach, since it tacitly
(and unreasonably) assumes that the very same set of brain and non-brain
source locations and, moreover, orientations, plus the very same
electrode montage exist in each session and/or subject.


After ICA decomposition of all selected datasets, you may use menu item
<font color=brown>File \> Create Study \> Using all loaded
datasets</font> to create a study using all loaded datasets (if you only
want to use the dataset you selected, you will have to remove the other
datasets from the list of datasets to include in the STUDY). Using a
STUDY, you may cluster ICA components across subjects. See the [multiple
subjects processing
tutorial](/II.Multiple_subject_processing_tutorial "wikilink") for more
details.

Concluding remark on data tutorial
----------------------------------

This tutorial only gives a rough idea of the utility of EEGLAB for
processing single-trial and averaged EEG or other electrophysiological
data, the analyses of the sample dataset(s) presented here are by no way
definitive. One should examine the activity and scalp map of each
independent component carefully, noting its dynamics and its
relationship to behavior, and to other component activities, to begin to
understand its role and possible biological function.

Further questions may be more important: How are the activations of
pairs of maximally independent components inter-related? How do their
relationships evolve across time or change across conditions? Are
independent components of different subjects related, and if so, how?
EEGLAB is a suitable environment for exploring these and other questions
about brain dynamics.

In the next tutorial, we show more about how to import data and events
into EEGLAB datasets.

[Category:I.Single subject data processing
tutorial](/Category:I.Single_subject_data_processing_tutorial "wikilink")
{ {Backward_Forward\|Chapter_11:_Timefrequency_decomposition\|(MT)
Chapter 11: Timefrequency
decomposition\|II.Multiple_subject_processing_tutorial\|II.Multiple
subject processing tutorial} }
