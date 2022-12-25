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

In [Mythical Man-Month, The: Essays on Software Engineering](https://www.amazon.com/Mythical-Man-Month-Software-Engineering-Anniversary/dp/0201835959),  Fred Brooks, a project manager for the IBM in the 1990s, emphasize how difficult it is to maintain the conceptual integrity of software products. The approach we have implemented in EEGLAB is to have a relatively small core, supplemented by plugins/extensions. The integrity of the EEGLAB core is maintained by  a single researcher (Arnaud Delorme), who has full understanding of the intricacies of all parts of EEGLAB. This researchers receive inputs from colleagues and other researchers. 

Having a single person maintain the conceptual integrity of a software is not ideal, but it works for relatively small projects like EEGLAB. This is the same approach Fieldtrip and Brainstrom where Robert Oostenveld and Francois Tadel, respectively, maintaining these software core integrity.

The advantange of EEGLAB is that, on top of this strong core, extensions and plugins may be developed by other researchers. This makes development of new features organic, and unsupervised, well adapted to open source research software. Researchers also get credit for their own extensions. Important extensions EEGLAB relies on are the clean_rawdata plugin to automatically clean data (Christian Kothe), ICLabel (Luca Pions Toninachi), FirFilt (Andreas Widmann), SIFT (Tim Mullen), LIMO (Cyril Pernet), etc...
