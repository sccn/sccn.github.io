---
layout: default
parent: SIFT
grand_parent: Plugins
render_with_liquid: false

title: Chapter-5.3.-SIFT-preprocessing
long_title: Chapter-5.3.-SIFT-preprocessing
---
The first step in our pipeline is to pre-process the data. Select **SIFT > Pre-processing** to bring up the Preprocessing GUI. This can also be opened from the command-line using:

``` matlab
EEG = pop_pre_prepData(EEG)
```

The figure below shows the
GUI, set to the options we will be using for this example. For most
GUIs, help text for each menu item appears in the **Help Pane** at the
bottom of the GUI when the menu item is selected. The **VerbosityLevel** determines how much information SIFT will
communicate to the user, via command-window or graphical output,
throughout the remaining pipeline (0=no (or minimal) command-window
output, 1=full command-window output, 2=command-window and graphical
(progress-bars, etc) output). The **Data Selection** group contains
options for selecting ICs and re-epoching the data. The **Filtering**
group contains options for downsampling the data, filtering,
differencing and linear detrending. **Normalization** (removal of mean
and division by standard deviation) can be performed across the
ensemble (i.e., trials), across time, or both (first temporal then ensemble
normalization). For our example, we will use the options shown in the figure
and table below:



<table>
<tbody>
<tr class="odd">
<td><p>Option</p></td>
<td><p>Value</p></td>
</tr>
<tr class="even">
<td><p><strong>Verbosity Level</strong></p></td>
<td><p><strong>2</strong></p></td>
</tr>
<tr class="odd">
<td><p><strong>NormalizeData</strong></p></td>
<td><p><strong>checked</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>Method</strong></p></td>
<td><p><strong>time;ensemble.</strong></p></td>
</tr>
</tbody>
</table>



