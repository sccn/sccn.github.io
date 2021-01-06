---
layout: default
title: Running EEGLAB on Octave
parent: Other documents
---
Running EEGLAB on Octave
====

Why Octave?
---

Matlab, although quite efficient,
is expensive. A single Matlab license may cost $2,100
($1,050 for academia), and with *all* its commercial toolboxes might
come to $145,000 or more.

We have attempted to tackle this problem and as of June 2018 (EEGLAB
2019), we are currently supporting Octave (v4.4.0) for supercomputing
applications (command line calls only, no graphic support). In our
tests, Octave is about 50% slower than Matlab but this can easily be
compensated by increasing the number of processors assigned to a
specific processing task. Note that EEGLAB functions have not been
parallelized (except a few rare exceptions). Therefore, you are required
to open a Octave/Matlab session on each node and run custom scripts you
write to take advantage of your parallel processing capability.

# Running EEGLAB on Octave


As of August, 2018 EEGLAB scripts written for MATLAB can be run on the
open source application Octave. Octave-compatible EEGLAB functions are
available only in EEGLAB 15 - at the time of writing, the current
developer version of EEGLAB - which is freely available from
[<https://github.com/eeglabdevelopers/eeglab>
github](/https://github.com/eeglabdevelopers/eeglab_github "wikilink").
To run EEGLAB on Octave, one must call EEGLAB functions from the Octave
command line. The EEGLAB graphic user interface (GUI) and functions that
create interactive pop-up windows still do not run on Octave. However,
scripts that call EEGLAB <em>pop_</em> functions should still work and
plot results if their pop-up interactive window function is not engaged.

How to install and open Octave
------------------------------

Download the latest version of Octave from [this
page](https://www.gnu.org/software/octave/download.html). EEGLAB has
been best tested using Octave 4.4, but should also run on later
versions.

Then start Octave. Some Octave modules need to be installed for EEGLAB
to function properly. Octave needs to be started with the option
<em>--traditional</em> to ensure maximal compatibility with Matlab. From
the command line, start Octave using:


``` matlab
octave --traditional
```


This option is likely available from the Octave GUI settings (if you are
using the Octave GUI). Then, you will need to install the Octave signal
processing package. If the signal processing package is not installed,
about 5% of EEGLAB functions will not run. On the Octave command line,
type:



``` C
pkg install -forge control
pkg install -forge signal
pkg load signal
```



Note that you need to run the last command <em>pkg load signal</em>
every time you start Octave from the command line. (If you are using the
Octave graphic interface there might be a way to load it automatically).
You may also install the statistics toolkit although this is not
critical. This toolbox is used for study statistics when present.



``` C
pkg install -forge io
pkg install -forge statistics
pkg load statistics
```



Known issues with EEGLAB and Octave graphics compatibility
----------------------------------------------------------

All EEGLAB signal processing functions will run on Octave. Although
[Octave](http://www.gnu.org/software/octave/) is relatively compatible
with Matlab for functions purely performing computations, the Octave
graphic rendering engine sometimes cannot render all the subtleties of
EEGLAB graphics. In particular, we have encountered the following
issues:



-   EEGLAB interactive pop-up windows and the eegplot() interactive data
    scrolling function are not functional

Examples of head plot in Matlab
(left) and Octave (right)
![Examples of head plot in Matlab
(left) and Octave (right)](/assets/images/Octave_headplot.png)

-   Head plots are missing a shadow property (see figure below right -
    facial feature shadowing is absent)
-   Plug-ins need to be installed manually (downloaded as zip files and
    uncompressed in the EEGLAB plugins folder). Most plug-ins (including
    SIFT and LIMO) have not been tested on Octave and will likely not be
    functional. They could probably be made functional by their
    developers or by motivated users...
-   Memory mapping functions are not functional (this is a minor
    limitation as this is beta functionality in EEGLAB)

Dipole plots in Matlab (left)
and Octave (right) - these match
perfectly:

 ![dipole in matlab and octave](/assets/images/Eeglab_dipoles_matlab_octave.png)

As long as you are using EEGLAB command line functions, all EEGLAB
plotting functions should be functional. This includes all EEGLAB
scripts that run on Matlab. If you find an EEGLAB script that does not
run not, please submit an EEGLAB [bug report](/EEGLAB_Bugs "wikilink").
Even some of the most complex EEGLAB plots can be rendered on Octave -
for example, on the left a complex 3-D dipole plot (plotted by
<em>dipplot</em>) is shown.

Octave is still actively evolving and might support a more complete
graphics environment in future. Also, Matlab code can often be modified
to be more Octave compatible. 

If you modify an interactive EEGLAB
function for that purpose and want others to benefit from your changes,
fork the code and create a pull request as explained on [this
page](/Fork_the_EEGLAB_repo "wikilink"). [This
page](/A07:_Contributing_to_EEGLAB "wikilink") contains other
information on how to contribute to EEGLAB.

Simple example: an EEGLAB script run in Octave
----------------------------------------------

As mentioned previously, any EEGLAB Matlab script should now run under
Octave.

Below is a time-frequency decomposition plotted by Octave 4.4 for the
EEGLAB tutorial dataset by the EEGLAB/Matlab code below. The plot below
is provided for illustrative purposes only; we had to implement some
minor changes to make the EEGLAB time-frequency function *newtimef()*
compatible with Octave (since the changes were also compatible with
MATLAB itself, we placed them in the main repository). Other EEGLAB
functions (even signal processing functions) may also still require
minor changes to run under Octave.

`% cd xxxxx/eeglab                                   % move to the proper directory/folder`
`% octave --traditional                              % start Octave`

` eeglab                                                         % call EEGLAB`
` EEG = pop_loadset('sample_data/eeglab_data_epochs_ica.set');   % load an EEGLAB dataset`
` [ersp itc imbase time freqs] = newtimef(EEG.data(1,:,:), ...`
`            EEG.pnts, [-1000 2000], EEG.srate, [3 0.5]);        % compute and plot a trial-average ERSP`
`                                          `


![](/assets/images/Octave2.png)



For comparison, below is the graphic output of *newtimef()* run in
Matlab.



![600px\|EEGLAB newtimef output](/assets/images/Eeglab_newtimef2.png)

