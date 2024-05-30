
![700px\|link=](https://github.com/sccn/SIFT/assets/1872705/1abc1d2d-36bb-4cfb-9328-b57a96044f55)

# The Source Information Flow Toolbox tutorial (SIFT)

<table>
<tbody>
<tr class="odd">
<td><p>Developed and Maintained by: Tim Mullen and Arnaud Delorme (SCCN, INC, UCSD) 2009-
</tr>
</tbody>
</table>

SIFT is an EEGLAB-compatible toolbox for the analysis and visualization of
multivariate causality and information flow between sources of
electrophysiological (EEG/ECoG/MEG) activity. It consists of a suite of
command-line functions with an integrated Graphical User Interface for
easy access to multiple features. There are currently six modules: data
preprocessing, model fitting and connectivity estimation, statistical
analysis, visualization, group analysis, and neuronal data simulation.

Methods currently implemented include:

-   Preprocessing routines
-   Time-varying (adaptive) multivariate autoregessive modeling
    -   granger causality
    -   directed transfer function (DTF, dDTF)
    -   partial directed coherence (PDC, GPDC, PDCF, RPDC)
    -   multiple and partial coherence
    -   event-related spectral perturbation (ERSP)
    -   and many other measures...
-   Bootstrap/resampling and analytical statistics
    -   event-related (difference from baseline))
    -   between-condition (test for condition A = condition B)
-   A suite of programs for interactive visualization of information
    flow dynamics across time and frequency (with optional 3D
    visualization in MRI-coregistered source-space).
