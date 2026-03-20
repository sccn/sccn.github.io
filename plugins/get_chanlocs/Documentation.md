---
layout: default
parent: get_chanlocs
grand_parent: Plugins
render_with_liquid: false

title: Documentation
long_title: Documentation
---
![](Get_chanlocs.jpg)

[Download the *get_chanlocs* User Guide](https://sccn.ucsd.edu/eeglab/download/Get_chanlocs_userguide.pdf)

### What is *get_chanlocs*?

The *get_chanlocs* EEGLAB plug-in is built on functions in
[FieldTrip](http://www.fieldtriptoolbox.org/) to locate 3-D electrode
positions from a 3-D scanned head image. Robert Oostenveld, originator
of the FieldTrip toolbox, alerted us in 2017 that he and his students in
Nijmegen had put functions into FieldTrip to compute positions of scalp
electrodes from the recorded 3-D images for one 3-D camera, the
[Structure scanner](https://structure.io/) mounted to an Apple iPad.
(Read [Homölle and Oostenveld
(2019)](https://doi.org/10.1016/j.jneumeth.2019.108378) and [notes on
the incorporated FieldTrip
functions](http://www.fieldtriptoolbox.org/tutorial/electrode/)). We at
SCCN have created an EEGLAB plug-in extension, *get_chanlocs*, to ease
the process of digitizing the positions of the electrodes from the
acquired 3-D and entering them into the *EEG.chanlocs* data structure
for use with other EEGLAB (plotting and source localization) functions
that require electrode position information.

The <b>major advantages</b> of using <em>get_chanlocs</em> to measure
electrode positions are that: 1) <b>the 3D image can be recorded quickly
(\<1 min)</b>, thereby saving precious subject time (and attention
capacity) better used to record EEG data! The researchers who have been
most enthusiastic to hear about <em>get_chanlocs</em> are those
collecting data from children and infants -- though even normal adult
participants must feel less cognitive capacity for the experimental
tasks after sitting, wearing the EEG montage, for 20 min while research
assistants record the 3D location of each scalp electrode. 2) <b>The 3D
image connects the electrode locations to the head fidicuals in a very
concrete and permanent way</b>; future improved head modeling will be
able to use the 3D head surface scans to fit to subject MR images or to
warp template head models to the actual subject head. 3) Unlike with
wand-based electrode localizing (neurologists call this electrode
'digitizing'), <b>retaining the 3D head image allows rechecking the
electrode positions</b> (e.g., if some human error occurs on first
readout).

In brief, the process is as follows:

<b>Scanning the head surface:</B> A 3-D head image (3-D head ‘scan’) is
acquired using the Structure scanner showing the subject wearing the
electrode cap; this image acquisition typically requires a minute or
less to perform. The resulting 3-D *.obj* image file is stored along
with the EEG data. *get_chanlocs* also supports use of *.obj* 3D image
files obtained using the [itSeez3D scanning app](https://itseez3d.com/),
which we have found to be easier to capture good 3D images with than the
Structure scanner's native app (Suggestion: Ask iSeez3D about a
non-commercial license).

<B>Localizing the electrodes in the 3D scan:</B> When the data are to be
analyzed, the *get_chanlocs* plug-in, called from the Matlab command
line or EEGLAB menu, guides the data analyst through the process of
loading the recorded 3-D head image and then clicking on each of the
electrodes in the image in a pre-planned order to compute and store
their 3-D positions relative to 3 fidicual points on the head (bridge of
nose and ears). (Note: in future, this digitizing step may be automated
at some point in the future using a machine vision approach). The
electrode labels and their 3-D positions relative to the three skull
landmarks (‘fiducial points’) are then written directly into the dataset
*EEG.chanlocs* structure. During this process, a montage template
created for the montage used in the recorded experiment can be shown by
*get_chanlocs* as a convenient visual reference to speed and minimize
human error in the electrode digitization process.

<B>User Guide</B> See the illustrated [*get_chanlocs* User
Guide](https://sccn.ucsd.edu/mediawiki/images/5/5f/Get_chanlocs_userguide.pdf) for details.

<B>Uses:</B> Once the digitized electrode positions have been stored in
the dataset, further (scalp field plotting and source localization)
processes can use the digitized positions.

<b>Ethical considerations:</B> An institutional review board (or
equivalent ethics review body) will likely consider head images as
personally identifiable information. <b>Here is the IRB-approved [UCSD
subject Consent
form](/Media:Get_chanlocs_sampleConsent.pdf "wikilink")</B>, allowing
participants to consent to different degrees of use of their 3D head
image, that we use at SCCN.

### Why *get_chanlocs*?

To achieve <b>high-resolution EEG (effective) source imaging</b>
requires (a) <b>an accurate 3-D electrical head model</b>, and (b)
<b>accurate co-registration of the 3-D scalp electrode positions to the
head model</b>. Several packages are available for fashioning a
geometrically accurate head model from an anatomic MR head image. We use
Zeynep Akalin Acar's [Neuromagnetic Forward problem Toolbox
(NFT)](https://sccn.ucsd.edu/wiki/NFT), which she is now coupling to the
first non-invasive, universally applicable method (SCALE) for estimating
individual skull conductivity from EEG data (Akalin Acar et al., 2016;
more news of this soon!). When a subject MR head image is *not*
available, equivalent dipole models for independent component brain
sources can use a template head model. Zeynep has shown that the dipole
position fitting process is more accurate when the template head is
warped to fit the actual 3-D positions of the electrodes -- IF these are
recorded accurately. This kind of warping is performed in Zeynep's
[**NFT** toolbox for EEGLAB](https://sccn.ucsd.edu/wiki/NFT).

For too long, it has been expensive and/or time consuming (for both
experimenter and subject) to record (or 'digitize') the 3-D positions of
the scalp electrodes for each subject. In recent years, however, cameras
capable of recording images in 3-D have appeared and are now becoming
cheaper and more prevalent. Robert Oostenveld, originator of the
FieldTrip toolbox, alerted us that he and his students in Nijmegen had
added functions to FieldTrip to compute the 3-D positions of scalp
electrodes from scanned 3-D images acquired by one such camera, the
[Structure scanner](https://store.structure.io/store) mounted to an
Apple iPad.

Recording the actual electrode positions in a 3-D head image minimizes
the time spent by the experimenter and subject on electrode position
recording during the recording session to a minute or less, while also
minimizing position digitizing system cost (to near $1000) and the space
required (to an iPad-sized scanner plus enough space to walk around the
seated subject holding the scanner). Digitizing the imaged electrode
positions during data preprocessing is made convenient in *get_chanlocs*
by using a montage template. In future, we anticipate an automated
template-matching app will reduce time required to simply checking the
results of an automated procedure.

Required Resources
------------------

The *get_chanlocs* plug-in has been tested under Matlab 9.1 (R2016b) on
Windows 10 as well as OS X 10.10.5. Please provide feedback concerning
any incompatibilities, bugs, or feature suggestions using the [GitHub
issue tracker](https://github.com/cll008/get_chanlocs/issues/).

<b>Scanning software:</B> In theory, any combination of 3-D scanning
hardware and software that produces a Wavefront OBJ file (.obj) with the
corresponding material texture library (.mtl) and JPEG (.jpg) files can
be used for the plug-in. *get_chanlocs* has only been tested with head
models produced by the [Structure Sensor
camera](https://store.structure.io/store) attached to an iPad Air (model
A1474). We use the default [calibrator
app](https://itunes.apple.com/us/app/structure-sensor-calibrator/id914275485?mt=8)
to align the Sensor camera and the tablet camera, and both the default
scanning software
([Scanner](https://itunes.apple.com/us/app/scanner-structure-sensor-sample/id891169722?mt=8))
and a third-party scanning software ([itSeez3D](https://itseez3d.com/)).

<b>Scanner vs. itSeez3D:</B> While the default scanning app
([Scanner](https://itunes.apple.com/us/app/scanner-structure-sensor-sample/id891169722?mt=8))
is free and produces models that are of high enough quality for the
plug-in, we find the third-party app ([itSeez3D](https://itseez3d.com/))
easier to use. It seems to be more robust, providing better tracking and
faster scans while minimizing the effects of adverse lighting
conditions. itSeez3D features a user friendly online account system for
accessing high-resolution models that are processed on their cloud
servers. Users may contact [itSeez3D](mailto:support@itseez3d.com) to
change processing parameters; for *get_chanlocs*, we found that
increasing the model polygon count beyond 400,000 results in longer
processing time without providing an appreciable increase in resolution.
Unfortunately, while scanning is free, exporting models (required for
*get_chanlocs*) has a [per export or subscription
cost](https://itseez3d.com/pricing.html). Please contact
[itSeez3D](mailto:support@itseez3d.com) regarding discounts for
educational institutions and other non-commercial purposes.

Common Issues
-------------

<b>Incorrect units in resulting electrode locations:</b> 3-D .obj model
units are estimated by relating the range of the recorded vertex
coordinates to an average-sized head: a captured model that is much
larger or smaller than average will cause errors. If your project
requires scanning an atypically-sized model (e.g. large bust scan
including ECG electrode, arm scan for EMG sleeve, etc.), manually set
obj.unit - [instead of using
*ft_determine_units*](https://github.com/cll008/get_chanlocs/blob/master/private/ft_convert_units.m#L86)
- to the correct unit used by your scanner {'m','dm','cm','mm'} to avoid
complications.

<b>Keyboard settings:</b> Key presses are used to rotate 3-D head models
when selecting electrode locations in *get_chanlocs*. Key press
parameters should be adjusted per user discretion: macOS and Windows
systems have adjustable Keyboard Properties, where 'Repeat delay' and
'Repeat rate' may be modified. For some versions of macOS, long key
presses will instead bring up an accent selection menu; in such cases,
repeated single key presses can be used to control MATLAB, or users may
disable the accent selection menu and enable repeating keys by typing
(or pasting) the following in the terminal:
`defaults write -g ApplePressAndHoldEnabled -bool false`

One way to circumvent this issue is to use the 3-D figure rotation tool
in MATLAB. First select the rotation tool, then mark electrodes by
clicking as normal; to rotate the model, hold the click after selecting
an electrode and drag the mouse; else, be sure to press 'r' to remove
points as necessary.

<b>Low resolution in head model:</b> Models will have lowered resolution
in MATLAB due to how 3-D .obj are imported and handled, even if they
have show a reasonable resolution in other 3-D modeling software (e.g.
Paint 3D). Increase the polygon count of the model to circumvent this
issue (we recommend 400,000 uniform polygons for itSeez3D).

Download
--------

To download *get_chanlocs*, use the extension manager within EEGLAB.
Alternatively, plug-ins are available for manual download from the
[EEGLAB plug-in
list](https://sccn.ucsd.edu/eeglab/plugin_uploader/plugin_list_all.php).

Revision History
----------------

Please check the [commit
history](https://github.com/cll008/get_chanlocs/commits/master) of the
plug-in's GitHub repository.

*get_chanlocs* User Guide
-------------------------

View/download the [*get_chanlocs* User
Guide](https://sccn.ucsd.edu/eeglab/download/Get_chanlocs_userguide.pdf)

<div align=left>

Creation and documentation by:

**Clement Lee**, Applications Programmer, SCCN/INC/UCSD,
<cll008@eng.ucsd.edu>
**Scott Makeig**, Director, SCCN/INC/UCSD, <smakeig@ucsd.edu>

</div>

