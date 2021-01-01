---
layout: default
title: e. Statistics
parent: 10. Group analysis
grand_parent: Tutorials 
has_toc: true
---

Study Statistics and Visualization Options
============================================
{: .no_toc }

Statistics are at the core of EEG analysis. Here, we will briefly
review how to use different types of statistics at the group level. For a complete introduction to robust statistics in EEG research, read [the statistics theory](/tutorials/ConceptsGuide/statistics_theory.html) section of the tutorial or watch the series of short videos below. Click on the icon on the top right corner to access the list of videos in the playlist.

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PLXc9qfVbMMN3M_CGqAOEIIOKhjTPS9T2n" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe></center>

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

Channel ERP statistics
--------------
EEGLAB allows users to use either
parametric or non-parametric statistics to compute and estimate the
reliability of these differences within *STUDY* designs. Below we illustrate the use of these options on scalp channel ERPs,
though they apply to all measures and are valid for both scalp channels
and independent component (or other) source activity clusters.

### Load tutorial data and precompute ERPs

For this tutorial we will use the [STERN STUDY](http://sccn.ucsd.edu/eeglab/download/STUDYstern.zip) (1.9 Gb). Please download the data on your computer. See the [STUDY design](/tutorials/10_Group_analysis/working_with_study_designs.html) section of the tutorial for more information about this dataset.

Use menu item <span style="color: brown">File → Load existing study</span> and select the *stern_3designs.study* file. After the *STUDY* is loaded in EEGLAB, precompute ERPs by selecting <span style="color: brown">Study → Precompute channel measures</span>. The following interface will pop up.

After loading the data, to review the *STUDY* design, use the <span style="color: brown">Study → Select/Edit study design</span> menu item. See the [STUDY design tutorial](/tutorials/10_Group_analysis/working_with_study_designs.html) for details on how to create these designs.

Before plotting the channel measures, you must precompute
them using the <span style="color: brown">Study → Precompute channel measures</span> menu item, as shown below.
- Select the checkbox *Remove ICA artifactual components pre-tagged in each dataset*
- Select the *ERPs* checkbox
- Change the baseline to -200 to 0 as shown below
- Press *Ok* 

![px](/assets/images/studystats1.png)

### 1-way ANOVA on ERP plots

Select menu item <span style="color: brown">Study → Plot channel measures</span>. Select channel *Oz* in the left column, as shown below.

![image not found](/assets/images/studystats03.png)

First, select a shorter time range for plotting ERPs. Press the *Params* button and enter a time range from -200 ms to 600 ms as shown below. Select the checkbox for plotting the first independent variable on the first panel. Press *Ok*.

![image not found](/assets/images/studystats04.png)

In the middle of the two lists of channels, click on the
large *STATS* pushbutton. The following graphic interface pops up. Click on the *Compute 1st independent variable statistics* checkbox.
Note that, since if there were no second independent variable selected in this study design, the *Compute 2nd independent variable statistics* would not be available. Select *Use permutation statistics* in the dropdown list for the type of statistics. *Parametric statistics* should be used for quick assessment only.  While parametric
statistics might be adequate for exploring your data, it is better to
use permutation-based statistics (see above) to plot final results. Select the False Discovery Rate (FDR) method in the dropdown list to correct for multiple comparisons. Enter *0.05* for the p-value threshold. Press *Ok*.

![image not found](/assets/images/studystats05.png)

Then press the *Plot ERPs* button on the right column. The following plot pops up, showing the ERPs for the three types of letter *ignore*, *memorize*, and *probe*. We observe a significant difference from about 450 ms to about 570 ms, indicated by the black bar under the ERP plots. We also observe transient significance in the baseline at about 100 ms.

![image not found](/assets/images/studystats06.png)

Let's try a different method to correct for multiple comparisons. Click on the *STATS* button again, and check the checkbox *Use Fieldtrip statistics*. Select *montecarlo/permutation* as the type of statistics and the cluster correction method to correct for multiple comparisons. Refer to the Fieldtrip documentation to tune the parameters for the cluster correction (use the defaults for now). Use also *0.05* for the statistics threshold. Press *Ok*.

![image not found](/assets/images/studystats07.png)

Then press the *Plot ERPs* button again on the right column. The region of significance is similar to the previous method, although the transient statistical difference in the baseline has disappeared.

![image not found](/assets/images/studystats08.png)

### 1-way ANOVA on ERP scalp topographies

Now let's plot the scalp topography in this time region. To do this, press again the *Params* button, and select the 150 to 300 ms time range. Select *Plot averaged topography over time* in the bottom panel and press *Ok*.

![image not found](/assets/images/studystats10.png)

Press the *STATS* button and select permutation statistics with FDR correction for multiple comparisons as shown below.

![image not found](/assets/images/studystats11.png)

Now press the *Sel all.* button in the right column to select all channels. Then press the *Plot ERPs* button. The following plot pops up. This plot shows the scalp topography from 150 ms to 300 ms and the p-value map (extreme right). The difference, in this case, seems driven by the probe condition. In the following section, we will look at the difference between the *ignore* and *memorize* letters.

![image not found](/assets/images/studystats12.png)

### 2-way ANOVA

Let's select the third design in the *STUDY* plotting interface as shown below. This design compares the *ignore* and *memorize* conditions under different memory loads (from 0 to 5). The [STUDY design](/tutorials/10_Group_analysis/working_with_study_designs.html) section of the tutorial describes how this design was created. Select also the *Oz* channel.

![image not found](/assets/images/studystats15.png)

Now press the *Params* button and change the plotting time range to -200 ms to 600 ms as shown below. Make also sure to select the option to *Plot channels individually*. Press *Ok*.

![image not found](/assets/images/studystats16.png)

Press *Plot ERPs* button. The plot below pops up.

![image not found](/assets/images/studystats17.png)

We will study significance over the scalp topographies in the 150 ms to 300 ms range as in the previous section. To do so, press the *Params* button and enter a time range from 150 ms to 300 ms as shown below. Make also sure to select the option to *Plot averaged topography over time*. Press *Ok*.

![image not found](/assets/images/studystats18.png)

Press the *STATS* button and both independent variables as shown below. Select permutation statistics with no correction for multiple comparisons. Press *Ok*.

![image not found](/assets/images/studystats19.png)

Press the *Plot ERPs* button again. The following plot pops up and shows an array of 2 x 5 scalp topographies for the 2 x 5 design (2 conditions *ignore* and *memorize* times 5 memory load conditions). The scalp topography on the bottom shows the p-value map across conditions (*ignore* vs. *memorize*). The scalp topography on the right shows the p-value map across memory loads. The scalp topography in the bottom right corner shows the p-value for the ANOVA interaction term between conditions and memory loads. In this case, there might be a trend for the memory load.

![image not found](/assets/images/studystats20.png)

We now select the *STATS* button again and add check the *FDR* correction for multiple comparisons checkbox (not shown). Press the *Plot ERPs* button again. As shown below, the p-value statistical maps are all green indicating no significance.

![image not found](/assets/images/studystats22.png)

Let's try the cluster method to correct for multiple comparisons. Press the *STATS* button again. Check the checkbox to compute statistics only on the first variable (Fieldtrip cannot perform 2-way ANOVAs only 1-way ANOVAs) and check the checkbox *Use Fieldtrip statistics*. Select *Montecarlo/permutation* as the type of statistics and the cluster correction method to correct for multiple comparisons. Press *Ok*.

![image not found](/assets/images/studystats23.png)

Press the *Plot ERPs* button, and the following plot appears, showing a statisticallly significant difference between the *ignore* and *memorize* conditions.

![image not found](/assets/images/studystats24.png)

To look at the marginal statistics, select the *STATS* button and check the checkbox to compute marginal statistics (only the upper panel of the GUI is shown below).

![image not found](/assets/images/studystats25.png)

Then press the *Plot ERPs* again. We see that the difference is mostly due to memory loads 0, 1 and 2.

![image not found](/assets/images/studystats26.png)

Note that the analysis above is preliminary at best. The fact that uncorrected significance was low for the comparison between conditions, then showed up as significant with the cluster analysis, indicate weakly significant regions. Based on the scalp topography for the cluster analysis, it is unclear if significance is below 0.05. You may retrieve the p-values from the command line, as explained in the [group analysis scripting tutorial](/tutorials/11_Scripting/command_line_study_functions.html).

In general, we advise focusing on reporting unambiguous results (significance below 0.005 after correction for multiple comparisons).

Statistics on spectra, ITC and ERSP
-------------------------------

The graphic interfaces for both power spectral and ERSP/ITC measures are
similar to those used for ERPs and need not be described in detail. You
may refer to the relevant function help messages for more detail. 

The
same graphic interface is used by all measures to select options for
computing statistics.


ICA component cluster statistics
----
The same methods for statistical comparison apply both to component clusters and to groups of data channels. 

The plotting interface is virtually identical for channels and ICA component clusters. In the channel plotting interface, the left column is used to plot grand averages, and the right column to plot individual subjects. Similarly, for clusters, the left column plots ICA clusters, and the right column plot individual components.

General Linear Modelling using LIMO
----
The [LIMO toolbox](https://limo-eeg-toolbox.github.io/limo_meeg/) allows you to use general linear modeling approaches on your data within EEGLAB. For more complex designs, one must use the LIMO plugin. For more information, refer to the [LIMO plugin documentation](https://github.com/LIMO-EEG-Toolbox/limo_meeg/wiki) and the [LIMO tutorial video series](https://www.youtube.com/embed/videoseries?list=PLXc9qfVbMMN2Vrzte9ul3nrrG8AgB5OkU).
