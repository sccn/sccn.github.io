---
layout: default
title: Chapter-5.5.-Connectivity-Estimation
long_title: Chapter-5.5.-Connectivity-Estimation
parent: SIFT
grand_parent: Plugins
---
Now that our model has been fit, we’d like to calculate some
frequency-domain measures, such as the spectrum, coherence, and
granger-causality. Bring up the Connectivity Estimation GUI by selecting the menu item 
**Tools > SIFT > Connectivity**. You can start this from the command line for a single dataset EEG using:

``` matlab
 EEG = pop_est_mvarConnectivity(EEG);
```

You should now see the GUI shown in the figure below. Here, we can
compute all the measures (and more) listed in Table 4 in section 4.3. We
can specify a list of frequencies at which to compute the measure(s), and we can do some simple conversions of complex measures and spectral
densities.


For our example, let’s compute the direct DTF (with full causal
normalization, denoted dDTF08), the complex coherence, the partial
coherence, and the complex spectral density over the frequency range
2-50 Hz (with 1 Hz resolution). Your options should be set as the figure and table below:

<table>
<tbody>
<tr class="odd">
<td><p>Option</p></td>
<td><p>Value</p></td>
</tr>
<tr class="even">
<td><p><strong>Select connectivity measures</strong></p></td>
<td><p><strong>Direct DTF (with full causal norm.)</strong><br />
<strong>Complex Coherence (Coh)</strong><br />
<strong>Partial Coherence (pCoh)</strong><br />
<strong>Complex Spectral Density (S)</strong></p></td>
</tr>
<tr class="odd">
<td><p><strong>return squared amplitude of complex measures</strong></p></td>
<td><p><strong>checked</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>convert spectral density to decibels</strong></p></td>
<td><p><strong>checked</strong></p></td>
</tr>
<tr class="odd">
<td><p><strong>Frequencies (Hz)</strong></p></td>
<td><p><strong>2:50</strong></p></td>
</tr>
</tbody>
</table>


![Screen Shot 2023-08-25 at 5 02 27 PM](https://github.com/sccn/SIFT/assets/1872705/06297970-6826-420e-aede-7da9937fe095)

*Figure caption. Connectivity estimation GUI generated
by `pop_est_mvarConnectivity()`. Here, we have chosen to estimate the
Direct DTF (with full causal normalization; dDTF08), the Complex
Coherence (Coh), the Partial Coherence (pCoh), and the Spectral Density
(S).*


While selecting additional measures only marginally increases the
computational time, doubling the number of measures will generally
double the memory demands. Click **OK** to continue. You should now get
a prompt notifying you of how much memory will be required (for each
condition). If you have enough memory to continue, click **OK**. A
progress bar will appear, showing the status of the connectivity
estimation for each condition.

If you do not wish to use the GUI, the same may be achieved from the command line using:

```matlab
EEG = pop_est_mvarConnectivity( EEG, 'nogui', 'ConnectivityMeasures', ...
             {'dDTF08' 'Coh' 'pCoh' 'S'}, 'Frequencies', [2:50], 'VerbosityLevel', 1); 
```

