---
layout: default
title: Firfilt FAQ
parent: Other documents

---
EEGLAB Filtering FAQ <font color=green> - Done</font>
===
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

### Q. What are passband, stopband, transition bandwidth, cutoff frequency, passband ripple/ringing, and stopband ripple/attenuation?

A. You can find explanations in this
[PDF presentation](https://github.com/downloads/widmann/Firfilt/Firfilt.pdf)
created by Andreas Widmann.

### Q. What is the difference between the “Basic FIR filter (legacy)” and the “Basic FIR filter (new)”? Which should I use?

A. The heuristic for automatically determining the filter length in the
legacy basic FIR filter (pop_eegfilt) was inappropriate (possibly
causing suboptimal filtering or unexpected filter effects). The new
basic FIR filter (pop_eegfiltnew) has a new heuristic for automatically
determining the filter length and is based on the Firfilt plugin. The
legacy function should only be used for backward compatibility purposes.

### Q. What is the difference between the “Basic FIR filter (new)” and the “Windowed sinc FIR filter”?

A. Both are based on windowed sinc filters. The basic filter applies a
hardcoded hamming window, has an automatic default for filter length,
and is defined by the passband edges. The windowed sinc FIR filter
allows manual selection of window type, estimation of filter length by
transition bandwidth (no default), and is defined by cutoff frequencies
(-6dB, half amplitude).

### Q. Why does Firfilt-plugin run faster than the legacy EEGLAB filter?

A. The Firfilt plugin does not use filtfilt to achieve zero-phase but
shifts the signal by the filter’s group delay (NB: requiring ODD filter
length/even filter order). So, the data are only filtered once with
multi-threading (filtfilt does not seem to be multi-threading capable).

### Q. What is the recommended passband ripple/stopband attenuation/window type?

A. Ripple, i.e. deviation from the requested frequency response (0 in
stopband, 1 in passband) is equal in passband and stopband in windowed
sinc FIR filters. Ripple/attenuation is defined by the window type.
0.002 to 0.001 (that is, 0.2 to 0.1%; Hamming or Kaiser window) are
reasonable starting values. This equals a stopband attenuation of -53 to
-60 dB which is ok.

### Q. Should we prefer separate high- and low-pass filters over bandpass filters? (09/30/2020 updated)

A. With separate high- and low-pass filters, transition bandwidth can
be defined independently. High-pass filters often require narrower
transition bands than low-pass filters. Separate filtering is preferable
in these cases.

### Q. What is the difference between filter length and filter order?

A. Filter order is defined as filter length minus 1.

### Q. What is the transition band?

A. The transition band is the frequency band/range between the passband
edge and the stopband edge. In windowed sinc FIR filters the -6dB cutoff
is in the center of the transition band.

### Q. What is the slope of windowed sinc FIR filters in dB/oct (as in IIR filters)?

A. Slope CANNOT be defined in dB/oct for windowed sinc FIR filters.
Rather use transition bandwidth. There is no straightforward conversion
of slope in dB/oct to transition bandwidth due to conceptual
differences between FIR and IIR filters. IIR filters do not have a
defined stopband.

### Q. What is the lower limit for cutoff frequency for high-pass filter?

A. There is no theoretical lower limit, however, the lower the cutoff
the steeper is the roll-off and the higher is the filter order (length).
Very low cutoff frequencies as low as 0.01 Hz as sometimes found in the
literature require extremely long filters (FIR) or are prone to
instability (IIR). To our experience a lower limit of about 0.1 Hz is
recommendable for FIR filters. For lower cutoff frequencies consider IIR
filters combined with a reduced sampling frequency of the signal.

### Q. What is the recommended transition bandwidth (for a windowed sinc FIR high-pass filter)?

A. Generally, the slope in the frequency domain should be as low/flat as
possible, that is the transition band as wide as possible. Steeper
slopes reduce the precision in the time domain; distortions and
artifacts are additionally spread wider due to the longer filter length.
A good staring value for a high-pass filter: twice the cutoff frequency
(-6 dB) for cutoff \<= 1 Hz, 2 Hz for cutoff frequency \< 1 and \<= 8 Hz
and 25% of cutoff frequency for cutoff \> 8 Hz. This is also the
heuristic implemented in the new basic FIR filter (generalized for all
critical frequencies). However, please note, that it is recommended to
(manually) adjust this heuristic to the application of interest. Do not
go beyond twice of the cutoff frequency (i.e., transition band goes
below DC/0 Hz). TIP: Strong attenuation (\<\< -60dB) can be important
for DC/0 Hz (e,g,, to get rid of the DC offset for Biosemi files or to
avoid baseline correction). By using twice of the cutoff frequency for
transition bandwidth, a type 1 windowed sinc filter can be tuned for
excellent DC attenuation.

### Q. What stopband attenuation is good?

A. The community default of Hamming window/-53dB is a good starting
value. With Kaiser windows stopband attenuation can be precisely
adjusted.

### Q. How can I find optimal values for cutoff frequencies, attenuation, and filter length for my particular application?

A. By testing and systematically comparing the effects of different
filters on the signal in the time domain.

### Q. Where can I read more about windowed sinc FIR filters?

A. Check out [Engineers guide to digital signal
processing](http://www.dspguide.com/).

### Q. For Granger Causality analysis, what filter should be used? (11/21/2020 Updated)

A. There are a few important things to confirm.

-   Barnett and Seth (2011) showed that multivariate Granger causality
    is in theory invariant under zero-phase (a.k.a. phase-invariant)
    filter. They do recommend filtering to achieve stationarity (e.g.,
    drift, line noise) See Seth, Barrett, Bernett (2015).
-   However, in practice, filtering causes problems in calculating
    multivariate Granger causality. The main problem is the increase in
    model order. This is because filtering makes the power spectrum
    density of the signal complicated (low power in the stopband, steep
    roll-off, etc). See the following example: 33ch EEG, downsampled to
    100 Hz, without (top) and with (bottom) applying 44.5Hz low-pass
    filter (FIR, Blackman, TBW 1 Hz). Notice that the estimated model
    orders is worsened from 10 (without LPF) to 14 (with LPF)--but
    apparently taking 16 (with LPF) is the right decision here from AIC,
    FPE and HQ results.

![](/assets/images/ModelOrderComparison.png)

Here is another comparison: with and without notch filter at 30Hz
(cutoff freq 28 and 32Hz, TBW 0.5Hz). Note the suggested order became
10-12 to 11-15 with the notch filter on.

![](/assets/images/NotchFilterDemo.png)

-   The second problem, which comes from the same reason mentioned
    above, is that empirical estimates of VAR parameters yields unstable
    models due to poor parameter estimate for increased model order.
-   The third problem is that filtering causes numerical instabilities
    in estimating causality.

How can we address these problems?

-   When applying a high-pass filter to achieve stationarity, let the
    transition band end at DC (i.e. 0Hz). For example, when you use
    EEGLAB's 'Basic FIR filter (new, default)‘ to apply high-pass filter
    with 'passband edge' below 2-Hz, the transition band is
    automatically adjusted so that it always ends at DC. (We use 1-Hz
    high-pass for the ICA purpose; empirical test is required to see
    whether 2-Hz high-pass is beneficial for GCA compared with 1-Hz). If
    you want to set the high-pass filter passband edge above 2 Hz, we
    recommend you use 'Windowed sinc FIR filter' to design the filter so
    that it has the stopband at DC. (CAUTION: 'Windowed sinc FIR filter'
    uses **cutoff frequency** and not **passband edge** i.e. cutoff
    frequency of 1 Hz is equivalent to passband edge at 2 Hz; See
    [Q3](http://sccn.ucsd.edu/wiki/Firfilt_FAQ#Q._What_is_the_difference_between_the_.E2.80.9CBasic_FIR_filter_.28new.29.E2.80.9D_and_the_.E2.80.9CWindowed_sinc_FIR_filter.E2.80.9D.3F))
-   When treating the line noise, use CleanLine() instead of notch
    filter because the former is phase-invariant.
-   When downsampling data (which is useful for multivariate Granger
    causality analysis), use mild anti-aliasing filter and do not let
    the stopband below the Nyquist frequency. In practice, use the
    following example. In this example, you are downsampling your data to 200Hz, with the cutoff
frequency being 160Hz (i.e. 200Hz\*0.8) and the transient bandwidth 80Hz
(i.e. 200Hz\*0.4).

    ```matlab
    EEG = pop_resample(EEG, 200, 0.8, 0.4);
    ```

This page was created by Makoto Miyakoshi and Andreas Widmann.

## References and recommended readings

-   Duncan-Johnson, C. C., & Donchin, E. (1979). The time constant in
    P300 recording. Psychophysiology, 16, 53–56.



-   Barnett, L., & Seth, A. K. (2011). Behaviour of Granger causality
    under filtering: theoretical invariance and practical application.J
    Neurosci Methods. 201, 404-419.



-   Van Rullen, R. (2011). Four common conceptual fallacies in mapping
    the time course of recognition. Frontiers in Psychology, 2, 365.
    doi: 10.3389/fpsyg.2011.00365



-   Acunzo, D. J., MacKenzie, G., & van Rossum, M. C. W. (2012).
    Systematic biases in early ERP and ERF components as a result of
    high-pass filtering. Journal of Neuroscience Methods, 209, 212–218.
    doi: 10.1016/j.jneumeth.2012.06.011



-   Rousselet GA (2012) Does filtering preclude us from studying ERP
    time-courses? Front. Psychology 3:131. doi: 10.3389/fpsyg.2012.00131



-   Widmann, A., & Schröger, E. (2012). Filter effects and filter
    artifacts in the analysis of electrophysiological data. Frontiers in
    Psychology, 3, 233. doi: 10.3389/fpsyg.2012.00233



-   Zoefel, B., & Heil P. (2013). Detection of near-threshold sounds is
    independent of EEG phase in common frequency bands. Front Psychol,
    4, 262.



-   Luck, S. J. (2014). An introduction to the event-related potential
    technique (2nd ed.). Cambridge, MA: MIT Press.



-   Widmann, A., Schröger, E., & Maess, B. (2015). Digital filter design
    for electrophysiological data--a practical approach. J Neurosci
    Methods, 250, 34-46. doi: 10.1016/j.jneumeth.2014.08.002
    [link](http://home.uni-leipzig.de/~biocog/eprints/widmann_a2015jneuroscimeth250_34.pdf)



-   Tanner, D., Morgan-Short, K., & Luck, S. J. (2015). How
    inappropriate high-pass filters can produce artifactual effects and
    incorrect conclusions in ERP studies of language and cognition.
    Psychophysiology, 52(8), 997-1009. doi: 10.1111/psyp.12437



-   Seth, A. K., Barrett, A. B., & Barnett, L. (2015). Granger causality
    analysis in neuroscience and neuroimaging. J Neurosci. 35,
    3293-3297.



-   Maess B, Schröger E, Widmann A. (2016). High-pass filters and
    baseline correction in M/EEG analysis. Commentary on: "How
    inappropriate high-pass filters can produce artefacts and incorrect
    conclusions in ERP studies of language and cognition". J Neurosci
    Methods. \[Epub ahead of print\]



-   Tanner D, Norton JJ, Morgan-Short K, Luck SJ. (2016). On high-pass
    filter artifacts (they're real) and baseline correction (it's a good
    idea) in ERP/ERMF analysis. J Neurosci Methods. \[Epub ahead of
    print\]



-   Maess B, Schröger E, Widmann A. (2016). High-pass filters and
    baseline correction in M/EEG analysis-continued discussion. J
    Neurosci Methods. \[Epub ahead of print\]



-   Liljander S, Holm A, Keski-Säntti P, Partanen JV. (2016). Optimal
    digital filters for analyzing the mid-latency auditory P50
    event-related potential in patients with Alzheimer's disease. J
    Neurosci Methods. 2016 Mar 22;266:50-67.
