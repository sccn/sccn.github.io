---
layout: default
title: Bci predict
permalink: /docs/Bci_predict
parent: Docs
---

Apply a predictive model to some data and optionally measure its
performance.

**\[Prediction, Loss, Statistics, Target\] = bci_predict(Model,
Dataset, Options...)**

Let a model make predictions of cognitive state on a data set (usually
with known target values), yielding one prediction per trial in the
data, as well as the average empirical loss, if the data set has an
attached target variable.

bci_predict is used to obtain and/or evaluate the outputs of a
predictive model on a recorded (usually raw) data set. Predictions are
made for every trial in the data set, where trials are derived from the
data in the same way as was used when the model was originally
calibrated. For example, if the model was calibrated w.r.t. events of
certain types in the calibration set (using the 'events' parameter of
the paradigm), trials will be extracted for these same events in the
supplied data set, as well. In the typical case where a target variable
can be derived from the data set in this way (e.g. via the 'event'
clause passed to bci_train - see bci_train), then the predictions of
the model are compared with the defined target values, and an average
loss is computed (and returned as the second output). This loss measure
has the same meaning as in bci_train, and can be customized via the
'metric' parameter, either as one of the predefined losses (described in
detail in machine_learning/ml_calcloss), or as a user-supplied custom
function. By default, the most appropriate loss is automatically
selected depending on the types of target and prediction values
(mis-classification rate for categorical target values, mean-square
error for continuous target values, etc.), so that user intervention is
rarely needed.

For advanced use, the actual predictions for every trial in the data are
returned, as well as the defined target values in the data set (if
available). The format of the targets depends on the procedure by which
they were assigned to the data (e.g., when the 'events' clause was used
to assign target values to certain events, targets is a numerical vector
of class numbers, e.g. \[1 2 2 1 4 1 3 2 3 2 1\] for some hypothetical
4-class data set with 11 trials). The format of the predictions depends
on the format of the targets (e.g., whether they were categorical values
or continuous values, usually the former), and the capabilities of the
'learner' component of the paradigm. A detailed exposition of the
possibilities is given in machine_learning/ml_predict.

