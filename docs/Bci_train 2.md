---
layout: default
title: Bci train
permalink: /docs/Bci_train
parent: Docs
---

Learn a predictive model given some data and approach, and estimate its
performance.

**\[Loss,Model,Statistics\] = bci_train(Training-Options,
Parameters...)**

Learns a model of the connection between abstract 'cognitive state'
annotations/definitions in a data set (e.g., event markers, target
variables) and the actual biosignal data, so that the learned model can
subsequently be used to predict the (defined) cognitive state of the
person (in real time or offline). Also estimates the quality of the
model's predictions, using a measure of 'mismatch' between what was
defined for a given time point and what the model would predict (the
'loss').

# Model Computation

The goal of BCI research is to enable a computer system to read the
ongoing EEG (or other brain-/biosignals) of a person and predict from
it, in real time, what his/her cognitive state is. Since the connection
between biosignals and cognitive state includes some information that is
highly specific to a person or group of persons, it can only be obtained
from actual data of that person (or group), which is here called a
'calibration data set'. For modern expositions of the general problem
and solutions, see \[7\] or \[8\].

There is currently no general automated method to learn the connection
(relation) between a calibration data set and the aspect of cognitive
state that is to be predicted, but there is a growing body of
approaches, here called 'paradigms', each of which imposes a different
set of assumptions about the nature of that relation. These paradigms
tend to find the relation if their assumptions match the data and if the
required information is sufficiently accessible in the calibration data
set. The result is a 'predictive model' in which the information about
the connection of interest is captured.

Almost all paradigms involve some parameters that can be varied to
obtain a different variant of the paradigm (e.g., the frequency range of
interest in the EEG signal), and the better these parameters are chosen,
the better will be the attainable quality of the models that the
paradigm can compute. In addition, there is the possibility to search
over different values of parameters to find the best combination, if
compute/time resources are available.

bci_train requires that a paradigm is specified (predefined ones are in
the folder code/paradigms) and that a calibration data set, annotated
with expected cognitive state is supplied. Since bci_train must learn a
relation between raw signal and abstract (human-defined) cognitive
state, the state must be specified by the user in a machine-accessible
format. A typical 'encoding' of such state is created as follows. The
user records a calibration data set from a person (a regular EEG
recording). Througout this recording, the person is in different states
at different times (preferably repeatedly and randomized), for example,
instructed to think or feel a sequence of specific things (e.g., imagine
a left/right hand gesture), or exposed to a series of artificial
conditions (e.g., high/low excitement), such that the answer to a
particular state question is known at particular times in the recording
(e.g. was a left or right hand gesture being imagined at time X?). The
times at which there is knowledge about the person's state, and its
value at these times is encoded into the EEG as 'events', or 'markers'.
In EEGLAB data sets, this is the field EEG.event, and its type (a
string) would be used to encode the state value. Usually, events are
produced by the software that guides the person though the calibration
session and are recorded by the data acquisition system.

Aside from the chosen paradigm's parameters, this is all there is to
specify to bci_train in order to obtain a predictive model and its
performance estimate. The paradigm's parameters are all optional, and
are by default set as in the representative (or most commonly) published
use of the paradigm, so most of them need to be specified only when the
user wants to deviate from those values. However, the paradigm at least
needs to be informed about how event types in the data set are to be
translated into to-be-predicted values (e.g., which of the (potentially
many) event types in the data set serve to encode cognitive state, and
does the relevant type 'left-hand-imagination' translate to -1 or +1?).
Most use cases are covered by the 'events' parameter that is shared by
all paradigms: it is specified as a list of (groups of) event types, and
all types in the n'th group are tranlated into the predicted number n
(which can then be translated by the user or a program in to whatever
value/action is desired).

# Simple Example

A model that predicts the laterality of imagined hand gestures can be
computed as follows (assuming that the data set contains events with
types 'left-imag' and 'right-imag', at the time points where the subject
was instructed to imagine the respective action). Since the relevant
brain signals (Event-Related Desynchronization, see \[1\]) are assumed
to be oscillatory processes that originate in distinct areas of the
brain, the CSP (Common Spatial Pattern, see, e.g., \[2\]) paradigm is
used here unmodified. The entire function handle to the respective
paradigm function, here paradigms/para_csp may be given, or just the
appendix 'csp' as a string.

