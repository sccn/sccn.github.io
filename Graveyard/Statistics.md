---
layout: default
---
Statistics discussion TO REDO AS Q/A

Below is a discussion between Robert Oostenveld, Guillaume Rousselet,
Tim Mullen and Arnaud Delorme about proper (advanced) statistical
methods. The discussion starts on using log or absolute values for
statistics and visualization and then deal with general statistical
guidelines.

### Testing for H1 instead of H0

<b>A. Delorme:</b> I have a question about the bootstrap H1 test
performed in the LIMO EEGLAB plugin. When I talk about this, people
usually have never heard about it -- they have heard about testing H0
(the null hypothesis) but not about testing H1 (the presence of an
effect). Also what is the relation between type I and type II error when
testing H0 compared to type I and type II error when testing H1?

<b>G. Rousselet:</b> Most tests in Wilcox's book (see end of this page)
assess H1, i.e. they are based on confidence intervals around the
effects. The goal remains to provide confidence intervals with high
power and type I error rate at the nominal level. In brain imaging we
are not so much interested in estimating H1, because people don't care
about effect sizes in my experience, but rather care about controlling
the type I error rate, which is best done by cluster statistics or the
new TFCE method (see end of this page). So in LIMO, H1 bootstrap is used
to provide confidence intervals around the effects, mostly for
illustrations. Beyond controlling the type I error, I think we should
look at effect sizes more carefully. I've been working on porting some
of Wilcox's R code to Matlab, with very interesting results - currently
working on a paper in which I apply non-parametric (robust and
informative!) measures of effect sizes to face and object ERPs. The new
tools will be released in LIMO eventually.

### Transforming data (taking the log in spectral decompositions)

<b>A. Delorme:</b> Another question. When computing spectrum of EEG/MEG
data, statistics (parametric or permutation) on averaged absolute
spectrum across subjects are not stable. This is because of outliers and
the fact that some subjects have much larger power than others.

In practice, we need to take the log of the spectrum for each subjects
before computing the stats. However, this account to taking the log of
the product of the subjects' spectrum. What do you make of that?

<b>R. Oostenveld:</b> If you have paired measurements (i.e. a baseline
and an active condition in each subject), then log transforming is not
required (although it still might help). So I don't disagree that it may
help, I do disagree with the statement "need to take".

Intermezzo: with MEG we have the same issues related to the source
activity that differs over subjects, but on top of that we have
between-subject differences that are due to some subjects simply sitting
closer or further away from the sensors in the MEG helmet.

Now continued:

If you want to perform statistical inference (i.e. a decision about a
H0) on the level of multiple subjects, that it often called a
second-level test. The first level is that of individuals (where you
have variance in your observations) and the second is at the group
(where you also have variance in your observations). What you do for the
2nd level is that you compute a summary measure for the 1st level and
base your 2nd level inference on that summary measure. That summary
measure is often the mean, which is a descriptive statistic. It is
descriptive because it describes something about the distribution(s) of
the data. Variance, median, skewness and many others descriptive
measures exist.

So I guess you are considering to take subject means and test them at
the group level to make an inference about the population from which you
sampled the group. I also guess that you are doing a paired test (i.e.
using the observation of the two conditions in each individual subject).

Rather than means, you can also take other 1st level descriptive
statistics into your 2nd level test. One that is often used in fMRI is
normalized regression coefficients (beta weights) from a GLM. Another
one that we use frequently is single-subject t-scores. Another one we
use often are average ratio's (i.e. the ratio between averages).

The 2nd level hypothesis for which you are stating the H0, computing the
probability and hopefully rejecting the H0 because the probability is
too small, is that of a difference of whatever descriptive (statistical)
measures you determined. So you can test whether the XXX is
significantly different, where for XXX you can fill in: mean, skewness,
ratio, .... If you use a paired t-test, then you are making the
assumption that the errors (the non-modelled variance) in XXX are
normally distributed. The assumption of normal distributions is one
potential issue (1). But let's first turn to another:

The problem (2) you run into with the single-subject-averaged power is
that power is non-uniformly distributed over subjects, hence the
increased variance of the subject-average-differences. That reduces the
statistical sensitivity. So the question is how to make the 1st level
statistics more uniform over subjects. Taking the log makes it slightly
more normal. Taking the ratio as 1st/subject level descriptive and
determining whether it is consistently different from 1 is another way
of conducting the test.

