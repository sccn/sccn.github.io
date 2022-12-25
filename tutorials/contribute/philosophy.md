---
layout: default
title: Create an EEGLAB plugin
long_title: Create an EEGLAB plugin
parent: How to contribute?
grand_parent: Tutorials
---
EEGLAB development philosophy
========================
{: .no_toc }

In Mythical Man-Month, The: Essays on Software Engineering, Fred Brooks, a project manager for IBM in the 1990s, emphasize how difficult it is to maintain the conceptual integrity of software products. The approach we have implemented in EEGLAB is to have a relatively small core supplemented by plugins/extensions. 

The advantage of EEGLAB is that other researchers may develop extensions and plugins on top of this strong core. This makes developing new features organic and unsupervised, well adapted to open-source research software. Researchers also get credit for their own extensions, which motivates them to implement them. Important extensions EEGLAB relies on are the clean_rawdata plugin to automatically clean data (Christian Kothe), ICLabel (Luca Pions Toninachi), FirFilt (Andreas Widmann), SIFT (Tim Mullen), LIMO (Cyril Pernet), etc...
