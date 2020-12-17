---
layout: default
title: a. Statistics Theory
categories: concepts
parent: Statistics
grand_parent: Tutorials
---

Some statistical theory
==============================

Computing statistics is essential to observation of group, session,
and/or condition measure differences. EEGLAB allows users to use either
parametric or non-parametric statistics to compute and estimate the
reliability of these differences across conditions and/or groups.
Here we describe some essential concepts behind the statistical methods implemented
in EEGLAB. 

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

We suggest consulting a relevant statistics book for more details: An
introduction to statistics written by one of us (AD) is available
[here](http://sccn.ucsd.edu/~arno/mypapers/statistics.pdf). 

A good
textbook on non-parametric statistics is the text book by Rand Wilcox,
["Introduction to robust estimation and hypothesis testing"](https://www.sciencedirect.com/book/9780123869838/introduction-to-robust-estimation-and-hypothesis-testing).

