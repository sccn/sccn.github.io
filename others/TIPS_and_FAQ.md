---
layout: default
title: General FAQ
long_title: General frequently asked questions
parent: Support
nav_order: 1
---
# EEGLAB TIPS and FAQ
{: .no_toc }

This FAQ page contains questions we receive and answers we give users,
as well as general tips we think it is important for users to know! Many
other tips are available on the eeglablist archive. To search the list
archive simply use Google, enter relevant keywords and add the
"eeglablist" keyword.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## Basic Topics

###  Is EEGLAB of any interest for expert MATLAB users?
**Answer:** We believe so. First, EEGLAB implements new algorithms for
artifact rejection. Second, for the experienced MATLAB user EEGLAB is a
fast and accurate way to start processing EEG and ERP data and to
directly manipulate signal arrays. If you intend to use the ICA toolbox
functions underlying EEGLAB, EEGLAB itself is a good starting point and
introduction. EEGLAB also provides a full EEG structure to describe your
data (signal, trials, channel location, reaction time, type of the
trials, time limits and sampling rate) and allows you to use this structure
either from the MATLAB command line or in MATLAB scripts.


###  Is MATLAB too slow and does it use too much memory?
**Answer:** Yes, to an extent, but... Because MATLAB sometimes uses large amount of RAM, we also took great care of inserting
options in EEGLAB and in several processing functions to handle low
memory conditions. On the other hand the MATLAB environment offers the
advantage of stability and ease of use. Even the novice user under
MATLAB can scale a data array by multiplying it by a scalar for instance
(and in our software the data array is directly accessible to the user).
MATLAB also offers the advantage of modularity. All of our functions, are
stand-alone functions and most of them can be used independently of each
other. Besides, MATLAB has grown much faster.


### What type of support is offered with EEGLAB?
**Answer:** We cannot guarantee that we will provide full support for
this software but we will be glad to help out if someone encountered any
problem and to correct bugs when reported to us: Write to
eeglab@sccn.ucsd.edu.

### What type of MATLAB license should I buy to run EEGLAB?

When I ask the Mathworks salesman to sell me "only" a
MATLAB license, he gave me prices for MATLAB, Simulink and Symbolic
Math. Do I need all these to run EEGLAB?
**Answer:** No, you do not need all that, you only need MATLAB. If
possible, ask for an educational or even student version, as they are
cheaper. For some spectral decompositions, you may also need the Signal
Processing toolbox which has to be purchased separately.

### Overloaded functions

Under Unix, I often get the following message
''Warning: One or more output arguments not assigned during call to
'XXX'.

??? Unable to find subsindex function for class char. ''


**Answer:** In most cases, this error indicates that MATLAB on Unix may
experience problems. MATLAB might return this error when you or EEGLAB
has defined a variable of the same name as any variable in your MATLAB
workspace or .m file in the MATLAB path. To solve the problem, clear the
variable or rename the function.

###  MATLAB/EEGLAB return an out of memory error

**Answer:** 2 solutions

-   Buy more memory (RAM) for your computer
-   Try the memory mapping scheme (in EEGLAB options) which will allow
    keeping the data on disk. Note that except for Neuroscan files, it
    is still necessary to import the full data file in memory.

### Multi-core use


Does it benefit to have a multi-core machine?

**Answer:** yes, it benefits in two ways. First, you may start in
parallel several MATLAB sessions. Each of them is assigned one of the
processors. Second, if you go to the MATLAB options, you may have the
option to enable multi-core computation (General \> Multithreading).
This option is usually set by default. This is a very efficient option
that will speed up your code usually linearly with the number of core (2
-\> twice faster etc...).

Files: Import/Export/Channel
----------------------------

### Saving single epochs in ASCII files

Is it possible with EEGLAB to save an EEG data sorted in
10 epochs (for example) in 10 ascii files?
**Answer:** you have to do this on the MATLAB command line:

> \>\> epoch1 = EEG.data(:,:,1); 
> \>\> save -ascii epoch1.txt epoch1 
> \>\> epoch2 = EEG.data(:,:,2); 
> \>\> save -ascii epoch2.txt epoch2 
> \>\> epoch3 = EEG.data(:,:,3); 
> \>\> save -ascii epoch3.txt epoch3

