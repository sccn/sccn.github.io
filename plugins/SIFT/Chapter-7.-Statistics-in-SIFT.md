---
layout: default
title: SIFT
long_title: SIFT
parent: SIFT
grand_parent: Plugins
---
When making inferences about information flow or causation in the neural
systems, it is highly important to also produce confidence intervals and
statistical significance thresholds for the estimator. The most common
statistical tests used in neural system identification are listed in
the table below. Statistical routines in SIFT are designed to address one or
more of these three tests and currently fall under two main categories:
non-parametric surrogate statistics, and asymptotic analytic statistics.



*Table caption. Common statistical tests. Here C(i,j) is
the measured information flow from process *j* to process *i*.
C<sub>null</sub> is the expected measured information flow when there is
no true information flow, C<sub>base</sub> is the expected information
flow in some baseline period.*

|                                                  |                                                                                                |                                    |
|--------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------|
| Test                         | Null Hypothesis                                  | What question are we addressing?                                                               | Applicable Methods                 |
| **<img src="https://latex.codecogs.com/svg.latex?{ {H}_{null} }">**                          | Is there significantly non-zero information flow from process *j* to *i* ?         | Phase randomization Analytic tests |
| **<img src="https://latex.codecogs.com/svg.latex?{ {H}_{base} }">**       | Is there a difference in information flow relative to the baseline?                            | Bootstrap resampling               |
| **<img src="https://latex.codecogs.com/svg.latex?{ {H}_{AB} }">** | Is there a difference in information flow between experimental conditions/populations A and B? | Bootstrap resampling               |

## 7.1. Asymptotic analytic statistics

In recent years, asymptotic analytic tests for non-zero information flow
*(H<sub>null</sub>)* at a given frequency have been derived and
validated for the PDC, rPDC, and DTF estimators (Schelter et al., 2005;
Eichler, 2006b; Schelter et al., 2009). These tests have the advantage
of requiring very little computational time, compared to surrogate
statistics. However, these tests are also based on asymptotic properties
of the VAR model, meaning they are *asymptotically* accurate and may
suffer from inaccuracies when the number of samples is not very large or
when assumptions are violated. Nonetheless, these tests can provide a
useful way to quickly check for statistical significance, possibly
following up with a more rigorous surrogate statistical test. These
tests are implemented in SIFT’s **`stat_analyticStats()`** function. To
our knowledge, SIFT is the only publically available toolbox that
implements these analytic tests.

## 7.2. Nonparametric surrogate statistics

Analytic statistics require knowledge of the probability distribution of
the estimator in question. When the distribution of an estimator is
unknown, nonparametric surrogate statistical methods may be used to test
for non-zero values or to compare values between two conditions.
Surrogate statistical tests utilize surrogate data (modified samples of
the original data) to empirically estimate the expected probability
distribution of either the estimator or a *null distribution*
corresponding to the expected distribution of the estimator when a
particular null hypothesis has been enforced. Two popular surrogate
methods are **bootstrap resampling and phase
randomization.** These
tests are implemented in SIFT’s **`stat_surrogateStats()`** function.

### 7.2.1. Bootstrap resampling

Bootstrap resampling (Efron and Tibshirani, 1994) approximates the true
distribution of an estimator by randomly resampling with replacement
from the original set of data and re-computing the estimator on the
collection of resampled data. This is repeated many (e.g., 200-2000)
times, and the value of the estimator for each resample is stored. When
the procedure terminates, we have an empirical distribution of the
estimator from which we can compute the expected value of the estimator,
obtain confidence intervals around the expected value, and perform
various statistical tests (t-tests, ANOVAs, etc.) to compare different
values of the estimator. It can be shown that, under certain conditions,
as the number of resamples approaches infinity, the bootstrap
distribution approaches the true distribution of the data. The
convergence speed depends largely on the nature of the data, but a rule
of thumb is that 250-1000 resamples are generally sufficient to produce a
reasonable estimate of the distribution. 

### 7.2.2. Phase Randomization

Phase randomization (Theiler, 1992) is a method for testing for non-zero
information flow in a dynamical system. The concept is quite simple: we
begin by constructing the expected probability distribution of the
estimator when the null hypothesis (no information flow) has been
enforced in the data. We call this the *null distribution.* An observed
value of the estimator is then compared to the quantiles of the null
distribution to obtain a significance level for rejection of the null
hypothesis for that value. Specifically, to generate our null
distribution we randomize only the phases of each time-series,
preserving the amplitude distribution. We then re-compute our estimator.
Repeating this procedure many times produces the desired null
distribution. Phase randomization should be implemented by
applying a fast-fourier transform (FFT) to obtain the complex power
spectrum, replacing the phases with those of a uniform random matrix,
and finally applying the inverse FFT to obtain our surrogate data
matrix. This procedure ensures that (a) the surrogate spectral matrix is
hermitian and (b) the real part of the surrogate spectrum is identical
to that of the original data. Since our frequency-domain information
flow estimators depend critically on the relative phases of the
multivariate time series, any observed information flow in the surrogate
dataset should be due to chance. Therefore, values of the estimator
greater than, say, 95% of the values in the null distribution should be
significant at a 5% level (p < 0.05). 

