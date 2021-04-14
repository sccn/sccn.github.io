---
layout: default
title: Coordinate systems
long_title: Coordinate systems
parent: Concepts guide
grand_parent: Tutorials
nav_order: 5
---
EEGLAB electrode coordinate systems
=========

EEGLAB supports multiple electrode coordinate systems. Typically, three fiducial or anatomical landmark points are used to define a system. See [this FieldTrip FAQ page](https://www.fieldtriptoolbox.org/faq/how_are_the_different_head_and_mri_coordinate_systems_defined/#details-of-the-mni-coordinate-system) for details on how the origin and the axes are defined in different systems.

- If digitized electrode locations are not recorded, we recommend importing the BEM template electrode file (default) to assign electrode locations based on 10-5 channel labels. 
- If digitized electrode locations are imported in EEGLAB, make sure that the orientation of the coordinate system is correct, with 'LPA' on the left (+Y), 'RPA' on the right (-Y), and the nasion facing forward (+X; up). If necessary, electrodes may be rotated in the horizontal plane using the <i>Rotate Axis</i> push button of the EEGLAB channel editor (menu item <span style="color: brown">Edit → Channel locations</span>).

## EEGLAB coordinate system
The left and right preauricular (LPA & RPA) points are commonly used as ear anatomical points (also known as fiducials). The default EEGLAB electrode coordinate system for datasets with anatomical landmarks labeled 'LPA' and 'RPA.' For backwards compatibility purposes, this coordinate system is used regardless of whether the points labeled 'LPA' and 'RPA' are marked according to their formal definition. The exact ear anatomical landmark may be described alongside the dataset (e.g. in the AnatomicalLandmarkCoordinateSystemDescription field of *_coordsystem.json for [BIDS specification](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/03-electroencephalography.html#coordinate-system-json-_coordsystemjson)). It is identical to the [CTF coordinate system](https://www.fieldtriptoolbox.org/faq/how_are_the_different_head_and_mri_coordinate_systems_defined/#details-of-the-ctf-coordinate-system) for MEG.
- Units in millimeter
- The origin is exactly between the points labeled as 'LPA' and 'RPA'
- The X-axis points towards and goes through the nasion
- The Y-axis points approximately towards the 'LPA,' orthogonal to the X-axis
- The Z-axis points from inferior to superior, orthogonal to X and Y

Note the EEGLAB coordinate system is rotated by 90 degrees in the horizontal plane when compared with MNI.  

<center><img src="https://www.fieldtriptoolbox.org/assets/img/faq/how_are_the_different_head_and_mri_coordinate_systems_defined/coordinatesystem_ctf.png" width="30%" height="30%"></center>

## EEGLAB-HJ coordinate system
PA points are palpable anatomical features, but they are difficult to locate in anatomical MR head images. Furthermore, some experiment protocols call for using other anatomical points on the ears (e.g.,  ear canal, ear lobes, etc.) while retaining the inaccurate PA label. While consistency is key when gathering data for a study, collaborative or data mining projects are undermined when accurate labels or descriptions are not used. With photogrammetry improving the availability of electrode localization, we strongly recommend the use of the helix-tragus junction (LHJ &  RHJ) as the ear fiducials: these points are identifiable in 3-D head models as well as MR head images. 

<p align="center">
  <img src="https://sccn.github.io/assets/images/helixTragus.PNG" width="50%" height="50%">
</p>

A coordinate system used by [<i>get_chanlocs</i>](https://github.com/sccn/get_chanlocs/wiki), an EEGLAB plug-in for photogrammetric electrode localization using 3-D head models. The default EEGLAB coordinate system, except the aforementioned helix-tragus junction (HJ) points, is used as the ear anatomical landmarks.
- Units in millimeter
- The origin is exactly between the left and right ear helix-tragus junction
- The X-axis points towards and goes through the nasion
- The Y-axis points approximately towards the LHJ, orthogonal to the X-axis
- The Z-axis points from inferior to superior, orthogonal to X and Y

## Create and optimize your own montage

If you wish to create your own montage, see this [project](https://github.com/arnodelorme/optimize_montage). In general, we recommend sparse coverage over one that has dense coverage at the top. The bottom electrodes capture a lot of depth information and are useful for source localization.

