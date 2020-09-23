---
layout: default
title: Bci annote
permalink: /docs/Bci_annote
parent: Docs
---

Annotate a raw dataset with a bci-derived channel

**Signal = bci_annotate(Model,Signal,Options...)**

This function allows to add channels to a continuous (or epoched) data
set which contain the estimates of a predictive model applied to the
data. The resulting set can then be analyzed and visualized using a
variety of tools (e.g. some of EEGLAB's plot tools).

# Input Arguments

**Model**

a predictive model (previously learned with bci_train)

**Signal**

a continuous raw data set

**Options...**

optional name-value pairs; the following names can be used:

'name' : name of the channel(s) to be derived (default: 'BCI')

if the model's output is multi-dimensional, the channels created will

have a trailing number (1,2,...)

'format': format of the prediction (see utl_formatprediction); can be
'expectation': the output is the expected value (i.e., posterior mean)
of the quantity to be predicted; can be multi-dimensional \[NxD\]
'distribution': the output is the probability distribution (discrete or
continuous) of the quantity to be predicted usually, this is a discrete
distribution - one probability value for every possible target outcome
\[NxV\] it can also be the parameters of a parametric distribution
(e.g., mean, variance) - yielding one value for each parameter \[NxP\]
(default) 'mode': the mode \[Nx1\], or most likely output value (only
supported for discrete probability distributions)

'srate': sampling rate at which to predict (in Hz; default: 25)

'interpolation': interpolation method to be used; can be: 'resample':
upsample using the resample method 'nans': do not interpolate; introduce
NaN's in between estimates 'nearest': piecewise constant interpolation
'linear': piecewise linear interpolation 'spline': use a spline
interpolation (default)

'windowlen': length of the interpolation window, in seconds, if using
moving average or resample

(default: \[\] = use built-in default for resample or 5x the sampling
interval for moving average)

# Output Arguments

Signal: the new signal, with BCI-derived annotation

# Notes

if this function is applied to epoched data, there will be a period at
the beginning of each epoch for which there exist no meaningful
predictions, because each model usually requires a minumum amount of
samples to operate.

# Examples:

``` matlab
% given a predictive model and a continuous data set, append a channel which encodes the BCI
% model's output
eeg = bci_annotate(lastmodel,eeg)
```

``` matlab
% as before, but use a different output format (namely: expected value instead of probability
% distribution)
eeg = bci_annotate(lastmodel,eeg,'format','expectation')
```

``` matlab
% as before, but this time use a higher sampling rate (slower, but more precise)
eeg = bci_annotate(lastmodel,eeg,'srate',60)
```

``` matlab
% as before, but use a more conservative interpolation method
eeg = bci_annotate(lastmodel,eeg,'interpolation','resample')
```


Christian Kothe, Swartz Center for Computational Neuroscience, UCSD



2010-03-28


[Category:IV.Scripting.A.Offline
Analysis](/Category:IV.Scripting.A.Offline_Analysis "wikilink")