Importantly, the above tests (both analytic and surrogate) are only
pointwise significance tests, and therefore, when jointly testing a
collection of values (for example, obtaining p-values for a complete
time-frequency image), we should expect some number of non-significant
values to exceed the significance threshold. As such, it is important to
correct for multiple comparisons using tests such as False Discovery
Rate (FDR) (Benjamini and Hochberg, 1995) using EEGLAB’s **`fdr()`** function. 

## 7.3. Practical statistics in SIFT

Once a model has been fit and connectivity estimates computed, we often
wish to compute statistics for the dataset. As discussed above, this can be achieved in SIFT using several approaches, including
asymptotic analytic tests (for PDC, RPDC, and DTF measures) and
surrogate statistics (bootstrapping, phase randomization). 

### 7.3.1. SIFT native functions

SIFT statistical functions are only available from the command line. Look at the help of these functions for how to use them. 

```matlab
% Analytic stats
EEG = pop_stat_analyticStats(EEG);

% Generate surrogate distribution 
EEG = pop_stat_surrogateGen(EEG);

% Compute stats on the surrogate distribution 
EEG = pop_stat_surrogateStats(EEG);
```

The **EEG.CAT.Stats** structure should store statistics computed by these functions and can be used by the **TimeFreqGrid**  and **Brainmovie** functions presented earlier. Look in the **SIFT/stats** folder for other functions that may compute statistics. Most of these functions are a work in progress and were never finished, so they were not included in the SIFT menu. 

### 7.3.2. Working with SIFT connectivity structure

Another current method to compute statistics is to export the connectivity matrices stored in the CAT substructure of the EEG dataset. On the MATLAB command line type:

```
>> EEG(1).CAT.Conn

ans = 

  struct with fields:

      winCenterTimes: [0.1992 0.2070 0.2148 0.2227 0.2305 0.2383 0.2461 0.2539 0.2617 0.2695 0.2773 0.2852 0.2930 0.3008 … ]
    erWinCenterTimes: [-0.8008 -0.7930 -0.7852 -0.7773 -0.7695 -0.7617 -0.7539 -0.7461 -0.7383 -0.7305 -0.7227 -0.7148 … ]
               freqs: [2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 … ]
                dims: {'var_to'  'var_from'  'freq'  'time'}
              dDTF08: [8×8×49×238 single]
                 Coh: [8×8×49×238 single]
                pCoh: [8×8×49×238 single]
                   S: [8×8×49×238 single]
```

The connectivity matrix in the **dDTF08** substructure, for example, is of size 8 components x 8 components x 49 frequencies x 238 time windows. Other substructures contain an array of frequencies and window centers.

### 7.3.2.1. Comparing post-stimulus connectivity to baseline

Bootstraping to compute confidence intervals remains relatively simple. You may randomly select data epochs and rerun the connectivity analysis multiple times.

**Important note:** You can look for effect using the simple thresholding method presented in the visualization section. However, computing significance of connectivity measures can take hours. This is also why it is only presented as a script. Be patient.

If you have followed the tutorial, you need not prepare the data, but if you have not, the following script will apply the analyses performed in the previous sections of the tutorial (you still need to import the data with EEGLAB and perform EEGLAB-based preprocessing presented in section 5.2).

```matlab
% prepare data
EEG = pop_pre_prepData(EEG, 'nogui', 'SignalType',{'Components'}, 'NormalizeData', {'Method' {'time'  'ensemble'} }, 'verb', 1);

% fit AR model
EEG = pop_est_fitMVAR( EEG, 'nogui', 'Algorithm', 'Vieira-Morf', 'ModelOrder', 15, 'WindowLength', 0.4, 'WindowStepSize', 0.01, 'verb', 1); 

% Compute connectivity
EEG = pop_est_mvarConnectivity( EEG, 'nogui', 'ConnectivityMeasures', {'Coh' 'S'}, 'freqs', [2:50], 'verb', 1); 
```

Then, we can compute bootstrap connectivity, repetitively selecting data trials in a random fashion and recomputing connectivity.

