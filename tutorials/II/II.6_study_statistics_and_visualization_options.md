---
layout: default
title: II.6 Study Statistics and Visualization Options
parent: II.Multiple subject processing tutorial
grand_parent: Tutorials 
---


Study Statistics and Visualization Options
============================================

Computing statistics is essential to observation of group, session,
and/or condition measure differences. 

EEGLAB allows users to use either
parametric or non-parametric statistics to compute and estimate the
reliability of these differences across conditions and/or groups. The
same methods for statistical comparison apply both to component clusters
and to groups of data channels. 

Here, we will briefly
review, for each mean measure (ERP, power spectrum, ERPS, ITC), how to
compute differences accross the two conditions in a STUDY. At the end,
we will show examples of more complex analyses involving 3 groups of
subjects and 2 conditions. We will also briefly describe the
characteristics of the function that performs the statistical
computations, and discuss how to retrieve the p-values for further
processing or publication.

For a complete introduction to robust statistics in EEG research watch this serie of short-videos:

<a href="https://www.youtube.com/playlist?list=PLXc9qfVbMMN3M_CGqAOEIIOKhjTPS9T2n"><img align="center" width="400" height="400" src= "{{ site.baseurl }}/assets/images/yt_stats.png"></a>




Parametric and non-parametric statistics
-----------------------------------------
EEGLAB allows performing classical parametric tests (paired t-test,
unpaired t-test, ANOVA) on ERPs, power spectra, ERSPs, and ITCs. 
*Below, we will use channel ERPs as an example, though in general we recommend
that independent component ERPs and other measures be used instead. This
is because no data features of interest are actually generated in the
scalp, but rather in the brain itself, and under favorable circumstances
independent component filtering allows isolation of the separate brain
source activities, rather than their correlated mixtures recorded at the
scalp electrodes.*

For example, given 15 subjects' ERPs for two task or stimulus
conditions, EEGLAB functions can perform a simple two-tailed paired
t-test at each trial latency on the average ERPs from each subject. 

If there are different numbers of subjects in each condition, EEGLAB will
use an unpaired t-test. If there are more than two STUDY conditions,
EEGLAB will use ANOVA instead of a t-test. For mean power spectra, the
p-values are computed at every frequency; for ERSP and ITC
time/frequency transforms, p-values are computed at every time/frequency
point. See the sub-section on component cluster measures below to
understand how to perform statistical testing on component measures.

EEGLAB functions can also compute non-parametric statistics. The null
hypothesis is that there is no difference among the conditions. In this
case, the average difference between the ERPs for two conditions should
lie within the average difference between 'surrogate' grand mean
condition ERPs, averages of ERPs from the two conditions whose condition
assignments have been shuffled randomly. An example follows:

Given 15 subjects and two conditions, let us use
<span style="color: red"> a1, a2, a3 ... a15 </span>, the scalp
channel ERP values (in microvolts) at 300 ms for all 15 subjects in
the first condition, and <span style="color: green">b1, b2, b3, ... b15</span>,
 the ERP values for the second condition. 

 The grand average ERP condition difference is


>
<span style="color: blue">d</span> = mean(
(<span style= "color: red">a1</span>-<span style="color: green">b1</span>) +
(<span style= "color: red">a2</span>-<span style="color: green">b2</span>) + ... +
(<span style= "color: red">a15</span>-<span style="color: green">b15</span>) ).

Now, if we repeatedly shuffle these values between the two condition
(under the null hypothesis that there are no significant differences
between them), and then average the shuffled values,
>
<span style="color: blue">d1</span> = mean(
(<span style="color: green">b1</span>-<span style = "color: red">a1</span>) +
(<span style = "color: red">a2</span>-<span style="color: green">b2</span>) + ... +
(<span style="color: green">b15</span>-<span style = "color: red">a15</span>) ).
>
<span style="color: blue">d2</span> = mean(
(<span style="color: red">a1</span>-<span style="color: green">b1</span>) +
(<span style="color: green">b2</span>-<span style="color: red">a2</span>) + ... +
(<span style="color: red">a15</span>-<span style="color: green">b15</span>) ).
>
<span style="color: blue">d3</span> = mean(
(<span style="color: green">b1</span>-<span style="color: red">a1</span>) +
(<span style="color: green">b2</span>-<span style="color: red">a2</span>) + ... +
(<span style="color: red">a15</span>-<span style="color: green">b15</span>) ).
...

We then obtain a distribution of surrogate condition-mean ERP values
<i>dx</i> constructed using the null hypothesis (see their smoothed
histogram below). If we observe that the initial value <i>d</i> lies
in the very tail of this surrogate value distribution, then the
supposed null hypothesis (no difference between conditions) may be
rejected as highly unlikely, and the observed condition difference may
be said to be statistically valid or significant.




![Image:Statistics.gif](/assets/images/Statistics.gif)



Note that the surrogate value distribution above can take any shape and
does not need to be gaussian. In practice, we do not compute the mean
condition ERP difference, but its t-value (the mean difference divided
by the standard deviation of the difference and multiplied by the square
root of the number of observations less one). The result is equivalent
to using the mean difference. The advantage is that when we have more
conditions, we can use the comparable ANOVA measure. Computing the
probability density distribution of the t-test or ANOVA is only a
"trick" to be able to obtain a difference measure across all subjects
and conditions. It has nothing to do with relying on a parametric t-test
or ANOVA model, which assume underlying gaussian value distributions.
Note that only measures that are well-behaved (e.g., are not strongly
non-linearly related) should be processed by this kind of non-parametric
testing.

