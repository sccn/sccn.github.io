---
layout: default
title: BSS Comparison
permalink: /docs/BSS_Comparison
parent: Docs
---

[Figure 4B from Delorme et al., Independent EEG sources are
dipolar](../assets/images/Delorme_Fig4B.jpg)

This web page is associated with the paper

> **Independent EEG sources are dipolar**
> by Arnaud Delorme, Jason Palmer, Julie Onton, Robert Oostenveld, and
> Scott Makeig

accepted for publication in <i>PloS One</i> in December, 2011.

### Abstract

Independent component analysis (ICA) and blind source separation (BSS)
methods are increasingly used to separate individual brain and non-brain
source signals mixed by volume conduction in electroencephalographic
(EEG) and other electrophysiological recordings. We compared results of
decomposing thirteen 71-channel human scalp EEG datasets by 22 ICA and
BSS algorithms, assessing the pairwise mutual information (PMI) in scalp
channel pairs, the remaining PMI in component pairs, the overall mutual
information reduction (MIR) effected by each decomposition, and
decomposition ‘dipolarity’ defined as the number of component scalp maps
matching the projection of a single equivalent dipole with less than a
given residual variance. The least well-performing algorithm was
principal component analysis (PCA); best performing were AMICA and other
likelihood/mutual information based ICA methods. Though these and other
commonly-used decomposition methods returned many similar components,
across 18 ICA/BSS algorithms mean dipolarity varied linearly with both
MIR and with PMI remaining between the resulting component time courses,
a result compatible with an interpretation of many maximally independent
EEG components as being volume-conducted projections of
partially-synchronous local cortical field activity within single
compact cortical domains.

To encourage further method comparisons, the data and software used to
prepare the results are available below.

### How to add one or more new algorithms to the list and plot results of their application to the data used in our paper

### 0\. Download the data and plotting functions

The data used in the manuscript and the associated plotting functions
are available [**HERE**](ftp://sccn.ucsd.edu/pub/mica_release.zip)
(**Note:** The total file size is 1.2GB. For users with slow or
unreliable web connections, we recommend using *wget* which is native or
downloadable for Linux, Mac, and Windows. From a terminal commandline,
issue the command

`          wget `<ftp://sccn.ucsd.edu/pub/mica_release.zip>

The advantage of using *wget* is that if interrupted, it will resume
from the point at which it stopped in the previous attempt). Email any
questions to EEGLAB at UCSD dot edu.

#### 1\. Edit the script 'processdat.m'

Edit the Matlab script **processdat.m**, adding your algorithm (*MyICA*,
called by *matlab_function()* ) at the end of the list like this
(assume here that 47 algorithms are then in the list; yours then should
be 48):

`       allalgs(48).algo = 'matlab_function';   % name of Matlab function - the function must be added`
`                                               %   to the list of functions recognized by pop_runica (see`
`                                               %   pop_runica() help message for how to add a function to this list)`
`       allalgs(48).speed = 0;                  % speed of the algorithm (simply enter 0)`
`       allalgs(48).name = 'MyICA';             % brief name or acronym for the algorithm (for figures etc...)`
`       allalgs(48).options = { };              % options to give to the pop_runica function to forward`
`                                               %   to your function (if/as needed)`

Note: You may add several BSS algorithms, each time incrementing the
index to 48, 49, 50, etc... Note that if you run the same algorithm with
different parameters, you need to give it a new name.

#### 2\. Run your algorithm on each dataset

If your algorithms has index 48, to apply it to all 13 datasets run this
loop in MATLAB:

`>>  ALGONUM = 48;`
`    for d=1:13`
`        DATASET=d; processdat;`
`    end`

#### 3\. Compute the mutual information reduction (MIR) produced by your algorithm

To compute MIR (mutual information reduction) for all datasets, in the
function **mutualinfoalgo.m**, add the name of your algorithm to the
list of algorithms at the beginning of the function. **NOTE**: THIS MUST
be the same name as the string **allalgs(48).name** above. The function
will rescan all algorithms on all datasets; this may take several hours.

#### 4\. Plot the results together with those for other algorithms as shown in our Figure 4

Finally, add the name of your algorithm to the beginning of the
**plotresults.m** script. Because some ICA algorithms are computed but
not plotted, you must add the name of your algorithm to the list. Then

`>> plotresults`

#### 5\. Send us a copy?

We would be pleased to receive a copy of resulting plots (\>\> print
-depsc MyCA.eps ), if you so wish, so as to publicize them on this web
page. Send us as well the MIR file with your results in it, plus a
paragraph on the nature of the algorithm(s) you added to the list, and a
reference article (if any). Finally, let us know whether or not you give
your permission to publish the results on this wiki.

Mail results, questions, and suggestions to EEGLAB at SCCN dot UCSD dot
edu.