```matlab
% Bootstrap data trials and repeat 100 times, assuming you have already preprocessed data from the GUI
allCoh = cell(1,100);
parfor iAccu = 1:100
     EEGTMP = EEG(1);
     EEGTMP.CAT.srcdata = EEG(1).CAT.srcdata(:,:,ceil(rand(1,EEG(1).trials)*EEG(1).trials)); % randomly select data epochs
     EEGTMP = pop_est_fitMVAR( EEGTMP, 'nogui', 'Algorithm', 'Vieira-Morf', 'ModelOrder', 15, 'WindowLength', 0.4, 'WindowStepSize', 0.01, 'verb', 1); 
     EEGTMP = pop_est_mvarConnectivity( EEGTMP, 'nogui', 'ConnectivityMeasures', {'Coh' 'S'}, 'freqs', [2:50], 'verb', 1); 
     allCoh{iAccu} = EEGTMP.CAT.Conn.Coh;
end
cohConcat = cat(5, allCoh{:}); % concatenate along 5th dim
cohConcatBaselined = bsxfun(@minus, cohConcat, mean(mean(cohConcat(:,:,:,1:71,:),4),5); % 1 to 71 correspond to -1 to -0.25 seconds

% compute 95% confidence interval
ci = stat_surrogate_ci(cohConcat, 0.05, 'both');

% compute p-value (baseline bootstrap compared to 0) and correct for multiple comparisons using FDR
pVals = stat_surrogate_pvals(cohConcatBaselined, zeros(size(cohConcatBaselined,[1:4])), 'both');
pValsCorrected = fdr(pVals); % for info only. For FDR correction, we would need at least 1000 repetitions.
```

You may then plot the result using the following script. Below we are using the low-level function **vis_TimeFreqGrid** to plot the result, but if we place the statistics in the **EEG.CAT.Stats** sub-structure, we may also use the higher-level **pop_vis_TimeFreqGrid** function to do so.

```matlab
stats = [];
stats.alpha = 0.05;
stats.tail  = 'both';
stats.Coh.ci = ci;
stats.Coh.pval = pVals; % uncorrected
vis_TimeFreqGrid('EEG', EEG(1), 'Conn', EEG(1).CAT.Conn, 'MatrixLayout', {'Partial', 'UpperTriangle', 'Coh' 'LowerTriangle', 'Coh' 'Diagonal' 'S', 'AllColorLimits', 99.9  }, ...
   'baseline', [-1 -0.25], 'Thresholding', {'Statistics', 'ThresholdingMethod', 'pval'}, ...
   'nodelabels', { 'IC8' 'IC11' 'IC13' 'IC19' 'IC20' 'IC23' 'IC38' 'IC39' }, 'stats', stats);
```

<img width="1110" alt="Screen Shot 2023-08-26 at 9 31 05 AM" src="https://github.com/sccn/SIFT/assets/1872705/4b490066-ee57-42d8-b399-82bc86af33e4">

*Figure caption. Connectivity compared to baseline and masked for significance (uncorrected for multiple comparisons).*

### 7.3.2.2. Comparing two conditions

The data is prepared in the same way as above. This is to compare connectivity against the null hypothesis where the distribution of connectivity values comes from the same distribution (we thus fuse the data for both datasets and rebuild them by randomly pulling trials from the fused data).

```matlab
% Bootstrap data compare EEG(1) and EEG(2)
originalDiff = EEG(1).CAT.Conn.Coh - EEG(2).CAT.Conn.Coh; % this is the original difference
allTrials = cat(3, EEG(1).CAT.srcdata, EEG(2).CAT.srcdata); % concatenate all normalized trials
allCoh = cell(1,100);
parfor iAccu = 1:100
     allDataShuffled = shuffle(allTrials,3);
     EEGTMP1 = EEG(1); EEGTMP1.CAT.srcdata = allDataShuffled(:,:,1:EEGTMP1.trials); % randomly select data epochs
     EEGTMP2 = EEG(2); EEGTMP2.CAT.srcdata = allDataShuffled(:,:,EEGTMP1.trials+1:end); % Second dataset contains all the other epochs
     EEGTMP1 = pop_est_fitMVAR( EEGTMP1, 'nogui', 'Algorithm', 'Vieira-Morf', 'ModelOrder', 15, 'WindowLength', 0.4, 'WindowStepSize', 0.01, 'verb', 1); 
     EEGTMP2 = pop_est_fitMVAR( EEGTMP2, 'nogui', 'Algorithm', 'Vieira-Morf', 'ModelOrder', 15, 'WindowLength', 0.4, 'WindowStepSize', 0.01, 'verb', 1); 
     EEGTMP1 = pop_est_mvarConnectivity( EEGTMP1, 'nogui', 'ConnectivityMeasures', {'Coh' 'S'}, 'freqs', [2:50], 'verb', 1); 
     EEGTMP2 = pop_est_mvarConnectivity( EEGTMP2, 'nogui', 'ConnectivityMeasures', {'Coh' 'S'}, 'freqs', [2:50], 'verb', 1); 
     allCoh{iAccu} = EEGTMP1.CAT.Conn.Coh - EEGTMP2.CAT.Conn.Coh;
end
cohConcat = cat(5, allCoh{:}); % concatenate along 5th dim

% compute 95% confidence interval
ci = stat_surrogate_ci(cohConcat, 0.05, 'both');

% compute p-value (compared to no effect or 0) and correct for multiple comparisons using FDR
pVals = stat_surrogate_pvals(cohConcat, originalDiff, 'both');
pValsCorrected = fdr(pVals); % For illustration only, increase repetition to 1000 or more to use FDR in practice
```