Depending on the descriptive measure, taking the log will improve the
statistical homogeneity (2) or uniformity. Taking the log might also
improve the normality of the non-modelled variance (1). In the case of
averaged power in each condition at the single-subject level, the log
does both. In the case of ratio A/B, the log also does both. Now think
of what happens with the log for the activity and baseline in one
subject:

log(A/B) = log(A) - log(B)

So testing the log-transform of the ratio's between power is the same as
testing the difference between log-transformed power. Consequently the
t-test (ttest in MATLAB) on log-ratio's is the same as a paired t-test
(ttest2 in MATLAB) on the log of the differences.

The interpretation of the 2nd level statistic does not change. You
compute the probablily of the null hypothesis that states: a) the mean
power over the two conditions is not different, or stated otherwise: the
mean-difference is not different from zero b) the log-transformed mean
power over the two conditions is not different (the mean-difference of
the low-transformed power is not different from zero) c) the ratio
between the two conditions is not different from 1 d) the log of the
ratio between the two conditions is not different from zero

a has the problem of non-normal errors and of inhomogeneity c has the
problem of non-normal errors b and d don't have these two problems. In
fact, they are mathematically the same, so the probabilities and H0s are
also identical.

Taking GLM betas, t-scores or another single subject measure to the 2nd
level is also fine (but keep in mind that the H0 and H1 pertain to the
single-subject statistic, so the inference might be slightly diferent).
So that is why the statement "you must take logs" does not always hold,
but for testing the difference in mean power it is indeed a good idea.

The consequence of taking the log and it representing power is something
I would not worry about. Statistical inference is about H0 something
being the same, or H1 something being different. What that "something"
is does not really matter too much (in general). There might be cases
where it does, but a monotonous transformation such as the log does not
change the inference obn the similarity or difference of the underlying
mean-power values. Or short: if the power is different, then log-power
is also different. And if teh power is the same, then log-power is also
the same. The probability of making these statements however is
different (due to the homogeneity and non-normal variance affecting the
test sensitivity).

<b>G. Rousselet</b>

A few thoughts:

In general, there is absolutely no guarantee that transforming your
data, log or other, will get rid of skewness problems. In some
situations a transformation can actually make things worse. In
psychophysics, people often log transform some of their data because
many measurements become linear after log transformations. So it makes
sense in that context. This is different from log transformation to
reduce skewness.

However, what most researchers forget when they interpret their results,
is that you can only conclude about what you have measured: so in your
case you should only conclude about differences in means of log
transformed data. Indeed, using other transformations, or no
transformations, and different estimators of different aspects of your
distributions might lead to different results. I find particularly
annoying when people don't get a significant effect and then conclude
that 2 conditions don't differ: because most people only test means,
they should not conclude about entire distributions.

As an alternative to log transformation, and according to Wilcox, a
bootstrap-t test can help alleviate skewness issues. If you have
outliers, a t-test on a trimmed mean might help boost your power (check
the LIMO EEG functions with 'yuen' in the name). You could also
normalise the results within subjects, as people do with single-neuron
recordings: because single-neurons can vary dramatically in their
maximum firing rates, group comparisons require normalisation. It would
seem fair to do the same with your subjects if they differ a lot in
their maximum power.

The median is a special case, it requires special adjustments. if the
tails of the distributions are a problem, outliers or not, a 20% trimmed
mean is a good choice in a lot of situations. the standard error of the
trimmed mean is computed by using the winsorised variance in the yuen
ttest - that's the name of the statistician who extended the ttest to
trimmed means. only drawback of trimmed means: they take time to compute
because you need to sort the values, so that makes for slower
bootstraps.

As Wilcox would say: it depends what you're trying to do. In his book,
there is a special technique handling medians for each sort of tests.
For a ttest equivalent, Wilcox does not recommend to use a 50% trimmed
mean, because 'As the amount of trimming approaches 0.5, Yuen's method
breaks down; the method for estimating the standard error becomes highly
inaccurate' - i.e. poor confidence intervals and poor control of type i
error rate. Instead, if there are no tied values, Wilcox suggest using
the McKean-Schrader estimates of the standard-error (page 159 of his
2012 book). No code is provided though. If there are tied values then it
seems only the percentile bootstrap works. When I compare medians at the
group level, I've settled on a percentile bootstrap of the harrell-davis
estimator of the 5th decile, which provides better median estimations in
some situations.

