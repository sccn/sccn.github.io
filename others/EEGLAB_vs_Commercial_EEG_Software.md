---
layout: default
title: EEGLAB vs. commercial soft.
summary: EEGLAB vs. Commercial EEG Software
parent: Other documents
---
EEGLAB vs Commercial EEG software packages  <span style="color: green">- DONE</span>
====

<blockquote>
<i>Can we trust the results of a new paper if they depend on calculations
carried out by proprietary software with non-public source code?</i> <a href="http://www.nature.com/nphys/journal/v12/n7/full/nphys3815.html?WT.feed_name=subjects_physical-sciences">M. Buchanan, Nature Physics, 2016</a>
</blockquote>

This page compares the feature of EEGLAB some of the most common
features in what is currently best in the industry.

<table>
<th></th>
<th>EEGLAB</th>
<th>Leading EEG commercial softwares</th>
<tbody>
<tr>
	<td>Binary file import</td>
	<td style="background-color:lightgreen">EEGLAB offers a comprehensive library of file import functions. Most data formats can be imported using three different methods.</td>
	<td style="background-color:#FFAAAA">File import and export are usually limited to a few formats.</td>
</tr>
<tr>
	<td>Memory requirements</td>
	<td style="background-color:#FFAAAA">EEGLAB must be able to hold in memory any single data set. When processing multiple data sets, they may stay on disk.</td>
	<td style="background-color:lightgreen">Most commercial software has been designed to allowing processing of large datasets using relatively little memory.</td>
</tr>
<tr>
	<td>Features</td>
	<td style="background-color:lightgreen">EEGLAB has more features than any current commercial software. In general EEGLAB provides the user with a wider range of processing choices.</td>
	<td style="background-color:#FFAAAA">Some leading (though frequently expensive) commercial software might offers more methods for source localization than are available in EEGLAB tools.</td>
</tr>
<tr>
	<td>Availability of new features</td>
	<td style="background-color:lightgreen">EEGLAB benefits from tools implemented by the scientific community. As of 2021, there are 120 EEGLAB plugins available.</td>
	<td style="background-color:#FFAAAA">A large part of commercial software development supports software complied under Windows OS. Development of both EEGLAB and dedicated commercial software are driven by the open source and research community; as it adopts a new methods, commercial software will implement them eventually. EEGLAB allows testing relatively new tools, many of which may not yet be available in any commercial software packages.</td>
</tr>
<tr>
	<td>Graphic interface</td>
	<td style="background-color:#FFAAAA">EEGLAB graphic interface may not be as refined as in commercial software. A lot of the processing is performed on the command line; the EEGLAB graphic user interface is only a convenient way to automate such processing.</td>
	<td style="background-color:lightgreen">Commercial software developers usually perfect their graphic interface, sometimes at the expense of the breadth of tools implemented.</td>
</tr>
<tr>
	<td>Documentation</td>
	<td style="background-color:lightgreen">EEGLAB has more than 300 pages of tutorial documentation. Users may also access the EEGLAB code to check exactly what processing is performed. In addition, each function has its own documentation</td>
	<td style="background-color:#FFAAAA">Documentation is usually not a top priority of commercial software, and its source code is not available.</td>
</tr>
<tr>
	<td>Code stability</td>
	<td style="background-color:#FFAAAA">Because EEGLAB is in constant development, the code stability of the development version may not be as optimal as for commercial software. The EEGLAB code is also not rigorously validated against given standard or certification by industry standards. Note also that EEGLAB is not approved for routine clinical use and should not be used for such purposes.</td>
	<td style="background-color:lightgreen">The most reliable commercial code may be more stable; though this is not necessarily true for all commercial code.</td>
</tr>
<tr>
	<td>Scripting capabilities</td>
	<td style="background-color:lightgreen">The EEGLAB scripting language is MATLAB itself. Commercial code cannot compete with MATLAB for range, flexibility, and the amount of code available -- both for purchase from MATLAB and freely available from the research community.</td>
	<td style="background-color:#FFAAAA">Scripting capabilities usually rely on a proprietary language. Some commercial software allows running MATLAB code within their scripts -- but since its graphic output is then limited, why not run MATLAB itself?</td>
</tr>
<tr>
	<td>Preparation of figures for publication</td>
	<td style="background-color:lightgreen">EEGLAB and MATLAB allow creation of complex figures with panels. Most of EEGLAB functions are compatible with panels so users may use EEGLAB function to generate their own paneled results. Formating details of figures may be edited directly under MATLAB from the command line or from the MATLAB GUI. Even complex figures containing bitmaps may be saved as postscript files for further detailed editing. MATLAB also allow saving figures and movies in about 10 different formats.</td>
	<td style="background-color:#FFAAAA">Figures may only be saved using a few formats. Capabilities to build complex figures from within the software is absent.</td>
</tr>
<tr>
	<td>Dedicated user support team</td>
	<td style="background-color:#FFAAAA">EEGLAB Bugzilla database helps track EEGLAB bugs. In the best case scenario, bugs may be fixed within 24 hours and a new release issued automatically overnight. However, the EEGLAB team does not have dedicated personnel for supporting users, and the help provided may depend on availability and advancement on other research projects.</td>
	<td style="background-color:lightgreen">Support personnel are usually more readily available to help users, and they can have high level of expertise. Note that this is not true of all commercial software.</td>
</tr>
<tr>
	<td>Price</td>
	<td style="background-color:lightgreen">A minimal MATLAB installation may be within most research budgets or be already available for other purposes in research and university settings. The compiled version of EEGLAB does not require MATLAB although scripting capabilities are more limited.</td>
	<td style="background-color:#FFAAAA">Prices range from $5000 to $30000</td>
</tr>
</tbody>
</table>
