---
layout: default
title: retaining ICA weight script
parent: 11. Scripting
grand_parent: Tutorials
---

Retaining multiple ICA weights in a dataset
---------------------------------------------

To retain multiple copies of ICA weights (e.g. EEG.weights and
EEG.sphere), use the extendibility property of Matlab structures. On the
Matlab command line, simply define new weight and sphere variables to
retain previous decomposition weights. For example,

``` matlab
>> EEG.icaweights2 = EEG.icaweights; % Store existing ICA weights matrix
>> EEG.icasphere2 = EEG.icasphere; % Store existing ICA sphere matrix
>> [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET); % copy to EEGLAB memory
>> EEG = pop_runica(EEG);  % Compute ICA weights and sphere again using
% binica() or runica(). Overwrites new weights/sphere matrices
% into EEG.icaweights, EEG.icasphere
>> [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET); % copy to EEGLAB memory
```

Both sets of weights will then be saved when the dataset is saved, and
reloaded when it is reloaded. See the [script
tutorial](/tutorials/advanced-topics/writing-EEGLAB-scripts.html) for more
information about writing Matlab scripts for EEGLAB.