``` matlab
calib = io_loadset('data sets/john/gestures.eeg')
[loss,model,stats] = bci_train({'data',calib, 'paradigm',@para_csp}, 'events',{'left-imag','right-imag'})
```

When the loss is good (low) enough to justify online use, the model
would then be loaded by the user into BCILAB's online system and would
predict, whenever it receives EEG that indicates an imagined left hand
gesture, the number 1 with high probability (and 2 with low
probability), and in the case of an imagined right hand gesture, the
number 2 with high probability (and 1 with low probability). At times
where the person being measured imagines neither of the defined
gestures, the system may produce arbitrary predictions. To handle such
cases, a further condition (the 'rest' condition) can be defined for the
model, by inserting 'rest' events into the data set whenever the subject
was in neither of the two other states. The model could then be trained
as

``` matlab
[loss,model,stats] = bci_train({'data',calib, 'paradigm',@para_csp}, 'events',{'left-imag','right-imag','rest'}),
```

and would predict 3 with high probability (and 1/2 with low probability)
in periods where the person being measured is in a resting state (note:
the function set_insert_markers can be used to insert markers of given
types into specific periods of the data). Since CSP is by nature a
method defined for only two conditions, the framework automatically
applies it on every pair of conditions, which is called voting (see
ml_trainvote). Another way to obtain similar results is by using two
separate models at the same time, one to detect the type of imagination,
and the other to detect whether an imagination (defined as a group of
multiple event types) or resting is happening:

``` matlab
[lossA,modelA] = bci_train({'data',calib, 'paradigm',@para_csp}, 'events',{'left-imag','right-imag'}),[lossB,modelB] = bci_train({'data',calib, 'paradigm',@para_csp}, 'events',{'rest', {'left-imag','right-imag'} })
```

Though, in this case it is up to the application to combine the state
probabilities that are produced by model B with those produced by model
A.

# Loss Estimation

The most important question to ask about a predictive model is how well
it performs, i.e. how well do its outputs match the desired outputs --
and for a complete system that performs actions depending on a
predictive model, what overall cost is incurred by (potentially
sub-optimal) behavior of the system. Both cases can be covered by a
formal 'loss' metric \[3\]. Different types of systems / types of
predictive models require different loss metrics, which can be chosen in
the 'metric' parameter (part of the Training-Options) from a set of
pre-defined ones, or supplied as a custom function. An introduction to
various predefined loss functions and their uses is given in the help of
the function machine_learning/ml_calcloss.

The loss of a model can be computed in a variety of settings. Most
obviously and realistically, a model can be run online, and the loss
incurred by its predictions can be recorded (for example, number of
mis-classifications, virtual money lost by a BCI-supported gamer). This,
however, requires multiple (controlled) runs through an experiment to
compare different models and/or methods, which is usually prohibitively
costly. A more effective approach is to record the online EEG/biosignal
data and the desired outputs of the system whenever they are known, and
then estimate the loss of any models "offline" on the data, using the
loss metric that best reflects the actual loss in the chosen scenario
(for example mis-classification rate or ROC area); this approach
requires just one session, and can be used to compare arbitrarily many
models post-hoc (using the function bci_predict). The caveat is that
any chaotic dynamics that may unfold between a system mis-behaving and a
user reacting are not covered by the estimate (for example, when a
system fails for more than a minute, the user may start to control it
more aggressively, which may in turn make it even more difficult for the
model to interpret brain signals).

Finally, a loss estimate can be computed directly by bci_train, on the
given calibration data, using cross-validation (CV) \[4\]. This is a
data resampling procedure in which models are repeatedly computed, each
time on a different subset of the data (called the training set) and
compared on another disjoint portion of the data (called the test set)
using the defined (i.e. desired) outputs, and some user-selected loss
measure. In the default CV, the data is partitioned into 10 blocks,
where for each block, a model is computed on the remaining 9 ones and
tested against the target values in the current block (called 10-fold
blockwise CV). Other variants include k-fold randomized CV, where the
data trials are randomly shuffled before a regular blockwise k-fold CV,
n times repeated k-fold CV, in which n repeated runs over different
shufflings are executed and results averaged, and leave-one-out CV
(LOOCV), where a model is computed on all except for one trial, and is
then tested on the held-out trial. The loss measure is by default chosen
depending on the type of target values in the calibration set and the
features of the paradigm so that the user rarely needs to override it
(misclassification rate for categorical outputs, mean-square error for
continuous outputs, negative log-likelihood for probabilistic regression
models, etc.).

