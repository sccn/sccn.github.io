---
layout: default
title: ERP images 
permalink: /tutorials/IV.Appendix/erp_image_background.html
parent: IV.Appendix
grand_parent: Tutorials
---

Some background information on ERP images
==========================================

Here are some useful background information on ERP images. 

To learn how to construct ERP images please refer to the 
[tutorial](/tutorials/single-subject/plotting-erp-images).

The field of electrophysiological data analysis has been dominated by
analysis of 1-dimensional event-related potential (ERP) averages.
Various aspects of the individual EEG trials that make up an ERP may
produce nearly identical effects. For example, a large peak in an ERP
might be produced by a single bad trial, an across-the-board increase in
power at the same time point, or a coherence in phase across trials
without any noticeable significance within individual trials. In order
to better understand the causes of observed ERP effects, EEGLAB allows
many different *ERP image* trial-by-trial views of a set of data epochs.

ERP-image plots are a related, but more general 2-D (values at
times-by-epochs) view of the event-related data epochs. ERP-image plots
are 2-D transforms of epoched data expressed as 2-D images in which data
epochs are first sorted along some relevant dimension (for example,
subject reaction time, alpha-phase at stimulus onset, etc.), then
(optionally) smoothed (cross adjacent trials) and finally color-coded
and imaged. As opposed to the average ERP, which exists in only one
form, the number of possible ERP-image plots of a set of single trials
is nearly infinite -- the trial data can be sorted and imaged in any
order -- corresponding to epochs encountered traveling in any path
through the 'space of trials'. However, not all sorting orders will give
equal insights into the brain dynamics expressed in the data. It is up
to the user to decide which ERP-image plots to study. By default, trials
are sorted in the order of appearance in the experiment.

It is also easy to misinterpret or over-interpret an ERP-image plot. For
example, using phase-sorting at one frequency (demonstrated below) may
blind the user to the presence of other oscillatory phenomena at
different frequencies in the same data. Again, it is the responsibility
of the user to correctly weight and interpret the evidence that a 2-D
ERP-image plot presents, in light of to the hypothesis of interest --
just as it is the user's responsibility to correctly interpret 1-D ERP
time series.