We are plotting the difference below.

```matlab
stats = [];
stats.alpha = 0.05;
stats.tail  = 'both';
stats.Coh.ci = ci;
stats.Coh.pval = pVals; % uncorrected
EEGTMP = EEG(1); EEGTMP.CAT.Conn.Coh = originalDiff;
vis_TimeFreqGrid('EEG', EEGTMP, 'Conn', EEGTMP.CAT.Conn, 'MatrixLayout', {'Partial', 'UpperTriangle', 'Coh' 'LowerTriangle', 'Coh' 'Diagonal' 'S', 'AllColorLimits', 99.9  }, ...
   'baseline', [-1 -0.25], 'Thresholding', {'Statistics', 'ThresholdingMethod', 'pval'}, ...
   'nodelabels', { 'IC8' 'IC11' 'IC13' 'IC19' 'IC20' 'IC23' 'IC38' 'IC39' }, 'stats', stats);
```

![Screen Shot 2023-08-26 at 3 17 28 PM](https://github.com/sccn/SIFT/assets/1872705/1138b9a5-36d3-4d66-b7c7-3bd4e44c1032)

*Figure caption. Connectivity difference between correct and wrong conditions of the tutorial dataset thresholded for significance (uncorrected).*

The solution above will also generalize to ANOVA and other types of statistical plots. The TFCE (threshold-free cluster enhancement method) is less aggressive than FDR (false discovery rate) to correct for multiple comparisons. You may use *limo_tcfe* function to apply TFCE.

## 7.4. Group analysis in SIFT

Cognitive experiments are typically carried out across a cohort of
participants, and it is useful to be able to characterize differences in
brain network activity within and between groups of individuals for
different conditions. 

While such analysis is
relatively simple when performing analyses on scalp channels, it becomes
more complicated when estimating connectivity in the source domain
between dipolar IC processes. This is primarily due to the fact that it
is often difficult to equate IC sources between participants. While we
typically utilize clustering techniques to help equate dipolar sources
across participants, in some cases, a subset of participants will still
not exhibit one or more sources observed in all other
participants. If one does not take into account these *missing
variables*, one may risk obtaining biased estimates of the average
connectivity across the subject population. This missing variable
problem is well-known in statistics, and several approaches have been
proposed for dealing with this. 

Currently, group analysis in the source
domain is possible using two methods: disjoint clustering, which does
not take into account the missing variable problem, but may still be
useful for a general analysis, particularly if there is high agreement
across the cohort of datasets in terms of source location and a
Bayesian mixture model approach, which provides more robust statistics
across datasets. A brief description of these methods is provided below.

### 7.4.1. Disjoint Clustering

As mentioned above, users need to export connectivity matrices stored in the **EEG.CAT.Conn** structure and use external software to compute significance. 

This approach adopts a 3-stage process:

**1. Identify K ROI’s (clusters).** You may use affinity clustering of sources
across subject populations using EEGLAB’s Measure-Product clustering.

**2. Compute all incoming and outgoing individually statistically
significant connections between each pair of ROIs.** To do so, for each connection between 2 clusters, assess if it is significant across subjects, then create a \[ K X K
\[x freq x time \] \] group connectivity matrix. Some pairs of connections might have more subjects than others, and that's OK. Note that users may also build a large connectivity matrix for all subjects, replacing missing connections in some subjects with NaNs and then using LIMO to compute statistics (as LIMO can handle the NaNs).

**3. Visualize the results using any of SIFT's visualization routines.**
This method suffers from low statistical power when subjects do not have
high agreement in terms of source locations (missing variable problem).

### 7.4.2. Bayesian Mixture Model

A more robust approach (in development with Wes Thompson) uses smoothing splines and Monte-Carlo methods
for joint estimation of posterior probability (with confidence
intervals) of cluster centroid location and between-cluster
connectivity. This method takes into account the “missing variable”
problem inherent to the disjoint clustering approach and provides robust
group connectivity statistics. A poster was [published](https://sccn.ucsd.edu/~scott/pdf/Thompson_and_Mullen_Poster_ICONXI.pdf) on this topic, but the code is not yet available.

### 7.4.3. Group SIFT

[Group SIFT](https://github.com/sccn/groupSIFT) was developed by Makoto Miyakoshi and collaborators. Its validity has not been assessed by SIFT authors, so use it at your own risk.