The loss estimates of bci_train are very convenient and can be used to
evaluate a large variety of models on data from a single calibration
session. The caveat is that that the estimate systematically fails to
cover certain features of actual online situations. First, chaotic
dynamics are not captured, as in the other offline case, and second,
only a certain fraction of the (time-varying) non-stationarities in the
data are captured by the estimate. Most biosignals contain features that
vary at certain time scales, from second to second (e.g., dopamine
level), minute to minute (e.g., background situation), hour to hour
(e.g., tiredness), day to day (e.g., medication) and year to year (e.g.,
long-term brain plasticity), all of which can affect the output
(quality) of the model. Since calibration sessions are usually short,
training/test data is close to each other in time, and the situation
typically has little variation (e.g. it may be all offline with no user
control involved), the majority of non-stationarities that could degrade
the model's performance are not captured, and the estimate is almost
surely overly optimistic. How large this effect is depends among others
on the stability of the features used by the model, the strength of
assumptions imposed by the paradigm, and the variety/coverage of
situations present in the calibration data.

# Paradigm Customization and Structure

In the Parameters... part of the bci_train arguments, a list of
name-value pairs (e.g. ..., 'srate',200, 'spectrum',\[7 30\],
'epoch',\[-1.5 2.5\], ...) can be specified, to override the default
values of the chosen paradigm for the given named parameters -
practically all paradigms have named parameters (although some
community-supplied ones may have position-dependent parameters - like
most MATLAB functions). All parameters are basically passed through
unmodified to the paradigm function in question (usually one of the
paradigms/para_\* functions), so the place to look up what can be
specified is the help of the respective function (but note that the
first 2 arguments of the paradigm function are not user-accessible --
these are implicitly specified by bci_train itself and contain the
actual biosignal data).

Most paradigms contain similar internal structure, and therefore share
common components, which in turn means that most of them share multiple
common parameters. It is therefore helpful to know these components. The
internal structure of most paradigms contains a sequence of three
overall data processing stages. The first stage, Signal Processing,
receives (multi-channel) signals, such as EEG, and filters these signals
to amplify and focus the information of interest, and to discard the
remaining information. The outputs of the first stage are again signals,
either continuous or epoched/segmented. The stage may have several
successive sub-steps (most of them called filters, some called data set
editing operations), such as resampling, frequency filtering, spatial
filtering, time window selection, artifact removal, etc.. The toolbox
offers a collection of pre-defined filter components (in
filters/flt_\*) and data set operations (in dataset_ops/set_\*), each
with their respective default parameters. Most paradigms use at least
one or two of these components, usually with custom parameters for them,
and the user can override these parameters by specifying the component
name (e.g. 'resample' to control the settings of the used sampling rate
filter, flt_resample) followed by the parameter value to be passed
(e.g. 200 for 200 Hz in the case of flt_resample), or a cell array of
parameters if the component accepts multiple parameters, such as
flt_ica does. Furthermore, most paradigms not only use a subset of the
provided filters, but instead use the entire default Signal Processing
pipeline of the toolbox, explained in filters/flt_pipeline. For this
reason, all parameters of flt_pipeline can be customized by the user
for any paradigm (and not just those chosen by the paradigm), i.e. the
user can enable and configure stages in the default pipeline which are
normally disabled in the given paradigm. Note that flt_pipeline offers
a few alias names for some parameters, e.g. 'channels' can be used
instead of 'selchans', both controlling filters/flt_selchans; these are
listed in flt_pipeline.

The second stage of most paradigms is the Feature Extraction stage,
which receives the preprocessed signals from the Signal Processing, and
extracts certain informative features (e.g. logarithm of the signal
power). This stage is usually custom to the paradigm, and is therefore
controlled by unique parameters (e.g. 'patterns' in the Common Spatial
Patterns \[2\] paradigm, para_csp).

