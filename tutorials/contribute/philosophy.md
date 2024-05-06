---
layout: default
title: EEGLAB dev philosophy
long_title: EEGLAB dev philosophy
parent: Contribute
grand_parent: Tutorials
nav_order: 2
---
EEGLAB development philosophy
========================
{: .no_toc }

In [Mythical Man-Month, The: Essays on Software Engineering](https://www.amazon.com/Mythical-Man-Month-Software-Engineering-Anniversary/dp/0201835959), Fred Brooks, a project manager for IBM in the 1990s, emphasizes how difficult it is to maintain the conceptual integrity of software products. The approach we have implemented in EEGLAB is to have a relatively small core supplemented by plugins/extensions. 

The advantage of EEGLAB is that other researchers may develop extensions and plugins on top of this strong core. This makes developing new features organic and unsupervised, well adapted to open-source research software. Researchers also get credit for their own extensions, which motivates them to implement them. Important extensions EEGLAB relies on are the clean_rawdata plugin to automatically clean data (Christian Kothe), ICLabel (Luca Pions Toninachi), FirFilt (Andreas Widmann), SIFT (Tim Mullen), LIMO (Cyril Pernet), etc...
