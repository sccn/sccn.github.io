---
layout: default
title: LIMO
long_title: LIMO
parent: Plugins
render_with_liquid: false
has_children: true
nav_order: 6
---
To view the plugin source code, please visit the plugin's [GitHub repository](https://github.com/LIMO-EEG-Toolbox/limo_meeg).

# LInear MOdeling of MEEG data

The LInear MOdelling of MEEG data (LIMO MEEG) toolbox is a Matlab toolbox dedicated to the statistical analysis of MEEG data. It has some  interfacing with EEGLAB (in particular the STUDY in the EEGLAB develop version) to act as a plug in. However, once data are imported all is performed within LIMO MEEG and the toolbox can thus work for any data sets.

This repo is the stable version of LIMO MEEG (v2) to be used with EEGLAB (https://sccn.ucsd.edu/eeglab/) but can be used with in other applications like FieldTrip (http://www.fieldtriptoolbox.org/) or BrainStorm (https://neuroimage.usc.edu/brainstorm/) for your research applications. The previous version (1.5) is now archived here: http://datashare.is.ed.ac.uk/handle/10283/2190

## Installation

Have EEGLAB installed (because we call some functions) and LIMO in the plug-in directory.

## Documentation
in the doc directory (a bit outdated)
and of course the [wiki](https://github.com/LIMO-EEG-Toolbox/limo_eeg/wiki)

## LIMO tutorial dataset

With the software we released a dataset that can now be cited and downloaded here: http://datashare.is.ed.ac.uk/handle/10283/2189

## Questions

Best to use the discussion forums like the eeglab mailing list or neurostar (tagging people) for general analysis questions.  
You can also email directly or raise a github issue, in particular for bugs.

## Contribute

Anyone is welcome to contribute ! check here [how you can get involved](https://github.com/LIMO-EEG-Toolbox/limo_eeg/blob/master/contributing.md), the [code of conduct](https://github.com/LIMO-EEG-Toolbox/limo_eeg/blob/master/code_of_conduct.md).

Contributors are listed [here](https://github.com/LIMO-EEG-Toolbox/limo_eeg/blob/master/contributors.md)
# **Tutorial**

Details on the different functions and usage can be found on the [wiki pages here](https://github.com/LIMO-EEG-Toolbox/limo_tools/wiki) while this is a step-by-step tutorial.

_Important notice_

Whatever you display using LIMO plotting functions, all the variables are returned in the Matlab workspace. For instance, if you plot all channels vs time (ERP results), then the raw statistical map and the significance mask are returned. If you plot a time course, that time course with confidence interval is returned, etc. You may type "who" on the Matlab command line to see these variables.

## Getting started

The tutorial is using [Wakeman and Henson (2015)](https://www.nature.com/articles/sdata20151) face data. In short, famous, unfamiliar and scrambled faces were presented, and repeated immediately or later. Subjects had to do a judgment task orthogonal to the design to keep them engaged. The EEG channels were extracted and preprocessed. [DOWNLOAD THE DATA FOR THIS TUTORIAL HERE](https://openneuro.org/datasets/ds002718/versions/1.0.5) in BIDS format.

This tutorial assumes you are using the latest [EEGLAB](https://github.com/sccn/eeglab) version (2020.0 or later) that uses [STUDY](https://sccn.ucsd.edu/wiki/Chapter_02:_STUDY_Creation) to link with [LIMO tools](https://github.com/LIMO-EEG-Toolbox/limo_tools).


 