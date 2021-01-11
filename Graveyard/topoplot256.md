---
layout: default
---

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