Finally, the feature produced by the Feature Extraction are usually
subjected to a last stage, the Machine Learning. In this, a learning
component, which is one of the provided machine_learning/ml_train\*
functions, computes a statistical model of the feature distributions,
and their relation to the desired output values. This component is
generally selected via the 'learner' parameter, which is exposed by most
paradigms. The learner can be specified as a function handle, e.g.
@ml_trainsvmlinear for the SVMlinear component (linear Support Vector
Machines), or - preferred - as just as the name tag, here 'svmlinear'.
If the learner component contains parameters which shall be costomized
as well, a cell array is passed which contains the name tag followed by
the custom parameters, in the order of appearance in the respective
learning function. For example, 'learner',{'svmlinear',0.5} selects The
linear SVM component and sets its Cost parameter to 0.5, and
'learner',{'logreg',\[\],'variant','vb-ard'} selects the Logistic
Regression component, keeps its first parameter at the default value,
and uses the custom variant 'vb-ard', which stands for Variational Bayes
with Automatic Relevance Determination (see, e.g., \[7\]). A small but
useful subset of the provided Signal Processing, Feature Extraction and
Machine Learning components is compactly described in \[5\].

# Customized Example

To obtain an online prediction of the working-memory load of a person, a
calibration data set in which the person has to maintain varying numbers
of items is his/her memory (e.g., using the n-back task, see \[6\]) can
be used as a starting point. In this data set, conditions with one item
in memory are marked with the event 'n1', conditions with two items in
memory are marked with 'n2', etc. Assuming that working-memory load may
be reflected in certain oscillatory processes, though in unknown
locations and frequency bands, the paradigm Spec-CSP (\[9\]) is used as
a basis. In its default configuration (see paradigms/para_speccsp), it
focuses on a relatively narrow frequency band, which shall be relaxed
here (in particular, the theta band \[10\] should be included). Also, by
default, the Spec-CSP paradigm selects data epochs at 0.5-3.5 seconds
following each (selected) event, which shall be modified to \[-2.5
2.5\], to get a time coverage that is better adapted to the task.
Finally, Spec-CSP by default contains a non-probabilistic classifier
(Linear Discriminant Analysis, see machine_learning/ml_trainlda),
which we want to change into a largely equivalent, but probabilistic one
(Logistic regression, see machine_learning/ml_trainlogreg). Since we
assume that the most important part of the spectrum will be the alpha
and theta rhythm (peaked at \~10 and \~4Hz), but do not want to
completely rule out other frequencies, we additionally impose a prior as
a custom in-line (lambda) function of frequency). Since we have more
than two classes, but the Spec-CSP is only defined for two classes, the
framework automatically applies it to every pair of conditions and uses
voting (see machine_learning/ml_trainvote) to arrive at per-class
probabilities. Note that this is a major customization, which might even
be considered a novel method.

``` matlab
data set = io_loadset('data sets/mary/nback.eeg')
[loss,model,stats] = bci_train({'data',data set, 'paradigm',@para_speccsp}, 'events',{'n1','n2','n3'}, ...
    'epoch',[-2.5 2.5], 'learner','logreg', 'spectrum',[2 45], 'pp',-1, 'prior',@(f)1+exp(-(x-10).^2)+exp(-(x-4).^2))
```

This model will predict either 1,2, or 3 with high confidence, when the
user is maintaining the respective number of items in his/her working
memory, but will likely be fairly specific to the task on which it was
calibrated. Out of the specified parameters, 'events', 'epoch' and
'spectrum' are available in most other paradigms, too, as they are
exposed by the default Signal Processing pipeline that is used by them.
The 'learner' parameter selects the machine learning component of the
paradigm. The 'pp' and 'prior' parameters are specific to the Spec-CSP
paradigm, and control how features are being extracted from pre-filtered
data (for subsequent processing by the learner); see para_speccsp.

# Parameter searching

In some cases, the optimal setting of certain parameters of a paradigm
might not be known, but may drastically affect the performance of the
method. One example are the time boundaries w.r.t. to the supplied
events, which may depend on the reaction time of the user, among other
things. Another example are regularization parameters which are used to
constrain the complexity of the learned model (see, e.g. \[11\]).
Regularization is a very powerful concept which enables methods such as
Support Vector Machines and LASSO, in which the parameter is neither
designed to be manually selected nor is it very interpretable in terms
of brain processes. But most importantly, manual selection of these
parameters (by trial and error) invalidates the performance guarantees
that are made by the loss estimates: the performance estimate found for
the hand-selected model is likely far better than the actual performance
of that model. This is because the influence of random fluctuations in
the estimate over the possible parameters is maximized by the user when
he/she accepts the best one as the actual performance of the method
(similar in spirit to the fallacy of multiple hypothesis tests without
correction).

