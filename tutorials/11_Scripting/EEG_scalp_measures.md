---
layout: default
title: Measure topo. plot
parent: 11. Write scripts
grand_parent: Tutorials
---
Plotting measures in scalp topography
=====

Plot time-frequency decomposition
----
The [metaplottopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=metaplottopo.m) function is a powerful function that
allows plotting any measure for all channels and components. For
example, the code below allows plotting time-frequency decompositions for
all data channels.

``` matlab
eeglab; close; % add path
eeglabp = fileparts(which('eeglab.m'));
EEG = pop_loadset(fullfile(eeglabp, 'sample_data', 'eeglab_data_epochs_ica.set'));
figure; metaplottopo( EEG.data, 'plotfunc', 'newtimef', 'chanlocs', EEG.chanlocs, 'plotargs', ...
                   {EEG.pnts, [EEG.xmin EEG.xmax]*1000, EEG.srate, [0], 'plotitc', 'off', 'ntimesout', 50, 'padratio', 1});
```

![400px](/assets/images/Newtimeftopo.png)

Plot ERP image
----

Another example below allows plotting ERPimage for all data channels.
Note that for ERPimage, the function does not show the axis for each
plot making it convenient to plot hundreds of channels if necessary. It
is also possible to plot ICA components in this way by replacing
EEG.data with EEG.icaact and removing the *'chanlocs'* argument.

``` matlab
figure; metaplottopo( EEG.data, 'plotfunc', 'erpimage', 'chanlocs', EEG.chanlocs, 'plotargs', ...
         { eeg_getepochevent( EEG, {'rt'},[],'latency') linspace(EEG.xmin*1000, EEG.xmax*1000, EEG.pnts) '' 10 0 });
```

![400px](/assets/images/Erpimagetopo.png)