### Channels with no assigned position

I work with recordings from 30 channels + 2 EOG channels.
Naturally while exploring the data for artifact components, I want to
have a look at the EOG too. As soon as I want to plot maps, I liked to
leave the EOG out. But if I want to load an electrode position file with
less electrodes than channels in the dataset, EEGLAB doesn't accept
that. Is there a more convenient method than creating two datasets (one
without eog or without an electrode location file)?
**Answer:** Simply blank out all the position fields for these channels
using the channel editor after you have imported the channel location
file (so they do not have an assigned position). Note: You may still
include these channels in the ICA decomposition, even if their reference
is different from the other scalp channels, though you should not
attempt to plot them with a mixed reference. (We are working on a
solution to this for other purposes).

### Importing problem

EEGLAB does not work when I try select the type of data
file to import under \>File \> Import data > From ASCII ...".

**Answer:** Next to the importing text box there is a list box to
indicate which type of data you want to import. Note that, not only you
need to scroll the the list box but also to CLICK on the selected
importing options so that they become selected.

Basic Processing
----------------

### Polhemus orientation

We have been trying to input our polhemus 3-d file into
EEGLAB. Displaying it in 2-d, the main problem is that "0 degrees" is
towards the right ear in Polhemus and "90 degrees" is toward nasion,
while in EEGLAB "0 degrees" is toward nasion and "90 degrees" is toward
the right ear. In other words not only that everything is shifted 90
degrees, but Polhemus (Neuroscan) goes counter-clockwise and EEGLAB goes
clockwise. We are trying to develop some conversion solution for this,
but if

1.  you already have some experience w/ a situation like this and you may
    have some easy solution;
2.  you could advise us on how to get our Polhemus coordinates into EEGLAB
    some other (easier) way, we would appreciate.


**Answer:** It actually depends on how you recorded your Polhemus
coordinates. To fix this problem, under EEGLAB, in the channel editing
window, there is a button "transform axes". Press this button and enter
"theta = 90-theta;" and that will do the trick. Note: press the "auto
shrink" button to visualize all your electrodes. You may also manipulate
the XYZ coordinates and reconvert them to polar.

### Processing current dataset

Remember that all EEGLAB graphic interface always process the current
dataset. This means that if you use an interactive function (Data
scrolling, Epoch rejection, Component rejection) and manually select or
load another dataset from the EEGLAB interface, EEGLAB will apply all
the changes or plot to the new dataset being scrolled. For instance, if
you are scrolling data and select bad epochs, then load another data to
look at it, then come back to your scrolling window to reject these
epochs (and actually press the reject button), the epochs will be
rejected in the **New** recently loaded dataset.

### Epoch time limits

The maximum time does not correspond to the maximum time I
specified. For instance I asked for epochs between 0 and 3 seconds at
125 Hz and end up with an interval of 0 to 2.992 s. There should be
something wrong!
**Answer:** Nothing is wrong. In your example, we must draw (125Hz \*
3seconds = 375 points) and not 376 otherwise we would lose time
linearity i.e. 2 epochs of 3 seconds would be 752, whereas if we draw 6
seconds of the data we would get 751 points !), but if we assign time 0
to the first point, then we must assign time 2.992 to the last point.
Actually, the first point time is undetermined. Since the recording is
made at 125 Hz, there is no possibility to know when the first point was
recorded in between 0 or 0.08 seconds (otherwise one has to sample
faster). By convention we take the first point to be at latency 0 and
the last one at 2.992 (but we could choose latency 0.04 for the first
point and 2.996 for the last one or 0.08 to 3...).

### Too many events?


Could you help me to know why :
I have 7 events, 3 being = 2 and 4 being = 1 in a "mother" file
why, when I extracted epochs on event = 2, I only got 3 epochs (that's
right) and 6 events (that's wrong, isn't it?)?


