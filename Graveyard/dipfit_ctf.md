DIPFIT supports source localization for MEG data (tested with CTF data). Note that a custom head model needs
to be used for MEG source localization since it is not possible to do
accurate source localization on a template head model. The
main reason for this limitation is that, first, MEG sensor positions do
not follow any positioning standard. Each system may have its own
arrangement. Furthermore, unlike EEG, the sensors are not placed on an
elastic cap that automatically fits the subject's head. The MEG
sensor coils are located within a fixed helmet in which the majority of
subjects' heads fit loosely. The position of a given sensor relative to
a cortical structure could be quite different from subject to subject,
and even across different recordings from the same subject. For this
reason, the sensor's location is always reported relative to the center
and the orientation of the subject's head during the recording, which is
never exactly the same across recordings. Consequently, a head model
needs to be created for each recording using the CTF MRIViewer and
localSphere programs (see the CTF documentation). Then, in EEGLAB, call
menu item <span style="color: brown">Tools → Locate dipoles using DIPFIT → Head model and settings</span>, and select the tab *CTF* in the upper
pop-window (note that the GUI below is an older version compared to the
one available in DIPFIT, but the field remain fairly similar). Set up the
DIPFIT model and preferences as follows:

-   Select CTF as model.
-   The model file is the file *default.hdm* created by CTF localSphere,
    located in the *xxx.ds* folder.
-   The MRI head image should be the *xxx.mri* file used by MRIViewer to
    extract the cortical surface.
-   The channel file should be the *xxx.res4* file within the *xxx.ds*
    folder. This file also contains gradiometer-specific information,
    including sensor orientation, that is not in the EEG structure.

![](/assets/images/Dipole_settings_meg.gif)

As for EEG data, you first need to scan a relatively coarse grid to find
an appropriate starting position for each dipole, by calling the
<span style="color: brown">Tools → Locate dipoles using DIPFIT → Coarse fit (grid scan)</span> menu item. 

Note that CTF head models are in centimeters (cm). Consequently,
the grid used for grid search needs to be specified in cm (this is done
automatically by pop_dipfit_gridsearc.m).


![Image:Dipole_grid_meg.gif](/assets/images/Dipole_grid_meg.gif)

Then as in EEG dipole fitting,
use the <span style="color: brown">Tools → Locate dipoles using DIPFIT → Fine fit (iterative)</span> menu item to optimize dipole positions nonlinearly.

Finally, you may plot dipoles on the subject MRI using menu item <span style="color: brown">Tools → Locate dipoles using DIPFIT → Plot component dipoles</span>, as shown below. The corresponding scalp map is also shown
on the right. Because of co-registration issues, it is not possible to
plot the dipole positions on the scalp map as in EEG). It is strongly
advisable to normalize dipole lengths when plotting MEG equivalent dipoles.


![](/assets/images/Dipole_plot_meg.gif)

You can also run DIPFIT for MEG data without a subject MR image if you
have extracted the subject head surface from another source like a head
model acquired using a Polhemus 3-D location system. However, it would
then not be possible to visualize the dipole within EEGLAB. Any
comparison between or drawing of dipoles for different subjects requires
a thorough understanding of the MEG coordinate system since that is
being used to express the dipole position. The default is in individual
subjects' head coordinates, and given that head sizes differ between
subjects, the position of dipoles cannot be directly compared between
subjects. It is therefore advisable to coregister and spatially
normalize your subjects' MRIs to a common template (such as the MNI
template) and to apply the same coregistration and normalization to the
dipole positions before comparing them. These operations need to be
executed outside EEGLAB. A test set is available
[here](http://sccn.ucsd.edu/eeglab/dipfittut/testmeg.zip) (thanks to Nicolas
Robitaille for providing the test data). Simply load
the test file and follow the instruction above (note that newer versions of FieldTrip cannot process this file anymore, so use FieldTrip versions up to 2016).
