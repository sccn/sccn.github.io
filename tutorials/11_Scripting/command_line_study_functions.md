---
layout: default
title: d. Group level
parent: 11. Write scripts
grand_parent: Tutorials 
---
Group-level analyses using EEGLAB scripts
=====
{: .no_toc }

Building a *STUDY* from the graphic interface (as described in previous
sections) calls eponymous Matlab functions that may also be called
directly by users. Below we briefly describe these functions. See their
Matlab help messages for more information. Functions whose names begin
with *std_* take *STUDY* and/or *EEG* structures as arguments and
perform signal processing and/or plotting directly on cluster
activities.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

Creating a STUDY
-----------------

If a *STUDY* contains many datasets, you might prefer to write a small script to build the *STUDY* instead of using the [pop_study.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_study.m) GUI. This is also helpful when you need to build many studysets or to
repeatedly add files to an existing studyset.

*Important note:* If you want to modify the STUDY structures, you need to be careful as the STUDY checking function ([std_checkset.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_checkset.m)) performs all kinds of checks to keep the STUDY
structures compatible with the datasets it represents. So this function
might undo your changes (a warning will be issued on the command line).
It is often possible to modify the datasets themselves to achieve the
same goal, and changes will be automatically reported in the STUDY
structures.

Below is a Matlab script
calling the GUI-equivalent command line function [std_editset.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_editset.m) 
from the "5subjects" folder (you may download tutorial data [here](https://sccn.ucsd.edu/eeglab/download/STUDY5subjects.zip)):

``` matlab
[STUDY ALLEEG] = std_editset( STUDY, [], 'name','N400STUDY',...
        'task', 'Auditory task: Synonyms Vs. Non-synonyms, N400',...
        'filename', 'N400empty.study','filepath', './',...
        'commands', { ...
    { 'index' 1 'load' 'S02/syn02-S253-clean.set' 'subject' 'S02' 'condition' 'synonyms' }, ...
    { 'index' 2 'load' 'S05/syn05-S253-clean.set' 'subject' 'S05' 'condition' 'synonyms' }, ...
    { 'index' 3 'load' 'S07/syn07-S253-clean.set' 'subject' 'S07' 'condition' 'synonyms' }, ...
    { 'index' 4 'load' 'S08/syn08-S253-clean.set' 'subject' 'S08' 'condition' 'synonyms' }, ...
    { 'index' 5 'load' 'S10/syn10-S253-clean.set' 'subject' 'S10' 'condition' 'synonyms' }, ...
    { 'index' 6 'load' 'S02/syn02-S254-clean.set' 'subject' 'S02' 'condition' 'non-synonyms' }, ...
        { 'index' 7 'load' 'S05/syn05-S254-clean.set' 'subject' 'S05' 'condition' 'non-synonyms' }, ...
        { 'index' 8 'load' 'S07/syn07-S254-clean.set' 'subject' 'S07' 'condition' 'non-synonyms' }, ...
        { 'index' 9 'load' 'S08/syn08-S254-clean.set' 'subject' 'S08' 'condition' 'non-synonyms' }, ...
        { 'index' 10 'load' 'S10/syn10-S254-clean.set' 'subject' 'S10' 'condition' 'non-synonyms' }, ...
    { 'dipselect' 0.15 } });
```

Above, each line of the command loads a dataset. 

The last line
preselects components whose equivalent dipole models have less than 15%
residual variance from the component scalp map. See *\>\> help
std_editset* for more information. 

Notice that the path to the datasets
in the code above is a relative path. Then, to run the same code
snippet, your current directory in MATLAB should contain the datasets.

Once you have created a new studyset (or once you have loaded it from disk), both the
*STUDY* structure and its corresponding *ALLEEG* array of resident *EEG*
structures will be variables in the Matlab workspace. 

Typing *\>\>
STUDY* on the Matlab command line will list field values:

``` matlab
>> STUDY =

  struct with fields:

          history: 'STUDY = []; [STUDY ALLEEG] = std_checkset(STUDY, ALLEEG);'
          datasetinfo: [1×10 struct]
          name: 'N400STUDY'
          task: 'Auditory task: Synonyms Vs. Non-synonyms, N400'
          notes: ''
          filename: 'N400empty.study'
          filepath: '.'
          subject: {'S02'  'S05'  'S07'  'S08'  'S10'}
          group: {}
          session: []
          condition: {'non-synonyms'  'synonyms'}
          etc: [1×1 struct]
          cache: []
          preclust: [1×1 struct]
          cluster: [1×1 struct]
          changrp: [1×61 struct]
          design: [1×1 struct]
          currentdesign: 1
          saved: 'yes'
```

Computing and plotting channel measures
----------------------------------------
You may use the function [pop_precomp.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_precomp.m) (which calls function
[std_precomp.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_precomp.m) to precompute channel measures). For instance,
the following code calls the graphic user interface for computing
measures in channels.

``` matlab
 >> [STUDY ALLEEG] = pop_precomp(STUDY, ALLEEG);
```

On the other hand, entering the code below will interpolate all the
missing channels and compute ERP for all channels and all datasets of a
given study. Here an additional parameter to remove the baseline (*erpparams*) comprised from latencies (-200 0) has been used as well.

``` matlab
>> [STUDY ALLEEG] = std_precomp(STUDY, ALLEEG, 'channels', 'erp', 'on', 'erpparams', {'rmbase' [-200 0]});
```

The plotting may then be performed using the same functions that are used
for component clusters. For instance, to plot the grand average ERP for
channel 'Oz', you may try:

``` matlab
>> STUDY = std_erpplot(STUDY, ALLEEG, 'channels', {'Oz'});
```

You may retrieve data by adding output variables as described in the help message of the [std_erpplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_erpplot.m) function, and then replot it using the std_plotcurve function.

``` matlab
[STUDY erpdata erptimes] = std_erpplot(STUDY, ALLEEG, 'channels', {'Oz'}, 'timerange', [-200 1000]);
std_plotcurve(erptimes, erpdata, 'plotconditions', 'together', 'plotstderr', 'on', 'figure', 'on', 'filter', 30);
```

As shown above, the [std_plotcurve.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_plotcurve.m) function has additional
parameters to plot the standard error which are not available from the
EEGLAB graphic interface. The output of the function [std_erpplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_erpplot.m) can also be controlled by the addition of
parameters native to [std_erpplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_erpplot.m) and [pop_erpparams.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_erpparams.m). 


For example, notice the addition of the
option *timerange* above to constrain the latency range to be between
-200 to 1000ms.

![File:Erp_chann_oz](/assets/images/Erp_chann_Oz.png)

Try some other commands from the channel plotting graphic interface and look at what is returned in the history (via the [eegh.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eegh.m) function) to plot ERP in different formats.

Plotting measures and retrieving results
-----------------------------------------
All STUDY plotting functions are able to return plotted results. After
plotting STUDY results, look into the EEGLAB history (<i>eegh</i> from
the Matlab command line) to see which STUDY function was called, then
look at the help of this function. It is usually possible to add
additional parameters.

For example, if the following line appears in the EEGLAB history:

``` matlab
>> STUDY = std_erpplot(STUDY,ALLEEG,'channels',{ 'FP1'});
```

Simply add the two output, one for the ERP data and one for the ERP
time, as follow

``` matlab
>> [STUDY erpdata erptimes] = std_erpplot(STUDY,ALLEEG,'channels',{ 'FP1'});
```

The <i>erpdata</i> array contains the ERP data for all subjects.
Its size also depends on the STUDY design. The following command will
plot the ERP for all subjects (included in the design) for the first
cell in the STUDY design.

``` matlab
>> figure; plot(erptimes, erpdata{1});
```

The small script computes time-frequency decomposition on a small study.
It also compares a time-frequency decomposition at the dataset
level with a time-frequency decomposition at the STUDY level. The
data for this script is available
[here](https://sccn.ucsd.edu/eeglab/download/STERN_test_1file_per_subject.zip).

``` matlab
% Compute newtimef on first dataset for channel 1
options = {'freqscale', 'linear', 'freqs', [3 25], 'nfreqs', 20, 'ntimesout', 60, 'padratio', 1,'winsize',64,'baseline', 0};
TMPEEG = eeg_checkset(ALLEEG(1), 'loaddata');
figure; X = pop_newtimef( TMPEEG, 1, 1, [TMPEEG.xmin TMPEEG.xmax]*1000, [3 0.8] , 'topovec', 1, 'elocs', TMPEEG.chanlocs, 'chaninfo', TMPEEG.chaninfo, 'plotphase', 'off', options{:},'title',TMPEEG.setname, 'erspmax ',6.6);

% Compute newtimef for all datasets and plot first channel of first dataset
[STUDY, ALLEEG] = std_precomp(STUDY, ALLEEG, 'channels','recompute','on','ersp','on','erspparams',{'cycles' [3 0.8] 'parallel' 'on' options{:} },'itc','on');
STUDY = std_erspplot(STUDY,ALLEEG,'channels',{TMPEEG.chanlocs(1).labels}, 'subject', 'S02', 'design', 1 );
```

This is the result of the script below (after clicking on the plot to remove the side panels adjusting the color scale). 
It is not surprising that the result is the same since the same functions
are being used in both cases.

![border\|700px](/assets/images/newtimef_res.png)


Computing component measures
-----------------------------
The function pop_precomp.m can also be used to compute measures when
working with components. Similarly to when working with channels, this
function calls the function std_precomp.m to precompute component
measures. The syntax is very similar in both cases. For
instance, the function pop_precomp called in the following way will
launch the graphic user interface for computing measures on components:

``` matlab
[STUDY ALLEEG] = pop_precomp(STUDY, ALLEEG, 'components'); % pop up graphical interface
```

The same operation may be performed without the need to use the
GUI when the function is called with parameters defining the type of
measure that wants to be computed. For example, in the following code
snippet, ERP will be computed for all components:

``` matlab
[STUDY ALLEEG] = std_precomp(STUDY, ALLEEG, 'components', 'recompute', 'on', 'erp', 'on', 'filter', 30);
```

The type of measures computed are in close relationship with the
hypothesis that wants to be tested, and the selection of the measures
technically constrains the type of analysis that can be performed. For
instance, in the next section, the measures from each component will be
aggregated in order to perform clustering on them. In the EEGLAB jargon,
this is called *pre-clustering*. The measures used at the pre-clustering
level have to be precomputed to be used for plotting. Then, ahead of
pre-clustering, a careful assessment of the measures to be used and the
parameters to use on its generation have to be carried.

Computing the measures on components may be computationally expensive,
especially if time-frequency measures are generated. Fortunately, the
measures for the tutorial data have been precomputed in the file
downloaded. Here is the code used for generating the measures in the
file:

``` matlab
[STUDY ALLEEG] = std_precomp(STUDY, ALLEEG, 'components',...
    'erp','on','erpparams',{'rmbase' [-200 0] },...
    'scalp','on',...
    'spec','on','specparams',{'freqrange' [3 50] 'specmode' 'fft' 'logtrials' 'off'},...
    'ersp','on','erspparams',{'cycles' [3 0.8] 'nfreqs' 100 'ntimesout' 200},...
    'itc','on');
```

Remember that you do not need to generate the measures now, the file
downloaded already contains these files.

Component clustering and pre-clustering
----------------------------------------
To select components of a specified cluster for sub-clustering from the command line, the call to [pop_preclust.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_preclust.m) should have the
following format (do not attempt to run this code):

``` matlab
 >> [ALLEEG, STUDY] = pop_preclust(STUDY, ALLEEG, cluster_id,  {'measure1' 'opt 1' 'opt 2'}, {'measure2' 'opt 3' 'opt 4'});
```

If 'cluster_id' is the index of the cluster you wish to sub-cluster,
use an empty array (\[\]) for the whole STUDY (top-level) clustering if
no other clusters are yet present. Components rejected because of high residual variance (see the help message of the [std_editset.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_editset.m)
function above) will not be considered for clustering. Following, we
will see the meaning of the rest of the options.

For the STUDY created above, we usualy first meed to compute all available activity measures (in this case, this is not necessary since the measures have been precomputed in the file you have downloaded). 

Note that changing the pre-existing
measure parameters might require EEGLAB to recompute or adapt some of
these measures (spectral frequency range \[3 25\] Hz; ERSP /ITC
frequency range \[3 25\] Hz, cycles \[3 0.5\], time window \[-1600
1495\] ms, and 'padratio' 4). To specify clustering on power spectra in
the \[3 30\]-Hz frequency range, ERPs in the \[100 600\]-ms time window,
dipole location information (weighted by 10), and ERSP information with
the above default values, type:

``` matlab
>> [STUDY ALLEEG] = std_preclust(STUDY, ALLEEG, 1,...
        {'spec' 'npca' 10 'weight' 1 'freqrange' [3 25] },...
        {'erp' 'npca' 10 'weight' 1 'timewindow' [100 600]  'erpfilter' '20'},...
        {'dipoles' 'weight' 10},...
        {'ersp' 'npca' 10 'freqrange' [3 25]  'timewindow' [-1600 1495]  'weight' 1 'norm' 1 'weight' 1});
```

Alternatively, to enter these values in the graphic interface, type:

``` matlab
>> [STUDY ALLEEG] = pop_preclust(STUDY, ALLEEG);
```

The equivalent command line call to cluster the *STUDY* is:

``` matlab
>> [STUDY] = pop_clust(STUDY, ALLEEG, 'algorithm','kmeanscluster', 'clus_num', 10);
```

or to pop up the graphic interface:

``` matlab
>> [STUDY] = pop_clust(STUDY, ALLEEG);
```

Visualizing component clusters
-------------------------------
The main function for visualizing component clusters is [pop_clustedit.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_clustedit.m). 

To pop up this interface, simply type:

``` matlab
>> [STUDY] = pop_clustedit(STUDY, ALLEEG);
```

This function calls a variety of plotting functions for plotting: - scalp maps ([std_topoplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_topoplot.m)), 
 - power spectra ([std_specplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_specplot.m)), 
 - equivalent dipoles ([std_dipplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_dipplot.m)), 
 - ERPs ([std_erpplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_erpplot.m)), 
 - ERSPs ([std_erspplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_erspplot.m)), 
 - ITCs ([std_itcplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_itcplot.m)). 

All of these functions follow the same calling format (though [std_dipplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_dipplot.m) is slightly different; refer to its help message). 
Using function [std_topoplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_topoplot.m) as an example, the following code will plot the

average scalp map for Cluster 3 :

``` matlab
 >> [STUDY] = std_topoplot(STUDY, ALLEEG, 'clusters', 3, 'mode', 'together');
```

The code snippet below will plot the average scalp map for Cluster 3
plus the scalp maps of components belonging to Cluster 3:

``` matlab
 >> [STUDY] = std_topoplot(STUDY, ALLEEG, 'clusters', 3, 'mode', 'apart');
```

The following code will plot component 3 of Cluster 6:

``` matlab
 >> [STUDY] = std_topoplot(STUDY, ALLEEG, 'clusters', 6, 'comps', 3);
```

To read any information about the cluster (scalp map, power spectrum,
ERSP, ITC, etc...) for further processing under Matlab, you should refer
to the part of the tutorial describing [the STUDY.cluster structure](/tutorials/ConceptsGuide/Data_Structures.html#the-study-structure).

The EEGLAB developers plan to develop more functions allowing users to
directly access clustering data. Some plotting functions, like the one
described below, are currently available only from the command line.

Plotting statistics and retrieving statistical results
--------------------------------------------------------
All plotting functions able to compute statistics will return the
statistical array in their output. You must first enable statistics
either from the graphic interface or using a command-line call. 

For instance to compute condition statistics for ERP (bot channel and
component clusters), type:

``` matlab
>> STUDY = pop_statparams(STUDY, 'condstats', 'on');
```

Then, for a given channel, type:

``` matlab
>> [STUDY erpdata erptimes pgroup pcond pinter] = std_erpplot(STUDY,ALLEEG,'channels',{ 'FP1'});
```

Or, for a given component cluster, type:

``` matlab
>> [STUDY erpdata erptimes pgroup pcond pinter] = std_erpplot(STUDY,ALLEEG,'clusters', 3);
```

Now, typing:

``` matlab
>> pcond

    pcond =
        [820x1]
```

The statistical array contains 820 p-values, one for each time point.

Note that the type of statistics returned depends on the parameter you
selected in the ERP parameter graphic interface (for instance, if you
selected 'permutation' for statistics, the p-value based on surrogate
data will be returned).

The 'pgroup' and 'pinter' arrays contain statistics across groups and
the ANOVA interaction terms, respectively, if both groups and conditions
are present. 

Note that for more control, you may also use directly call the [statcond.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=statcond.m) function, giving the 'erpdata' cell array as
input (the 'erpdata' cell array is the same as the one stored in the
*STUDY.cluster.erpdata* or the *STUDY.changrp.erpdata* structures for
the cluster or channel of interest). 
See the help message of the [statcond.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=statcond.m) function for more help on this subject. Other functions such as [std_specplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_specplot.m), [std_erspplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_erspplot.m), and [std_itcplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_itcplot.m) behave in a
similar manner (see the function help messages for more details).

Multiple components from the same subjects in ICA clusters
------------------------------------------------------------

When plotting ICA clusters, EEGLAB allows by default several components
from the same subject to be included in a given cluster. This can sometimes cause problems when using statistics. 

When you include more than one component from the same subject, you are not making inferences
about the general population of subjects anymore but instead about
components of the specific subjects you are studying. It is all a matter
of how many components you have per subject compared to the number of
subjects. 

For example, if you have on average one component per subject
(some subjects having 0, some other two components in the cluster), and you
have 200 subjects, then the original null hypothesis (which allows
making inferences about the general population of subjects) is mostly
preserved. If you have 10 subjects and 10 components per subject, it is
not.

In general, when multiple components from the same subjects in ICA
clusters becomes a problem, we prefer to use at most one
component per subject per cluster because this avoids having to
compromise with the statistics (this is possible when using the EEGLAB Corrmap
plugin for clustering data; there is also a version of *kmean* that
forces to use one component per cluster). Alternatively, remove components manually in clusters.

Computing and plotting custom measures
-----------------------------------------
It is possible to compute custom measures on STUDY in the std_precomp
function. It is now possible to execute a specific function on each
EEGLAB dataset of the selected STUDY design. The first argument to the
function is an EEGLAB dataset. 

For example, using the anonymous function
*@(EEG)mean(EEG.data,3)* will compute the ERP for the STUDY design. EEG is
the EEGLAB dataset corresponding to each cell design. They correspond to
datasets computed dynamically based on the design selection - although
they use data from datasets contain in the STUDY, they do not
necessarily correspond to these datasets. 

Before calling the custom
function, the [std_precomp.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_precomp.m) function will apply dataset modifiers such as
'rmclust', 'rmicacomps' or 'interp' to remove components or interpolate
channels. You may use the option 'customparam' to pass additional
parameters to your custom function.

The output of the custom computation is returned in the *customRes* variable. The output of the custom function may be an numerical array or a structure. For example, the function below computes the ERP of the EEG data for
each channel and plots it. Note that the [std_plotcurve.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_plotcurve.m) expects channels in the last dimension so the output the *mean* function applied to the *EEG.data* structure is transposed.

``` matlab
[~,~,customRes] = std_precomp(STUDY, ALLEEG, 'channels', 'customfunc', @(EEG,varargin)(mean(EEG.data,3))', 'interp', 'on');
std_plotcurve([1:size(customRes{1})], customRes, 'chanlocs', ALLEEG(1).chanlocs);
```

The script below only processes one channel and plots it.

``` matlab
[~,~,customRes] = std_precomp(STUDY, ALLEEG, { 'Fz' },  'customfunc', @(EEG,varargin)mean(EEG.data,3)', 'interp', 'on');
figure; plot([customRes{:} ]);
```
