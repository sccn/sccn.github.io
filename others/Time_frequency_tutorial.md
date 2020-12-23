---
layout: default
title: Time frequency tutorial
parent: Other documents
---

Time frequency decompostions
============================

Time frequency decomposition are a central part of EEG data analysis. In
this section, we will review the basic and also some more advanced
features of time frequency decompositions. The function that computes
time-frequency decomposition, has about a 100 different parameters.

There are standard range of frequencies in human that have been
designated using specific names.

![center\|alt text](/assets/images/Freqs.jpg)

Note that these frequencies are never present as sinosoids in actual EEG
data. Instead, we most often always observe a mixture of such
frequencies.

![center\|alt text](/assets/images/Freqs2.jpg)

Actual EEG signal can be seen as a mixture of different frequencies. As
shown below, when mixing 2Hz, 10Hz, and 20Hz signals, a complex signal
may be observed.

![center\|alt text](/assets/images/Timefreq1.jpg)

If we run a simple Fourier Transform on this data (we will see later in
this document what is actually a Fourrier Transform), then we will be
able to observe 3 peaks of the same amplitude at 2, 10 and 20 Hz.

![center\|alt text](/assets/images/Timefreq2.jpg)

Now, if we take a real EEG signal, it is possible to decompose such
signal into a superposition of signal at different sinusoidal signal at
different frequencies. Note that not only the amplitude of such
sinoisoid but also their "phase" (the horizontal offset).

![center\|alt text](/assets/images/Timefreq3.jpg)

<div align=right>

Return to [EEGLAB Wiki](/EEGLAB "wikilink")
Return to [SCCN Wiki Home](/Main_Page "wikilink")

</div>