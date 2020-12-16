---
layout: default
title: IV.3 Importing Channel Locations
parent: IV. Appendix
grand_parent: Tutorials
nav_order: 3
---
Supported Electrode Data Formats
--------------------------------

| File Format     | File Extension     | Coordinate System  | Import Mode      | EEGLAB                                  | Biosig | File IO | Support                                       |
|-----------------|--------------------|--------------------|------------------|-----------------------------------------|--------|---------|-----------------------------------------------|
| BESA            | .elp               | Spherical          | _               | { {table\|status=y\|color=lightgreen} } | _     | _      | [Comments](/Talk:besa_elp "wikilink")         |
| BESA/EGI        | .sfp               | Cartesian          | native           | { {table\|status=y\|color=lightgreen} } | _     | _      | [Comments](/Talk:.sfp "wikilink")             |
| EEGLAB          | .loc, .locs, .eloc | Polar              | _               | { {table\|status=y\|color=lightgreen} } | _     | _      | [Comments](/Talk:.loc/.locs/.eloc "wikilink") |
| EEGLAB (ASCII)  | .ced               | Cartesian          | default (eeglab) | { {table\|status=y\|color=lightgreen} } | _     | _      | [Comments](/Talk:.ced "wikilink")             |
| EEGLAB (Matlab) | .xyz               | Cartesian          | default (eeglab) | { {table\|status=y\|color=lightgreen} } | _     | _      | [Comments](/Talk:.xyz "wikilink")             |
| EETrack         | .elc               | Cartesian          | _               | { {table\|status=y\|color=lightgreen} } | _     | _      | [Comments](/Talk:.elc "wikilink")             |
| EMSE            | .elp               | _                 | _               | _                                      | _     | _      | [Comments](/Talk:emse_elp "wikilink")         |
| FreeSurfer      | .tri               | _                 | _               | _                                      | _     | _      | [Comments](/Talk:freesurfer_tri "wikilink")   |
| Matlab          | .sph               | Spherical          | _               | { {table\|status=y\|color=lightgreen} } | _     | _      | [Comments](/Talk:.ced "wikilink")             |
| Neuroscan       | .asc               | Cartesian or Polar | _               | { {table\|status=y\|color=lightgreen} } | _     | _      | [Comments](/Talk:electrode_asc "wikilink")    |
| Neruoscan       | .dat               | Cartesian or Polar | _               | { {table\|status=y\|color=lightgreen} } | _     | _      | [Comments](/Talk:.elc "wikilink")             |
| Neuroscan       | .tri               | _                 | _               | _                                      | _     | _      | [Comments](/Talk:neuroscan_tri "wikilink")    |
| Neuroscan       | .3dd               | _                 | _               | _                                      | _     | _      | [Comments](/Talk:.3dd "wikilink")             |
| Polhemus        | .elp               | Cartesian          | default (eeglab) | { {table\|status=y\|color=lightgreen} } | _     | _      | [Comments](/Talk:polhemus_elp "wikilink")     |
|                 |                    |                    |                  |                                         |        |         |                                               |


**Please upload test files at <ftp://sccn.ucsd.edu/incoming> or [Channel
Location Files](/Channel_Location_Files "wikilink") to help us build the
table.**
File Format Compatibility is noted by the following:

|                                                                             |                                         |
|-----------------------------------------------------------------------------|-----------------------------------------|
| Supported Formats                                                           | { {table\|status=y\|color=lightgreen} } |
| Supported but requires MEX file                                             | { {table\|status=y\|color=green} }      |
| Unverified                                                                  | _                                      |
| Currently unsupported formats or not working                                | { {table\|status = n\|color=red} }      |
| Functionality via third-party [EEGLAB Plug-Ins](/EEGLAB_Plugins "wikilink") | { {table\|status=p\|color=yellow} }     |


**For more information, please refer to [readlocs.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=readlocs.m) or go to
[Channel Location Files](/Channel_Location_Files "wikilink")**

Importing channel location
--------------------------

To plot EEG scalp maps in either 2-D or 3-D format, or to estimate
source locations for data components, an EEGLAB dataset must contain
information about the locations of the recording electrodes.

To load or edit channel location information contained in a dataset
(with or without channel location), select <font color=brown>Edit \>
Channel locations</font>. If you do not have a dataset loaded, you can
test this section by typing on the Matlab command line:

> \>\>pop_chanedit(\[\]);




