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
review how to use different types of statistics at the group level. For a complete introduction to robust statistics in EEG research, read this [the statistics theory](/tutorials/ConceptsGuide/statistics_theory.html) section of the tutorial or watch the series of short videos below. Click on the icon on the top right corner to access the list of videos in the playlist.

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

Use menu item <span style="color: brown">File → Load existing study</span> and select the *stern.study* file. After the *STUDY* is loaded in EEGLAB, precompute ERPs by selecting <span style="color: brown">Study → Precompute channel measures</span>. The following interface will pop up.



Select the checkbox *Remove ICA artifactual components pre-tagged in each dataset*, change the baseline to -200 to 0 as shown and press *OK*. 


In this tutorial, we will use an 14-subject animal/non-animal categorization task. The data in *STUDY* format is available [here](https://sccn.ucsd.edu/eeglab/download/animal_study.zip). See the [data visualization](/tutorials/10_Group_analysis/study_data_visualization_tools.html) section of the tutorial for more information about this dataset.

Select menu item <span style="color: brown">File</span> and press sub-menu item <span style="color: brown">Load existing study</span>. Select the tutorial file "animal.study" then press *Open*.

After loading the data, to review the *STUDY* design, use menu item <span style="color: brown">Study → Select/Edit study design</span>. The default design is to compare images containing *animals* with images containing *distrators*. Press *Ok* to close the window. 

Before plotting the channel measures, you must precompute
them using the <span style="color: brown">Study → Precompute channel measures</span> menu item as shown below. Select the *ERPs* checkbox and press *Ok*.

![px](/assets/images/studyprecomp1.png)

### Plot ERP statistics

Select menu item <span style="color: brown">Study → Plot channel measures</span>. 

![600px](/assets/images/studyplot5.png)

In the middle of the two list of channels, click on the
large *STATS* pushbutton. The following graphic interface pops up. Click on the *Compute 1st independent variable statistics* checkbox.
Note that, since if there were no second independent variable selected in
this study design, the *Compute 2nd independent variable statistics* would not
not available.

![image not found](/assets/images/Pop_statparams2.png)

Press *OK* then select channel "Fz" in the left columns
and press the *Plot ERPs* button in the same column. The following plot
appears. The last panel shows the actual p-values.

![image not found](/assets/images/Erp4.gif)

To set a threshold, call back the ERP parameter interface and set the
entry in the *Statistical threshold* edit box to <i>0.01</i>.







You may also click on the middle of the two *Plot ERPs* buttons on the
*Params* button. In this interface, check the option *Plot first
variable on the panel* as shown below.




![image not found](/assets/images/Pop_erpparamsnew1_1.png)



Press *OK*. Now click again *Plot ERPs*: the following figure pops up.



![image not found](/assets/images/Erp5.gif)




All of the plots above report parametric statistics. While parametric
statistics might be adequate for exploring your data, it is better to
use permutation-based statistics (see above) to plot final results. Call
back the graphic interface and select *Permutation* as the type of
statistics to use, as shown below. You may also correct for multiple
comparison using False Discovery rate.



![image not found](/assets/images/Pop_statparams3.png)




Below, we will use non-parametric statistics for all data channels.
Click on the *Sel. all* pushbutton in the channel selection interface,
and then push the *Plot ERPs* button. The shaded areas behind the ERPs
indicate the regions of significance.



![image not found](/assets/images/Erp6.gif)



Finally, for data channels (but not for component clusters) an
additional option is available to plot ERP scalp maps at specific
latencies. Using the ERP parameter graphic interface once again, enter
"200" as the time range (in ms) and under the drop down menu of *Multiple channels selection*  select
*Plot averaged topography over time range*:



![image not found](/assets/images/Pop_erpparams_new2_2.png)




Select all channels (or a subset of channels) and press the *Plot ERPs*
button. The following figure appears.



![image not found](/assets/images/Erp7.gif)




There are more options in Plotting Options gui we have not discussed --
they should be self-explantory:
 - the *Time range to plot* edit box allows
plotting a shorter time range than the full epoch. 

- the *Plot limits*
edit box allows setting fixed lower and upper limits to the plotted
potentials. 

- the *Display filter* edit box allows entering a
frequency (for instance 20 Hz) below which to filter the ERP. This is
only applied for the ERP display and does not affect computation of the
statistics. This option is useful when plotting noisy ERPs for single
subjects.

Note that a command line function, [std_envtopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_envtopo.m), can also

visualize cluster contributions to the grand mean ERP in one or two
conditions, and to their difference. 

For more details refer [this wiki description](/Chapter_08:_Command_line_STUDY_functions#Modeling_condition_ERP_differences_using_std_envtopo() "wikilink").

Options for computing statistics on and plotting results for spectrum, ITC and ERSP
------------------------------------------------------------------------------------

The graphic interfaces for both power spectral and ERSP/ITC measures are
similar to that used for ERPs and need not be described in detail. You
may refer to the relevant function help messages for more detail. 

The
same graphic interface is used by all measures to select options for
computing statistics.

### Computing statistics for studies with multiple groups and conditions


At the end,
we will show examples of more complex analyses involving 3 groups of
subjects and 2 conditions. We will also briefly describe the
characteristics of the function that performs the statistical
computations, and discuss how to retrieve the p-values for further
processing or publication.

This functionality is still under development. 

Although we believe it is
working properly, we are planning to update its graphic interface to
make it more understandable. The current interface shows the ANOVA
interaction term for groups and conditions along with marginal
statistics. In a near-future release we are planning to have users
select showing either the marginal statistics or the statistical main
effects and interactions. 

Here we show a plot obtained from a clinical
study on three patient groups of 16 subjects each in two experimental
conditions (KAN, representing responses to the appearance of Kaniza
triangles, and NONKAN, representing responses to the appearance of
inverted Kaniza triangles; result courtesy of Rael Cahn). Selecting only
condition statistics and plotting conditions on the same panel returns
the figure below.

Statistics on ICA component clusters
----
The same methods for statistical comparison apply both to component clusters and to groups of data channels. 

![image not found](/assets/images/Erp_condstat.gif)


## General Linear Modelling

The [LIMO toolbox](https://limo-eeg-toolbox.github.io/limo_meeg/) allows you to use general linear modelling approaches on your data within EEGLAB.

If you click on the icon on the top right corner you can see the list of all the videos in the playlist - select the second one for a practical introduction to using LIMO with EEGLAB:


<center><iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PLXc9qfVbMMN2Vrzte9ul3nrrG8AgB5OkU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe></center>