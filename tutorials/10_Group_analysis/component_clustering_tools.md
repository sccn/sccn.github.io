---
layout: default
title: f. Component clustering
parent: 10. Group analysis
grand_parent: Tutorials 
---

Clustering ICA components
===========================


This part of the tutorial will demonstrate how to use EEGLAB to
interactively preprocess, cluster, and then visualize the dynamics of
ICA (or other linear) signal components across one or many subjects by
operating on the [tutorial study](ftp://sccn.ucsd.edu/pub/5subjects_full.zip).

Note that with only a few subjects and a few clusters (a necessary
limitation, to be able to easily distribute the example), it may not be
possible to find six consistent component clusters with uniform and
easily identifiable natures. We have obtained much more satisfactory
results clustering data from 15 to 30 or more subjects.

After following this tutorial using the sample data, we recommend you
create a study for a larger group of datasets, if available, whose
properties you know well. Then try clustering components this study in
several ways. Carefully study the consistency and properties of the
generated component clusters to determine which method of clustering
produces clusters adequate for your research purposes.

Note that we recommend performing one ICA decomposition on all the data
collected in each data collection session, even when task several
conditions are involved. In our experience, ICA can return a more stable
decomposition when trained on more data. Having components with common
spatial maps also makes it easier to compare component behaviors across
conditions. To use the same ICA decomposition for several conditions,
simply run ICA on the continuous or epoched data *before* extracting
separate datasets corresponding to specific task conditions of interest.
Then extract specific condition datasets; they will automatically
inherit the same ICA decomposition.

An example of ICA clustering is also available
[here](/Independent_Component_Clustering_Example "wikilink").

<details>
  <summary><b>Why cluster ICA components?</b></summary>


<u>Is my Cz your Cz?</u> 

To compare electrophysiological results across
subjects, the usual practice of most researchers has been to identify
scalp channels (for instance, considering recorded channel "Cz" in every
subject's data to be spatially equivalent). Actually, this is an
idealization, since the spatial relationship of any physical electrode
site (for instance, Cz, the vertex in the International 10-20 System
electrode labeling convention) to the underlying cortical areas that
generate the activities summed by the (Cz) channel may be rather
different in different subjects, depending on the physical locations,
extents, and particularly the orientations of the cortical source areas,
both in relation to the 'active' electrode site (e.g., Cz) and/or to its
recorded reference channel (for example, the nose, right mastoid, or
other site).

That is, data recorded from equivalent channel locations (Cz) in
different subjects may sum activity of different mixtures of underlying
cortical EEG sources, no matter how accurately the equivalent electrode
locations were measured on the scalp. This fact is commonly ignored in
EEG research.

<br>
<br>

<u>Is my IC your IC?</u> 

Following ICA (or other linear) decomposition,
however, there is no natural and easy way to identify a component from
one subject with one (or more) component(s) from another subject. A pair
of independent components (ICs) from two subjects might resemble and/or
differ from each other in many ways and to different degrees -- by
differences in their scalp maps, power spectra, ERPs, ERSPs, ITCs, or
etc. Thus, there are many possible (distance) measures of similarity,
and many different ways of combining activity measures into a global
distance measure to estimate component pair similarity.
<br>
<br>
Thus, the problem of identifying equivalent components across subjects
is non-trivial. An attempt at doing this for 31-channel data was
published in [2002](http://sccn.ucsd.edu/science2002.html) and
[2004](http://sccn.ucsd.edu/papers/PLOS04_animation.html) in papers
whose preparation required elaborate custom scripting (by Westerfield,
Makeig, and Delorme). A
[2005](http://sccn.ucsd.edu/papers/OntonTheta05.html) paper by Onton et
al. reported on dynamics of a frontal midline component cluster
identified in 71-channel data. EEGLAB now contains functions and
supporting structures for flexibly and efficiently performing and
evaluating component clustering across subjects and conditions. With its
supporting data structures and stand-alone **'std_**' prefix analysis
functions, EEGLAB makes it possible to summarize results of ICA-based
analysis across more than one condition from a large number of subjects.
This should make more routine use of linear decomposition and ICA
possible to apply to a wide variety of hypothesis testing on datasets
from several to many subjects.
<br> <br>
The number of EEGLAB clustering and cluster-based functions will
doubtless continue to grow in number and power in the future versions,
since they allow the realistic use of ICA decomposition in
hypothesis-driven research on large or small subject populations.
<br> <br>
<b>NOTE:</b> Independent component clustering (like much other data clustering)
has no single 'correct' solution. Interpreting results of component
clustering, therefore, warrants caution. Claims to discovery of
physiological facts from component clustering should be accompanied by
thoughtful caveat and, preferably, by results of statistical testing
against suitable null hypotheses.

</details>

EDIT STUDY INTERFACE CLUSTERING
====

The second checkbox removes all current cluster information and will be explained when we perform ICA component clustering. When
cluster information is present, it is not possible to add or remove
datasets and to edit certain fields (because this would not be
consistent with the already computed clusters). 


Re-clustering the
altered STUDY does not take much time, once the pre-clustering
information for the new datasets (if any) has been computed and
stored.

- The *Components* column contains the
components for each dataset that will be clustered. , so the same ICA decomposition was
used for both conditions. Uniform default values will be used by
EEGLAB for those fields. 

Note that if you
change the component selection (by pressing the relevant push button),
all datasets with the same subject name and the same session number
will also be updated (as these datasets are assumed to have the same
ICA components).


Both raw data and ICA component data may be processed in STUDY. 


Optional: Pre-selecting components for clustering.

If you wish to process ICA component data with the STUDY you need to complete the step below.

Simply press the *Select by r.v.* (r.v. = residual variance) push
button in the gui above. 

The entry box below will appear. This allows
you to set a threshold for residual variance of the dipole model
associated with each component.


*Note*: Using this option requires that dipole model information ispresent in each dataset. Use EEGLAB plug-in [dipfit.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=dipfit.m)

options and save the resulting dipole models into each dataset
*before* calling the study guis. Otherwise, options related to dipole
localization will not be available.


![Pop study rv gui](/assets/images/Pop_study_rv.gif)


This interface allows specifying that components used in clustering
will only be those whose equivalent dipole models have residual dipole
variance of their component map, compared to the best-fitting
equivalent dipole model projection to the scalp electrodes, less than
a specified threshold (0% to 100%). The default r.v. value is 15%,
meaning that only components with dipole model residual variance of
less than 15% will be included in clusters. This is useful because of
the modeled association between components with near 'dipolar' (or
sometimes dual-dipolar) scalp maps with physiologically plausible
components, those that may represent the activation in one (or two
coupled) brain area(s). For instance, in the interface above, the
default residual variance threshold is set to 15%. This means that
only component that have an equivalent dipole model with less than 15%
residual variance will be selected for clustering. Pressing *OK* will
cause the component column to be updated in the main study-editing
window. Then press *OK* to save your changes.


*Important note for ICA component clustering*:
 
 Continuous data collected in one task or
experiment session are often separated into epochs defining different
task conditions (for example, separate sets of epochs time locked to
targets and non-targets respectively). Datasets from different
conditions collected in the same *session* are assumed by the clustering
functions to have the same ICA component weights (i.e., the same ICA
decomposition is assumed to have been applied to the data from all
session conditions at once). If this was not the case, then datasets
from the different conditions must be assigned to different
*sessions*.





Note that channel
locations may be edited for all datasets at the same time (simply call
menu item <span style="color: brown">Edit → Channel locations</span>). 



Clustering Methods
-------------------

EEGLAB implements the following clustering methods:

- [PCA method (original method)](/tutorials/multi-subject/component-clustering-tools.html#preparing-to-cluster-pre-clustering-with-pca-original-method)
- [Affinity Product Method](/tutorials/multi-subject/component-clustering-tools.html#preparing-to-cluster-pre-clustering-with-affinity-product-method)
- [Using the Corrmap plugin](/tutorials/multi-subject/component-clustering-tools.html#finding-clusters-with-the-corrmap-plugin)
- Measure Product (MP) method 
*The MP method has been removed from version 9.0.3.3b for
lack of stability but you may contact the author at nima@sccn.ucsd.edu
to obtain a copy.*

Preparing to cluster (Pre-clustering) with PCA (original) method
-----------------------------------------------------------------

The next step before clustering is to prepare the *STUDY* for
clustering. This requires:
 - first, identifying the components from each
dataset to be entered into the clustering (as explained briefly above),
- second, computing component activity measures for each study dataset
(described below). 

For this purpose, for each dataset component thepre-clustering function [pop_preclust.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_preclust.m) first computes

desired condition-mean measures used to determine the cluster 'distance'
of components from each other. 

The condition means used to construct
this overall cluster 'distance' measure may be selected from a palette
of standard EEGLAB measures: ERP, power spectrum, ERSP, and/or ITC, as
well as the component scalp maps (interpolated to a standard scalp grid)
and their equivalent dipole model locations (if any).


*Note*: Dipole locations are the one type of pre-clustering information*not* computed by [pop_preclust.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_preclust.m). As explained previously,

to use dipole locations in clustering and/or in reviewing cluster
results, dipole model information must be computed separately and savedin each dataset using the [dipfit.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=dipfit.m) EEGLAB plug-in.



The aim of the pre-clustering interface is to build a global distance
matrix specifying 'distances' between components for use by the
clustering algorithm. This component 'distance' is typically abstract,
estimating how 'far' the components' maps, dipole models, and/or
activity measures are from one another in the space of the joint,
PCA-reduced measures selected. This will become clearer as we detail the
use of the graphic interface below.

### Computing component measures
Invoke the pre-clustering graphic interface by using menu item
<span style="color: brown">Study → Build pre-clustering array</span>.


![image not found](/assets/images/Pop_preclust.gif)
The top section of the [pop_preclust.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_preclust.m) gui above allows

selecting clusters from which to produce a refined clustering. There
is not yet any choice here -- we must select the parent datasets that
contain all selected components from all datasets (e.g., the
components selected at the end of the previous section).

The checkboxes on the left in the second section of the [pop_preclust.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_preclust.m) interface above allow selection of the

component activity measures to include in the *cluster location
measure* constructed to perform clustering. 

The goal of the
pre-clustering function is to compute an N-dimensional cluster
position vector for each component. These 'cluster position' vectors
will be used to measure the 'distance' of components from each other
in the N-dimensional cluster space. The value of N is arbitrary but,
for numeric reasons pertaining to the clustering algorithms, should be
kept relatively low (e.g., \<10). 

In the cluster position vectors, for
example, the three first values might represent the 3-D (x,y,z)
spatial locations of the equivalent dipole for each component. The
next, say, 10 values might represent the largest 10 principal
components of the first condition ERP, the next 10, for the second
condition ERP, and so on.

If you are computing (time/frequency) spectral perturbation images,
you cannot use all their (near-3000) time-frequency values, which are
redundant, in any case. Here also, you should use the *Dim.* column
inputs to reduce the number of dimensions (for instance, to 10).
*Note*: [pop_preclust.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_preclust.m) reduces the dimension of the cluster

position measures (incorporating information from ERP, ERSP, or other
measures) by restricting the cluster position vectors to an
N-dimensional principal subspace by principal component analysis
(PCA).

#### Dimension normalization
 
You may wish to "normalize" these principal dimensions for the location
and activity measures you select so their metrics are equivariant across
measures. Do this by checking the checkbox under the *norm* column. 

This
'normalization' process involves dividing the measure data of all
principal components by the standard deviation of the first PCA
component for this measure. 

You may also specify a relative weight
(versus other measures). For instance if you use two measures (A and B)
and you want A to have twice the "weight" of B, you would normalize both
measures and enter a weight of 2 for A and 1 for B. If you estimate that
measure A has more relevant information than measure B, you could also
enter a greater number of PCA dimension for A than for B. Below, for
illustration we elect to cluster on all six allowed activity measures.

#### Component measures

All the measures described below, once computed, can be used
for clustering and/or for cluster visualization (see the following
section of the tutorial, ['Visualize Component Cluster Information'](/tutorials/multi-subject/component-clustering-tools.html#viewing-component-clusters)). 
If you do not
wish to use some of the measures in clustering but still want to be able
to visualize it, select it and enter 0 for the PCA dimension. This
measure will then be available for cluster visualization although it
will not have been used in the clustering process itself. This allows an
easy way of performing exploratory clustering on different measure
subsets.


-   **Spectra:** The first checkbox in the middle right of the
    pre-clustering window (above) allows you to include the log mean
    power spectrum for each condition in the pre-clustering measures.
    Clicking on the checkbox allow you to enter power spectral
    parameters. In this case, a frequency range \[lo hi\] (in Hz) is
    required. 
    
    Note that for clustering purposes (but not for display),
    for each subject individually, the mean spectral value (averaged
    across all selected frequencies) is subtracted from all selected
    components, and the mean spectral value at each frequency (averaged
    across all selected components) is subtracted from all components.
    The reason is that some subjects have larger EEG power than others.
    If we did not subtract the (log) means, clusters might contain
    components from only one subject, or from one type of subject (e.g.,
    women, who often have thinner skulls and therefore larger EEG than
    men).
    
-   **ERPs:** The second checkbox computes mean ERPs for each condition.
    Here, an ERP latency window \[lo hi\] (in ms) is required.
    
-   **Dipole locations:** The third checkbox allows you to include component
    equivalent dipole locations in the pre-clustering process. Dipole
    locations (shown as \[x y z\]) automatically have three dimensions
    
    *Note:* It is not yet possible to cluster on dipole orientations. 
    
    As mentioned above, the equivalent dipole model for each component and
    dataset must already have been pre-computed. If one component is    modeled using two symmetrical dipoles, [pop_preclust.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_preclust.m)

    will use the average location of the two dipoles for clustering
    purposes (Note: this choice is not optimum).
    
-   **Scalp maps:** The fourth checkbox allows you to include scalp map
    information in the component 'cluster location'. You may choose to
    use raw component map values, their laplacians, or their spatial
    gradients. 
    
    *Note*: We have obtained fair results for main components
    using laplacian scalp maps, though there are still better reasons to
    use equivalent dipole locations instead of scalp maps. 
    
    You may also
    select whether or not to use only the absolute map values, their
    advantage being that they do not depend on (arbitrary) component map    polarity. As explained in the [ICA_decomposition.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=ICA_decomposition.m), ICA

    component scalp maps themselves have no absolute scalp map polarity.
    
-   **ERSPs and/or ITCs:** The last two checkboxes allow including
    event-related spectral perturbation information in the form of
    event-related spectral power changes (ERSPs), and event-related
    phase consistencies (ITCs) for each condition. 
    To compute the ERSP
    and/or ITC measures, several time/frequency parameters are required.
    To choose these values, you may enter the relevant {
    {File\|timefreq.m} } keywords and arguments in the text box. You may
    for instance enter '' 'alpha', 0.01'' for significance masking. See    the [timefreq.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=timefreq.m) help message for information about

    time/frequency parameters to select.
    
-   **Final number of dimensions:** An additional checkbox at the bottom
    allows further reduction of the number of dimensions in the
    component distance measure used for clustering. Clustering
    algorithms may not work well with measures having more than 10 to 20
    dimensions. 
    
    For example, if you selected all the options above and
    retained all their dimensions, the accumulated distance measures
    would have a total of 53 dimensions. This number may be reduced
    (e.g., to a default 10) using the PCA decomposition invoked by this
    option. Note that, since this will distort the cluster location
    space (projecting it down to its smaller dimensional 'shadow'), it
    is preferable to use this option carefully. For instance, if you
    decide to use reduced-dimension scalp maps and dipole locations that
    together have 13 dimensions (13 = the requested 10 dimensions for
    the scalp maps plus 3 for the dipole locations), you might
    experiment with using fewer dimensions for the scalp maps (e.g., 7
    instead of 10), in place of the final dimension reduction option (13
    to 10).

- Finally, the [pop_preclust.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_preclust.m) gui allows you to choose to save

the updated *STUDY* to disk.

In the [pop_preclust.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_preclust.m) select all methods and leave all

default parameters (including the dipole residual variance filter at the
top of the window), then press *OK*. As explained below, for this
tutorial STUDY, measure values are already stored on disk with each
dataset, so they need not be recomputed, even if the requested
clustering limits (time, frequency, etc.) for these measured are
reduced.


### Re-using component measures computed during pre-clustering

Computing the spectral, ERP, ERSP, and ITC measures for clustering may,
in particular, be time consuming -- requiring up to a few days if there
are many components, conditions, and datasets! The time required will
naturally depend on the number and size of the datasets and on the speed
of the processor. 

Future EEGLAB releases will implement parallel
computing of these measures for cases in which multiple processors are
available. Measures previously computed for a given dataset and storedby [std_preclust.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=std_preclust.m) will not be recomputed, even if you narrow

the time and/or frequency ranges considered. Instead, the computed
measure information will be loaded from the respective Matlab files inwhich it was saved by previous calls to [pop_preclust.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_preclust.m).


Measure data files are saved in the same directory/folder as the
dataset, and have the same dataset name -- but different filename
extensions. For example, component ERSP information for the dataset
*syn02-S253-clean.set* is stored in a file named
*syn02-S253-clean.icaersp*. As mentioned above, for convenience it is
recommended that each subject's data be stored in a different
directory/folder. If all the possible clustering measures have been
computed for this dataset, the following Matlab files should be in the
*/S02/* dataset directory:

-   *syn02-S253-clean.icaerp* (ERPs)
-   *syn02-S253-clean.icaspec* (power spectra)
-   *syn02-S253-clean.icatopo* (scalp maps)
-   *syn02-S253-clean.icaersp* (ERSPs)
-   *syn02-S253-clean.icaitc* (ITCs)


The parameters used to compute each measure are also stored in the file,
for example the frequency range of the component spectra. Measure files
are standard Matlab files that may be read and processed using standard
Matlab commands. The variable names they contain should be
self-explanatory.


*Note:* For ERSP-based clustering, if a parameter setting you have
selected is different than the value of the same parameter used to
compute and store the same measure previously, a query window will pop
up asking you to choose between recomputing the same values using the
new parameters or keeping the existing measure values. Again, narrowing
the ERSP latency and frequency ranges considered in clustering will not
lead to recomputing the ERSP across all datasets.

Finding clusters with PCA (original) method
--------------------------------------------

### Computing and visualizing clusters.
Calling the cluster function [pop_clust.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_clust.m), then selecting

menu item <span style="color: brown">Study → Cluster components</span> will
open the following window.


![set clustering algo](/assets/images/Pop_clust.gif)



Currently, two clustering algorithms are available: 'kmeans' and
'neural network' clustering. 

As explained earlier, 'kmeans' requires
the Matlab Statistics Toolbox, while 'neural network' clustering uses
a function from the Matlab Neural Network Toolbox. 

Note that the
default number of clusters (10 in this case) is set so on average
there will be one computed per subject per cluster. For example, if
about 20 components per subjects are selected based on the residual
variance thereshold and the STUDY contains 10 subjects, the average
number of cluster will be set to 20 - so each cluster will contains on
average 10 components.


Both algorithms require entering a desired number of clusters (first
edit box).
 
 An option for the *kmeans()* algorithm can relegate
'outlier' components to a separate cluster. Outlier components are
defined as components further than a specified number of standard
deviations (3, by default) from any of the cluster centroids. To turn
on this option, click the upper checkbox on the left. Identified
outlier components will be put into a designated *Outliers* cluster
(Cluster 2). 

Click on the lower left checkbox to save the clustered
studyset to disk. If you do not provide a new filename in the adjacent
text box, the existing studyset will be overwritten.

In the [pop_clust.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_clust.m) gui:

 - enter *10* for the number of
clusters 
- check the *Separate outliers ...* checkbox to detect and
separate outliers. 
- Then press *OK* to compute clusters (clustering is
usually quick). 

The cluster editing interface detailed in the next
section will automatically pop up. 

Alternatively, for the sample data,
load the provided studyset *N400clustedit.study* in which
pre-clustering information has already been stored.

Preparing to cluster (Pre-clustering) with Affinity Product Method
--------------------------------------------------------------------
In Affinity Product clustering, IC measures, except equiv. dipoles,
(ERP, ERSP...) are compared for each IC pair and their dissimilarity is
multiplied together to form a combined pairwise dissimilarity matrix.
This matrix is then normalized, weighted and added to the normalized and
weighted IC equiv. dipole distance matrix. 
The final dissimilarity
matrix is then clustered using affinity clustering method (Fig. below).

As you can see this method does not perform any dimensionality reduction
on EEG measures (i.e PCA) as it only calculates pairwise
(dis)similarities.These similarity matrices (correlations) has to be
calculated in the pre-clustering step.


![900px\|center](/assets/images/Hybrid-measure-product-clustering-flowchart.png)


### Computing pairwise measures for AP clustering.

Invoke the pre-clustering graphic interface by using menu item
<span style="color: brown">Study → Affinity Product clustering → Build pre-clustering array</span>.


![Image:Mpreclust snapshot.png](/assets/images/Mpreclust_snapshot.png)


In the GUI you can select EEG measures for which pre-clustering matrices
should be calculated. 

Use 'Re-Calculate All' option to remove all these
matrices before calculating new ones. This might be useful if you have
changed the subset of STUDY components to be clustered.

### Finding clusters with Affinity Product Method

After the pre-clustering step (above) is finished, you can cluster STUDY
components based on any combination of measures included in
pre-clustering. The final clustering is performed on the combined
pairwise distance matrix using [Affinity Propagation](http://www.psi.toronto.edu/affinitypropagation/) algorithm.

#### Computing clusters.

Invoke the MP clustering graphic interface by using menu item
<span style="color: brown">Study → Affinity Product clustering → Cluster Components</span> will open the following window.

![Image:Popmpcluster.png](/assets/images/Popmpcluster.png)

Here you can specify the number of clusters and control the effect of
equiv. dipole distances in the clustering by setting the 'Relative
dipole weight' parameter. For example, by setting this value to 0.8, the
final dissimilarity matrix will consist of 80% distance dissimilarity
and 20% of other measures combined together.

Please note that the number of returned clusters may slightly (up to 5%)
differ from the number requested in the GUI. Also, currently only
clustering the parent cluster (containing all components) is supported.

An option for the Affinity Clustering algorithm can relegate 'outlier'
components to a separate cluster. Outlier components are defined as
components further than a specified number of standard deviations (3, by
default) from any of the cluster centroids. To turn on this option,
click the lower checkbox on the left. Identified outlier components will
be put into a designated Outliers cluster (Cluster 2).

Finding clusters with the Corrmap plugin
------------------------------------------
Corrmap is a plugin that is included in EEGLAB and that clusters
components based on the correlation of their scalp topographies. The
documentation for this plugin is available on Stefan Debener web page at
[<http://www.debener.de/corrmap/corrmapplugin1.html>](http://www.debener.de/corrmap/corrmapplugin1.html).

Viewing component clusters
----------------------------Calling the cluster editing function [pop_clustedit.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_clustedit.m) using

menu item <span style="color: brown">Study → Edit → plot clusters</span> will
open the following window. 

Note: The previous menu will also call
automatically this window after clustering has finished.



![600px](/assets/images/Pop_clustedit.gif)



Of the 305 components in the sample *N400STUDY* studyset, dipole model
residual variances for 154 components were above 15%. These components
were omitted from clustering. The remaining 151 components were
clustered on the basis of their dipole locations, power spectra, ERPs,
and ERSP measures into 10 component clusters.


### Visualizing clusters

Selecting one of the clusters from the list
shown in the upper left box displays a list of the cluster components in
the text box on the upper right. 

Here, *SO2 IC33* means "independent
component 33 for subject SO2," etc. 

The *All 10 cluster centroids*
option in the (left) text box list will cause the function to display
results for all but the *ParentCluster* and *Outlier* clusters.
Selecting one of the plotting options below (left) will then show all 10
cluster centroids in a single figure. 

For example, pressing the *Plot
scalp maps* option will produce the figure below:



![525px](/assets/images/Cls_plotclustmap1.gif)



In computing the mean cluster scalp maps (or scalp map centroids), the
polarity of each of the cluster's component maps was first adjusted so
as to correlate positively with the cluster mean (recall that component
maps have no absolute polarity). Then the map variances were equated.
Finally, the normalized means were computed.


To see individual component scalp maps for components in the cluster,
select the cluster of interest in the left column (for example, *Cluster
8* as in the figure above Then press the *Plot scalp maps* option in the
left column. The following figure will appear. (Note: Your *Cluster 8*
scalp map may differ after you have recomputed the clusters for the
sample STUDY).


![525px](/assets/images/Cls_plotclustmap2.gif)



To see the relationship between one of the cluster centroid maps and the
maps of individual components in the cluster, select the cluster of
interest (for instance Cluster 8), and press the *Plot scalp maps*option in the *right* [pop_clustedit.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_clustedit.m) column.



*Note:* Channels missing from any of the datasets do not affect clustering
or visualization of cluster scalp maps. Component scalp maps areinterpolated by the [toporeplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=toporeplot.m) function, avoiding the need

to restrict *STUDY* datasets to a common 'always clean' channel subset
or to perform 'missing channel' interpolation on individual datasets.


![525px](/assets/images/Cls_plotclustmap3.gif)



You may also plot scalp maps for individual components in the cluster by
selecting components in the right column and then pressing *Plot scalp
maps* (not shown).


A good way to visualize all the average cluster measures at once is to
first select a cluster of interest from the cluster list on the left
(e.g., 'Cluster 8'), and then press the *Plot cluster properties* push
button. The left figure below presents the Cluster-8 mean scalp map
(same for both conditions), average ERP and spectrum (for these, the two
conditions are plotted in different colors), average ERSP and ITC (grand
means for both conditions; the individual conditions may be plotted
using the *Plot cluster properties* push button). The 3-D plot on the
bottom left presents the locations of the centroid dipole (red) and
individual component equivalent dipoles (blue) for this cluster.


![775px](/assets/images/Cls_plotclust.gif)



To quickly recognize the nature of component clusters by their activity
features requires experience. 

Here Cluster 8 accounts for some right
occipital alpha activity -- note the strong 10-Hz peak in the activity
spectra. The cluster ERPs show a very slow (1-Hz) pattern peaking at the
appearance of *first* words of the word pairs (near time -1 s). The
apparent latency shift in this slow wave activity between the two
conditions may or may not be significant. A positive (though still quite
low, 0.06) ITC follows the appearance of the first word in each word
pair (see Experimental Design), indicating that quite weakly
phase-consistent theta-band EEG activity follows first word onsets.
Finally, blocking of spectral power from 7 Hz to at least 25 Hz appears
just after onset of the *second* words of word pairs (at time 0) in the
grand mean ERSP plot (blue region on top right)


To review all 'Cluster 8' component dipole locations, press the *Plot
dipoles* button in the left column. This will open the plot viewer
showing all the cluster component dipoles (in blue), plus the cluster
mean dipole location (in red). You may scroll through the dipoles one by
one, rotating the plot in 3-D or selecting among the three cardinal
views (lower left buttons), etc. Information about them will be
presented in the left center side bar (see the image below).


![525px](/assets/images/Cls_plotclustdip.gif)


As for the scalp maps, the [pop_clustedit.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_clustedit.m) gui will

separately plot the cluster ERPs, spectra, ERSPs or ITCs. Let us review
once more the different plotting options for the data spectrum. 

Pressing
the *Plot spectra* button in the left column will open a figure showing
the two mean condition spectra below.


![525px](/assets/images/Cls_plotclustspec1.gif)



Pressing the *Plot spectra* button in the right column with *All
components* selected in the left column will open a figure displaying
for each condition all cluster component spectra plus (in bold) their
mean.


![925px](/assets/images/Cls_plotclustspec2.gif)



Finally, to plot the condition spectra for individual cluster
components, select one component from the *Select component(s) to plot*
list on the right and press *Plot spectra* in the right column. 

For
example, selecting component 37 from subject S02 (*SO2 IC37*) will pop
up the figure below. Here, the single component spectra are shown in
light blue as well as the mean cluster spectrum (in black).



![650px](/assets/images/Cls_plotclustspec3.gif)


Editing clusters
-----------------
The results of clustering (by either the 'k-means' or 'Neural network'
methods) can also be updated manually in the preview cluster viewing and
editing window (called from menu item <span style="color: brown">Study → Edit/plot clusters</span>). These editing options allow flexibility for
adjusting the clustering. Components can be reassigned to different
clusters, clusters can be merged, new clusters can be created, and
'outlier' components can be rejected from a cluster. Note that if youmake changes via the [pop_clustedit.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_clustedit.m) gui, then wish to

cancel these changes, pressing the *Cancel* button will cause the
*STUDY* changes to be forgotten.



![image not found](/assets/images/Pop_clusedit.gif)



### Renaming a cluster
 
The *Rename selected cluster* option allows
you to rename any cluster using a (mnemonic) name of your choice.
Pressing this option button opens a pop-up window asking for the new
name of the selected cluster. For instance, if you think a cluster
contains components accounting for eye blinks you may rename it
"Blinks".

### Automatically rejecting outlier components:

Another editing
option is to reject 'outlier' components from a cluster *after*
clustering. 

An 'outlier' can be defined as a component whose cluster
location is more than a given number of standard deviations from the
location of the cluster centroid. 

Note that standard deviation and
cluster mean values are defined from the N-dimensional clustering space
data created during the pre-clustering process.

For example, if the size of the pre-clustering cluster location matrix
is 10 by 200 (for 200 components), then N = 10. The default threshold
for outlier rejection is 3 standard deviations. 

To reject 'outlier'
components from a cluster, first select the cluster of interest from the
list on the left and then press the *Auto-reject outlier components*
option button. A window will open, asking you to set the outlier
threshold. 'Outlier' components selected via either the *'eject outlier
components* option or the *Remove selected outlier component(s)* option
(below) are moved from the current cluster '\[Name\]' to a cluster named
'Outlier \[Name\]'.


### Removing selected outlier components manually
 Another way to
remove 'outlier' components from a cluster is to do so manually. This
option allows you to de-select seeming 'outlier' components irrespective
of their distance from the cluster mean. To manually reject components,
first select the cluster of interest from the list on the left, then
select the desired 'outlier' component(s) from the component list on the
right, then press the *Remove selected outlier comps.* button. A
confirmation window will pop up.


### Creating a new cluster

To create a new empty cluster, press the
*Create new cluster* option, this opens a pop-up window asking for a
name for the new cluster. If no name is given, the default name is 'Cls
\#', where '\#' is the next available cluster number. For changes to
take place, press the *OK* button in the pop-up window. The new empty
cluster will appear as one of the clusters in the list on the left of
the editing/viewing cluster window.


### Reassigning components to clusters

To move components between
any two clusters, first select the origin cluster from the list on the
left, then select the components of interest from the component list on
the right, and press the *Reassign selected component(s)* option button.
Select the target cluster from the list of available clusters.


### Saving changes

As with other pop_ functions, you can save the
updated *STUDY* set to disk, either overwriting the current version - by
leaving the default file name in the text box - or by entering a new
file name.

Hierarchic sub-clustering (PCA method only)
--------------------------------------------
The clustering tools also allow you to perform hierarchic
sub-clustering. For example, imagine clustering all the components from
all the datasets in the current *STUDY* (i.e., the Parent Cluster) into
two clusters. One cluster turn out to contain only artifactual non-EEG
components (which you thus rename the 'Artifact' cluster) while the
other contains non-artifactual EEG components (thus renamed
'Non-artifact').


*NOTE:* *This is only a quite schematic example for tutorial purposes: It
may normally <u>not</u> be possible to separate all non-brain artifact
components from cortical non-artifact components by clustering all
components into only two clusters -- there are too many kinds of scalp
maps and artifact activities associated with the various classes of
artifacts!*


![Image:Cluster_img3.gif](/assets/images/Cluster_img3.gif)



At this point, we might try further clustering only the 'Artifact'
cluster components, e.g., attempting to separate eye movement processes
from heart and muscle activity processes, or etc. A schematic of a
possible (but probably again not realistic) further decomposition is
shown schematically above.


In this case, the parent of the identified eye movement artifact cluster
is the 'Artifact' cluster; the child cluster of 'eye' artifacts itself
has no child clusters. On the other hand, clustering the 'Non-artifact'
cluster produces three child clusters which, presumably after careful
inspection, we decide to rename 'Alpha', 'Mu' and 'Other'.


To refine a clustering in this way, simply follow the same sequence of
event as described above. Call the pre-clustering tools using menu item
<span style="color: brown>Study \"> Build preclustering array</span>. You may now
select a cluster to refine. In the example above, we notice that there
seem to be components with different spectra in Cluster 8, so let us try
to refine the clustering based on differences among the Cluster-8
component spectra.


![775px](/assets/images/Pop_preclust1.jpg)



Select the <span style="color: brown>Study \"> Cluster components</span> menu
item. Leave all the defaults (e.g., 2 clusters) and press *OK*.


![image not found](/assets/images/Pop_clust2.gif)



The visualization window will then pop up with two new clusters under
Cluster 8.


![600px](/assets/images/Pop_clustedit2.gif)



Below the component spectra for Cluster 13 are plotted. Note that
Cluster-13 components have relatively uniform spectra.


![875px](/assets/images/Cls_plotclustspec4.gif)



You may also plot the scalp map of Cluster 13. All the cluster
components account for occipital activity and have similarly located
equivalent dipole sources.


![image not found](/assets/images/Cls_plotclustmap4.gif)


Clustering and study design
----------------------------

When pre-clustering ICA components, the current STUDY.design is taken
into account. 

For example, if you have two conditions per subject and
both conditions share the same set of ICA components, then during
preclustering, when computing the component distance measure used for
clustering, data measures from both conditions are concatenated. For
example, when using the mean power spectrum to cluster components,
instead of having say 50 spectral values (one per frequency) for each
component, during preclustering 100 values (two sets of 50 frequencies,
one for each condition) will be placed one after the other. EEGLAB will
not allow you to cluster components using a STUDY design that does not
include all STUDY data sets and all ICA components. 

Once your components
are clustered, it is possible to reduce the size of your STUDY design
(see below). However, if the design you are using when preclustering
your data does not include all datasets, it would not be possible to
include them in another design later on. 

To precluster, therefore we
advise using the simplest STUDY design possible. Often, this is the one
that is most natural for the experiment. An exception would be a case
when, for example, your experiment uses a 2x2 design, but you decide to
include a fifth condition for exploratory purposes. In this case an
initial 5x1 design should be used during preclustering. For the main
analysis, a 2x2 STUDY design (involving only 4 or the 5 conditions) can
be created, along with, perhaps, another 2x1 design to compare the fifth
condition (not included in the 2x2) versus one of the others.

*Note*: If you are using anatomical component information only (scalp
topographies and/or equivalent dipoles) and no other measures to cluster
components, then the STUDY design does not impact the clustering
solution.

After clustering, since all ICA components are included in the
clustering, ICA clusters are constant for all conditions and STUDY
designs. 

Once ICA components are clustered, it is possible to *compute
differences between conditions* using any STUDY design. Whenever you
select a different design, ICA components are assigned to the conditions
in the design according to your design as per the clustering solution.
For example, if you have only one ICA decomposition per subject and a
2x1 design (2 conditions, 1 subject group, collected in 1 session), then
both conditions share the same components.

Comparing activities of ICA components between conditions is like
comparing activities in different electrode channels. Comparing the
activities of a cluster of components between conditions could be seen
as similar to comparing the activity of an individually assigned
electrode channel for each subject (for instance, a channel to which
some measure projects most strongly). 

Remember that ICA components and
electrode channels are both <em>spatial filters.</em> Each electrode
channel gives the arithmetic difference between the potential reaching
some scalp electrode and the potential reaching a reference electrode
(or the mean of the potentials reaching the set of reference
electrodes). Each ICA component gives the arithmetic weighted
sum/difference of the signals reaching each of the electrodes. Here the
negatively weighted electrode signals can be said to serve the role of
the reference channel (although this channel combination will typically
be different for each component).

For STUDY designs in which component activities of two subject groups
are to be compared, the computed measure differences will be between
components for each group within each cluster.


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