For these reasons, bci_train offers a generic mechanism to search over
parameters (or parameter combinations), in user-defined intervals and
granularity, and uses a nested cross-validation method to give unbiased
loss estimates. In this method, the search for the best parameter (using
cross-validation derived estimates) is done inside an outer
cross-validation, in each of its steps, and is restricted to the
respective training set of that step. This way, the performance of the
search procedure itself can be objectively evaluated on held-out test
data. The cross-validation scheme for this inner search procedure can be
specified via the 'opt_scheme' parameter (part of the
Training-Options), which has the same format as the 'eval_scheme'
parameter. By default, it is set to a 5-fold blockwise cross-validation
with 5 trials safety margin. As a downside, parameter search multiplies
the time it takes to compute a model by a potentially large factor; the
total computation time of bci_train is (\# of folds in the outer
cross-validation) \* (\# of folds in the inner cross-validation) \* (\#
of parameter combinations) \* (time to compute a single model). Thus,
the evaluation (outer) cross-validation may in some cases be turned off
('eval_scheme' set to 0) to obtain a model in a reasonable time, e.g.,
between a calibration session and a subsequent online session.

Any value supplied to the paradigm can be replaced by a search range,
written as search(...), to indicate to bci_train that this parameter is
subject to a search. The search() clause can be used in any place of the
data passed to the paradigm (e.g. inside cell arrays and/or structs),
and can run over any data type supported by MATLAB, such as numbers,
strings, structs, and vectors.

# Parameter Search Examples

In the case of imagined hand gestures (see first example), the time
period in which the user performs the imaginations may not be known in
advance (e.g. one user may imagine to clench the fist, while another
user may imagine a whole sequence of finger movements). Therefore, the
exact boundaries of the relevant data are not known, and can be searched
(or spectral heuristics could be used). We assume that the response time
of the user following the instruction may vary between 0.25 seconds and
0.75 seconds, and we choose to search over the range at a granualarity
of 0.1 seconds. The time it takes until the imagination is finished may
vary between 1.5 seconds and 4.5 seconds, and we search over values at a
granularity of 0.5 seconds. Thus, para_csp's default 'epoch' parameter
\[0.5,3.5\] is replaced by \[search(0.25:0.1:0.75),
search(1.5:0.5:4.5)\]:

``` matlab
calib = io_loadset('data sets/john/gestures.eeg')
[loss,model,stats] = bci_train({'data',calib, 'paradigm',@para_csp}, 'events',{'left-imag','right-imag'}, 'epoch',[search(0.25:0.1:0.75),search(1.5:0.5:4.5)])
```

Since the search runs over 6\*7 parameters, and a 5x inner
cross-validation is performed, the overall running time will be 6\*7\*5
= 210x the default running time. If such a procedure shall berun
immediately prior to an online session, it is better to disable the
outer cross-validation altogether, which brings the time down to 21x of
the default.

As a second example, suppose that the goal is to predict whether the
user perceives some event as being erroneous or not. A possible
calibration data set could contain events of two classes, 'err' and
'cor', which encode time points where the user encountered errorneous
and correct events. The assumption is that the user's event processing
is accompanied by a characteristic slow cortical potential \[12\] which
allows to discern between the two conditions. As a paradigm, we use the
low-frequency version of the Dual-Agumented Lagrange method \[13\],
which makes few assumptions except that the cognitive process of
interest is simple enough in its time/space behavior to be tractably
recognized. We restrict the analysis to the period of 0-0.8s following
the event, resample to 100Hz, filter to 0.1-15Hz, and use DAL (see
machine_learning/ml_traindal) as the learning function. The complexity
of the learned model is controlled via a regularization parameter,
called Lambda. This parameter is the first user-accessible parameter in
the learning function ml_traindal (its first two parameters are
implicitly specified by the framework and contain the actual data; this
contract holds for all other learning functions
machine_learning/ml_train\*, as well). As explained in Paradigm
Customization and Structure, the first user parameter for the DAL
component would normally be set as 'learner',{'dal' value}, whereas
here, we search over an entire range of possible values (2^-5 to 2^10,
in logarithmic increments of 2^0.75).

