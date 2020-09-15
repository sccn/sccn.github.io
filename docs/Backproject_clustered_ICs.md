---
layout: default
title: Backproject clustered ICs
permalink: /docs/Backproject_clustered_ICs
parent: Docs
---

**Note: In this page I call 'cluster' in the sense of 'independent
component clusters created by EEGLAB STUDY'. Also, IC stands for
independent component.**

## What is std_backproj

The backprojection means the forward mixing process from EEG sources
(i.e. ICs) to scalp channels. std_backproj is recommended for

  - Quickly showing cluster-to-channel backprojection at the group level
    in the form of ERP and variance accounted.
  - Creating another set of .set files that have only ICs included in
    the selected cluster(s).

It comes with a powerful (for EEGLAB) interactive visualization tools
too.

Note that the envelope plots and percent variance accounted for (PVAF)
calculated here are different from those produced by std_envtopo(). The
difference derives from that std_backproj() computes envelopes and PVAF
across subjects, while std_envtopo() computes them across clusters.

Note also that PVAF is subadditive, namely
PVAF(a)+PVAF(b)+PVAF(c)\>=PVAF(a+b+c) because (a+b+c) causes
cancellation.

## Why std_backproj

  - As a visualization tool for the group-level source-to-channel
    backprojection

std_backproj provides the quickest pathway to visualize the group-level
IC clustering results backprojected to a single-channel ERP/variance
accounted. std_backproj() performs the following operations

1.  Identifies which ICs are included acorss the selected clusters (by
    using the admittedly 'apparently complex scheme' by the developer)
2.  Open each selected dataset, reject all ICs that are not included in
    the selected cluster(s).
3.  Compute ERP/variance accounted.
4.  Repeat above 2 and 3 for all the datasets.
5.  Compute the grand-average ERP/variance accounted across all
    datasets.
6.  Visualize the results.

<!-- end list -->

  - As a group-level filter to manually exclude non-EEG ICs for SIFT and
    Measure Projection

One may use it as a group-level filter. Creating STUDY is to clean the
data since it provides two powerful filters

1.  To kick out ICs with dipoles located outside the brain
2.  To kick out ICs whose dipoles' residual variance is larger than a
    certain threshold (default 15%) This usually removes 70-80% of ICs.
    Nonetheless, quite a few number of artifactual ICs survives these
    criteria. I show example below. This is the spectrum plot of
    STUDY-level IC clusters. One can easily notice non-EEG spectrum
    patterns (i.e. non-1/f patterns) in Cluster 5, 6, 12, 18, 37, and 40
    (highlighted with red crosses). Total of 83/1066 ICs (7.8%) in the
    final clustering results are identified as non-EEG sources.

[500px|Figure 6. Cluster-level filtering using
spectra.](/File:Std_backproj_example.jpg "wikilink")

To address this issue, one may use std_backproj in the following way:

1.  Create STUDY and cluster ICs as usual, but only precompute spectra.
2.  Set the final cluster number to be large (e.g. 40).
3.  Identify clusters that shows apparent EMG or whatever non-EEG
    pattern (i.e. non 1/f curve) in the spectra plot.
4.  Select the remaining good clusters to backproject to create whole
    another set of datasets with good ICs.

The finally created super-clean datasets are perfect for **SIFT** (now
all ICs are clean and usable\!), **Measure Projection** (it does have
eyeCatch to exclude EOG ICs, but does not have a solution to exclude
EMG, so EMG ICs should be better removed beforehand), and so on.

## Screenshots

[500px|Figure 1. std_backproj:Compute
backprojection](/File:Std_backproj01.png "wikilink")

[800px|Figure 2. std_backproj:Plot ERP
results](/File:Std_backproj02.png "wikilink")

[800px|Figure 3. std_backproj:Plot PVAF(percent variance accounted
for)](/File:Std_backproj03.png "wikilink")

## Validation

I performed validation to make sure that nothing wrong should happen in
figuring out the labyrinth of STUDY.

**Materials and Methods**

1.  Load a STUDY with 17 IC Clusters, select Cluster 3,9,14,17 for
    inclusion and 2,6 for exclusion, start backprojection. Save the new
    .set files with the selected ICs to the folder X.
2.  Show Fz ERP obtained from std_backproj.
3.  Clear the STUDY. Next, load all the .set files from the folder X.
    Compute grand average of Fz ERP for comparison. Compare the two ERP
    plots in the figure below.

[800px|Figure 4. std_backproj: The result compared with grand-average
of the backprojected acorss all the
subjects](/File:Validation1.png "wikilink")

**Results**

1.  The effect of ascii conversion was in the order of 10^-9 (see the
    top plot below).
2.  The difference between the two results were in the order of 10^-4
    (see the middle plot below).
3.  However, the main difference was in DC part that was 3.7853e-04. The
    difference in AC part was in the order of 10^-7 (see the bottom plot
    below_.
4.  The SNR in the AC part is at least 120dB (ERP wave ranges is about
    1; AC difference in the order of 0.0000001)

[800px|Figure 5. std_backproj: validation
results](/File:Validation2.png "wikilink")

**Conclusion** The method fulfills the precision in practice. I don't
know exactly where the numerical difference in both DC and AC come from.

Authors: Makoto Miyakoshi. SCCN, INC, UCSD