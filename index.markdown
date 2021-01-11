---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: home
nav_exclude: true
has_toc: true
---
# Welcome to the EEGLAB Wiki





![EEGLAb sum-up picture](/assets/images/tuto_pic.png)




### Download EEGLAB

-    [EEGLAB hardware and software
    recommendations](/others/EEGLAB_hardware_and_software_recommendations.html)
-   [Download EEGLAB as a ZIP file](/others/How_to_download_EEGLAB.html)
-    [Download EEGLAB from GIT](/How_to_download_EEGLAB "wikilink")
-    [Download the compiled version of EEGLAB](/others/Compiled_EEGLAB.html)
-    [EEGLAB extensions/plugins](/others/EEGLAB_Extensions.html)
-    [EEGLAB revision history](/others/EEGLAB_revision_history.html)

### Useful EEGLAB documentation pages

The EEGLAB tutorial is available in a subsequent section on this page.
Other type of documentation are listed below.

-    [EEGLAB reference articles - Please cite](/others/EEGLAB_References.html)
-    [Quick ICA Component Rejection Tutorial](/tutorials/misc/Quick_Tutorial_on_Rejection.html)
-    [Using EEGLAB vs. Commercial EEG Software](/others/EEGLAB_vs_Commercial_EEG_Software.html)
-    [Working with EEGLAB and Fieldtrip](/others/EEGLAB_and_Fieldtrip.html)
-    [Using EEGLAB on open-source Octave](/others/Running_EEGLAB_on_Octave.html)
-    [Using EEGLAB on high performance computing resources](/others/EEGLAB_and_high_performance_computing.html)
-    [EEGLAB on MATLAB versus Python](/others/EEGLAB_and_python.html)
-    [EEGLAB History: The first two decades from 2001-2021](/others/The_first_decade_of_EEGLAB.html)

### Troubleshooting

-    [Ask eeglablist@sccn.ucsd.edu (requires subscription here)](/others/EEGLAB_mailing_lists.html)
-    [Use Google - add "eeglablist" or "EEGLAB" to your querry](http://google.com)
-    [Bugs and Suggestions](/others/EEGLAB_Bugs.html)
-    [Post a bug issues on Github](https://github.com/sccn/eeglab/issues)
-    [Download EEGLAB test cases](/EEGLAB_test_cases "wikilink")
-    [Other TIPS and FAQ](/FAQ/TIPS_and_FAQ)
-    [EEGLAB filtering FAQ](/FAQ/Firfilt_FAQ)

<h3><a href="/tutorials"><span style="color: black;">EEGLAB Tutorial</span></a></h3>
{%- assign children_list = site.pages | where: "parent", "Tutorials" -%}
{% include toc_nav.html nav=children_list %}

<h3><a href="/workshops"><span style="color: black;">Workshops</span></a></h3>
{%- assign children_list = site.pages | where: "parent", "Workshops" -%}
{% include toc_nav.html nav=children_list %}

<hr>

<i><font size="-1">This tutorial was written by <a href="mailto:EEGLAB@sccn.ucsd.edu">Arnaud
Delorme</a> with feedback and edits from <a href="mailto:EEGLAB@sccn.ucsd.edu">Scott Makeig</a>. Other essential contributors include Dung Truong, Claire Braboszcz, Makoto Miyakoshi, Ramon Martinez, Devapratim Sarma, Derrick Lock, Hilit Serby, Toby Fernsler.</font><i>

