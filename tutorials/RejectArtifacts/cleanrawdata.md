---
layout: default
title: b. Automated rejection
categories: artifact
parent: 6. Reject artifacts
grand_parent: Tutorials
---
Automated artifact rejection
-------------------

### Load the sample EEGLAB dataset

Select menu item <span style="color: brown">File</span> and press sub-menu item
<span style="color: brown">Load existing dataset</span>. Select the tutorial file "eeglab_data.set" which is distributed with
the toolbox, located in the "sample_data" folder of EEGLAB. Then press *Open*.

![Image:Pop_loadset.png]({{ site.baseurl }}/assets/images/Pop_loadset.png)

### Automated artifact rejection

<a href="https://github.com/sccn/clean_rawdata">Clean_rawdata</a> is an EEGLAB plugin installed by default with EEGLAB. It can remove both bad data channels and bad portions of data. Select menu item <span style="color: brown">Tools</span> and press sub-menu item
<span style="color: brown">Reject data using Clean Rawdata and ASR</span>.

![Image:pop_clean_rawdata_new.png]({{ site.baseurl }}/assets/images/pop_clean_rawdata_new.png)

There are several sections to this menu indicating different sequential processes:

<li>The top section is about high-pass filtering your data. By default this option is not selected since EEGLAB assumes that you might have filtered your data already. However, if this is not the case, you may select that option. The frequency limits indicate the transition bandwidth for the high pass filter (so 0.25 to 0.75 Hz indicate a high-pass filter at 0.5 Hz).</li>
<li>The second option deals with removing bad data channels. There are 3 methods to remove bad channels. Flat channels may be removed. Channels with large amount of noise may be removed based on their standard deviation, and channels which are poorly correlated with other channels may be removed. The threshold for channel correlation is set to 0.8. Note that channel rejection based on their correlation is performed differently if you have imported channels location (a different heuristic that takes into account channel location is used in case you have them - and we strongly advise to import channel location prior to performing automated artifact rejection).</li>
<li>The third section deals with rejecting bad portions of data using the Artifact Subspace Reconstruction (ASR) Algorithm. The full description of this algorithm is outside the scope of this tutorial. For more information, we refer to this <a href="broken link">Annex</a>. ASR may be used to correct bad portions of data or to simply remove them. For the purpose of offline EEG processing, we advise to simply remove them, which corresponds to the default options. First, ASR finds calibration data - which are (very) clean portions of data and calculate standart deviation of PCA-extracted components (ignoring physiological EEG alpha and theta waves by filtering them out). Then it reject data based on a standard deviation threshold -- in this case 20 times the standard deviation of the calibration data. The lower this threshold, the more agressive the rejection is. The Riemanian distance is an experimental metric published in this <a href="https://www.frontiersin.org/articles/10.3389/fnhum.2019.00141/full">article</a> -- its claims are disputed by ASR author C. Kothe.</li>
<li>The fourth option deals with additional rejection of bad portions of data based on standard deviation of channels and number of bad channels flagged in a given time window. The time window size can be fine tuned when running the function from the command line. This allows rejecting bad portions of data that might not have been captured by ASR above.</li>
<li>The last option allow plotting results of the rejection with rejected data highlighted.</li>

The result of rejecting data on the tutorial dataset are shown below. We can see the rejected channels in red and the rejected data portion when all channels are marked as red in a given time segment. If correcting data using the ASR algorithm (not shown here), the old and new (corrected) data will be overlaid. The reason we do not recommend using the correction on pre-recorded data is that this functionality was developed for real-time applications. The effect of using ASR correction on EEG metrics remains unclear although several articles have been published on this subject.

![Image:pop_clean_rawdata_new2.png]({{ site.baseurl }}/assets/images/pop_clean_rawdata_new2.png)
