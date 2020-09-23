---
layout: default
title: Channel Location Files
permalink: /docs/Channel_Location_Files
parent: Docs
---

<center>

![Image:channel location.jpg](../assets/images/channel_location.jpg)

</center>

### Links and Information

  - Access [Sample files sent to us](ftp://sccn.ucsd.edu/pub/locfiles/)
    in the following formats:

> EEGLAB ".loc" and ".txt",
> Polhemus ".elp",
> EGI ".spl" and ".xyz",
> Besa ".elp",
> Neuroscan ".map"

  - EEGLAB can read all these file formats (except for Neuroscan
    ".map"). Share your location files by adding files directly to the
    wiki [HERE](/Special:Upload "wikilink"). Please do not forget to add
    the link to your uploaded files
    [*below*](/#Uploaded_Files "wikilink") or in the [Talk:Channel
    Location Files](/Talk:Channel_Location_Files "wikilink") page.

<!-- end list -->

  - [Neuroscan company web page](http://www.neuro.com/) with 32- and
    64-channel headmodel files (see also
    [dave.zip](ftp://ftp.neuroscan.com/scan4/dave.zip)).

<!-- end list -->

  - [EGI/Philips Neuro](ftp://sccn.ucsd.edu/pub/philips_neuro) channel
    location files with BESA-compatible electrode location.

<!-- end list -->

  - [Standard](http://astronomy.swin.edu.au/%7Epbourke/dataformats/electrocap/Electrocap)electrode
    locations

<!-- end list -->

  - [Easy-cap](http://www.easycap.de/easycap/) electrode locations in
    [3-D spherical](http://www.easycap.de/easycap/english/mktp01s.htm),
    [3-D cartesian](http://www.easycap.de/easycap/english/mkxy01s.htm),
    and [3-D spherical
    equidistant](http://www.easycap.de/easycap/english/mktp10s.htm)
    coordinates.

We have created software (in EEGLAB) to transform between spherical, 3-D
cartesian and polar coordinates in a variety of file formats (see
[readlocs()](http://sccn.ucsd.edu/eeglab/allfunctions/readlocs.m)
function help). We will post more information here soon...

### Upload Files

  - *Upload Files* by clicking ['Upload
    file'](/Special:Upload "wikilink") on the sidebar to the left and
    then add the link below. These files should be zipped as wikimedia
    only allow downloading a limited number of file types.
  - Add a link to the files you have uploaded in the list above.

-----

**Image at top of page:** *Independent component of 252-channel EEG data
with bilateral occipital scalp projection.* Derived by independent
component analysis of approximately 700,000 points of data using
runica() in the EEGLAB Toolbox, implementing extended infomax ICA. Here,
the 252-channel data were reduced to 160 independent components by PCA
prior to ICA training. Channels located below the head center are shown
in this topoplot() as extending out from the model head borders. Note
that ICA finds the gradient of the projection from the source to the
skin surface not only at the scalp electrodes but also for channels on
the neck, forehead and temples. Residual variance of the bet-fiting
symmetric dual-dipole model in a model sphere head was 2.0%. Dipole
calculations used the DIPFIT plug in.

-----

[Category:EEGLAB](/Category:EEGLAB "wikilink")

{ {Backward_Forward|Main_Page|SCCN Wiki
Home|A03:_Importing_Channel_Locations|Importing Channel Locations} }