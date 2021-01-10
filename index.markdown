---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: home
nav_exclude: true
has_toc: true
---
# Welcome to the EEGLAB Wiki

### Download EEGLAB

-    [EEGLAB hardware and software
    recommendations](/others/EEGLAB_hardware_and_software_recommendations.html)
-   [Download EEGLAB](/others/How_to_download_EEGLAB.html)
-    [Download EEGLAB from GIT](/How_to_download_EEGLAB "wikilink")
-    [Download a compiled version of EEGLAB](/others/Compiled_EEGLAB.html)
-    [EEGLAB extensions/plugins](/others/EEGLAB_Extensions.html)
-    [EEGLAB revision history](/others/EEGLAB_revision_history.html)
-    [EEGLAB reference articles - Please cite](/others/EEGLAB_References.html)

#### Useful EEGLAB documentation pages

The EEGLAB tutorial is available in a subsequent section on this page.
Other type of documentation are listed below.

-    [Using EEGLAB vs. Commercial EEG Software](/others/EEGLAB_vs_Commercial_EEG_Software.html)
-    [Working with EEGLAB and Fieldtrip](/others/EEGLAB_and_Fieldtrip.html)
-    [Running EEGLAB on open source Octave](/others/Running_EEGLAB_on_Octave.html)
-    [Running EEGLAB on high performance computing resources](/others/EEGLAB_and_high_performance_computing.html)
-    [EEGLAB on MATLAB versus Python](/others/EEGLAB_and_python.html)
-    [EEGLAB History: The first two decades from 2001-2021](/others/The_first_decade_of_EEGLAB.html)

#### Troubleshooting

-    [Ask eeglablist@sccn.ucsd.edu (requires subscription here)](/others/EEGLAB_mailing_lists.html)
-    [Use Google - add "eeglablist" or "EEGLAB" to your querry](http://google.com)
-    [Bugs and Suggestions](/others/EEGLAB_Bugs.html)
-    [Post a bug issues on Github](https://github.com/sccn/eeglab/issues)
-    [Other TIPS and FAQ](/TIPS_and_FAQ "wikilink")
-    [EEGLAB filtering FAQ](/Firfilt_FAQ "wikilink")

#### Other downloads and resources

-  [Publicly available datasets for download](/Tutorials/tutorial_data.html)
-  [Download EEGLAB test cases](/EEGLAB_test_cases "wikilink")
-  [Quick ICA Component Rejection Tutorial](/tutorials/misc/Quick_Tutorial_on_Rejection.html)

## The EEGLAB Tutorial Outline

<h1><a href="/tutorials">Tutorials</a></h1>
{%- assign children_list = site.pages | where: "parent", "Tutorials" -%}
{% include toc_nav.html nav=children_list %}

### Quick tutorial resources

<h1><a href="/workshops">Workshops</a></h1>
{%- assign children_list = site.pages | where: "parent", "Workshops" -%}
{% include toc_nav.html nav=children_list %}

<hr>

This tutorial was written by [Arnaud
Delorme](mailto:EEGLAB@sccn.ucsd.edu) with feedback and edits from [Scott Makeig](mailto:EEGLAB@sccn.ucsd.edu). Other contributors include Dung Truong, Claire Braboszcz, Makoto Miyakoshi, Ramon Martinez, Devapratim Sarma, Derrick Lock, Hilit Serby, Toby Fernsler.

## Links and Documentation



**Image below:** *Independent component of 252-channel EEG data
with bilateral occipital scalp projection.* Derived by independent
component analysis of approximately 700,000 points of data using
runica() in the EEGLAB Toolbox, implementing extended infomax ICA. Here,
the 252-channel data were reduced to 160 independent components by PCA
prior to ICA training. 

Channels located below the head center are shown
in this topoplot() as extending out from the model head borders. Note
that ICA finds the gradient of the projection from the source to the
skin surface not only at the scalp electrodes but also for channels on
the neck, forehead and temples. Residual variance of the bet-fiting
symmetric dual-dipole model in a model sphere head was 2.0%. Dipole
calculations used the DIPFIT plug in.

![Image:channel location.jpg](/assets/images/Channel_location.jpg)

