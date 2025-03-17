---
layout: default
title: EEGLAB 2025 Aspet
long_title: EEGLAB 2025 Aspet workshop
parent: Past workshops
grand_parent: Workshops
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

If you do not have MATLAB, you can obtain a 30-day trial license for free on the [mathworks website](https://www.mathworks.com/campaigns/products/trials.html).

Workshop Program (with corresponding PDFs)
------------------------------------------

<b>Material for workshop tutorials (including EEGLAB) will be made available on
USB keys.</b> Presented slides will be made
available during the workshop. You only need to bring a
laptop with MATLAB installed.

<span style="color: purple">Purple lettering = lecture</span>
<span style="color: orange">Orange lettering = tutorial</span>

### Monday, June 30th

[**Free symposium: Cloud EEG/MRI/fMRI automated processing pipelines, the SIESTA project**](Symposium_SIESTA_2025.html)<br>
(Toulouse CerCo laboratory)

16:30 --  Shuttle bus pick up at Toulouse train station

17:00 -- Shuttle bus pick up at Toulouse airport

<span style="color: green">

19:45 -- Dinner in Aspet (included in registration)

20:45 – 21:30 -- Optional MATLAB fundamentals session by Ramon Martinez

### Tuesday, July 1st

<span style="color: green">7:00 - 8:30 Breakfast</span>


**Overview and ICA Theory/Practice**

<span style="color:purple"> 8:30 – 9:45 -- Mining event-related brain dynamics I (Scott Makeig)</span>
<!--[PDF](https://github.com/sccn/sccn.github.io/files/11948460/Makeig_Aspet23_Mining_I.pdf)-->

<span style="color: purple">9:45 – 10:15 -- EEGLAB overview (Arnaud Delorme)</span>
 <!--[PDF](https://github.com/sccn/sccn.github.io/files/11945743/EEGLAB_overview2023.pdf)-->

<span style="color: green">-- Break--</span>

<span style="color: purple">10:30 – 11:30 -- ICA theory (Scott Makeig)</span>
<!--[PDF](https://github.com/sccn/sccn.github.io/files/11948490/Makeig_ICA_Aspet23._pdf.pdf)-->

<span style="color: orange">11:30 – 13:00 -- Data import, Artifact rejection (Ramon Martinez) <!--[PDF](https://github.com/sccn/sccn.github.io/files/11947670/EEGLAB_WS_ASPET_2023_preprocessing_Session1.pdf)-->
</span>

<span style="color: green">13:00-14:00 Lunch --</span>

**ICA and source analysis**

<span style="color: orange">14:00 – 16:00 -- ICA decomposition practicum (Ramon Martinez)</span> <!--[PDF](https://github.com/sccn/sccn.github.io/files/11947670/EEGLAB_WS_ASPET_2023_preprocessing_Session1.pdf) (same PDF as previous session)-->


<span style="color: green">-- Break--</span>

<span style="color: purple">16:15 – 17:15 -- Forward and inverse models - the Dipfit tools (Robert Oostenveld)</span> 
<!--[PDF](https://github.com/sccn/sccn.github.io/files/11945798/forward.and.inverse.models.pdf)-->

<span style="color: purple">17:15 – 17:45 -- Using the EEGLAB Dipfit plug-in (Arnaud Delorme)</span> 
<!--[PDF](https://github.com/sccn/sccn.github.io/files/11950613/dipfit.pdf)-->

<!-- -->

<span style="color: green">19:45 -- Dinner</span>




### Wednesday, July 2nd

**Group analysis and ICA clustering in EEGLAB**


<span style="color: purple">8:30 - 9:15 -- Why cluster ICA components? (Scott Makeig)</span>

<span style="color: purple">9:15 - 10:00 -- Cluster permutation testing (Robert Oostenveld)</span> 
<!--[PDF](https://github.com/sccn/sccn.github.io/files/11954943/cluster.statistics.pdf)-->

<span style="color: green">-- Break--</span>

<span style="color: purple">10:15 - 10:45 -- Making data <i>FAIR</i> with BIDS (Robert Oostenveld)</span> 
<!--[PDF](https://github.com/sccn/sccn.github.io/files/11954944/fair.and.bids.pdf)-->

<span style="color: purple">10:45 - 11:45 -- Continued processing of HW dataset (ICA) (Ramon Martinez)</span> <!--[PDF](https://github.com/sccn/sccn.github.io/files/11980297/EEGLAB_WS_ASPET_2023_preprocessing_Session1_cont.pdf)-->


<span style="color: purple">11:45 - 12:45 -- Continued processing of HW dataset (STUDY design) (Ramon Martinez)</span> <!--[PDF](https://github.com/sccn/sccn.github.io/files/11965428/EEGLAB_WS_Aspet_2023_GroupAnalysis.pdf)-->

<!-- -->


<span style="color: green">12:45-14:00 Lunch --</span>

<!-- -->
<span style="color: orange">14:00 – 16:00 -- Practicum (use your own data)

<span style="color: green">-- Break--</span>

<span style="color: green">16:30-18:00-- Hiking excursion</span>

<!-- -->


<span style="color: green">19:45 -- Dinner</span>






### Thursday, July 3rd
 
<span style="color: green">7:30 - 8:30 Breakfast</span>


**Time-frequency analysis**

<span style="color: purple">8:30 – 9:30 -- Time-frequency decompositions: Theory and practice (Scott Makeig)</span> 

<span style="color: purple">9:30 – 10:00 -- Phase-Amplitude Coupling (Ramon Martinez)</span> <!--[PDF](https://github.com/sccn/sccn.github.io/files/11965384/RMC_PACTools_EEGLAB_WS_Aspet_2023_PDF.pdf)-->


<span style="color: green">-- Break--</span>


**General Linear Modeling**


<span style="color: orange">10:15 - 11:30 -- Continued processing of HW dataset (STUDY design) (Ramon Martinez)</span> <!--[PDF](https://github.com/sccn/sccn.github.io/files/11965428/EEGLAB_WS_Aspet_2023_GroupAnalysis.pdf) (same PDF as previous day)-->

<span style="color: orange">11:30 – 12:30 -- Theory and practice of applying general linear models to EEG data using the LIMO EEGLAB plug-in (Arnaud Delorme)</span>
<!--[PDF](https://github.com/sccn/sccn.github.io/files/11965482/EEGLAB_statistics2022.pdf)-->

<span style="color: green">12:30-13:45 Lunch --</span>

**Source information flow**

<span style="color: orange">13:45 – 15:00 -- Continued processing of HW dataset (STUDY design and LIMO) (Ramon Martinez and Arnaud Delorme)</span>

<span style="color: green">-- Break--</span>

<span style="color: purple">15:00 – 17:00 -- Source information flow and Granger-Causal modeling tools, SIFT and ROIconnect toolbox (Arnaud Delorme)</span>
<!--[PDF](https://github.com/sccn/sccn.github.io/files/11965451/Connectivity_lecture2023.pdf)-->

<span style="color: green">19:45 -- Dinner </span>
 
### Friday, July 4th

<span style="color: green">7:30-8:30 -- Breakfast</span>

<span style="color: purple">8:30 – 9:30 -- Deep learning and EEG (Arnaud Delorme, Dung Truong)</span> 
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