We suggest conculting a relevant statistics book for more details: An
introduction to statistics written by one of us (AD) is available
[here](http://sccn.ucsd.edu/~arno/mypapers/statistics.pdf). 

A good
textbook on non-parametric statistics is the text book by Rand Wilcox,
["Introduction to robust estimation and hypothesis testing"](https://www.sciencedirect.com/book/9780123869838/introduction-to-robust-estimation-and-hypothesis-testing).

Below we illustrate the use of these options on scalp channel ERPs,
though they apply to all measures and are valid for both scalp channels
and independent component (or other) source activity clusters.

Options for computing statistics on and plotting results for scalp channel ERPs
--------------------------------------------------------------------------------
Call again menu item <span style="color: brown">Study → Plot channel measures</span>. In the middle of the two list of channels, click on the
*STAT* pushbutton. The following graphic interface pops up:



![pop_stats param](/assets/images/Pop_statparams1.png)


Click on the *Compute 1st independent variable statistics* checkbox.
Note that, since if there were no second independent variable selected in
this study design, the *Compute 2nd independent variable statistics* would not
not available. 

Press *OK* then select channel "Fz" in the left columns
and press the *Plot ERPs* button in the same column. The following plot
appears. The last panel shows the actual p-values.



![image not found](/assets/images/Erp4.gif)




To set a threshold, call back the ERP parameter interface and set the
entry in the *Statistical threshold* edit box to <i>0.01</i>.



![image not found](/assets/images/Pop_statparams2.png)




You may also click on the middle of the two *Plot ERPs* buttons on the
*Params* button. In this interface, check the option *Plot first
variable on the panel* as shown below.




![image not found](/assets/images/Pop_erpparamsnew1.png)



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
"200" as the epoch latency (in ms) to plot.



![image not found](/assets/images/Pop_erpparamsnew2.png)




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


Note that a command line function, { {File\|std_envtopo.m} }, can also
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

Correcting for multiple comparisons and Fieldtrip statistics
-------------------------------------------------------------

When performing a large number of statistical inferences, it is
necessary to correct for multiple comparisons. For example, with a
statistical threshold at p\<0.05, by definition about 5% of the inferred
significant values will be false positives.

There are several methods for correcting for multiple comparisons.

-   <b>Bonferoni</b>: The most conservative method, the Bonferoni
    method, simply divides the p-value by the number of comparisons. For
    example, when computing ERSP time-frequency images of 100
    frequencies by 200 time points, the number of inferences is 20,000.
    To correct for multiple comparison at p\<0.05, a statistical
    threshold of 0.05/20000 = 0.0000025 should be applied. This method
    is quite conservative as, essentially, it assumes (erroneously) that
    each of the time/frequency point values is independent of the
    others.

<!-- -->

-   <b>Holms method</b>: The Holms method, also called Holms-Bonferoni
    method is not as conservative. Actual uncorrected p-values are
    sorted and, to assess whether a given p-value reaches the corrected
    threshold for multiple comparison, the lowest uncorrected p-value is
    compared to the Bonferoni statistical threshold of 0.05/20000. Next,
    the second lowest is compared to statistical threshold of
    0.05/(20000-1), etc. The highest uncorected p-value is compared to
    the uncorected threshold 0.05/(20000-19999)=0.05.

<!-- -->

-   <b>False Discovery Rate:</b> The False Discovery Rate (FDR) method
    is based on Holms correction. Under FDR, a common corrected
    threshold is applied to all p-values. This threshold is the last
    significant threshold calculated using Holms correction. For
    example, if the 511th strongest p-value is the smallest (and thus
    the last one in Holms correction) that is significant, this p-value
    is used as the corrected threshold for all uncorrected p-values.
    Note that under Holms correction, statistical assessment is
    performed independently for each p-value. Therefore, after sorting
    by p-value the 54th p-value might not be significant while the 55th
    might be. For FDR, the last <i>significant</i> p-value encountered
    during Holms correction is used as the corrected threshold for all
    measure dimensions (here, voxels).

Two other methods are made available using statistics routines written
for fieldtrip -- the max and cluster methods. The cluster method is now
widely been used. As it is the least conservative of all correction for
multiple comparison methods, it should be used with care. Note that
EEGLAB allows users to apply the cluster method to clusters of raw data
channels by automatically computing channel neighbor matrices -- though
we consider this to be less accurate and informative, in most cases,
than independent component clustering.

-   <b>Max method:</b> the max method is only available when using
    non-parametric (surrogate data-based statistics). At each iteration
    in computing a surrogate distribution of a time-frequency
    decomposition (for example), the maximum statistics accross all
    time-frequency points is considered. The surrogate distribution is
    compiled of these <i>maximum</i> statistics. The original statistics
    (for example, t-scores) at all time-frequency points are compared
    against this unique surrogate distribution (instead of each
    time-frequency point being compared to its corresponding surrogate
    distribution as in the other methods).

<!-- -->

-   <b>Cluster method:</b> The cluster method is also only available
    when using non-parametric (surrogate) statistics. It is an original
    method developed by [Oostenveld and
    Maris](http://fieldtrip.fcdonders.nl/references_to_implemented_methods#statistical_inference_by_means_of_permutation)
    and described in detail in the [Fieldtrip
    wiki](http://fieldtrip.fcdonders.nl/tutorial/eventrelatedstatistics#permutation_test_based_on_cluster_statistics).

### Computing statistics for studies with multiple groups and conditions

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



![image not found](/assets/images/Erp_condstat.gif)


