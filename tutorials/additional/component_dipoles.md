---
layout: default
title: component dipole
parent: z. additional
grand_parent: Tutorials
---

Our sample
decomposition used in this tutorial is based on clean EEG data, and may
have fewer artifactual components than decompositions of some other
datasets. 

The main criteria for recognizing brain-related components
are that they have:

1.  Dipole-like scalp maps,
2.  Spectral peaks at typical EEG frequence is (i.e., 'EEG-like'
    spectra) and,
3.  Regular ERP-image plots (meaning that the component does not account
    for activity occurring in only a few trials).

The component below has a strong alpha band peak near 10 Hz and a scalp
map distribution compatible with a left occipital cortex brain source.

When we localize ICA sources using single-dipole or dipole-pair source
localization. Many of the 'EEG-like' components can be fit with very low
residual variance (e.g., under 5%). 

![325px]({{ site.baseurl }}/assets/images/I94component2_properties.jpg)
 


<img src="https://sccn.github.io/assets/images/Comp252.jpg">



The EEGLAB v4.32 <a href="http://sccn.ucsd.edu/eeglab/locatefile.php?file=topoplot.m">topoplot.m</a> above shows an independent
component whose bilateral equivalent dipole model had only 2% residual
variance across all 252 electrode locations. This <a href="http://sccn.ucsd.edu/eeglab/locatefile.php?file=binica.m">binica.m</a>
decomposition used PCA to reduce the over 700,000 data points to 160
principal dimensions (a ratio of 28 time points per ICA weight).

</details>