**Answer:** Your 6 events are probably OK. It depends on the time window
you used for epoching. Any event within the time window of each epoch
will be taken into account. This means that some event outside of all
epoch time window will be ignored and that some events within several
time windows might be duplicated. You should look at the event latencies
before and after epoching and you will see that it is consistent.

### Data filtering

I have a problem to filter data: we see in our EEG data a
component with the frequency of the electronics here, 50 Hz. I would
like to remove only this frequency... but I don't really know to do this
with lowpass and high pass filtering. I think that this phenomenon of
"pollution" by the electric frequency is something current in EEG?
**Answer:** Yes, it is very common.

###  Are there advanced filter functions for EEGLAB?
**Answer:** Check out firfilt plugin at [EEGLAB Plugins page](/others/EEGLAB_Extensions.html).

Advanced Topics
===============

Functions
---------

### Missing trials in ERPimage?

When using the ERP image menu item ('Plot' -'Channel ERP
image'), the top part of the output is the window with the sorted
trials. The number of the trials seems to be off and it appears that not
all trials are displayed. For instance, using a file with 17 trials the
"Sorted Trials' numbering goes from 6 to 12 with apparently 5 trials
being displayed and two half trials on the top and at the bottom of the
display (see attached jpg). This was also observed with another file
that had more trials.


**Answer:** The erpimage() output is due to the smoothing window you
selected. If you use a 5-trial average moving window, the first output
should be the middle of this window (e.g., trial 2.5). Use a 0-smoothing
window (width 1) and all the trials will be shown.

### ERP standard deviation

Is there any way to add lines above and below the average
voltage line to indicate +/- 1 or 2 SD to show data dispersion across
trials?


**Answer:** Use option 'erpstd' of erpimage() in the "More options" text
box of the pop_erpimage() interactive window.

### Cross-subject analysis of spectral power and coherence?

Do you have any good way to across subject/patient
analyses with respect to power and coherence, especially making
statistical comparisons between subjects/patients? Could we somehow use
the data output of EEGLAB?


**Answer:** For cross-subject comparison, tftopo() is a powerful
function that can summarize this information (it uses stored timef() and
crossfO() function outputs). It has to be called from the command line
though.

Artifacts
---------

### Recognizing artifactual components

It is not very difficult to find components related to
eyeblinks, etc. In my case, there are phases during the experiment,
where people speak and/or move their eyes. I find it quite hard to
determine which components are related to these artifacts and I already
wonder if it is possible et all.
**Answer:** To determine which components are related to these artifacts,
one approach is to isolate these trials (selecting them) and then use
menu item "Plot \> Component ERPs \> With component maps" and select the
time window where these event appear. This function will plot which
components contribute to this type of artifact. However, you are correct
in thinking that ICA cannot cleanly resolve ALL artifacts into one or a
few components. For instance, "paroxysmal" artifacts (like the subject
scratching their head during recording) would require a large number of
ICA components to capture the variability of all the artifactual
contributions in the data. Similar events and artifacts should be
carefully pruned from the data before ICA decomposition.

Would muscle components be seen at high frequencies?
**Answer:** Yes, that is typically what we observe. Muscle artifacts
have a broadband high spectral amplitude at high frequencies (20-100 Hz
or more). Also their spectrum does not look like the standard EEG
(exponential decrease).

### Rejecting artifacts

I am currently using ica to correct for artifacts. In the
past I've visually inspected each single-trial epoch separately,
identified those trials with artifact activity, and then trained ICA on
each trial separately to identify and remove artifactual components. As,
you can imagine this process is extremely time consuming. Is it
effective to train ICA on multiple or all concatenated trials at once,
remove artifactual components, and then go back to visually inspect the
corrected data for outlying artifacts?


**Answer:** You may not have grasped the nature of ICA, which is to
extract data components whose activities (activations) are independent
of the activities of other data sources. For this independence to be
detected, it must be fully \*expressed in the data\* -- and this
normally requires many (\>nchannels^2) data points. So separately
decomposing individual epoch is just the wrong approach. We currently
favor a seven-step approach:

1.  Visually reject unsuitable (e.g. paroxysmal) portions of the
    continuous data.
2.  Separate the data into suitable short data epochs.
3.  Perform ICA to derive independent components.
4.  Perform rejection on the derived components based on inspection of
    their properties.
5.  Visually inspect the raw data epochs selecting some for further
    rejection.
6.  Reject the marked components and data epochs.
7.  Perform ICA a second time on the pruned data - this may improve the
    quality of the ICA decomposition, revealing more independent
    components accounting for neural, as opposed to mixed artifactual
    activity.

These steps are made easier and more efficient by EEGLAB, which also
includes functions suggesting to the user epochs, channels and
components suitable for rejection.

ICA
---

### Re-running ICA


While trying within EEGLAB to remove artifacts using ICA,
I had trouble in recalculating an ICA decomposition after removing
components. I tried to follow the guidelines in the tutorial, thinking
that with fuzzy components it might work better to remove some clear
artifact components first and the run a new ICA. When I tried to do
that, the second ICA always took much longer and I got also some error
message in the end telling me, that there was something wrong with the
result.


**Answer:** The standard procedure we advise is first to perform ICA on
the data and to remove bad trials using the ICA component activities. If
you remove ICA components, the rank of the data will decrease (to
\<nchans). If the data have n channels, the rank of the data is (most
probably) n. If you remove one component it will become n-1, and ICA
will not be able to find n components in the pruned data). Thus, as a
first step, you should only remove bad trials. This procedure will not
alter the dimensionality of the data. As a second step, recompute ICA
and remove bad components (the second run of ICA should result in
clearer artifact components (for instance muscle at high frequencies),
not contaminated by strong outlier trials. If you remove ICA components
and want to re-run ICA, you must decompose the data with the 'pca'
option to reduce the dimensionality of the decomposition to match the
data rank (see below).

### Baseline removal and preparing data for ICA


What is the rationale behind baseline zeroing the data
before running it thru ICA, and is that always recommended?


**Answer:** It is recommended because the EEG might have some electrical
artifacts (slow trends) that you want to remove. If your data is
perfectly flat (at very low frequencies), then you shouldn't need to do
that. You should baseline-zero each epoch, else use the continuous data
and lowpass it if you are interested in focusing on e.g. 3-40 Hz
activity. Also, you should prune the data of 'messy' patches (probably
associated with a series of 1-of-a-kind, non-stationary maps). The data
scrolling utility in EEGLAB makes this convenient, and if you perform
this on the continuous data, records breakpoint events that guide
subsequent epoching. Else, you can more severely prune the data to train
the ICA model, then pass more of the data through the model (at the cost
of somewhat higher SNR (signal to noise ratio) in the activation time
series).

### Reducing the number of ICA components


I don't know how to make the independent component
dimension reduced by PCA in EEGlab4.0. For example, I want to obtain 4
independent components from 32-channel EEG data.


**Answer:** To extract 4 components, in the second text box of the
"Tools \> Run ICA" interactive pop-up window, enter " 'pca', 4 " or
"'ncomps', 4" and that will do it.
Note we do not recommend using PCA (" 'pca', 4 ") unless you have some
good reason. Using first PCA components only will truncate the data
(irrespective of components), and then ICA may not be able to find
relevant components. The second possibility ("'ncomps', 4") is more
acceptable theoretically since it is a true ICA decomposition (that uses
a rectangular matrix). In general, we advise finding as many components
as possible (e.g. if you have enough memory on you computer to run ICA
over all the channels).

### Running Extended ICA


You mentioned that we should use the extended ICA
algorithm to extract subgaussian components (i.e., 60-Hz noise). For our
MEG data (using the old binica() for Windows) we get several subgaussian
components, but there is still leakage of 60 Hz onto many of the
supergaussian components as observed with an FFT (mutlitaper). In the
EEGLAB tutorial (1st_readme.txt) I noticed a question mark on whether
binica for Windows (the old one) was stable. Is it unstable? Should we
use the extended version? Can we use the old binica() for Windows?
**Answer:** MATLAB seems to have speeded up running runica() tenfold
from 5.3 to 6.x ! So binica() just gives us a 30% improvement in speed
these days (although also a 2-4-fold decrease in process size, important
for large datasets under 32-bit memory addressing). In the future, we
will compile the improved version of binica() for Windows. The
improvements concerned mainly the 'pca' option, which you may not need
to use.

### ICA applied to data epochs or continuous data

I have noticed that the runica() does not include a field
for epoch size, so how does ICA recognize the epochs? Doesn't this make
a difference to the way ICA is handled?
**Answer:** Epochs are concatenated before running ICA. In ICA, all time
points of all epochs are shuffled so that epoch information is
irrelevant.


I have some continuous 32-channel EEG data on which I
would like to apply Infomax ICA. I am primarily interested in the 100
epochs from the data, which are 3000 frames each. There are only about
20-40 frames between the end of one epoch and the beginning of the next.
Should I apply ICA to the continuous data, then epoch the ICs, or apply
ICA to the concatenated epochs?
**Answer:** You can apply ICA to either of them. Usually, we prefer to
apply ICA to the concatenated epochs so ICA component are more likely
to represent activity related to the task, but continuous data are fine
too, especially if you have few epochs or few data points, since most of
the same EEG and artifact processes are likely to be active 'between'
epochs.

### ICA scalp map polarity

For multiple-epoch data, the scalp map obtained for the
different epochs is the same for a particular component. Is this normal
or is there some mistake that's being done in the analysis?
**Answer:** Because the ICA algorithm is applied in the electrode space
domain, the same scalp maps are returned for all epochs. However, the
time course of one ICA component is different for each epoch (if its
activation value is 0 at a given time, it means that this component is
not expressed in the data at that particular time).

### ICA activity warning

I am seing the warning message below. What does it mean?

```
ICA activity do not match ICA weights, see ...
```

If you re-reference the data after running ICA, or if you remove channels, you might see the warning message above.
As a rule of thumb, never perform a lossy re-referencing or channel
removal after running ICA. Instead, remove the channel or re-reference the data, then run ICA again.
When data is referenced or when channels are removed, the ICA scalp topographies are also referenced, while the ICA activity remains unchanged.
However, this process violates the assumptions of ICA. Specifically, the relationship ICA_activations = ICA_weights * EEG_data no longer holds.
Despite this, we contend that this altered representation is the closest approximation to the state before re-referencing or the removal of channel(s). The alternative approach of recomputing activities is not ideal, as it does not constitute a standard ICA decomposition.
It is important to note that if you save and reload the data, ICA activations are not saved by default. As a result, EEGLAB will recompute them using the ICA weights and data when you load the data again, which deviates from the standard ICA decomposition. If it is important for you to retain the ICA activities, we
advise that you save the data from the command line using 

```
save('-mat', 'EEG_dataset_with_ica.set', '-struct', 'EEG');
```

Time Frequency
--------------

### Timef() spectral decompositions: properties and discrepancies

Is it not true that the ERP for a condition can be
completely reconstructed from the timef() results, including ITC? One
could write a function that takes the outputs of timef
('times','freqs','ersp','itc') and gives as it's output the ERP. Could
one then usefully manipulate the values in ERSP and ITC and see how the
ERP would have looked without some aspect of the ERSP (like, take away
the inter-trial coherence in the alpha band and leave all else the
same). Finally, could one subtract the 'ersp' and 'itc' between two
conditions and then reconstruct the difference ERP?

I've been playing with the parameters of timef() and am surprised by the
large differences in results dependent on the values for 'cycles',
'winsize', etc. This even makes we insecure about previous timef()
results ....


**Answer:** Yes, this is possible (with some fuzziness regarding
overlap-adding the overlapping spectral estimates, undoing the effects
of tapering (windowing), etc. I haven't focused on strictly "invertible"
time/frequency transforms - which tend to be restrictive, since I am
interested in analysis rather than synthesis.


However, in general the answers will be like the following:


Removing alpha ITC would be like filtering out the alpha in single
trials and replacing it with random-phase noise. The effect on the ERP
would be more or less exactly like filtering out the 10 Hz from the ERP,
plus adding some noisiness...


The ERSP is a different matter, as ERSP changes can only produce a
(stat. signif) ERP in conjunction with signif ITC. Adding an ampl.
increase at alpha, say, to the ERSP and then going back to the time
domain would scale up alpha band power in the ERP -- if the ITC stays
the same.


Changing both ERSP and ITC can be made to give any kind of mixed results
summing those above.


Re timef() variability - think of it like the focus / f-stops on a
camera - you cannot achieve focus on every plane at once. It is also
like Heisenbug uncertainty, I hear - you cannot localize a 'particle'
(wavelet) in time and frequency simultaneously. Or, as in cinema you,
where one cannot record motion in a single instant, one cannot record an
exact power estimate at an instant. Basically, a "good" time/frequency
method can only give an estimate within a time/frequency area whose area
is fixed, but not its shape. i.e. Do you want long-and-thin, or
fat-and-short, or square?


So, one can make exact comparisons only across channels or components
within the same t/f transform.

### Time-frequency decomposition time range problem

I am afraid that the time scale is slightly off for the
time-frequency plots. E.g. a component time-frequency plot from a
dataset where the epochs are from -2560 ms to +2046 ms and according to
the plot's time scale it appears that the epoch is from slightly before
-2000 ms to slightly over +1500 ms. Do you know why?
**Answer:** It is normal that the time limits are different from the
original dataset, since the FFT (or wavelet) is applied over time
windows and we consider the center of these windows. As a result, you lose half the window size on each edge of the plot (some hundred
milliseconds depending on the window size and the sampling rate).

### Spectrum using FFT, Welch or multitaper

You should most likely use the pwelch method (implemented in the EEGLAB
spectopo function). It is a windowed FFT (several FFT averaged).

The Thomson method (usually known as multitaper) is good too. It is
first projecting the data onto an orthogonal base, then performing FFT.

They should all return similar results (FFT, pwelch, multitaper). I
guess the Thomson method is less sensitive to noise but also
more complex to use. I guess it would also be possible to use the welch
method on top of multitaper. It is all a matter of preference. I would
advised using the pwelch method which is easy (you just give as an
option the length of the windows and the overlap). Multitaper would
require you to select the number of basis vector in your othogonal base
and this is much less intuitive (and also has consequences on the
frequency resolution you can achieve).

### Multitaper, FTT, wavelets for time-frequency decomposition?

I have been using the new EELAB toolbox for the past
couple of weeks, especially timef() and crossf(). The multitaper method
with bootstrap statistics has been giving me very nice stable results.
Timef() with wavelets gives slightly different results, but also
interesting. I noticed though that all the analysis has been designed to
study coherence, phase-coherence, ITC, etc, for data organized as
epochs. (e.g. inter-trial effects).


Is there a function for computing time-varying coherence between
'independent' activation functions for continuous spontaneous recordings?
(i.e., spontaneous coherence for brief windows of time, 200-300ms). J.P.
Lachaux (from Varela's Lab) has several papers investigating this issue.


**Answer:** We also programmed multitaper methods for timef(), but
removed them from the current more flexible versions (not available yet
on the Internet (May 23, 2003)). Note that we usually use neither the
FFT (0) or N-cycle wavelet methods, but a compromise (0.5) setting that
trades off frequency resolution (at low freqs) with stability at high
freqs.


We have not yet had cause to program flexible visualization and handling
of continuous coherence measures, though you can run timef()/crossf() on
a continuous dataset (which is internally considered by EEGLAB to be 1
epoch). We'd welcome suggestions and/or code.

In our experience, multitaper decomposition are not very useful because
we are interested in low frequency activities (i.e. 5 Hz) at which we
want the maximum time resolution. So we had to use 1 multitaper only
(using several multitapers reduces noise but also reduces the
time/frequency resolution) which is equivalent to a standard FFT. Using
several multitapers in the gamma band would make sense though because
the time resolution is much higher and not critical. Multitaper has been
removed from the newtimef() function but it is still possible to use it
in the timef() function.

### Spectrogram orientation?

We normally display our chrono-spectrograms with the lower
frequencies at the bottom of the plot, just the opposite how Eagle does
it. Is there an easy way to change this?


**Answer:** Right now the only way to change this is to click on the
figure and type


\>\> set(gca, 'ydir', 'normal');


I guess you could edit the timef() and crossf() MATLAB functions to
change all the plots to this format. We will introduce this as an option
in the future.

Single Trial
------------

### Can I sort single-trial ERPs on amplitude?

How can I sort single trial ERP in erpimage() based on
their amplitude at a determined latency.
**Answer:** use the 'ampsort' option of erpimage() (not separately
queried in GUI, you have to put it into the "More options" text box at
the bottom right of the pop_erpimage() interactive window). Erpimage()
option 'ampsort' sorts on spectral amplitude; if you want to sort on
potential value at some epoch time point, then use option 'valsort'.

Miscellaneous
=============

### Epoching data on custom events

For reasons too complex to describe, I am trying to epoch
with respect to various latencies RELATIVE to the events in my dataset.
For example, epoch onset = event latency + some value, so I can
calculate the set of latencies and use them in a call to epoch.m (the
second parameter). I couldn't specify the latencies directly using
pop_epoch function.


**Answer:** There are 2 solutions for this problem:

1\) modify event latencies or create new events. For instance

``` matlab
for index = 1:length(EEG.event)
    EEG.event(index).latency = EEG.event(index).latency + 10; % +10 sample points
end;
% then store data
[ALLEEG EEG CURRENTSET] = eeg_store(ALLEEG, EEG, CURRENTSET);
% then epoch from the menus
```

2\) use the epoch() function instead of the pop_epoch() function. The
epoch() function processes latencies directly. You will then obtain a
MATLAB array that you may import in EEGLAB.

Figures
-------

### Formatting figures for publication

The lines in erpimage() (e.g. 'X' axis on the average) are
too thick. How can I control their thickness?


**Answer:** To change the figure aspect for publication, you can go in
the figure menu and use the MATLAB menu item "Tools \> Edit". Then you
can select any object in the figure. The second button will display a
contextual menu where you will be able to change line thickness, color,
font aspects..., or even draw additional lines or add text. We also
export figures as Postcript files and open them with Adobe Illustrator
in vector format to fine tune it. See also this web page.

### Exporting figures

Could you tell me how to export figures from EEGLAB (to
include in a "word.doc" for example, or to export to Excel)? This for
the scroll channel data eegplot(), and for channel spectra and
maps...and other plots....


**Answer:** For most EEGLAB figures, simply use menu item "File \>
Export".


For the scrolling channel data function (eegplot()), first use menu item
"Figure \> Edit figure" to restore the default MATLAB menu. From the
command line, you may also use the command


\>'\>' print -djpeg scrollfigure.jpg %to print in jpeg

\>'\>' print -depsc scrollfigure.eps %to print in postcript color


Note: use the command "\>'\>' set(gcf, 'paperpositionmode', 'auto')"
first to print the figure in the same aspect ratio as it is shown on
screen.

### Figures and printing problems

When I tried to plot the channel spectrum, the axis labels
and tick labels did not appear clearly on the screen and I've got the
following error messages from the MATLAB command line: "Plotting scalp
distributions: Warning: Unrecognized OpenGL version, defaulting to
1.0"
**Answer:** You may solve the problem by changing the OpenGL version on
the MATLAB command line by typing: "feature('UseGenericOpenGL',1)".

Sometimes MATLAB crashes when I try to print a figure. If
I save the figure on disk, first, some parts are missing. Do you know
how to fix this problem?
**Answer:** You may solve the problem by changing the OpenGL version on
the MATLAB command line by typing: "feature('UseGenericOpenGL',1)" For
the printing error, we also experience this; it is a MATLAB problem
which is not consistent between Windows and Linux. We always print or
save to files (.jpg or .eps Postscript), then print the files. For
instance, use the software
[FreeRawPrint](http://download.com.com/3001-2088-10178995.html) to send
the Postscript file to the printer under windows. Even with this
strategy, some parts of complex figures may disappear, but this is rare
(then we use screen captures, or use a Windows machine, since printing
seems to be more reliable under Windows OS). We hope MATLAB will become
better at this in the future (Is MATLAB listening?).
