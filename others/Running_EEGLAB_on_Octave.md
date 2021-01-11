---
layout: default
title: EEGLAB on Octave
parent: Interoperability
---
Running EEGLAB on Octave <span style="color: green">- DONE</span>
====

Why Octave?
---

MATLAB, although quite efficient,
can be expensive. 
We have attempted to tackle this problem and, as of 2018, we are supporting Octave (command line calls only, no graphic support). In our
tests, Octave is about 50% slower than MATLAB, but this can easily be
compensated by increasing the number of processors assigned to a
specific processing task. Note that EEGLAB functions have not been
parallelized (except for a few rare exceptions). Therefore, you are required
to open a Octave/MATLAB session on each node and run custom scripts you
write to take advantage of your parallel processing capability.

# Running EEGLAB on Octave


To run EEGLAB on Octave, one must call EEGLAB functions from the Octave
command line. The EEGLAB graphic user interface (GUI) and functions that
create interactive pop-up windows might run on Octave, but are not actively supported. However,
all scripts that call EEGLAB <em>pop_</em> functions should work and
plot results if their pop-up interactive window function is not engaged.

How to install and open Octave
------------------------------

Download the latest version of Octave from [this
page](https://www.gnu.org/software/octave/download.html). EEGLAB has
been best tested using Octave 4.4, but should also run on later
versions.

Then start Octave. Some Octave modules need to be installed for EEGLAB
to function properly. Octave needs to be started with the option
<em>--traditional</em> to ensure maximal compatibility with MATLAB. From
the command line, start Octave using:


``` matlab
octave --traditional
```


This option is likely available from the Octave GUI settings (if you are
using the Octave GUI). Then, you will need to install the Octave signal
processing package. If the signal processing package is not installed,
about 5% of EEGLAB functions will not run. On the Octave command line,
type:

```
pkg install -forge control
pkg install -forge signal
pkg load signal
```

Note that you need to run the last command <em>pkg load signal</em>
every time you start Octave from the command line. (If you are using the
Octave graphic interface, there might be a way to load it automatically).
You may also install the statistics toolkit, although this is not
critical. This toolbox is used for EEGLAB *STUDY* statistics when present.

```
pkg install -forge io
pkg install -forge statistics
pkg load statistics
```

Known issues with EEGLAB and Octave graphics compatibility
----------------------------------------------------------

All EEGLAB signal processing functions should run on Octave. Although
[Octave](http://www.gnu.org/software/octave/) is relatively compatible
with MATLAB for functions purely performing computations, the Octave
graphic rendering engine sometimes cannot render all EEGLAB graphics subtleties. In particular, we have encountered the following
issues:



-   EEGLAB interactive pop-up windows and the *eegplot.m* interactive data
    scrolling function are not functional. Below, an example of head plot in MATLAB
(left) and Octave (right).
![](/assets/images/Octave_headplot.png)

-   Head plots are missing a shadow property (see figure above right -
    facial feature shadowing is absent)
-   Plug-ins need to be installed manually (downloaded as zip files and
    uncompressed in the EEGLAB plugins folder). Most plugins (including
    SIFT and LIMO) have not been tested on Octave and will likely not be
    functional. They could probably be made functional by their
    developers or by motivated users.
-   Memory mapping functions are not functional (this is a minor
    limitation as this is beta functionality in EEGLAB)

As long as you are using EEGLAB command-line functions, all EEGLAB
plotting functions should be functional. This includes all EEGLAB
scripts that run on MATLAB. If you have an EEGLAB script that does not
run on Octave, please submit an EEGLAB [bug report](/others/EEGLAB_Bugs.html).
Even some of the most complex EEGLAB plots can be rendered on Octave -
for example, below, dipole plots in MATLAB (left)
and Octave (right) match perfectly.


 ![dipole in matlab and octave](/assets/images/Eeglab_dipoles_matlab_octave.png)

Octave is still actively evolving and might support EEGLAB's complete
graphical environment in the future. Also, MATLAB code can often be modified
to be more Octave compatible. 

If you modify an interactive EEGLAB
function for that purpose and want others to benefit from your changes,
fork the code and create a pull request as explained on [this
page](/others/Fork_the_EEGLAB_repository.html). [This other 
page](/tutorials/misc/Contributing_to_EEGLAB.html) contains other
information on how to contribute to EEGLAB.

A simple example of running an EEGLAB script in Octave
----------------------------------------------

As mentioned previously, any EEGLAB MATLAB script should now run under
Octave.

Below is a time-frequency decomposition plotted by Octave 4.4 for the
EEGLAB tutorial dataset by the EEGLAB/MATLAB code below. The plot below
is provided for illustrative purposes only; we had to implement some
minor changes to make the EEGLAB time-frequency function *newtimef.m*
compatible with Octave (since the changes were also compatible with
MATLAB itself, we placed them in the main repository). Other EEGLAB
functions (even signal processing functions) may also require
minor changes to run under Octave.

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

