---
layout: default
title: Time-freq. topo
parent: 11. Write scripts
grand_parent: Tutorials
---
Time-frequency plot on all electrodes
=======

This example demonstrates some of the power of low-level
scripting that goes beyond the scope of functions currently available
through the graphical interface. Below we run this script on the tutorial epoched dataset.
The [tftopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=tftopo.m) function is a powerful function that
allows plotting time-frequency decompositions across all channels.
    
The script below can be found at [tftopo_example.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=tftopo_example.m)

``` matlab
% Compute a time-frequency decomposition for every electrode
eeglab; close; % add path
eeglabp = fileparts(which('eeglab.m'));
EEG = pop_loadset(fullfile(eeglabp, 'sample_data', 'eeglab_data_epochs_ica.set'));
for elec = 1:EEG.nbchan
    [ersp,itc,powbase,times,freqs,erspboot,itcboot] = pop_newtimef(EEG, …
    1, elec, [EEG.xmin EEG.xmax]*1000, [3 0.5], 'maxfreq', 50, 'padratio', 16, ...
    'plotphase', 'off', 'timesout', 60, 'alpha', .05, 'plotersp','off', 'plotitc','off');
    if elec == 1  % create empty arrays if first electrode
        allersp = zeros([ size(ersp) EEG.nbchan]);
        allitc = zeros([ size(itc) EEG.nbchan]);
        allpowbase = zeros([ size(powbase) EEG.nbchan]);
        alltimes = zeros([ size(times) EEG.nbchan]);
        allfreqs = zeros([ size(freqs) EEG.nbchan]);
        allerspboot = zeros([ size(erspboot) EEG.nbchan]);
        allitcboot = zeros([ size(itcboot) EEG.nbchan]);
    end;
    allersp (:,:,elec) = ersp;
    allitc (:,:,elec) = itc;
    allpowbase (:,:,elec) = powbase;
    alltimes (:,:,elec) = times;
    allfreqs (:,:,elec) = freqs;
    allerspboot (:,:,elec) = erspboot;
    allitcboot (:,:,elec) = itcboot;
end;
% Plot a tftopo() figure summarizing all the time/frequency transforms
figure;
tftopo(allersp,alltimes(:,:,1),allfreqs(:,:,1),'mode','ave','limits', …
[nan nan nan 35 -1.5 1.5],'signifs', allerspboot, 'sigthresh', [6], 'timefreqs', ...
[400 8; 350 14; 500 24; 1050 11], 'chanlocs', EEG.chanlocs);
```

The script produces the following figure.

![375px](/assets/images/tftopo.png)

Note that this function may also combine ERSP outputs from different subjects and apply binary statistics.
