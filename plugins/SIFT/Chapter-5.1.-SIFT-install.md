---
layout: default
parent: SIFT
grand_parent: Plugins
render_with_liquid: false

title: Chapter-5.1.-SIFT-install
long_title: Chapter-5.1.-SIFT-install
---
It is assumed that you have **Matlab® 2008a** or later, the Signal
Processing Toolbox, Statistics Toolbox,
[EEGLAB](http://sccn.ucsd.edu/eeglab/) and the
[SIFT](http://sccn.ucsd.edu/wiki/SIFT#SIFT_Downloads) toolbox. SIFT should work with all versions of EEGLAB (10 and later). This version of the tutorial was tested with EEGLAB 2023.1.

To **get started**, follow these steps:

1\) Start MATLAB

2\) [Download EEGLAB](https://sccn.ucsd.edu/eeglab/download.php). Add EEGLAB root folder to the path (**File -\> Set Path; Add
Folder**)

3\) Type `eeglab` at the command prompt

4\) Use EEGLAB menu item "Manage extension," select SIFT, and install it

5\) Optional: if you want to use the ARfit
model-fitting algorithm.  You must manually install
as follows: Download the free ARfit package from
<https://climate-dynamics.org/software/#arfit>. After downloading and
unzipping the ARfit package, place the **/arfit/** folder in
**SIFT-path/external/** where **SIFT-path** is the full path to
the SIFT root directory.

6\) Once the EEGLAB main GUI is visible, you are good to go! You will
find SIFT under the EEGLAB menu: **Tools-\>SIFT**. SIFT will
automatically be made accessible whenever you start EEGLAB.

**Important note about SIFT GUIs:** Unfortunately, SIFT GUIs have grown unstable over the years as the Mathworks (the makers of MATLAB) has modified the function supporting it (changing some of the parameters, the function may crash or return an error). For example, on MATLAB 2023a on MAC, it is not possible to use the GUI edit boxes. Therefore, using the command line to set different options is preferable in some cases. We have included command line calls equivalent to the GUI in this tutorial.

