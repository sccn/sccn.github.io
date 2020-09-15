---
layout: default
title: A04 Exporting Data
permalink: /docs/A04_Exporting_Data
parent: Docs
---

{ {Backward_Forward|A03:_Importing_Channel_Locations|A03: Importing
Channel Locations|A05:_Data_Structures|A05: Data Structures} }

## Supported Data Formats

| Data Type             | Export Type                   | File Extension     | EEGLAB                                | BIOSIG | Support                                 |
| --------------------- | ----------------------------- | ------------------ | ------------------------------------- | ------ | --------------------------------------- |
| EEG Data              | ASCII Text                    | .txt               | { {table|status=y|color=lightgreen} } | _     | [Comments](/Talk:export_txt "wikilink") |
| EEG Data              | European Data Format (16-bit) | .edf               | { {table|status=y|color=lightgreen} } | _     | [Comments](/Talk:export_edf "wikilink") |
| EEG Data              | Biosemi                       | .bdf               | { {table|status=y|color=lightgreen} } | _     | [Comments](/Talk:export_bdf "wikilink") |
| EEG Data              | BCI2000                       | .gdf               | { {table|status=y|color=lightgreen} } | _     | [Comments](/Talk:export_gdf "wikilink") |
| EEG Data              | Brain Vision Analyzer         | .dat, .vhdr, .vmrk | { {table|status=y|color=lightgreen} } | _     | [Comments](/Talk:export_BVA "wikilink") |
| ICA Activity          | ASCII Text                    | .txt               | { {table|status=y|color=lightgreen} } | _     | [Comments](/Talk:export_txt "wikilink") |
| Weight Matrix         | ASCII Text                    | .txt               | { {table|status=y|color=lightgreen} } | _     | [Comments](/Talk:export_txt "wikilink") |
| Inverse Weight Matrix | ASCII Text                    | .txt               | { {table|status=y|color=lightgreen} } | _     | [Comments](/Talk:export_txt "wikilink") |
| Binary                | Neuroscan                     | .cnt               | { {table|status=y|color=yellow} }     | _     | [Comments](/Talk:export_cnt "wikilink") |
|                       |                               |                    |                                       |        |                                         |

  - Find More information regarding possible supported data formats in
    the BIOSIG documentation,
    [here](http://hci.tugraz.at/schloegl/biosig/TESTED).


**Please leave comments to help us fill and expand this table.**
File Format Compatibility is noted by the following:

|                                                                             |                                       |
| --------------------------------------------------------------------------- | ------------------------------------- |
| Supported Formats                                                           | { {table|status=y|color=lightgreen} } |
| Supported but requires MEX file                                             | { {table|status=y|color=green} }      |
| Unverified                                                                  | _                                    |
| Currently unsupported formats or not working                                | { {table|status = n|color=red} }      |
| Functionality via third-party [EEGLAB Plug-Ins](/EEGLAB_Plugins "wikilink") | { {table|status=p|color=yellow} }     |




## Exporting data and ICA matrices

#### Exporting data to an ASCII text file

EEGLAB datasets can be exported as ASCII files using menu item
<font color=brown>File \> Exports\> Data and ICA activity to text
file</font>. Enter a file name (*mydata.txt*, for instance). Check the
second checkbox to export the average ERP instead of the data epochs. By
default, the electrode labels are saved for each row (4th check box) and
the time values are saved for each column (5th checkbox). Time units can
be specified in the edit box closest to the time values checkbox.
Finally, check the third checkbox to transpose the matrix before saving.

<center>


[Image:pop_export.gif](/Image:pop_export.gif "wikilink")


</center>

The file written to disk may look like this:

`FPz             EOG1       F3          Fz        F4        EOG2       FC5        FC1           ...`
`-1000.0000      -1.1091    2.0509      0.1600    -0.1632   -0.4848    -1.3799    -0.0254       -0.4788 ...`
`-992.1880       0.6599     1.7894      0.3616     0.6354    0.8656    -2.9291    -0.0486       -0.4564 ...`
`-984.3761       1.8912     1.3653      -0.6887   -0.0437   0.2176     -0.9767    -0.6973       -1.5856 ...`
`-976.5641       0.5129     -0.5399     -1.4076   -1.2616   -0.8667    -3.5189    -1.5411       -1.9671 ...`
`-968.7521       -0.0322    -0.4172     -0.9411   -0.6027   -0.9955    -2.3535    -1.6068       -1.0640 ...`
`-960.9402       0.1491     0.0898      -0.0828   0.3378    0.0312     -2.4982    -0.9694       -0.0787 ...`
`-953.1282       -1.9682    -1.5161     -1.2022   -0.8192   -1.1344    -3.3198    -1.6298       -0.9119 ...`
`-945.3162       -3.7540    -2.1106     -2.6597   -2.4203   -2.2365    -3.5267    -1.9910       -2.7470 ...`
`-937.5043       -2.4367    -0.1690     -0.9962   -1.7021   -2.8847    -2.1883    -0.2790       -1.5198 ...`
`-929.6923       -2.8487    -0.3114     -1.6495   -2.6636   -4.0906    -1.7708    -1.2317       -2.3702 ...`
`-921.8803       -2.8535    0.1097      -1.5272   -2.0674   -3.8161    -3.1058    -0.8083       -1.5088 ...`
`-914.0684       -3.9531    -0.4527     -1.8168   -2.2164   -3.4805    -2.1490    -1.0269       -1.3791 ...`
`-906.2564       -3.9945    -0.1054     -1.8921   -2.8029   -3.5642    -3.4692    -1.1435       -2.2091 ...`
`-898.4444       -4.4166    -0.8894     -3.3775   -3.8089   -3.8068    -1.7808    2.5074        -3.5267 ...`
`-890.6325       -3.0948    0.5812      -2.5386   -1.7772   -1.8601    -2.8900    -2.0421       -2.0238 ...`
`-882.8205       -3.1907    0.7619      -3.6440   -2.1976   -1.4996    -0.6483    -3.4281       -2.7645 ...`
`-875.0085       -1.7072    2.5182      -3.2136   -2.4219   -1.3372    -1.5834    -2.9586       -2.8805 ...`
`-867.1966       -1.8022    1.7044      -2.6813   -3.2165   -2.7036    0.0279     -2.5038       -3.4211 ...`
`-859.3846       -3.1016    -0.1176     -3.6396   -4.3637   -3.9712    -3.5499    -3.4217       -4.5840 ...`
`-851.5726       -1.7027    0.7413      -3.3635   -3.8541   -3.5940    -1.3157    -2.9060       -3.8355 ...`
`-843.7607       -0.2382    0.5779      -1.9576   -2.6630   -1.8187    -1.1834    -1.4307       -2.4980 ...`
`-835.9487       0.7006      0.4125     -0.4827   -1.7712    -2.0397    0.2534    0.2594        -1.2367 ...`
`-828.1367       -0.2056    -0.3509     0.4829    -0.6850   -1.1222    0.0394     1.4929        0.7069 ...`
`-820.3248       0.3797     -0.3791     0.9267    0.2139    -0.6116    -0.7612    1.3307        1.5108 ...`
`-812.5128       -0.8168    -1.4683     -0.3252   -0.8263   -1.5868    -0.7416    -0.2708       -0.1987 ...`
`-804.7009       -0.7432    -0.3581     -0.9168   -0.8350   -1.7733    -0.4928    -0.7747       -0.6256 ...`
`...`

The first column contains the time axis and the other the data for each
electrode. This file might, for example, be imported into SPSS or BMDP.

#### Exporting ICA weights and inverse weight matrices

Use menu item <font color=brown>File \> Export\> Weight matrix to text
file</font> to export the ICA unmixing matrix (weights\*sphere). Simply
enter a file name in the pop-up window and press *Save*.

<center>

[325px](/Image:pop_expica.gif "wikilink")

</center>

The text file on disk then contains the weight matrix. It may be
re-imported into another EEGLAB dataset using menu item
<font color=brown>Edit \> Dataset info</font>. As shown below, enter the
filename in the *ICA weight array* edit box. Leave the sphere edit box
empty, or empty it if it is not empty. See the [ICA decomposition
tutorial](/Chapter_09:_Decomposing_Data_Using_ICA "wikilink") for more
details on sphere and weight matrices.

<center>

[600px](/Image:pop_editset.gif "wikilink")

</center>

[Category:IV. Appendix](/Category:IV._Appendix "wikilink") {
{Backward_Forward|A03:_Importing_Channel_Locations|A03: Importing
Channel Locations|A05:_Data_Structures|A05: Data Structures} }