``` matlab
calib = io_loadset('data sets/john/errorperception.eeg')
[loss,model,stats] = bci_train({'data',calib,'paradigm',@para_dal_lf}, 'epoch',[0 0.8], 'srate',100, 'events',{'err','cor'}, 'spectrum',[0.1 15], ...
    'learner',{'dal', search(2.^(-5:0.75:10))})
```

As a third example, suppose that the goal is be able to predict the
emotional state of a user, out of five different possibilities. A
typical calibration data set would contain multiple blocks in each of
which the person is experiencing a particular emotion. Markers with
types 'e1','e2','e3','e4','e5' would then be scattered into these blocks
(using set_insert_markers). It is assumed that the difference between
emotional conditions is most likely expressed in spectral properties of
independent components (see \[14\]), so ICA will be enabled as a
preprocessing stage (see flt_pipeline), and configured to replace the
data with component activations (using the 'transform' option of
flt_ica), and a subsequent transform into the Fourier power spectrum
will be done (see flt_fourier). The resulting spectral data will be
normalized and vectorized (which is a feature of the generic DAL
paradigm, see para_dal). The problem is that it is not known which
classifier handles the resulting data best. Some possible options could
be shrinkage LDA, Variational Bayes Logistic Regression with Automatic
Relevance Determination, Linear Support Vector Machines, Kernel Support
Vector Machines (with RBF kernel), Relevance Vector Machines, or
group-sparse Dual-Augmented Lagrange Logistic Regression. We want to
search over all these options. Note that some of the possible
classifiers themselves have regularization parameters that require
multiple parameters to be searched. Since the search space is
extraordinarily large, we reduce the inner and outer cross-validations
as much as possible, each to a 4x chronological cross-validation (with 5
trials safety margin between training and test sets), to be able to
solve the problem within a day.

``` matlab
calib = io_loadset('data sets/john/emotions.eeg')
learners = search('lda',  ...
    {'logreg', [], 'variant','vb-ard'}, ...
    {'svmlinear', search(2.^(-5:2:15))}, ...
    {'svmperf', search(2.^(-5:2:15)), 'kernel','rbf', 'g',search(-15:2:6)}, ...
    {'rvm', 'gamma', search(2.^(-16:2:4))}, ...
    {'dal', search(2.^(-5:0.75:10)), 'regularizer','glr'});
```

``` matlab
[loss,model,stats] = bci_train({'data',calib,'paradigm',@para_dal, 'eval_scheme',{'chron',4,5}, 'opt_scheme',{'chron',4,5} }, ...
'epoch',[-2.5 2.5], ...
'srate',400, ...
'events',{'e1','e2','e3','e4','e5'}, ...
'ica',{[],'transform',1},  ...
'fourier','power', ...
'regions',{ {'freq',[0 1000]} }, ...
'learner',learners)
```

# Statistics

Aside from an average loss measure, a structure of additional statistics
can be obtained from bci_train via its third output parameter,
Statistics. The most relevant part of the statistics are the per-fold
loss measures (computed in each cross-validation fold), which can be
used to run statistical tests on the significance of outcomes, etc.;
these are in the struct array .per_fold. This also includes the target
values (.targ) and predicted values (.pred) for the trials in each fold,
as well as the indices of the fold's trials in the full original data
set (.indices). Depending on the type of loss measure, additional values
may be available per fold (e.g. fraction of true and false positives,
etc).

If the model was obtained in a parameter search, the field .model
contains the complete set of loss measures and computed models for each
tested parameter combination (on the entire calibration set), which
includes, among others, the regularization path for regularized
classifiers, which allows for very detailed analyses of the computed
models.

Additional fields include, depending on the type of target variables,
.classes and .class_ratio contain the possible output values of the
model (e.g. \[1,2,3,4,5\] in a standard 5-class classification task) as
well as the fraction of data trials belonging to each class. The field
.model contains the computed model, the field .expression contains an
expression data structure which summarizes the parameters that went into
the comptuation of the result(s), including those that determined the
data set(s) used for calibration. The function exp_fullform can format
it into a human-readable string.

# Model Usage

The computed model can subsequently be used with other parts of the
toolbox. Most importantly, the model can be used with the online system
of the toolbox, either via one of the provided online plugins or
directly through BCILAB's online application programming interface
(API), explained in online_analysis/onl_\*. Aside from online
analysis, the model can be used for offline analysis of data sets, via
the functions bci_predict (make predictions for every trial in a given
data set), onl_stream (make predictions for desired time points in a
given data set), and bci_preproc (preprocess a given data set into its
pre-feature extraction form for analysis and visualization with EEGLAB
tools). Finally, model properties can be visualized and inspected using
visualization methods (visualizations/vis_\*). The model can be saved
to disk and re-loaded later.

