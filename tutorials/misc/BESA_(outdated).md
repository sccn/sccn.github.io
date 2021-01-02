---
layout: default
title: BESA (outdated)
parent: Reference Topics
grand_parent: Tutorials
nav_order: 11
---
DIPFIT vs BESA study using the spherical head model
--------

We (AD) checked the results of fitting equivalent dipoles with DIPFIT
(spherical model) against results of BESA(3.0) for independent
components of data recorded in a working memory task in our laboratory.
There were 72 channels, of which 69 were used for dipole fitting. In
particular, we excluded tow EOG channels and the reference channel. We
performed ICA on data from three subjects and fit all 69 resulting
components with single dipoles using BESA (see the BESAFIT plug-in
Appendix) and DIPFIT. We then compared only those dipoles whose residual
variance was less than 15% (see plot below).

![Image:Comparedipfitbesa.gif](/assets/images/Comparedipfitbesa.gif)

Distances between equivalent dipole locations returned by DIPFIT1 and
BESA(3.0) were less than 3 mm (left panel) Note: The outliers were
infrequent failures to converge by either algorithm. Dipole angle
differences were below 2 degrees (middle panel). Residual variances
(mismatch between the component scalp map and the model pole projection)
were near equal (right panel). A few dipoles were localized with
residual variance below 15% by DIPFIT but not by BESA (4 of 213
components); a few others with residual variance below 15% by BESA but
not by DIPFIT (8 of 213 components). Optimization nonlinearities may
account for these small differences between the two algorithms, as the
solution models used in the two programs are theoretically identical.

The main advantage of using DIPFIT over BESA for localization of
equivalent dipoles for independent component scalp maps is that it is
integrated into Matlab and EEGLAB, and can be used in batch processing
scripts (see [Matlab
code](/#Using_DIPFIT_to_fit_EEG_or_ERP_scalp_maps "wikilink") and
[structures & functions](/#DIPFIT_structure_and_functions "wikilink")
above). BESA has additional capabilities not relevant to DIPFIT.
Succeeding versions of BESA did not allow a batch processing option.

### Spherical model error

The following article in Frontiers [Corrected Four-Sphere Head Model for
EEG Signals](https://www.frontiersin.org/articles/10.3389/fnhum.2017.00490/full)
claim "errors in the formulas \[for the spherical model\] both in the
original paper and in the book”, and then refer to a 1998 paper and 2006
book. It seems to me that Srinivasan made an error in 1998 that was
copied in his contribution to Nunez’ book in 2006. However, the author
have not looked up the original original work, which as far as we know
is [https://www.ncbi.nlm.nih.gov/pubmed/95707](https://www.ncbi.nlm.nih.gov/pubmed/95707) which is from 1979. And
note that in the 2nd half of the ’80s and certainly in the ‘90s the
4-concentric-sphere model was widely already (e.g. in BESA above). The
version of BESA we used to compare with Dipfit was BESA 3.0 which was
likely release before 1998 since it was released before BESA 99 (in
1999).

Our implementation in Dipfit (and Fieldtrip) was programmed by Robert
Oostenveld and is based on the Habilschrift (sort of advanced PhD thesis
that only exists in Germany) from Bernd Lutkenhoner from 1992. That
habilschrift is not available in pdf or online, but Robert Oostenveld
has a paper copy. The reason Robert Oostenveld used that description is
that it includes coordinate transformations for the dipole to be off
from the z-axis, i.e. at a arbitrary location in the brain. Right now,
until proven wrong, we don’t see a reason why the implementation in
Dipfit would be wrong, or that it would be based on an incorrect
published description.

There is another function to perform spherical source localization in
Brainstorm
<https://github.com/brainstorm-tools/brainstorm3/blob/master/toolbox/forward/bst_eeg_sph.m>
which is an approximation (Dipfit uses an exact computation, albeit a
series expansion that is truncated by default at order 60). It would be
worth to compare the results of this function with the result of Dipfit.