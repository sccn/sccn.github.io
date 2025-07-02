---
layout: default
title: EEGLAB 2025 Aspet
long_title: EEGLAB 2025 Aspet workshop
parent: Workshops
---

![Screen Shot 2023-03-06 at 7 40 14 AM](https://user-images.githubusercontent.com/1872705/223188423-e296a3e6-dd99-488b-b86d-1a6f8a8520e0.png)

EEGLAB Workshop
============================

<span style="color: blue">Aspet France - June 30-July 4th, 2025
</span>
The 34th EEGLAB Workshop will take place at the Bois Perche, about two hours by
chartered bus from Toulouse. Participants will be expected to bring laptops with
MATLAB installed so as to be able to participate in the practical
sessions. The tutorial workshop will introduce and demonstrate the use
of the EEGLAB software environment and EEGLAB-linked tools for
performing advanced analysis of EEG and related data, with detailed
method expositions and practical exercises. There will be an excursion.

A Free symposium on Cloud EEG data processing will precede the workshop in Toulouse.

Registration and cost
---------------------
Space at the workshop is limited to about 40 participants.

To reimburse travel expenses of Workshop faculty and facilities rental,
costs for the workshop will be as follows:

Registration cost is 280 Euros for students (plus 490 euros for accommodation) and post-docs, 380 Euros (plus 490 euros for accommodation) for
faculty and other professionals. Professionals are 580 Euros (plus 490 euros for accommodation). These registration costs include
conference space rental, all coffee breaks, and a short excursion. 
When registering, participants are also expected to pay for accommodation and all meals at the Bois Perche retreat center (a total of 490 euros). Included accommodation is in a private room at the Bois Perche resort for 4 days. Because of a grant from the CNRS, registration (and accommodation) is free for participants for the first three CNRS employees (including PhD students and post-docs) -- first come, first served.

[REGISTER HERE](https://dr14.azur-colloque.fr/inscription/fr/239/inscription)
<!-- font color=red>Registration is full, but email us at eeglab@sccn.ucsd.edu for last minute cancelations.</font -->

<b>Warning: </b> This workshop is <em>not</em> aimed for real beginners
in EEG - such persons would be wasting much of their time.
Some parts of the workshop are fairly technical. The main topics will be
advanced methods for analyzing EEG and allied behavioral data, methods
including spectral decomposition, independent component analysis,
inverse source analysis, information flow, etc.. Some other parts of the
workshop will require basic MATLAB scripting capabilities. Some basic
web resources for learning MATLAB are discussed below. Beginners may
also gain experience using MATLAB by applying the steps discussed in the
EEGLAB wiki tutorial to the sample dataset which you can freely
download.

MATLAB tutorial
----------------

*IMPORTANT NOTE:* A portion of the workshop will be dedicated to writing EEGLAB scripts -- Not being able
to understand MATLAB syntax will mean you will miss out on a large
portion of the workshop.

If you are new to MATLAB or need a refresher, please consult the material on the [Getting started with MATLAB page](/tutorials/misc/tutorial_matlab.html)

If you do not have MATLAB, you can obtain a 30-day trial license for free on the MathWorks website (https://www.mathworks.com/campaigns/products/trials.html).

Workshop material
-----------------

Workshop materials are provided on a USB flash drive. Copy the entire contents of the drive to your computer. Locate the file eeglab.zip, extract it, and follow the setup instructions. If you are using a Mac, make sure to follow these [instructions](https://www.fieldtriptoolbox.org/faq/matlab/mex_osx/) to enable binary files for source localization.

Workshop Program (with corresponding PDFs)
------------------------------------------

The presented slides will be made
available on this page. You only need to bring a
laptop with MATLAB installed.

<span style="color: purple">Purple lettering = lecture</span>
<span style="color: orange">Orange lettering = tutorial</span>

### Monday, June 30th

[**Free symposium: Cloud EEG/MRI/fMRI automated processing pipelines, the SIESTA project**](Symposium_SIESTA_2025.html)<br>
(Toulouse CerCo laboratory)

16:30 --  Shuttle bus pick up at Toulouse train station

17:00 -- Shuttle bus pick up at Toulouse airport

<span style="color: green">

20:30 -- Dinner in Aspet (included in registration). Note that the optional evening MATLAB session was canceled due to a late dinner and also because the speaker, Ramon, could not make it.

### Tuesday, July 1st

<span style="color: green">7:00 - 8:30 Breakfast</span>

**Overview and ICA Theory/Practice**

<span style="color:purple"> 8:30 – 9:45 -- Mining event-related brain dynamics I (Scott Makeig)</span>
<!--[PDF](https://github.com/sccn/sccn.github.io/files/11948460/Makeig_Aspet23_Mining_I.pdf)-->

<span style="color: purple">9:45 – 10:15 -- EEGLAB overview (Arnaud Delorme)</span>
[PDF](https://github.com/user-attachments/files/20992965/EEGLAB_overview2025.pdf)

<span style="color: green">-- Break--</span>

<span style="color: purple">10:30 – 11:30 -- ICA theory (Scott Makeig)</span>
<!--[PDF](https://github.com/sccn/sccn.github.io/files/11948490/Makeig_ICA_Aspet23._pdf.pdf)-->

<span style="color: orange">11:30 – 13:00 -- Data import, Artifact rejection (Claire Braboszcz)
[PDF](https://github.com/user-attachments/files/20995739/Preprocessing_braboszcz2025_edit.pdf)
</span>

<span style="color: green">13:00-14:00 Lunch --</span>

**ICA and source analysis**

<span style="color: orange">14:00 – 15:00 -- ICA decomposition practicum (Claire Braboszcz)</span> [ICLabel Practice](https://labeling.ucsd.edu/tutorial/practice) [PDF](https://github.com/user-attachments/files/20999025/ICLabel.pdf)

<span style="color: purple">15:00 – 16:15 -- Forward and inverse models - the Dipfit tools (Robert Oostenveld)</span> 
[PDF](https://github.com/user-attachments/files/20999227/forward_and_inverse_models_2025.pdf)

<span style="color: green">-- Break--</span>

<span style="color: purple">16:30 – 17:45 -- EEGLAB Dipfit plugin (Arnaud Delorme)</span> 
[PDF DIPFIT](https://github.com/user-attachments/files/21000200/Delorme2025_dipole_connectivity.pdf)
<!-- -->

<span style="color: green">19:45 -- Dinner</span>

### Wednesday, July 2nd

**Group analysis and ICA clustering in EEGLAB**

<span style="color: purple">8:30 - 9:15 -- The Brain Imaging Data Structure (Robert Oostenveld\)</span>
[PDF](https://github.com/user-attachments/files/21012586/fair.and.bids.pdf)

<span style="color: orange">9:15 - 10:30 -- Creating a STUDY using BIDS and preprocessing data (Arnaud Delorme)</span>

<span style="color: green">-- Break--</span>

<span style="color: purple">10:50 – 11:20 -- Finding the best parameter for clean_rawdata/ASR (Fiorenzo Artoni)

<span style="color: purple">11:20 – 11:50 -- PCA vs. ICA and bootstraping ICA using RELICA (Fiorenzo Artoni)

<span style="color: purple">11:50 - 12:30 -- Why cluster ICA components? (Scott Makeig)</span>

<span style="color: green">12:30-14:00 Lunch --</span>

<!-- -->
<span style="color: purple">14:00 - 14:30 -- Practical ICA clustering (Arnaud Delorme)</span>

<span style="color: purple">14:30 - 16:00 -- Statistical analysis: Hierarchical Linear Modelling of EEG data (Cyril Pernet)</span> 
[PDF LIMO](https://github.com/user-attachments/files/20999644/2025_LIMO_QuickStarter.pdf) [PDF HLM](https://github.com/user-attachments/files/20999647/2025_HLM_LIMO_EEGLAB.pdf)

<span style="color: green">-- Break--</span>

<span style="color: green">16:30-18:00-- Hiking excursion</span>

<!-- -->


<span style="color: green">19:45 -- Dinner</span>

### Thursday, July 3rd
 
<span style="color: green">7:30 - 8:30 Breakfast</span>

**Advanced EEG signal processing methods**

<span style="color: purple">8:30 – 9:30 -- Time-frequency decompositions: Theory and practice (Scott Makeig)</span> 

<span style="color: orange">9:30 – 10:00 -- What are EEG microstates? (Fiorenzo Artoni)

<span style="color: green">-- Break--</span>

**General Linear Modeling**

<span style="color: orange">10:20 - 11:30 -- Correcting for multiple comparisons (Cyril Pernet) [PDF](https://github.com/user-attachments/files/20999665/2025_MCC_and_boot_EEGLAB_workshop.pdf)

<span style="color: orange">10:20 - 11:30 -- More STUDY designs and GLM (Cyril Pernet and Arnaud Delorme)

<span style="color: orange">11:30 – 12:30 -- Theory and practice of applying general linear models to EEG data using the LIMO EEGLAB plug-in (Cyril Pernet)</span>
<!--[PDF](https://github.com/sccn/sccn.github.io/files/11965482/EEGLAB_statistics2022.pdf)-->

<span style="color: green">12:30-13:45 Lunch --</span>

**Source information flow**

<span style="color: orange">13:45 – 15:00 -- Continued processing of HW dataset (STUDY design and LIMO) (Arnaud Delorme)</span>

<span style="color: green">-- Break--</span>

<span style="color: purple">15:00 – 17:00 -- Source information flow and Granger-Causal modeling tools, SIFT and ROIconnect toolbox (Arnaud Delorme)</span>
[PDF connectivity](https://github.com/user-attachments/files/21000181/Connectivity_lecture2025.pdf)

<span style="color: green">19:45 -- Dinner </span>
 
### Friday, July 4th

<span style="color: green">7:30-8:30 -- Breakfast</span>

<span style="color: purple">8:30 – 9:30 -- Deep learning and EEG (Arnaud Delorme)</span> 
<!--[PDF](https://github.com/sccn/sccn.github.io/files/11975145/ucsd22workshop_DL-EEG.pdf)-->

<span style="color: purple">9:30 – 10:15 -- Mining event-related brain dynamics II (Scott Makeig)</span> 

<span style="color: green">-- Break--</span>

<span style="color: orange">10:30 – 11:30 -- Practicum, small group projects</span>

<span style="color: orange">11:30 – 12:00 -- General discussion</span>
<!-- -->


<span style="color: green">12:15 -- Lunch</span>

<span style="color: black">13:00 -- Airport/train station shuttle bus leaves Bois Perche</span>

<span style="color: black">Between 14:15 and 14:45 -- drop off at Toulouse/Blagnac Airport</span>

<span style="color: black">Between 14:30 and 15:15 -- drop off at Toulouse Matabiau train station</span>


Further reading
----------------
You can consult a list of relevant EEGLAB papers [here](/others/EEGLAB_References.html) 