Anyway: whatever you do will need to be validated or at least you need
to warn users that you cannot make universal recommendations. Also, with
small samples most techniques will be inappropriate. How small i don't
know.

<b>A. Delorme</b>: Thanks Guillaume, what kind of special adjustment
does the median require?

<b>G. Rousellet</b>: As Wilcox would say: it depends what you're trying
to do. In his book, there is a special technique handling medians for
each sort of tests. For a ttest equivalent, Wilcox does not recommend to
use a 50% trimmed mean, because 'As the amount of trimming approaches
0.5, Yuen's method breaks down; the method for estimating the standard
error becomes highly inaccurate' - i.e. poor confidence intervals and
poor control of type i error rate. Instead, if there are no tied values,
Wilcox suggest using the McKean-Schrader estimates of the standard-error
(page 159 of his 2012 book). No code is provided though. If there are
tied values then it seems only the percentile bootstrap works. When I
compare medians at the group level, I've settled on a percentile
bootstrap of the harrell-davis estimator of the 5th decile, which
provides better median estimations in some situations.

Anyway: whatever you do will need to be validated or at least you need
to warn users that you cannot make universal recommendations. Also, with
small samples most techniques will be inappropriate. How small i don't
know.

<b>T. Mullen</b>: I often recommend yuen t-tests to people as well (and
point to LIMO). However, in cases where the number of observations is
already quite low, removing 10-20% of the data may have undesirable
effects on statistical power. The reduction in variance may increase
effect size and thus power, but the reduced sample size may outweigh
these benefits...do you still advise this approach under small-sample
conditions?

About Guillaume's sentence "In general, there is absolutely no guarantee
that transforming your data, log or other, will get rid of skewness
problems". I agree -- and disagree. I fully agree that
log-transformations cannot be used "in general" to eliminate skewness
and, if used inappropriately, can make things worse. However, if a
distribution is log-normal, than by definition, taking the log is
guaranteed to produce a normal distribution with zero skewness. The
log-normal distribution has (positive) skewness given by: (exp(sigma^2)
+ 2) \* sqrt(exp(sigma^2) - 1). Since our random variables of interest
have asymptotic chi^2 distributions, which can be approximated by
log-normal distributions (i.e. Jouini et al, 2011
<http://bit.ly/Q4rD9C>), should we not assume that the log will at least
reduce skewness? Since I'm lazy and don't want to bother with proofs on
a saturday, I tried a quick empirical test: I generated 10K random
samples from a chi^2 distribution for varying degrees of freedom
(1-300). For each d.o.f I checked skewness and 'normality' (as measured
by the Lilliefors test statistic) for both original and log-transformed
data. Results are plotted below. On average, the log transformation
reduces skewness by a factor of 2. Excess kurtosis is also reduced for
d.o.f.\<50 (not shown). The Lilliefors test statistic for rejecting the
null hypothesis of normality is likewise reduced by about a factor of 2.
The impact of the log transform is most pronounced for fewer d.o.f., as
expected, since Chi2(V) --\> Norm(0,1) as V --\> Inf.

<b>G. Rousselet</b>: So as long as you are clear that your
recommendations apply only to this context, then i have no objections.
You just don't want people to start messing about with log or other
transforms in the hope that they will get a significant effect. People
will do that anyway, it's out of your control.

<b>G. Rousselet</b>: I was thinking of group analyses, in which few
subjects with strong power across conditions would increase
inter-subject variance and therefore decrease power. You could normalise
within subjects, by the max mean power across all frequencies and
conditions - assuming you have one mean value for every frequency and
condition. That way the results of each subject would be expressed
between 0 and 1, but you preserve the within-subject variance.

In my experience, and from reading Wilcox, with small samples everything
falls apart. In that case, the key is probably to describe your data
faithfully, for instance by showing each subject, without trying to make
big claims about the brain in general.

<i>References from G.Rousselet</i>

[Multivariate measures of
location](http://projecteuclid.org/DPubS?service=UI&version=1.0&verb=Display&handle=euclid.ss/1215441287)

[Cluster method derived from fMRI
analysis](http://www.ncbi.nlm.nih.gov/pubmed/23123297)

[Wilcox reference
book](http://www.amazon.com/Introduction-Estimation-Hypothesis-Statistical-Modeling/dp/0127515429/ref=la_B000APCI5U_1_3?ie=UTF8&qid=1353092305&sr=1-3)