---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: home
nav_exclude: true
has_toc: true
---
# Welcome to EEGLAB Wiki
[right|400px](/Image:Eeglab_small.jpg "wikilink")

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

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


#### Download EEGLAB


-    [EEGLAB hardware and software
    recommendations](/EEGLAB_hardware_and_software_recommendations "wikilink")
-   [Download EEGLAB as zip
    file](http://sccn.ucsd.edu/eeglab/download.php)
-    [Download EEGLAB from GIT](/How_to_download_EEGLAB "wikilink")
-    [Download a compiled version of
    EEGLAB](/A13:_Compiled_EEGLAB "wikilink")
-    [EEGLAB extensions/plugins](/EEGLAB_Extensions "wikilink")
-    [EEGLAB revision history](/EEGLAB_revision_history "wikilink")
-    [Bugs and Suggestions](/EEGLAB_Bugs "wikilink")

#### Useful EEGLAB documentation pages

The EEGLAB tutorial is available in a subsequent section on this page.
Other type of documentation are listed below.

-    [EEGLAB News and Discussion email lists](/EEGLAB_mailing_lists "wikilink")
-    [EEGLAB reference articles - Please cite](/EEGLAB_References "wikilink")
-    [Using EEGLAB vs. Commercial EEG
    Software](/EEGLAB_vs._Commercial_EEG_Software "wikilink")
-    [Working with EEGLAB and Fieldtrip](/EEGLAB_and_Fieldtrip "wikilink")
-    [Running EEGLAB on open source
    Octave](/Running_EEGLAB_on_Octave "wikilink")
-    [EEGLAB on MATLAB versus Python](/EEGLAB_and_python "wikilink")
-    [NEW Running EEGLAB on high performance computing resources - The Open EEGLAB Portal](/EEGLAB_and_high_performance_computing "wikilink")
-    [Using EEGLAB to process MEG data](/EEGLAB_and_MEG_data "wikilink")
-    [EEGLAB History: The first decade of
    2001-2011](/The_first_decade_of_EEGLAB "wikilink")
-    [Run EEGLAB on NSF
    Supercomputers\!](https://sccn.ucsd.edu/wiki/EEGLAB_on_NSG)

#### Troubleshooting

-    [EEGLAB and MEX functions to recompile](/Mex_EEGLAB "wikilink")
-    [EEGLAB filtering FAQ](/Firfilt_FAQ "wikilink")
-    [Use Google - add "eeglablist" or "EEGLAB" to your
    querry](http://google.com)
-    [Ask eeglablist@sccn.ucsd.edu](mailto:eeglablist@sccn.ucsd.edu)
-    [(requires subscription here)](/EEGLAB_mailing_lists "wikilink")
-    [Post a bug on Bugzilla for EEGLAB](https://sccn.ucsd.edu/bugzilla/)
-    [Other TIPS and FAQ](/TIPS_and_FAQ "wikilink")

#### Other downloads and resources

 - [EEGLAB extensions and
    plugins](/EEGLAB_Extensions_and_plugins "wikilink")
-  [Publicly available datasets for
    download](http://sccn.ucsd.edu/~arno/fam2data/publicly_available_EEG_data.html)
-    [Channel Location Files
    download](/Channel_Location_Files "wikilink")
-    [Download EEGLAB test scripts](/EEGLAB_test_cases "wikilink")

## The EEGLAB Tutorial Outline

### Quick tutorial resources

[Online EEGLAB Workshop](/Online_EEGLAB_Workshop "wikilink") - Includes
online videos, slides, and tutorial materials\!

[Download the 2011 Wiki Tutorial as a
PDFbook](ftp://sccn.ucsd.edu/pub/PDF_EEGLAB_Wiki_Tutorial.pdf) (later
versions of the tutorial in PDF format are not available for technical
reasons)

[Quick ICA Component Rejection
Tutorial](/Quick_Rejection_Tutorial "wikilink")

<hr>

This tutorial was written by [Arnaud
Delorme](mailto:EEGLAB@sccn.ucsd.edu) with feedback and edits from [Scott Makeig](mailto:EEGLAB@sccn.ucsd.edu). Other contributors include Dung Truong, Claire Braboszcz, Makoto Miyakoshi, Ramon Martinez, Devapratim Sarma, Derrick Lock,
Hilit Serby, Toby Fernsler.