![Image:Editchannelinfo.jpg](/assets/images/Editchannelinfo.jpg)



If you imported a binary data file in Neuroscan or Biosemi formats,
channel labels will be present in the dataset (as of EEGLAB v4.31). When
you call the channel editing window, a dialog box will appear asking you
if you want to use standard channel locations corresponding to the
imported channel labels (for example. Fz) from an channel locations file
using an extended International 10-20 System. Otherwise, you must load a
channel locations file manually.


To load a channel locations file, press the *Read Locations* button and
select the sample channel locations file *eeglab_chan32.locs* (this file
is located in the *sample_data* sub-directory of the EEGLAB
distribution).


![Image:Loadchannellocation.jpg](/assets/images/Loadchannellocation.jpg)



In the next pop-up window, simply press *OK*. If you do not specify the
file format, the [pop_chanedit.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_chanedit.m) function will attempt to use
the filename extension to assess its format. Press button *Read help* in
the main channel graphic interface window to view the supported formats.




![Image:Chaneditfileformat.jpg](/assets/images/Chaneditfileformat.jpg)



Now the loaded channel labels and polar coordinates are displayed in the
[pop_chanedit.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_chanedit.m) window.

To plot scalp maps only inside the head cartoon, enter 0.5 at the *Plot
radius* edit box. In this case, the two eye electrodes will not be
displayed nor considered computing interpolated 2-D scalp maps. If you
do not see enough of the recorded field, set this dialogue box to 1.0 to
interpolate and show scalp maps including all channels, with parts of
the head below the (0.5) head equator shown in a 'skirt' or 'halo'
outside the cartoon head boundary. (More precise separate controls of
which channel locations to interpolate and plot are available from the
command line in the topographic map plotting function {
{File\|topoplot.m} }.

In the window below, you may scroll through the channel field values
1-by-1 using the *\<* and *\>* buttons, or in steps of 10 using *\<\<*
and *\>\>*.




![Image:21pop_chanedit.jpg](/assets/images/21pop_chanedit.jpg)




The *Set channel type* button allows you to enter a *channel type*
associated with the channel (for example, 'EEG', 'MEG', 'EMG', 'ECG',
'Events', etc.). Although channel types are not yet (v5.0b) widely used
by other EEGLAB functions, they will be used in the near future to
restrict plotting and computation to a desired subset of channel types,
allowing easier analysis of multi-modal datasets. It is therefore well
worth the effort to add channel types to your data. It is important to
press *OK* in the channel editing window above to actually import the
channel locations!. Note that in the main EEGLAB window, the *channel
location* flag now shows *yes*.

</blockquote>

Following are examples of ascii channel locations data in
EEGLAB-supported formats.

**Supported channel locations file formats.**

-   Four channels from a polar coordinates file (with filename extension
    *.loc*, Do not include the (light blue) header line:


<table>
<tbody>
<tr class="odd">
<td><p>#<br />
</p></td>
<td><p>Deg.<br />
</p></td>
<td><p>Radius<br />
</p></td>
<td><p>Label<br />
</p></td>
</tr>
<tr class="even">
<td><p>1<br />
</p></td>
<td><p>-18<br />
</p></td>
<td><p>,352<br />
</p></td>
<td><p>Fp1<br />
</p></td>
</tr>
<tr class="odd">
<td><p>2<br />
</p></td>
<td><p>18<br />
</p></td>
<td><p>.352<br />
</p></td>
<td><p>Fp2<br />
</p></td>
</tr>
<tr class="even">
<td><p>3<br />
</p></td>
<td><p>-90<br />
</p></td>
<td><p>,181<br />
</p></td>
<td><p>C3<br />
</p></td>
</tr>
<tr class="odd">
<td><p>4<br />
</p></td>
<td><p>90<br />
</p></td>
<td><p>,181<br />
</p></td>
<td><p>C4</p></td>
</tr>
</tbody>
</table>


\*The same locations, from a spherical coordinates file (estension,
*.sph* ):


<table>
<tbody>
<tr class="odd">
<td><p><font color="#000000">#<br />
</font></p></td>
<td><p><font color="#000000">Azimut<br />
</font></p></td>
<td><p><font color="#000000">Horiz.<br />
</font></p></td>
<td><p><font color="#000000">Label</font><br />
</p></td>
</tr>
<tr class="even">
<td><p>1</p></td>
<td><p>-63.36</p></td>
<td><p>-72</p></td>
<td><p>Fp1</p></td>
</tr>
<tr class="odd">
<td><p>2</p></td>
<td><p>63.36</p></td>
<td><p>72</p></td>
<td><p>Fp2</p></td>
</tr>
<tr class="even">
<td><p>3</p></td>
<td><p>32.58</p></td>
<td><p>0</p></td>
<td><p>C3</p></td>
</tr>
<tr class="odd">
<td><p>4</p></td>
<td><p>32.58</p></td>
<td><p>0</p></td>
<td><p>C4</p></td>
</tr>
</tbody>
</table>


\*The same locations from a Cartesian coordinates file (extension,
*.xyz* ):


<table>
<tbody>
<tr class="odd">
<td><p>#<br />
</p></td>
<td><p>X<br />
</p></td>
<td><p>Y<br />
</p></td>
<td><p>Z<br />
</p></td>
<td><p>Label<br />
</p></td>
</tr>
<tr class="even">
<td><p>1</p></td>
<td><p>-0.8355</p></td>
<td><p>-0.2192</p></td>
<td><p>-0.5039</p></td>
<td><p>Fp1</p></td>
</tr>
<tr class="odd">
<td><p>2</p></td>
<td><p>-0.8355</p></td>
<td><p>0.2192</p></td>
<td><p>0.5039</p></td>
<td><p>Fp2</p></td>
</tr>
<tr class="even">
<td><p>3</p></td>
<td><p>0.3956</p></td>
<td><p>0</p></td>
<td><p>-0.9184</p></td>
<td><p>C3</p></td>
</tr>
<tr class="odd">
<td><p>4</p></td>
<td><p>0.3956</p></td>
<td><p>0</p></td>
<td><p>0.9184</p></td>
<td><p>C4</p></td>
</tr>
</tbody>
</table>

Note that in all the above examples, the first header line must not be
present.

<u>Other supported channel locations file formats</u>

> -   Polhemus (*.elp*) files
> -   Neuroscan spherical coordinates (*.asc, .dat*)
> -   Besa spherical coordinates (*.elp, .sfp*)
> -   EETrak sofware files (*.elc*)
> -   EEGLAB channel locations files saved by the {
>     {File\|pop_chanedit.m} } function (*.loc, .xyz, .sph, .ced*)

Note that [pop_chanedit.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_chanedit.m) and [pop_chanedit.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=readlocs.m) can also
be called from the command line to convert between location formats. For
more details, see the [readlocs.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=readlocs.m) help message.

<font color=green>Exploratory Step</font>: Viewing Channel Locations.

> Reopen <font color=brown>Edit \> Channel locations</font> if you
> closed it. To visualize the 2-D locations of the channels, press *Plot
> 2-D* above the *Read Locations* button. Else, at any time during an
> EEGLAB session you may refer to a plot showing the channel locations
> by selecting <font color=brown>Plot \> Channel location \> By
> name</font>. Either command pops up a window like that below. Note: In
> this plot, click on any channel label to see its channel number.


![500px](/assets/images/Channellocationname.gif)


> All channels of this montage are visible in the 2-D view above, since
> none of these channels are located below the head center and equator
> line. If the montage contained channel locations whose polar
> coordinate radius values were larger than the default value (e.g.,
> *0.5*) you entered in the [pop_chanedit.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_chanedit.m) window, those
> locations would not appear in the top-down 2-D view, and the
> interpolated scalp map would end at the cartoon head boundary. The 2-D
> plotting routine [topoplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=topoplot.m) gives the user full
> flexibility in choosing whether to show or interpolate data for
> inferior head channels; [topoplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=topoplot.m) is used by all EEGLAB
> functions that plot 2-D scalp maps.
> To visualize the channel locations in 3-D, press *Plot 3-D (xyz)*. The
> window below will appear. The plotting box can be rotated in 3-D using
> the mouse:


![Image:3dlpotxyz.gif](/assets/images/3dlpotxyz.gif)


> You may change channel locations manually using the edit box provided
> for each channel's coordinates. However, after each change, you must
> update the other coordinate formats. For instance, if you update the
> polar coordinates for one channel, then press the *polar-\>sph. & xyz*
> button on the right of the [pop_chanedit.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_chanedit.m) window (see
> above) to convert these values to other coordinate formats.

Retrieving standardized channel locations
-----------------------------------------

This section does not use the tutorial dataset. It intent is to provide
guidelines for automatically finding channel locations when channel
names are known. For instance, when importing a Neuroscan, an EGI, or a
Biosemi channel locations file, channel names are often stored in the
file header. EEGLAB will automatically read these channel labels. When
you then call the channel editing window, the function will look up
channel locations in a database of 385 defined channel labels, the file
"Standard-10-5-Cap385.sfp" in the "function/resources" sub-folder of the
EEGLAB distribution. You may add additional standard channel locations
to this file if you wish. Channel locations in this file have been
optimized for [dipole modeling](http://oase.uci.ru.nl/~roberto/) by
Robert Oostenveld.

For example, download the sample file,
[TEST.CNT](http://sccn.ucsd.edu/eeglab/download/TEST.CNT), then call up
the channel editing window. As an alternate example not requiring a data
download, we will build a channel structure using channel labels only,
then will call the channel editing window. In the Matlab command window,
type:

> \>\> chanlocs = struct('labels', { 'cz' 'c3' 'c4' 'pz' 'p3' 'p4' 'fz'
> 'f3' 'f4'});
> \>\> pop_chanedit( chanlocs );

The following window will pop-up:


![Image:Pop_chaneditmsg.jpg](/assets/images/Pop_chaneditmsg.jpg)



Press *Yes*. The function will automatically look up channel locations
for these known channel labels. The following channel editing window
will then pop up.


![Image:Pop_chaneditlookup.gif](/assets/images/Pop_chaneditlookup.gif)



Press *Plot 2-D* to plot the channel locations. Close the channel
editing window (using *Cancel* to discard the entered locations), then
proceed to the next section.


![Image:Topoplotlookup.gif](/assets/images/Topoplotlookup.gif)




Importing measured 3-D channel locations information
----------------------------------------------------

This section does not use the tutorial dataset. Its intent is to provide
guidelines for importing channel locations measured in Cartesian
coordinates using 3-D tracking devices (such as Polhemus). Use the
EEGLAB menu <font color=brown>Edit \> Channel location</font> or type
the following command on the Matlab command line


> \>\> pop_chanedit(\[\]);


An empty channel editing window will appear:



![Image:Editchannelinfo.jpg](/assets/images/Editchannelinfo.jpg)



Press the *Read locations* button and select the file *scanned72.dat*
from the *sample_data* subfolder of the EEGLAB distribution. This is a
channel locations file measured with the Polhemus system using Neuroscan
software (kindly supplied by Zoltan Mari). Use autodetect (\[ \]) for
the file format. When the file has been imported, press the *Plot 2-D*
button. The following plot will pop up.



![Image:Scanlocs1.gif](/assets/images/Scanlocs1.gif)



As you can see, the measured 3-D channel coordinates may not be
accurately distributed on the 2-D head model. This is because the
measured values have not been shifted to the head center. To fix this
problem, you must first find the head sphere center that best fits the
imported 3-D electrode locations. To do so, press the *Opt. head center*
(optimize head center). The following window will pop up:



![Image:Pop_chancenter.gif](/assets/images/Pop_chancenter.gif)



Possibly, some of the channels should not be included in the head center
optimization, if they are not on the head and/or do not have recorded
locations. Enter electrodes indices to use (here, 1:3 33 35 64:72) in
the edit window. You may also press the *Browse* button above to select
channels that are not on the head. When you press *OK* in the browser
window, the channel indices will be copied, as shown in the window
above. Then press *Ok*. After the optimization has finished, press the
*Plot 2-D* button once more.



![Image:Scanlocs2.gif](/assets/images/Scanlocs2.gif)



In the view above, some channel locations are still incorrect. For
instance, you may expect channel "Cz" to be at the vertex (plot center).
To adjust this, press the *Rotate axis* button. The following window
will pop up:



![Image:Forcelocs.gif](/assets/images/Forcelocs.gif)



Simply press *OK* to align channel 'Cz' to the vertex (by default). Then
press the *Plot 2-D* button once more to again plot the scalp map.



![Image:Scanlocs3.gif](/assets/images/Scanlocs3.gif)



You may now close the channel editing window.

This section has illustrated operations you may want to perform to adapt
measured 3-D channel locations for use in EEGLAB.


[Category:IV. Appendix](/Category:IV._Appendix "wikilink") {
{Backward_Forward\|A02:_Importing_Event_Epoch_Info\|A2: Importing Event
Epoch Info\|A04:_Exporting_Data\|A4: Exporting Data} }
