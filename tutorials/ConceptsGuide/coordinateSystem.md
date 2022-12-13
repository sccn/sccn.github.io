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

EEGLAB supports electrode coordinate systems with the nose pointing towards the direction +X (the origin - loosely defined - is situated at the center of the head, and the top of the head points towards the direction +Z). Electrode coordinate formats where the nose points in another direction are automatically converted, so the nose points toward +X. In terms of distance units or fiducial definition or position, EEGLAB is quite flexible. Nevertheless, for BIDS compatibility, the EEGLAB coordinate system for scanned electrodes is equivalent to the CTF MEG coordinate system, with the center of the head being situated between the LPA and RPA fiducials (see below).

Three fiducial or anatomical landmark points are typically used to define a system. See this Fieldtrip [FAQ page](https://www.fieldtriptoolbox.org/faq/how_are_the_different_head_and_mri_coordinate_systems_defined/#details-of-the-mni-coordinate-system) for details on how the origin and the axes are defined in different systems.

- If digitized electrode locations are not recorded, we recommend importing the BEM template electrode file (default) to assign electrode locations based on 10-5 channel labels. 
- If digitized electrode locations are imported in EEGLAB, make sure that the orientation of the coordinate system is correct, with 'LPA' on the left (+Y), 'RPA' on the right (-Y), and the nasion facing forward (+X; up). If necessary, electrodes may be rotated in the horizontal plane using the <i>Rotate Axis</i> push button of the EEGLAB channel editor (menu item <span style="color: brown">Edit → Channel locations</span>).
- You may use [scanned electrode coordinates](../09_source/Channel_Locations.md) and [MRI](../09_source/Custom_head_model.md) for localizing EEG sources.

## EEGLAB template files

EEGLAB uses two electrode montage for 2-D representation and source localization: the BESA and standard MNI BEM montages. These electrode systems are based on a sphere that best matches the geometry of the human head. This coordinate system is shifted upward compared to the coordinate system defined as nasion, left, and right fiducials (LPA and RPA). It is also tilted forward, so Cz is defined as vertical. The reason for shifting the coordinate system up is that a sphere would not match the head well -- it would not match the head well if we used a sphere centered at the origin of the nasion, LPA, and RPA coordinate frame.

![Screen Shot 2022-12-13 at 12 44 11 AM](https://user-images.githubusercontent.com/1872705/207268589-53f5e8f4-9138-4273-ade5-c8d8ee8729f9.png)

This is the reference frame when you use spherical coordinates for your 10-20 channel montage. The 10-10 channel coordinates from the boundary element model template also use the same reference frame.

### 2-D representation biases

When plotting 2-D scalp maps, Fpz is situated at the outer limit of the head. This might seem biased as FPz is clearly not located in the middle of the forehead in actual caps. Yet, considering the view below (from [Chatrian et al., 1988](https://pubmed.ncbi.nlm.nih.gov/3250964/)), this keeps Cz at the vertical of the reference frame. 

![Screen Shot 2022-12-12 at 6 35 29 PM](https://user-images.githubusercontent.com/1872705/207267890-43c43a92-53c8-483a-95f1-8c9483d57310.png)

### Building your ideal 2-D layout

In general, if you want to perform source localization with 10-20 montage and do not have scanned electrode locations, we advise that you use the electrode of the BEM template EEGLAB location file (the default when you select *Look up locs* in the channel editing window. This file is well-validated.

It does not mean you are stuck with the associated 2-D electrode layout, though. To achieve the desired 2-D effect, you may apply any linear transformation of the 3-D electrode coordinates. These transformations may be compensated for when coregistration them with the head model. For example, if you want to place the fiducials close to the outer limit of the head plot, you can transform the BEM template coordinates by shifting the center of the sphere down by 40 millimeters (*Opt. head center* in the channel editing window). The result is shown below. The figure below shows 81 electrodes in the original BEM coordinate system, the change in the origin of the 3-D coordinate frame, and the resulting 2-D project. 

![Screen Shot 2022-12-13 at 2 00 53 PM](https://user-images.githubusercontent.com/1872705/207454927-54e15856-bead-4ff3-948d-639240449b15.png)

This is not an ideal layout, as electrodes near the outer head limit are more spaced than electrodes near the center. A better option is to ask EEGLAB to change the head limit (the default is 0.5). Once you make these changes, it will affect all the 2-D plots for this dataset (EEGLAB 2023.0 and later versions only). On the command line, type

```matlab
EEG.chaninfo.headrad = 0.68;
EEG.saved = 'no';
[ALLEEG, EEG, CURRENTSET] = eeg_store(ALLEEG, EEG);
eeglab redraw
```

The screen captures below show a head radius of 0.4 (left), the default 0.5 value (center) and 0.68 (right).

![Screen Shot 2022-12-13 at 3 09 37 PM](https://user-images.githubusercontent.com/1872705/207464956-99339d9d-e163-443d-8720-5f3add67a6c1.png)

## Other EEGLAB template files

There is an extensive collection of EEGLAB template files when you look up electrode coordinates. For example, below, we import an EGI 128 channel file and show it the layout. It is fine to perform source localization with this file as it is impossible to use the template BEM location file (EGI channels are not defined in the 10-20 system).

![Screen Shot 2022-12-13 at 12 07 31 AM](https://user-images.githubusercontent.com/1872705/207260856-073113fb-cf7f-488a-8a5c-d118fccec67b.png)

# Create and optimize your own montage

Sometimes you might want to create your own montage. For example, you might want to add some electrodes in specific locations, and usually cap manufacturer will accommodate you. You might also want to maximize head coverage, including adding electrodes as low as possible  (see this [project](https://github.com/arnodelorme/optimize_montage)). We recommend maximum head coverage instead of dense coverage in the upper head region. Because of volume conduction, the bottom electrodes capture a lot of depth information and are useful for source localization.

# Other 2-D layout

If you are adamant about using a specific electrode layout for 2-D representation, you may use do so. However, you should not use the electrode locations for source localization or 3-D plotting as they are defined for 2-D plotting only (even though EEGLAB will automatically infer 3-D coordinates for them).

EEGLAB allows importing a variety of layouts. For example, below, after the tutorial dataset *eeglab_data.set*, we use the *eeglab_montage11_layout.loc* layout. To do so, call the channel editor using menu item <span style="color:brown">*Edit > Channel locations*</span>, then click on the *Look up locs* button. Depending on the layout, you may have to adjust the plotting radius in the channel editor interface, so the entire head is visible. EEGLAB also allows importing Fieldtrip's [layouts](https://www.fieldtriptoolbox.org/template/layout/) if it is installed. The figure below shows some of types of 2-D electrode layouts available.

![Screen Shot 2022-12-13 at 3 16 02 PM](https://user-images.githubusercontent.com/1872705/207465671-1327aaf3-be3f-4185-81a2-6cbdef29bfe0.png)

# Considerations about fiducials

The left and right preauricular (LPA & RPA) points are commonly used as ear anatomical points (also known as fiducials). Unfortunately, they are poorly defined.

The default EEGLAB electrode coordinate system for datasets with anatomical landmarks labeled 'LPA' and 'RPA' as shown in the figure below. For backward compatibility purposes, this coordinate system is used regardless of whether the points labeled 'LPA' and 'RPA' are marked according to their formal definition (points on the posterior root of the zygomatic arch, see [here](https://www.fieldtriptoolbox.org/faq/how_are_the_lpa_and_rpa_points_defined/) for more details).

The exact ear anatomical landmark may be included with the EEG or MEG data (e.g., in the AnatomicalLandmarkCoordinateSystemDescription field of *_coordsystem.json for [BIDS specification](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/03-electroencephalography.html#coordinate-system-json-_coordsystemjson)). It is identical to the [CTF coordinate system](https://www.fieldtriptoolbox.org/faq/how_are_the_different_head_and_mri_coordinate_systems_defined/#details-of-the-ctf-coordinate-system) for MEG.
- Units in millimeters
- The origin is exactly between the points labeled as 'LPA' and 'RPA'
- The X-axis points towards and goes through the nasion
- The Y-axis points approximately towards the 'LPA,' orthogonal to the X-axis
- The Z-axis points from inferior to superior, orthogonal to X and Y

As shown below, even when properly defined, the 3 points LPA, RPA, and nasion may not represent a perfectly orthogonal reference frame. Only one plane passes through these 3 points. The Z direction is set to be orthogonal to this plane. The center of the reference frame is defined (in this plane) as the intersection of a line passing through the nasion (+X direction) and an orthogonal line whose distance is equal for LPA and RPA (we define the distance as the length of the segment for the orthogonal projection of these points on the line). 

![Screen Shot 2022-12-13 at 12 29 36 AM](https://user-images.githubusercontent.com/1872705/207265225-94db3e70-3dab-48db-950d-230d9cc9b93b.png)

Eventually, the center of the reference frame defined by the LPA, RPA, and nasion fiducials is not critical. Fiducials must be defined accurately to align head montage with MRI scans, but their relative position matters little. For display purposes, it is important that electrodes be organized similarly to one of the standard 2-D layouts and that we may align them to a 3-D head model for source localization purposes. Both processes do not depend on using the reference frame defined by the LPA, RPA, and nasion fiducials.

## Use the helix-tragus junction for fiducials
PA points are palpable anatomical features but are challenging to locate in anatomical MR head images and 3-D EEG electrode scans. Furthermore, some experiment protocols call for using other anatomical points on the ears (e.g.,  ear canal, ear lobes, etc.) while retaining the inaccurate PA label. While consistency is critical when gathering data for a study, collaborative or data mining projects are undermined when accurate labels or descriptions are not used. With photogrammetry improving the availability of electrode localization, we strongly recommend using the helix-tragus junction (LHJ &  RHJ) as the ear fiducials: these points are identifiable in 3-D head models as well as MR head images. 

![Image:preferences.png](/assets/images/helixTragus.PNG)

This is the coordinate system we recommend for [<i>get_chanlocs</i>](https://github.com/sccn/get_chanlocs/wiki), an EEGLAB plug-in for photogrammetric electrode localization using 3-D head models. The default EEGLAB coordinate system, except the aforementioned helix-tragus junction (HJ) points, is used as the ear anatomical landmarks.

