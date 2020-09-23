---
layout: default
title: Bci preproc
permalink: /docs/Bci_preproc
parent: Docs
---

Preprocess a data set, either given a predictive model, or a paradigm.

**Out-Data = bci_preproc(In-Data, Paradigm-Or-Model, Parameters...)**

bci_preproc allows to manipulate and inspect the preprocessing / signal
processing steps performed on data by a paradigm or a model, with
default and/or custom user options. Most paradigms and models perform a
certain fraction of pure signal processing steps, i.e. steps that
operate on data and produce results that can be interpreted as
continuous or epoched signals (= EEGLAB data sets). These are usually
the first stages of data processing (beginning with raw EEG), where
successively more filtered versions of the data are created. Most
paradigms proceed beyond this stage by mapping the data into
high-dimensional feature spaces in the Feature Extraction Stage, and
further into predicted distributions, in the Machine Learning stage, so
that bci_preproc allows access only up to a certain point in the data
processing chain of a model.

Typical preprocessing steps are resampling, frequency filtering,
(adaptive or non-adaptive) spatial filtering, etc., and most relevant
components that implement these steps can be found in filters/flt_\*
and dataset_ops/set_\*. If no further options are given, bci_preproc
executes the entire preprocessing chain as it was configured, and when
user options are given, certain parts of this default configuration are
varied (e.g. different spectral filters parameters are used).
Specifically stages in the preprocessing can be enabled or disabled (by
passing the name of the stage, e.g. 'ica', followed by a \[\]). The list
of stages that is available in most paradigms is defined and explained
in filters/flt_pipeline.

> <font color = green>Example:</font color>

``` matlab
raw = io_loadset('data sets/john/gestures.eeg')
prc = bci_preproc('paradigm',@para_speccsp, 'events',{'left-imag','right-imag'});
```

prc is now an EEGLAB data set containing fully filtered and epoched
data, as defined by the Spec-CSP paradigm for the given user options,
which can be subsequently analyzed using EEGLAB tools.

# Input Arguments

**In-Data**

input (usually raw) data set (e.g., loaded with io_loadset or via
EEGLAB)

**Paradigm-Or-Model**

either a BCI paradigm function (para_\*, e.g. para_csp, para_dal)
according

to which the data should be processed or a predictive model previously

computed with bci_train; note: if the preprocessing of a model is

customized, it will be entirely recomputed with the new options, which
may

include a readaptation of any adaptive filters

**Parameters...**

optional parameters to deviate from the preprocessing defaults of the
paradigm

or model

# Output Arguments

**Out-Data**

preprocessed datasset

# Examples:

``` matlab
% pre-process a raw data set according to a predictive model
eeg = bci_preproc(eeg,lastmodel)
```

``` matlab
% pre-process a raw data set according to a BCI approach
myapproach = {'SpecCSP', 'events',{'S  1' S  2'} };
eeg = bci_preproc(eeg,myapproach)
```

``` matlab
% pre-process a raw data set according to a BCI paradigm plus some parameters
eeg = bci_preproc(eeg,@para_csp,'events',{'S  1','S  2'},'epoch',[0 3])
```


Christian Kothe, Swartz Center for Computational Neuroscience, UCSD



2010-04-29


[Category:IV.Scripting.A.Offline
Analysis](/Category:IV.Scripting.A.Offline_Analysis "wikilink")