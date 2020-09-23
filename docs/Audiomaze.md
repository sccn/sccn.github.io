---
layout: default
title: Audiomaze
permalink: /docs/Audiomaze
parent: Docs
---

![400px|](/assets/images/wire18.jpg)

## What is Audiomaze?

Audiomaze is a integrated mobile brain-body imaging (MoBI) paradigm to
study human navigation and the corresponding brain electric activities
during free, natural walking and exploring behavior through real space.
Participant's task is to explore and learn the maze with a blindfold
using the right hand as the only guide that can 'touch' walls (which
returns sound feedback). During the task, her EEG is continuously
recorded using completely portable 128-ch active EEG recording systems,
and her body movement is recorded as well using 32-ch motion tracker
system attached to head, torso, right arm and hand, and both knees and
feet. This paradigm realizes our novel concept "Sparse AR" which is to
control the flow of perceptual input, which is usually too fast, vast,
and parallelized to be studied in cognitive neuroscience, to be slow,
quantized, and sequentialized, as if the incoming information is
transformed into "perceptual atoms" which we can study with EEG.

## Report at Collaborative Research in Computational Neuroscience (CRCNS) 2017 Annual PI Meeting

[Access to the pdf
file.](https://crcns2017.worldeventsforum.net/wp-content/uploads/2017/07/CRCNS-2017-Abstracts-Book-Jun-12.pdf)

![300px|](/assets/images/crcns2017_01.jpg)
![300px|](/assets/images/crcns2017_02.jpg)
![300px|](/assets/images/crcns2017_03.jpg)

## Download Links for Demo Data and Proof-of-concept EEGLAB Plugin (05/16/2020 updated)

![300px|](/assets/images/gui.png)

Download EEGLAB .set and .fdt files that contains 128-ch EEG plug 32-ch
motion tracker data from one session of one participant. [from here
(total 332MB)](ftp://sccn.ucsd.edu/pub/audiomaze/audiomazeDemoData.zip).

Download EEGLAB plugin to process the above data
[motionTrackerCorrectionTool1.00](/Media:motionTrackerCorrectionTool1.00.zip‎ "wikilink").
To use this plugin, please follow the standard EEGLAB plugin procedure
to use it i.e., unzipping it first, then locate it the folder under
/(EEGLABroot)/eeglab/plugins and reboot EEGLAB. Under 'Tools' menu,
there appears 'Motion Tracker Correction Tool'. The algorithm and the
flow of the process is summarized in the PDF file linked below. Note
that this is an old demo version from 2018.

Download the PDF file for description of the motion tracker data and
correction methods [from here
(488KB)](ftp://sccn.ucsd.edu/pub/audiomaze/audiomazeMaterials.pdf).

Download movies demonstrating the effect of motion tracker correction:
[before correction
(4.8MB)](ftp://sccn.ucsd.edu/pub/audiomaze/beforeCorrection.mp4) and
[after correction
(3.8MB)](ftp://sccn.ucsd.edu/pub/audiomaze/afterCorrection.mp4).

(Added 05/16/2020) Let me also upload the updated version of the
processing pipeline. The difference from the above is that it is not
wrapped up as a EEGLAB plugin but Matlab functions. For non-rigid-body
marker correction, it uses neural network. [updated preprocessing
pipeline](/Media:updatedPreprocessingPipeline.zip‎ "wikilink")

## Acknowledgement

This project is funded by: Collaborative Research in Computational
Neuroscience (CRCNS) NSF 1516107 US-German Research Proposal "Neural
Dynamics of the Integration of Egocentric and Allocentric Cues in the
Formation of Spatial Maps During Fully-Mobile Human Navigation" PI Scott
Makeig. See [NSF
website](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1516107) A
companion project is being funded by the Federal Ministry of Education
and Research, Germany (BMBF). Swartz Center for Computational
Neuroscience is supported by Swartz Foundation.

## Appendix: load_xdf() issue (12/20/2018 updated)

The current default option for 'handlejitterremoval' in load_xdf() is
'true'. The assumption for this is, I guess, that the data behaves well
and the amount of jitter is trivial. However, I found that this is a
dangerous assumption after experiencing with several MoBI projects. I
recommend people check what they have in the raw data BEFORE applying
linear regression on time stamp data. For detail, see [this
slide](/Media:_How_to_make_irregular_and_missing_sampling_points_uniform_in_LSL_data.pdf "wikilink").