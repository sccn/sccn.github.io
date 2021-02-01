---
layout: default
title: EEGLAB on Octave
long_title: EEGLAB on Octave
parent: Interoperability
---
Running EEGLAB on Octave
====

Why Octave?
---

MATLAB, although quite efficient,
can be expensive. 
We have attempted to tackle this problem and, as of 2021, we are supporting Octave (both command line calls and graphic interface).

# Running EEGLAB on Octave

EEGLAB on Octave is not as stable as EEGLAB on Matlab. EEGLAB on Matlab should be your first choice. Your second choice should be the compiled version of EEGLAB, and the third and last choice should be EEGLAB on Octave.

Install Octave and EEGLAB
-------------------------

Download the latest version of Octave from [this
page](https://www.gnu.org/software/octave/download.html). EEGLAB has
been best tested using Octave 6.1 on Windows but might also run on later
versions and other platforms. We recommend the Octave installer for Windows, which has all toolboxes (signal processing, statistics, etc...) pre-installed. 

### Optional octave settings

To avoid having Octave show warning messages constantly, change the startup option and add "--traditional --brainless --quiet" (on Windows, select the Octave icon's property, and add the following options to the *Target* field).

### Non-windows Octave releases

If you are running Octave on Linux or macOS, in addition to Octave, you will need to install the Octave signal
processing and statistics package. On the Octave command line, type:

```
pkg install -forge control
pkg install -forge signal
pkg load signal
pkg install -forge io
pkg install -forge statistics
pkg load statistics
```

Note that you need to run the last command <em>pkg load signal</em> and <em>pkg load statistics</em>
every time you start Octave.

### Install EEGLAB

EEGLAB for Octave is a work in progress. As of EEGLAB 2021.0, we recommend using the development version of [EEGLAB on GitHub](https://github.com/sccn/eeglab). For later EEGLAB versions, you may use the official EEGLAB releases.

To install the development version of EEGLAB, install [Git for windows](https://git-scm.com/download/win) and clone the repository with submodules. If you encounter problems with Octave, please submit an issue on [GitHub](https://github.com/sccn/eeglab/issues).

Known issues with EEGLAB and Octave graphics compatibility
----------------------------------------------------------

All EEGLAB signal processing functions should run on Octave. Although
Octave is supposed to be fully compatible
with MATLAB, the Octave
graphic rendering engine sometimes cannot render all EEGLAB graphics subtleties. In particular, we have encountered the following
issues:

-   Graphical figure updating is buggy. Users must move their mouse for multi-panel figures to be updated. Or sometimes, the figure itself must be moved or resized to be shown properly. For example, the *eegplot.m* interactive data
    scrolling function is not fully functional: selecting data regions in continuous data involves waiting for 10 seconds or so between mouse clicks.
-   Speed: Processing data is often about twice slower in Octave.
-   Plug-ins need to be installed manually (downloaded as zip files and
    uncompressed in the EEGLAB plugins folder). Most plugins (including
    SIFT and LIMO) have not been tested on Octave and will likely not be
    functional. They could probably be made functional by their
    developers or by motivated users.

Nevertheless, even some of the most complex EEGLAB plots can be rendered on Octave - for example, below, dipole plots in MATLAB (left)
and Octave (right) match perfectly.

 ![dipole in matlab and octave](/assets/images/Eeglab_dipoles_matlab_octave.png)

If you modify an interactive EEGLAB
function for that purpose and want others to benefit from your changes,
fork the code and create a pull request as explained on [this
page](/tutorials/contribute/Contributing_to_EEGLAB.html#forking-the-eeglab-repository). [This other 
page](/tutorials/contribute/) contains additional
information on how to contribute to EEGLAB.

Comparing EEGLAB output in Octave and Matlab
----------------------------------------------
Below is a time-frequency decomposition plotted by Octave 4.4 for the
EEGLAB tutorial dataset by the EEGLAB/MATLAB code below.

``` matlab
% cd xxxxx/eeglab        % move to the proper directory/folder
% octave --traditional   % start Octave

eeglab; % call EEGLAB
EEG = pop_loadset('sample_data/eeglab_data_epochs_ica.set');  % load an EEGLAB dataset
newtimef(EEG.data(1,:,:), EEG.pnts, [-1000 2000], EEG.srate, [3 0.5]); % compute and plot a trial-average ERSP
```

![](/assets/images/Octave2.png)

For comparison, below is the graphic output of *newtimef.m* run in MATLAB.

![600px\|EEGLAB newtimef output](/assets/images/Eeglab_newtimef2.png)