# Input Arguments

**Training-Options**

cell arrray of name-value pairs specifying the training options.

May also be a struct.

mandatory arguments:

  - 'data': training data; data set, or cell array of EEG data sets
    (also STUDY

in the future) in reasonable time.

  - 'para': BCI paradigm to be used (function handle or string; strings
    are

translated into the corresponding para_\* function)

  - 'approach': alternative to para: specify a complete approach, of the
    form

{paradigm, Parameters...}; the paradigm can be overridden by also
specifying the 'para' argument, and the Parameters... are merged wih the
Parameters... arguments of bci_train, where the latter take precedence
if a parameter is specified in both lists

optional arguments:

  - 'metric': custom loss measure used to compute the performance
    estimate; applied in a (nested) cross-validation, can be empty, a
    string or a function handle; see ml_calcloss() for the options
    (default: \[\] -- auto-select between kullback-leibler divergence
    (kld), mean square error (mse), mis-classification rate (mcr) and
    negative log-likelihood (nll) depending on the type of the target
    and prediction variables, further detailed in ml_calcloss())

<!-- end list -->

  - 'eval_scheme'/'outerfold': cross-validation scheme used while
    evaluating the optimal model's performance (default: {'chron',10,5})
    if specified as 0, the evaluation is omitted (and no measure is
    computed) uses the scheme format of utl_crossval()

<!-- end list -->

  - 'opt_scheme'/'innerfold': cross-validation scheme used for
    searching for the optimal model parameters (default: {'chron',5,5})
    uses the scheme format of utl_crossval() if no parameter search
    ranges were specified, this cross-validation is automatically
    omitted

parallelization options (see par_beginschedule for details):

  - 'engine_ps': the parallelization engine to be used for the
    parameter search (default: 'local')

<!-- end list -->

  - 'engine_cv': the parallelization engine to be used for the
    cross-validation (default: 'global')

<!-- end list -->

  - 'pool': node pool to be used for parallelization, when using the BLS
    scheduler (default: 'global')

<!-- end list -->

  - 'policy' : scheduling policy to be used, when using the BLS
    scheduler (default: 'global')

<!-- end list -->

  - 'Parameters...' : optional list of parameters to be passed as 3rd to
    last argument of the specified BCI paradigm function parameter
    ranges may be specified via search(), in which case optimal
    parameters are searched by nested cross-validation

# Output Arguments

**Loss**

a measure of the overall performance of the paradigm combination, w.r.t.
to the target variable returned by gettarget, computed by the specified
loss metric.

**Model**

a predictive model ("detector"), as computed by the specified paradigm;
can be loaded into the online system via onl_loaddetector, applied
offline to new data via bci_predict, and analyzed using various
visualizers

**Statistics**

additional statistics, as produced by the specified metric; if the model
itself is determined via parameter search, further statistics from the
model searching are in the subfield stats.model

# Examples:

``` matlab
% assuming that a data set has been loaded, and a computational approach has been defined
% similarly to the following code:
traindata = io_loadset('bcilab:/userdata/tutorial/imag_movements1/calib/DanielS001R01.dat');
myapproach = {'CSP' 'SignalProcessing',{'EpochExtraction',{'TimeWindow',[0 3.5],'EventTypes',{'StimulusCode_2','StimulusCode_3'} }} };
```

``` matlab
% learn a model and get the mis-classification rate, as well as statistics
[trainloss,lastmodel,laststats] = bci_train({'data',traindata,'approach',myapproach});
```

``` matlab
% as before, but use a coarser block-wise (chronological) cross-validation (5-fold, with 3 trials margin)
[trainloss,lastmodel,laststats] = bci_train({'data',traindata,'approach',myapproach,'eval_scheme',{'chron',5,3} });
```

``` matlab
% as before, but use a 10-fold randomized cross-validation (rarely recommended)
[trainloss,lastmodel,laststats] = bci_train({'data',traindata,'approach',myapproach,'eval_scheme',10});
```

``` matlab
% as before, using a 10-fold, 10x repeated randomized cross-validation
[trainloss,lastmodel,laststats] = bci_train({'data',traindata,'approach',myapproach,'eval_scheme',[10 10]});
```

