## EEGLAB electrode coordinate systems

EEGLAB supports multiple electrode coordinate systems. Typically, three fiducial or anatomical landmark points are used to define a system. See [this FieldTrip FAQ page](https://www.fieldtriptoolbox.org/faq/how_are_the_different_head_and_mri_coordinate_systems_defined/#details-of-the-mni-coordinate-system) for details on how the origin and the axes are defined in different systems.

The left and right preauricular (LPA & RPA) points are commonly used as ear anatomical points. PA points are palpable anatomical features, but they are difficult to locate in anatomical MR head images. Furthermore, some experiment protocols call for using other anatomical points on the ears (e.g. ear canal, ear lobes, etc.) while retaining the inaccurate PA label. While consistency is key when gathering data for a study, collaborative or data mining projects are undermined when accurate labels or descriptions are not used. With photogrammetry improving the availability of electrode localization, we strongly recommend the use of the helix-tragus junction (LHJ &  RHJ) as the ear fiducials: these points are identifiable in 3-D head models as well as MR head images. 

<p align="center">
  <img src="https://sccn.github.io/assets/images/helixTragus.PNG" width="50%" height="50%">
</p>

If digitized electrodes locations are imported, EEGLAB inherits the coordinate system but will rotate the coordinates in the X-Y plane such that the nose is pointed in the direction of +X. The philosophy is that such differences in electrode coordinates are trivial for visualization and source localization, because head model co-registration warps and scales the coordinates. 

#### EEGLAB
If digitized electrode locations are not imported, we recommend importing the Montreal Neurological Institute (MNI) template locations included in EEGLAB. Note that EEGLAB will rotate this template's native MNI coordinate system such that the nose is in the +X direction.
- Units in millimeter
- The origin is the anterior commissure
- The X-axis points from posterior to anterior
- The Y-axis points from the left side of the brain to the right side
- The Z-axis points from inferior to superior

#### EEGLAB-HJ
A coordinate system used by [<i>get_chanlocs</i>](https://github.com/sccn/get_chanlocs/wiki), an EEGLAB plug-in for photogrammetric electrode localization using 3-D head models. It is based on the [CTF coordinate system](https://www.fieldtriptoolbox.org/faq/how_are_the_different_head_and_mri_coordinate_systems_defined/#details-of-the-ctf-coordinate-system), except the aforementioned helix-tragus junction (HJ) points are used as the ear anatomical landmarks.
- Units in millimeter
- The origin is exactly between the left and right ear helix-tragus junction
- The X-axis points towards and goes through the nasion
- The Y-axis points approximately towards the LPA, orthogonal to the X-axis
- The Z-axis points from inferior to superior, orthogonal to X and Y

 <img src="https://www.fieldtriptoolbox.org/assets/img/faq/how_are_the_different_head_and_mri_coordinate_systems_defined/coordinatesystem_ctf.png" width="30%" height="30%">
