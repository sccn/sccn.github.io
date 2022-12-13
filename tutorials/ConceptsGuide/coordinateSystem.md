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

EEGLAB supports electrode coordinate systems with the nose pointing towards the direction +X (the origin - loosely defined - is situated at the center of the head, and the top of the head points towards the direction +Z). Electrode coordinate formats where the nose is pointing in another direction are automatically converted, so the nose points toward +X. In terms of distance units or fiducial definition or position, EEGLAB is quite flexible. Nevertheless, for BIDS compatibility, the EEGLAB coordinate system for scanned electrodes is set to be equivalent to the CTF MEG coordinate system, with the center of the head being situated between the LPA and RPA fiducials (see below).

Typically, three fiducial or anatomical landmark points are used to define a system. See [this FieldTrip FAQ page](https://www.fieldtriptoolbox.org/faq/how_are_the_different_head_and_mri_coordinate_systems_defined/#details-of-the-mni-coordinate-system) for details on how the origin and the axes are defined in different systems.

- If digitized electrode locations are not recorded, we recommend importing the BEM template electrode file (default) to assign electrode locations based on 10-5 channel labels. 
- If digitized electrode locations are imported in EEGLAB, make sure that the orientation of the coordinate system is correct, with 'LPA' on the left (+Y), 'RPA' on the right (-Y), and the nasion facing forward (+X; up). If necessary, electrodes may be rotated in the horizontal plane using the <i>Rotate Axis</i> push button of the EEGLAB channel editor (menu item <span style="color: brown">Edit → Channel locations</span>).

## EEGLAB coordinate system

EEGLAB uses the BESA electrode coordinate system for 2-D representation. This electrode system is based on a sphere that best matches the geometry of the human head. This coordinate system is shifted up compared to the coordinate system defined as nasion, left and right fiducials (LPA and RPA). The reason for shifting the coordinate system up is that a sphere would not match well the head if it used for center the origin of the nasion, LPA, and RPA coordinate frame.

![Screen Shot 2022-12-12 at 6 29 33 PM](https://user-images.githubusercontent.com/1872705/207211594-73987343-0ae8-4fb6-8943-834a680c14ef.png)

## 2-D representation biases

When plotting 2-D scalp map, with the 

![Screen Shot 2022-12-12 at 6 29 33 PM](https://user-images.githubusercontent.com/1872705/207211594-73987343-0ae8-4fb6-8943-834a680c14ef.png)


# Fiducials

The left and right preauricular (LPA & RPA) points are commonly used as ear anatomical points (also known as fiducials). The default EEGLAB electrode coordinate system for datasets with anatomical landmarks labeled 'LPA' and 'RPA.' For backwards compatibility purposes, this coordinate system is used regardless of whether the points labeled 'LPA' and 'RPA' are marked according to their formal definition (points on the posterior root of the zygomatic arch, see [here](https://www.fieldtriptoolbox.org/faq/how_are_the_lpa_and_rpa_points_defined/) for more details). The exact ear anatomical landmark may be described alongside the dataset (e.g. in the AnatomicalLandmarkCoordinateSystemDescription field of *_coordsystem.json for [BIDS specification](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/03-electroencephalography.html#coordinate-system-json-_coordsystemjson)). It is identical to the [CTF coordinate system](https://www.fieldtriptoolbox.org/faq/how_are_the_different_head_and_mri_coordinate_systems_defined/#details-of-the-ctf-coordinate-system) for MEG.
- Units in millimeter
- The origin is exactly between the points labeled as 'LPA' and 'RPA'
- The X-axis points towards and goes through the nasion
- The Y-axis points approximately towards the 'LPA,' orthogonal to the X-axis
- The Z-axis points from inferior to superior, orthogonal to X and Y

In addition, the EEGLAB default coordinate system for 2-D vizualisation is historically based on BESA electrode coordinates. These electrodes lie on a sphere that 


![Image:preferences.png](/assets/images/coordinatesystem_ctf.png)

![Image:preferences.png](/assets/images/coordsysXY.png)

## EEGLAB-HJ coordinate system
PA points are palpable anatomical features, but they are difficult to locate in anatomical MR head images and 3-D head images. Furthermore, some experiment protocols call for using other anatomical points on the ears (e.g.,  ear canal, ear lobes, etc.) while retaining the inaccurate PA label. While consistency is key when gathering data for a study, collaborative or data mining projects are undermined when accurate labels or descriptions are not used. With photogrammetry improving the availability of electrode localization, we strongly recommend the use of the helix-tragus junction (LHJ &  RHJ) as the ear fiducials: these points are identifiable in 3-D head models as well as MR head images. 

![Image:preferences.png](/assets/images/helixTragus.PNG)

A coordinate system used by [<i>get_chanlocs</i>](https://github.com/sccn/get_chanlocs/wiki), an EEGLAB plug-in for photogrammetric electrode localization using 3-D head models. The default EEGLAB coordinate system, except the aforementioned helix-tragus junction (HJ) points, is used as the ear anatomical landmarks.
- Units in millimeter
- The origin is exactly between the left and right ear helix-tragus junction
- The X-axis points towards and goes through the nasion
- The Y-axis points approximately towards the LHJ, orthogonal to the X-axis
- The Z-axis points from inferior to superior, orthogonal to X and Y

## Create and optimize your own montage

If you wish to create your own montage, see this [project](https://github.com/arnodelorme/optimize_montage). In general, we recommend sparse coverage over one that has dense coverage at the top. The bottom electrodes capture a lot of depth information and are useful for source localization.