Almost all learners produce discrete probability distributions for
categorical targets, so this is the format of the predictions in 90% of
the situations. A sequence of discrete probability distributions (one
per trial) as produced by bci_predict is formatted as a MATLAB cell
array with the three entries {'disc', Probabilities, Classes}. 'disc' is
the format tag of the predictions and indicates discrete probabilities,
Probabilities is an array of probabilities for each trial and class,
with \# of trials rows and \# of classes columns, i.e. it has size
\[NxC\], and Classes is a column vector which specifies the desired
target value for each of the C classes, in the same order as the rows in
Probabilities. For this reason, the expected target value for any trial
is pred{2}\*pred{3}, and the most likely target value for any trial can
be obtained as pred{3}(argmax(pred{2}')), if pred are the predictions
return by bci_predict.

In addition, further statistics are returned, which may contain
additional values (e.g. false positive rate in the case of binary
classification).

> <font color = green>Example:</font color>

``` matlab
% load a calibration data set
calib = io_loadset('data sets/john/gestures.eeg')
% train a model (see bci_train for an explanation of this stage)...
[loss,model,stats] = bci_train({'data',calib, 'paradigm',@para_csp}, 'events',{'left-imag','right-imag','rest'})
```

``` matlab
% load a test data set
testdata = io_loadset('data sets/john/gestures2.eeg')
```

``` matlab
% and apply the model on that data set to get predictions and a loss estimate...
[predictions,loss2,stats2,targets] = bci_predict(model,testdata);
```

The application of the model results in predictions for every of its
trials, an empirical average loss measure, statistics, and the original
target values for every trial in the test data. This is under the
assumption that the file gestures2 contains markers 'left-imag',
'right-imag', 'rest', just like the first data set, so that a loss
(deviation from desired outcomes) can be computed. Note that applying a
model to its own calibration data set gives overly optimistic results,
and is usually scientifically invalid.

A less common use case is to exchange the default preprocessing that is
applied by a paradigm by some alternative preprocessing (for example,
one which slighty deviates from the model's settings, or a manually
implemented one, or the by the preprocessing of an entirely different
model). To this end, not the raw data is passed to bci_predict, but
instead data that was manually processed, for example using bci_preproc
(see bci_preproc). In the follwing example, a test data set is loaded
(as in the previous sample), but it is manually preprocessed using the
model's defined preprocessing, with re-customized options (here:
'events', to define how trials are to be extracted). We assume that the
data contains events of the type 'user-action' whenever the user
performs a (not further known) action, such as one of the imagined hand
gestures.

``` matlab
testdata = io_loadset('data sets/john/unknown_gestures.eeg')
testdataproc = bci_preproc(testdata, model, 'events',{'user-action'})
predictions = bci_predict(model, testdataproc, 'process',0);
disp('the user performed the following actions: ' num2str(predictions{2}(argmax(predictions{3}')))]);
```

In this case, we obtain predictions for every trial of the data (this
time relative to events of the type 'user-action'), whereas the the
predictions will still be either 1,2, or 3, since the predictive part of
the model has not been changed. Further, since the activity of the user
was not known a priori, a meaningful loss cannot be computed. Note that
if the preprocessing of the model contains filters that are adaptively
tuned to the data (such as ICA), this strategy will give unexpected
results, because bci_preproc re-runs the preprocessing (i.e. readapts
the filters) for the test data, which gives intermediate values that are
not expected by the rest of the model.

For these reasons, the recommended way to obtain predictions for a data
set at the times of arbitrary events, or in arbitrary intervals, is to
use onl_stream, which streams the given raw data set into the model and
obtains predictions at the desired time points. bci_predict should only
be used to evaluate the performance of models on data set where the
desired outcomes are known and encoded in the same way as in the
respective calibration data set of the used model (i.e. for pure offline
analyses). See onl_stream for further details.

# Input Arguments

**Model**

a detector model, as produced by bci_train

Dataset : a raw or fully preprocessed data set from which to derive
predictions

Options... : optional name-value pairs to control the function's
behavior:

'metric' : evaluation metric to be employed, can be one of the
following:

'function handle': a custom, user-supplied loss function; receives
target data in the first argument and prediction data in the second
argument; each can be in any format that can be produced by ml_predict
(but can be expected to be mutually consistent). shall return a real
number indicating the summary metric over all data, and optionally
additional statistics in a struct

'string': use ml_calcloss, with 'metric' determining the loss type

'default/empty': use 'mcr','mse','nll','kld', depending on supplied
target & prediction data formats

'target': a function to derive the target variable from the data, for
evaluation; the allowed format is anything that may be output by
ml_predict (default: @set_gettarget)

'process' : whether to process & treat the data set as raw data (0/1,
default: 1)

# Output Arguments

**Prediction**

the target variable as predicted by the model for every index in the
data set

Loss : a measure of the average loss of the model, w.r.t. to the target
variable (as

evaluation; the allowed format is anything)

Stats : additional statistics, as produced by the metric

Target : original target variable, as determined by the target function

# Examples:

``` matlab
% given a predictive model and a continuous data set with markers that are compatible to those
% that were used for training, derive per-epoch/per-marker BCI outputsm and estimate the loss
% plus additional statistics
[predictions,loss,stats] = bci_predict(model,data)
```

``` matlab
% as before, but use a custom metric (here: mean-square error)
[predictions,loss,stats] = bci_predict(model,data,'metric','mse')
```

<center>

Christian Kothe, Swartz Center for Computational Neuroscience, UCSD

</center>

<center>

2010-05-24

</center>

[Category:IV.Scripting.A.Offline
Analysis](/Category:IV.Scripting.A.Offline_Analysis "wikilink")