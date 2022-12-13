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

## EEGLAB template files

EEGLAB uses the BESA electrode coordinate system for 2-D representation. This electrode system is based on a sphere that best matches the geometry of the human head. This coordinate system is shifted up compared to the coordinate system defined as nasion, left and right fiducials (LPA and RPA). It is also tilted forward so Cz is defined as the vertical. The reason for shifting the coordinate system up is that a sphere would not match well the head if it used for center the origin of the nasion, LPA, and RPA coordinate frame.

![Screen Shot 2022-12-13 at 12 39 31 AM](https://user-images.githubusercontent.com/1872705/207267582-d3f2bcc5-36b0-437a-bfa3-851f6acffe3f.png)

This is the reference frame when you use spherical coordinates for your 10-20 channel montage. The 10-10 channel coordinates from the boundary element model template also uses the same reference frame.

### 2-D representation biases

When plotting 2-D scalp map, Fpz is situated at the outer limit of the head. This might seem biased as FPz is clearly not located in the middle of the forehead. Yet, considering the view below (from [Chatrian et al., 1988](https://pubmed.ncbi.nlm.nih.gov/3250964/)), this keeps Cz at the vertical of the reference frame. 

![Screen Shot 2022-12-13 at 12 35 26 AM](https://user-images.githubusercontent.com/1872705/207266236-00997518-dae0-407f-9d06-10b5b4d5e133.png)


### Building your ideal 2-D layout

In general, if you want to perform source localization, we advise that you manipulate the coordinate of the electrode of the BESA or BEM template EEGLAB location files to achieve the desired 2-D effect rather than loading random 3-D channel locations. These files are well validated, and any transformation will not affect the coregistration with the head model (3-D EGI files which are also well validated and may safely be used). for example, if you want to place the fiducials at the outer limit of the head plot. You can transform the coordinate by shifting them down by -42.54 and rotating Cz by 12.97 degrees. You can then check that coordinate X and Z are 0 for LPA and RPA, and coordinates Y and Z are 0 for the nasion. The result is shown below. You may also contract electrodes using transformation (click the *transform button*) such as *X=0.9*X*. We do not advocate for this layout. It is simply provided as an example. 

![Screen Shot 2022-12-13 at 12 32 26 AM](https://user-images.githubusercontent.com/1872705/207265613-329d35a4-e540-47c2-b7c5-82063a16722e.png)

## Other EEGLAB template files

There is a large collection of EEGLAB template files when you look up channel. For example, below we import an EGI 128 channel file and show it is layout. It is perfectly fine to perform source localization with this file.

![Screen Shot 2022-12-13 at 12 07 31 AM](https://user-images.githubusercontent.com/1872705/207260856-073113fb-cf7f-488a-8a5c-d118fccec67b.png)

# Create and optimize your own montage

Sometimes you might want to create your own montage. For example, you might want to add some electrodes in specific locations, and usually cap manufacturer will acomodate you. You might also want to maximize head coverage including adding electrodes as low as possible  (see this [project](https://github.com/arnodelorme/optimize_montage)). In general, we recommend sparse coverage over one that has dense coverage at the top. The bottom electrodes capture a lot of depth information and are useful for source localization.

# Other 2-D layout

EEGLAB allows importing a variety of layout. For example below, after the tutorial dataset *eeglab_data.set*, we use the easycapM25 layout, call the channel editor using menu item <span style="color:brown">*Edit > Channel locations*</span>. Depending on the layout, you may have to adjust the plotting radius in the channel editor interace, so the entire head is visible. These layout should not be used for source localization or 3-D plotting as they are defined for 2-D plotting only (even though EEGLAB will associate 3-D coordinates to them). EEGLAB also allow importing [Fieldtrip's layouts](https://www.fieldtriptoolbox.org/template/layout/) if Fieldtrip is installed.

![Screen Shot 2022-12-13 at 12 06 17 AM](https://user-images.githubusercontent.com/1872705/207261211-d4b3408a-ef84-42b9-82b4-22bfc9677b4c.png)


# Considerations about fiducials

The left and right preauricular (LPA & RPA) points are commonly used as ear anatomical points (also known as fiducials). Unfortunately they are poorly defined.

The default EEGLAB electrode coordinate system for datasets with anatomical landmarks labeled 'LPA' and 'RPA.' For backwards compatibility purposes, this coordinate system is used regardless of whether the points labeled 'LPA' and 'RPA' are marked according to their formal definition (points on the posterior root of the zygomatic arch, see [here](https://www.fieldtriptoolbox.org/faq/how_are_the_lpa_and_rpa_points_defined/) for more details).

The exact ear anatomical landmark may be described alongside the dataset (e.g. in the AnatomicalLandmarkCoordinateSystemDescription field of *_coordsystem.json for [BIDS specification](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/03-electroencephalography.html#coordinate-system-json-_coordsystemjson)). It is identical to the [CTF coordinate system](https://www.fieldtriptoolbox.org/faq/how_are_the_different_head_and_mri_coordinate_systems_defined/#details-of-the-ctf-coordinate-system) for MEG.
- Units in millimeter
- The origin is exactly between the points labeled as 'LPA' and 'RPA'
- The X-axis points towards and goes through the nasion
- The Y-axis points approximately towards the 'LPA,' orthogonal to the X-axis
- The Z-axis points from inferior to superior, orthogonal to X and Y

In addition, the EEGLAB default coordinate system for 2-D vizualisation is historically based on BESA electrode coordinates. These electrodes lie on a sphere that 

![Screen Shot 2022-12-13 at 12 29 36 AM](https://user-images.githubusercontent.com/1872705/207265225-94db3e70-3dab-48db-950d-230d9cc9b93b.png)

## Use the helix-tragus junction for fiducials
PA points are palpable anatomical features, but they are difficult to locate in anatomical MR head images and 3-D head images. Furthermore, some experiment protocols call for using other anatomical points on the ears (e.g.,  ear canal, ear lobes, etc.) while retaining the inaccurate PA label. While consistency is key when gathering data for a study, collaborative or data mining projects are undermined when accurate labels or descriptions are not used. With photogrammetry improving the availability of electrode localization, we strongly recommend the use of the helix-tragus junction (LHJ &  RHJ) as the ear fiducials: these points are identifiable in 3-D head models as well as MR head images. 

![Image:preferences.png](/assets/images/helixTragus.PNG)

This is the coordinate system we recommend for [<i>get_chanlocs</i>](https://github.com/sccn/get_chanlocs/wiki), an EEGLAB plug-in for photogrammetric electrode localization using 3-D head models. The default EEGLAB coordinate system, except the aforementioned helix-tragus junction (HJ) points, is used as the ear anatomical landmarks.