![Screen Shot 2023-08-24 at 10 38 56 PM](https://github.com/sccn/SIFT/assets/1872705/b9cdc357-b413-419c-982c-f1b8b81a0765)

*Figure 9 Preprocessing GUI. Accessible through pop_pre_prepData().*

Once these options have been input, click **OK**. Both datasets will be
pre-processed using these settings, and you will be prompted to create a
new dataset(s) or overwrite the current datasets. Check “Overwrite” and
click OK.

The same may be achieved from the command line using the following command. Look at the function help and the function GUI above for more information on the allowable parameters.

```matlab
EEG = pop_pre_prepData(EEG, 'nogui', 'SignalType',{'Components'}, ...
        'NormalizeData', {'Method' {'time'  'ensemble'} }, 'verb', 1);
```

SIFT currently allows the user access to the following pre-processing options:
1. Component selection (command line call only)</p>
2. Epoching (command line call only)
3. Filtering (command line call only)
4. Downsampling
5. Differencing
6. Detrending
7. Normalization

The first three preprocessing steps can also be performed from EEGLAB prior to starting SIFT, as we did in the previous section. Preprocessing steps 5, 6, and 7 can only be performed using the SIFT preprocessing function described above.

### 5.3.1. Component selection

Ideally, one should fit a multivariate causal model to <em>all</em> available variables. This helps reduce the chances of false positives in connectivity (e.g., spurious causation) due to exogenous causal influences from excluded variables – i.e., “non-brain” components (Schelter et al., 2006; Pearl, 2009). However, increasing the number of variables also increases the number of parameters that we must estimate using a VAR model. For example, if we wish to fit a VAR model of order <em>p</em>, increasing the number of variables from <em>M</em> to <em>M</em>+1 requires us to estimate (2<em>M</em> + 1)<em>p</em> additional parameters. This, in turn, increases the minimal amount of data we need to adequately fit our model (see the discussion on Window Length in section 6.6.1. ). Thus, when limited data is available, it is often necessary to fit our models to a subset of relevant variables (about 10).

Variables can be selected using several approaches. One approach is to estimate the partial coherence between all variables using a non-parametric method (e.g., FFTs, or wavelets) and then only keep those variables that show significant partial coherence with at least one other variable. If one is working with ICA components, another (possibly complementary) approach is to select only a subset of ICs that are clearly related to brain activity. This can be performed manually (Onton and Makeig, 2009) or with the assistance of automation tools such as ADJUST (Mognon et al., 2010). The validity of this approach relies on the (rather strong) assumption that ICA has effectively removed all non-brain activity from brain components, such that there is no shared information between variables in the preserved set and those excluded from the set. See (Fitzgibbon et al., 2007; Onton and Makeig, 2009) for discussions on the topic. Both approaches can be performed using standard EEGLAB routines, as documented in the EEGLAB Wiki. In practice, one should apply a combination of these two approaches, selecting the largest subset of partially coherent ICs that will afford an adequate model fit given the amount of data available while giving the highest priority to those ICs that likely arise from brain sources and which demonstrate significant partial coherence with one or more other “brain” ICs.

Sparse VAR estimation methods generally obviate the need to select variables by imposing additional sparsity constraints on the model coefficients. Although we may have a large number of variables and, therefore, a large number of coefficients to estimate, we assume that only a small subset of the coefficients are non-zero at any given time, effectively decreasing the amount of data required to obtain unbiased coefficients estimates (Valdés-Sosa et al., 2005; Schelter et al., 2006). Sparse methods are not currently implemented in SIFT. 

### 5.3.2. Epoching

We have selected shorter epochs in a previous section. This simply allows the user to analyze a subset of the original epochs. When using a sliding-window AMVAR modeling approach with a window length of <em>W</em> seconds, if one wishes to analyze time-varying connectivity from T1 to T2 seconds, he should choose his epoch length to be T1-0.5<em>W</em> to T2+0.5<em>W</em> seconds. This is because the connectivity estimate at time <em>t</em> will correspond to the connectivity over the <em>W</em>-second window <em>centered at time t</em>. Thus, the earliest timepoint for which we will have a connectivity estimate is T1+0.5<em>W</em>, where T1 denotes the start of the epoch.</p>

### 5.3.3. Filtering

We chose not to filter the data since it was already filtered when we imported it. However, filtering can be a useful pre-processing step if the data contains low-frequency drift or pronounced artifacts in one or more frequency bands. Removal of drift (trend) can dramatically improve data stationarity and, thereby, the quality of a VAR model fit. Since the relative phases of each time series are a key element in information flow modeling, it is critical to apply a zero-phase (acausal) filter, which introduces no phase distortion. Filtering is performed using EEGLAB’s <strong><code>eegfilt()</code></strong> function. This, in turn, calls <strong><code>filtfilt()</code></strong> from the Matlab Signal Processing Toolbox, which implements a forward-reverse (zero-phase) FIR filter.</p>

### 5.3.4. Downsampling

Downsampling can be an important step when fitting parametric autoregressive models. Time series with high sampling rates generally require large model orders to appropriately capture the process dynamics, particularly if interactions occur over a relatively long time lag. As in the discussion above regarding variable selection, increasing the model order increases the number of model coefficients that must be estimated, which can lead to biased estimates when limited data is available. Generally speaking, spectral and causal estimates derived from models of high order exhibit increased variability relative to those with low model order, which can complicate interpretation unless appropriate statistics are applied (Schelter et al., 2005a). In SIFT, downsampling is implemented using EEGLAB’s <strong><code>pop_resample()</code></strong> function, which employs a zero-phase antialiasing filter before downsampling. The use of a zero-phase antialiasing filter is critical for the same reasons described above for band-pass filtering.</p>

### 5.3.5. Differencing

Differencing is a standard operation for improving stationarity before fitting time-domain parametric VAR models (Chatfield, 1989). A first-order difference filter for input <em>x</em> is given by <img src="https://latex.codecogs.com/svg.latex?{ {y}_{t} }={ {x}_{t} }-{ {x}_{t-1} }=\nabla { {x}_{t} }">. This operation can be applied repeatedly to obtain an n<sup>th</sup> order difference filter: <img src="https://latex.codecogs.com/svg.latex?{ {y}_{t} }={ {x}_{t} }-{ {x}_{t-1} }=\nabla { {x}_{t} }">. Orders larger than two are rarely needed to ensure stationarity. An important point to note is that differencing is a high-pass filter and may complicate frequency-domain interpretations of connectivity (Seth, 2010). Differencing is implemented in <strong><code>pre_diffData()</code></strong>.</p><p><br />
Recently published reports have examined the effect of different forms of downsampling, differencing, and filtering on granger-causal measures and demonstrate that, in some cases, these operations may produce spurious connectivity estimates (Florin et al., 2010; Seth, 2010). In general, if the sampling rate is not excessively high (&gt; 500 Hz) and there are not large frequency-specific artifacts in the data, it is advisable to avoid downsampling or filtering. Differencing should also be treated with great caution if one wishes to examine frequency-domain connectivity. In general, one should maintain caution when applying any transformation to their data – either to remove artifacts or improve stationarity – because it may not be well-understood how these operations affect connectivity estimates, particularly under less-than-ideal, real-world conditions. When possible, a safer alternative to stationarity-improving transformations is to instead use adaptive algorithms that either fit a model to locally stationary windows of data (e.g., sliding-window AMVAR), estimate model coefficients from spectral density matrices (e.g., minimum-phase factorization) or utilize a state-space representation (e.g., Kalman Filter). SIFT allows the user to select from several such adaptive algorithms and also provides methods for rigorously testing the stationarity and quality of the fitted model.</p>

### 5.3.6. Detrending

When only linear trend/drift is present in the data, an alternative to high-pass filtering is to linearly detrend the time series using a least-squares fit. This is a phase-preserving operation. Detrending and centering (subtraction of the temporal mean) are implemented in SIFT’s <strong><code>pre_detrend()</code></strong>.</p>

### 5.3.7. Normalization

SIFT allows you to perform two kinds of normalization: <em>ensemble normalization</em> and <em>temporal normalization</em>. In section 3.4.1., we noted that ensemble normalization (pointwise subtraction of an ensemble mean and division by ensemble standard deviation; for example, normalization across trials) is an important preprocessing step when using multi-trial sliding-window AMVAR.

In contrast, when using short windows, temporal normalization (subtraction of the mean of each window and division by standard deviation) is not a good choice since the small-sample estimate of the mean and variance within each small window will be highly biased (inaccurate). As such, SIFT only allows you to perform temporal normalization across the <em>whole trial</em> before segmentation. This should be performed prior to ensemble normalization and ensures that all variables have equal weight (variance) across the trial. This is important since the units of many of our derived VAR-based causal measures, like any regression method, are not scale-free and depend highly on the units and variance of the signals. Thus, severely unbalanced variances amongst the variables will likely lead to model misspecification (e.g., the variables with the highest variance may be incorrectly indicated as causal sources). It is worth noting that scale-free measures such as renormalized PDC (rPDC) are theoretically immune to this problem. Nonetheless, temporal normalization, when possible and reasonable, is usually a good idea.