``` matlab
% using a different loss measure (here: mean-square error, instead of the default mis-classification rate)
[trainloss,lastmodel,laststats] = bci_train({'data',traindata,'approach',myapproach,'metric','mse'});
```

``` matlab
% assuming that the defined approach involved a parameter that needs to be searched, such as the
% following one:
myapproach = {'CSP' 'SignalProcessing',{'EpochExtraction',{'TimeWindow',[0 3.5],'EventTypes',{'StimulusCode_2','StimulusCode_3'} }}, ...
'MachineLearning',{'Learner',{'logreg', search(2.^(-6:0.5:10)), 'variant','l2'} }};
```

``` matlab
% learn a model, but use a coarser nested cross-validation (3x) to optimize the parameter
[trainloss,lastmodel,laststats] = bci_train({'data',traindata,'approach',myapproach,'opt_scheme',{'chron',3,3} });
```

``` matlab
% attempt to run the cross-validation on a cluster (consisting of the listed hostnames)
% (note that by default the global BCILAB setting is used, which is set via the bcilab startup command)
[trainloss,lastmodel,laststats] = bci_train({'data',traindata,'approach',myapproach,'engine','BLS','pool',{'computer1','computer2','computer3','computer4','computer5'} });
```

# References

\[1\] Pfurtscheller, G., and da Silva, L. "Event-related EEG/MEG
synchronization and desynchronization: basic principles."

  -
    Clin Neurophysiol 110, 1842-1857, 1999

\[2\] Ramoser, H., Mueller-Gerking, J., Pfurtscheller G. "Optimal
spatial filtering of single trial EEG during imagined hand movement."

  -
    IEEE Trans Rehabil Eng. Dec 8 (4): 441-6, 2000

\[3\] MacKay, D. J. C. "Information theory, inference, and learning
algorithms."

  -
    Cambridge University Press, 2003.

\[4\] Duda, R., Hart, P., and Stork, D., "Pattern Classification.",
Second Ed.

  -
    John Wiley & Sons, 2001.

\[5\] Dornhege, G. "Increasing Information Transfer Rates for
Brain-Computer Interfacing."

  -
    Ph.D Thesis, University of Potsdam, 2006.

\[6\] Owen, A. M., McMillan, K. M., Laird, A. R. & Bullmore, E. "N-back
working memory paradigm: A meta-analysis of normative functional
neuroimaging studies."

  -
    Human Brain Mapping, 25, 46-59, 2005

\[7\] Bishop, C. M. "Pattern Recognition and Machine Learning."

  -
    Information Science and Statistics. Springer, 2006.

\[8\] Hastie, T., Tibshirani, R., and Friedman, J. H. "The elements of
statistical learning (2nd Ed.)."

  -
    Springer, 2009.

\[9\] Tomioka, R., Dornhege, G., Aihara, K., and Mueller, K.-R.. "An
iterative algorithm for spatio-temporal filter optimization."

  -
    In Proceedings of the 3rd International Brain-Computer Interface
    Workshop and Training Course 2006, pages 22-23. Verlag der
    Technischen Universitaet Graz, 2006.

\[10\] Buzsaki, G., "Rhythms of the brain"

  -
    Oxford University Press US, 2006

\[11\] Tibshirani, R. . "Regression Shrinkage and Selection via the
Lasso"

  -
    Journal of the Royal Statistical Society, Series B (Methodology) 58
    (1): 267-288, 1996

\[12\] Holroyd, C.B., Coles, M.G.. "The neural basis of human error
processing: reinforcement learning, dopamine, and the error-related
negativity"

  -
    Psychological Review, 109, 679-709, 2002

\[13\] Tomioka, R. and Mueller, K.-R. "A regularized discriminative
framework for EEG analysis with application to brain-computer interface"

  -
    Neuroimage, 49 (1) pp. 415-432, 2010.

\[14\] Onton J & Makeig S. "Broadband high-frequency EEG dynamics during
emotion imagination."

  -
    Frontiers in Human Neuroscience, 2009.

<center>

Christian Kothe, Swartz Center for Computational Neuroscience, UCSD

</center>

<center>

2010-04-24

</center>

[Category:IV.Scripting.A.Offline
Analysis](/Category:IV.Scripting.A.Offline_Analysis "wikilink")