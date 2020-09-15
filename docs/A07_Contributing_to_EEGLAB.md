---
layout: default
title: A07 Contributing to EEGLAB
permalink: /docs/A07_Contributing_to_EEGLAB
parent: Docs
---

{ {Backward_Forward|A06:_Maximizing_Memory|A06: Maximizing
Memory|A08:_DIPFIT|A08: DIPFIT} }

# EEGLAB Development

The chief EEGLAB developers are Arnaud Delorme and Scott Makeig. The
predecessor to EEGLAB, the ICA/EEG Toolbox (1997-2001), comprised
functions written by Makeig with Tony Bell, Colin Humphries, Sigurd
Enghoff, Tzyy-Ping Jung, Te-Won Lee, and others, was first released on
the Web in 1997 by Scott Makeig at the Computational Neurobiology
Laboratory of Terrence J. Sejnowski at The Salk Institute, La Jolla. The
first version of the integrated EEGLAB toolbox was written there by
Delorme and Makeig with subsequent contributions by many including
Marissa Westerfield, Jörn Anemüller, Luca Finelli, Robert Oostenveld,
Hilit Serby, Toby Fernsler, Nima Shamlo Bigdeley, Jason Palmer and many
others. Dedicated beta testers include Andreas Romeyke and his team, who
developed a test suite for EEGLAB, and other advanced users including
Stefan Debener and Andreus Widmar. EEGLAB development is now centered at
the Swartz Center for Computational Neuroscience (SCCN) of the Institute
for Neural Computation at the University of California San Diego (UCSD).
Core EEGLAB maintenance and development is supported by the US National
Institute of Neurological Disorders and Stroke (NINDS). Recent additions
to EEGLAB from SCCN include several plug-in toolboxes (described here)
including NFT (head modeling tools), SIFT (effective connectivity
tools), MPT (source comparison tools), BCILAB (BCI modeling tools), and
PACT (epileptic spike detection),

The EEGLAB core code cannot be modified by third party directly. Instead
users submits bug reports, function patches, or function improvements
through the [EEGLAB Bugzilla
interface](https://sccn.ucsd.edu/bugzilla/). EEGLAB core developers then
review the code and add it to the repository.

For third party developpers, we welcome collaborations with users and
open source developers to expand and improve EEGLAB functions and/or to
independently write and release EEGLAB plug-in/extension applications
and environments. If you have written plug-ins for use in your
laboratory, please consider releasing them for use by others.

EEGLAB is under active open-source development. Together with user
developers, we are extending its capabilities to include across-subject
general linear model statistics. User-contributed features and
suggestions are welcome and we encourage and plan to interconnect EEGLAB
with other Matlab-compatible toolboxes.

# Open source policy

1.  EEGLAB is distributed under the [BSD
    license](https://opensource.org/licenses/BSD-2-Clause). Any
    contributed functions we add to EEGLAB will be made available for
    free commercial and non-commercial use under this license.
2.  We will credit your authorship of the functions on the function help
    pages. The authors will retain all commercial rights to the
    functions.
3.  Functions that we find to be accurate, stable, of some general
    interest and complementary to existing EEGLAB functions will first
    be included in a 'contributed' directory distributed as a part of
    EEGLAB. If a contributed function proves to be stable and of
    widespread interest, we may integrate it into the main EEGLAB menu.

Also consider the <b>extension</b> (formerly 'plug-in') option described
in Section above. EEGLAB extensions allow authors to flexibly
incorporate new functions into the EEGLAB menu of every user who has
downloaded the extension.

# Code of conduct

We strive to follow the Open Source code of conduct of community,
collaboration, respect, and responsibility first outlined by the [Ubuntu
community](https://ubuntu.com/community/code-of-conduct).

# Using GIT to contribute code

To contribute code to the EEGLAB core code, fork the code and create a
pull request as indicated on this
[page](/Fork_the_EEGLAB_repo "wikilink"). You will need a Github account
to perform these operations, but do not require any special permission
from us.

# Developing under Matlab

EEGLAB operates in the very rich Matlab environment. The structure of
EEGLAB functions makes it easy to combine them in new ways in original
Matlab scripts that can also incorporate any of the wide variety of
processing tools and methods available in Matlab. Thus, the most
straightforward way to add to EEGLAB capabilities is to use EEGLAB
functions and data structures within your own Matlab scripts, something
many or most EEGLAB users do routinely.

Matlab functions provide a level of encapsulation and isolation that
minimizes the possibility of interference between variable names within
and outside of the functions themselves, e.g. in Matlab scripts or
functions that may call them. EEGLAB is, in essence, a large set of
Matlab functions. Please send us (<eeglab@sccn.ucsd.edu>) any
EEGLAB-compatible functions you think would be of interest to other
researchers. We will consider any functions sent us for inclusion in the
EEGLAB distribution. Include a succinct explanation and references for
the signal processing methods used. If possible, write a clear function
help message using the style of EEGLAB help messages. However, first
consider the desirability of making your function into an EEGLAB
extension (formerly termed plug-in), as described later in this page.

# How to help with EEGLAB

We need help to fix important issues for EEGLAB users.

## EEGLAB possible projects

Below some projects posted by the EEGLAB developpers.

##### Plugins

A large collection of plugins are not maintained any more by their
author. Yet, they are still widely use. For example, the
[FMR-IB](https://github.com/sccn/fMRIb) plugin from Rami Niazi (for
artifact removal) is not supported any more. If you want to take over
maintaining this plugin, there are several issues listed on Gitbub. You
would maintain this plugin on Github. Email us for a list of unsuported
plugins.

##### Bug reports and improvements

The [Github EEGLAB repository](https://github.com/sccn/eeglab/issues/)
contain a list of issues. Any contribution to the discussion (or code
fixes) is welcomed. If you fix a bug, fork the EEGLAB repository and
issue a pull request. For more information about this process,
\[\[Fork_the_EEGLAB_repository|see this page about forking the EEGLAB
repository\].

A list of improvements is also available on the [Bugzilla legacy web
site](https://sccn.ucsd.edu/bugzilla/buglist.cgi?bug_severity=development&bug_severity=enhancement&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&f0=OP&f1=OP&f3=CP&f4=CP&list_id=422&query_based_on=Good_improv_P5&query_format=advanced).
This site contain a list of improvements that we do not have the
resources to implement but are nevertheless interested in seeing happen.
As above, fork the EEGLAB repository and issue a pull request.

##### Interactive Epoch Interpolation and Artifact Rejection

This project was initially proposed in this
[email](http://sccn.ucsd.edu/pipermail/eeglablist/2009/003048.html). Per
Arno's suggestion we have created a
[page](/Interactive_Epoching_Project "wikilink") specifically for this
project:

<http://sccn.ucsd.edu/wiki/Interactive_Epoching_Project>

# How to write EEGLAB functions

Adding new functionality to EEGLAB requires a pair of functions, a
signal processing function (Ex:
[sample.m](http://sccn.ucsd.edu/eeglab/download/sample.m)) and an
accompanying pop_function (Ex:
[pop_sample.m](http://sccn.ucsd.edu/eeglab/download/pop_sample.m)). The
pop_function pops up a text input window allowing the user to specify
arguments to the signal processing function. The Matlab help messages
for each function should state clearly what input arguments the
functions require and what they output, using the help message format
explained below. You should read the beginning of the [script
section](/Chapter_02:_Writing_EEGLAB_Scripts "wikilink") to understand
the different levels of functions in EEGLAB.

## Signal processing functions

Functions that direct operate on EEG data fields should comply with the
EEGLAB help-message syntax to allow the function header to be converted
into an .html help page by (functions
[makehtml()](http://sccn.ucsd.edu/eeglab/allfunctions/makehtml.m) and
[help2html()](http://sccn.ucsd.edu/eeglab/allfunctions/help2html.m). We
propose this [sample
header](http://sccn.ucsd.edu/eeglab/download/sample.m). Below is the GNU
license disclaimer to include in the function header.

> *This program is free software; you can redistribute it and/or modify
> it under the terms of the GNU General Public License as published by
> the Free Software Foundation; either version 2 of the License, or (at
> your option) any later version.* *This program is distributed in the
> hope that it will be useful, but WITHOUT ANY WARRANTY; without even
> the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
> PURPOSE. See the GNU General Public License for more details.* *You
> should have received a copy of the GNU General Public License along
> with this program; if not, write to the Free Software Foundation,
> Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA*

## Associated pop_ functions

A pop_function associated with a signal processing function creates a
graphic user interface to it. The pop_ function (whole name should
begin with *pop_* followed by the name of the signal processing
function) should include the same disclaimer as the signal processing
function and

1.  It must take the EEGLAB data structure 'EEG' as a first input. The
    second parameter may specify whether the signal processing function
    will be applied to ICA component activations or to the raw EEG data
    channels.
2.  Additional parameters should be optional. If they are left blank in
    a command line or script call to the the pop_function a Matlab
    window should pop-up to ask for their values.
3.  The pop_function must return a 'string' containing the resulting
    call to the signal processing function (or in some cases to the
    pop_function). When this string is evaluated (using the Matlab
    function 'eval()'), the result must be the same as that of the
    pop_function itself, e.g. including all the parameters the user may
    have entered into the pop-up interface window. This string will be
    pushed into the EEGLAB command history stack.
4.  By convention, if the function draws a figure, calling the function
    without enough arguments should pop up a new figure. However, given
    enough arguments (e.g. as a macro call), the function should
    directly draw the output graphic in the current figure (thus
    allowing the user to build multi-part figures, e.g. using 'sbplot()'
    commands). Writing a pop_function is easy and can usually be done
    in a few minutes if you just modify this
    [pop_sample.m](http://sccn.ucsd.edu/eeglab/download/pop_sample.m)
    function source.

## How to debug EEGLAB functions

When called from the EEGLAB GUI, EEGLAB intercepts errors which can make
it difficult to debug functions. The solution for this is to call the
function from the command line (preceded for example by "dbstop if
error") and in this case EEGLAB will not intercept the error.

# How to write an EEGLAB extension

EEGLAB also has an <b>extension</b> (formerly *plug-in*) facility that
automatically searches for functions loaded into a specified *plug-in*
directory, causing one or more menu items calling the extension to
appear in the EEGLAB menu. EEGLAB **extensions** can be offered for
download and use by anyone, independent of the EEGLAB distribution. Else
after preliminary review of the EEGLAB developers, they can be included
in the EEGLAB extension manager.


EEGLAB will automatically incorporate any appropriately named "plug-in"
functions that are named <b>eegplugin_\[myfunc\].m</b> that EEGLAB
finds in the same directory as 'eeglab.m'. (Here, *myfunc* should be the
name of the main signal processing function for the extension). Creating
an <b>eegplugin_</b> function in this directory will add a menu item
with the menu label(s) specified in your eegplugin_ function to the
bottom of the specified top-level EEGLAB menu (this extension menu label
being possibly linked to an unlimited number of sub-menus). This menu
item (or itemss) can call standard or custom EEGLAB data processing and
"pop_" functions (see examples below). When a user downloads an EEGLAB
extension (either from the EEGLAB extension manager, from the main
EEGLAB site, or from any other web site), he or she simply has to
uncompress the extension files into the plugin function sub-directory or
into the main EEGLAB directory (the directory in which *eeglab.m* is
located). The <b>eegplugin_</b> function will then be detected by
EEGLAB at startup (by looking for files or directories with names
beginning *eegplugin_* in the main EEGLAB directory). You may also
place the "eegplugin_" function in a sub-directory of the EEGLAB plugin
function directory.

## Creating an eegplugin_ function

To create a new EEGLAB extension, simply create a Matlab function file
whose name begins with **<b>eegplugin_</b>** and place it in the
'plugin' function subdirectory (or in your main EEGLAB directory). This
function must take three arguments, as in the 'test' extension
eegplugin_ function shown below:

> \>\> eegplugin_test (fig, try_strings, catch_strings);

The three arguments above are provided to the eegplugin_ function by
*eeglab()*. The first argument ('fig') is the handle of the main EEGLAB
window. The second and third arguments are structures passed by EEGLAB
that allow the eegplugin_ function to check parameters, detect errors,
etc. (see below). If for some reason you do not want your extension to
use EEGLAB history and error message handling, you can ignore the latter
two parameters (although the eegplugin_ function <em>definition</em>
still must list all three arguments).

## Adding an extension menu item or sub-menu

To create a new menu item for your extension under a top-level EEGLAB
menu, simply add a command like this to your eegplugin_ function:

> `>> uimenu( fig, 'label', '[My function]', 'callback', ... [ 'EEG = pop_[myfunc](EEG, ...); [ALLEEG EEG CURRENTSET] ... = eeg_store(ALLEEG, EEG, CURRENTSET);' ]); `


The statement *\[ALLEEG EEG CURRENTSET\] = eeg_store(ALLEEG, EEG,
CURRENTSET);* above insures that your modified EEG dataset will be
stored in the EEGLAB *ALLEEG* structure. \[myfunc\] should be replaced
with the name of your extension, and \[My function\] with brief
menu-item text (typically the name of your extension).

## Extensions and EEGLAB history

If you want your extension to interact with the EEGLAB history
mechanism, you should take advantage of the second ('try_strings') and
third ('catch_strings') arguments to your eegplugin_ function call.
The second argument (see *eegplugin_test()* above) contains commands
(organized into a Matlab structure) that check the input dataset and
attempt to execute your command. The third argument ('catch_strings')
contains commands to handle errors and add the contents of the LASTCOM
(i.e., last command) variable to the EEGLAB history.


eegplugin_ functions should declare one or more EEGLAB menu items. Each
menu declaration should look like this:

``` matlab
uimenu( submenu, 'label', 'My function', 'callback', ...
          [ try_strings.anyfield '[EEG LASTCOM] ... = pop_[myfunc](EEG, ...);' arg3.anyfield ]);
```


Possible fields for 'try_strings' (above) are:

  - *try_strings.no_check* : check for the presence of a non-empty EEG
    dataset only
  - *try_strings.check_ica* : check that the dataset includes ICA
    weights
  - *try_strings.check_cont* : check that the dataset is continuous
  - *try_strings.check_epoch* : check that the dataset is epoched (not
    continuous data)
  - *try_strings.check_event* : check that the dataset contains events
  - *try_strings.check_epoch_ica* : check that the dataset is epoched
    **and** includes ICA weights
  - *try_strings.check_chanlocs* : check that the dataset contains a
    channel location file
  - *try_strings.check_epoch_chanlocs* : check that the dataset is
    epoched **and** includes a channel locations (chanlocs) file
  - *try_strings.check_epoch_ica_chanlocs* : check that the dataset
    is epoched **and** includes ICA weights **and** a channel locations
    file.


Possible fields for 'catch_strings' are:

  - *catch_strings.add_to_hist* : add the LASTCOM variable content
    (if not empty) to the EEGLAB history
  - *catch_strings.store_and_hist* : add the LASTCOM variable content
    (if not empty) to the EEGLAB history **and** store the EEG dataset
    in the ALLEEG variable.
  - *catch_strings.new_and_hist* : add the LASTCOM variable content
    (if not empty) to the EEGLAB history **and** pop up a window for a
    new dataset.

## eeglugin_ function examples

A simplest type of eegplugin_ function might only call a plotting
function. For instance, to write a simple extension to plot the ERP
trial average at every channel in a different color (without performing
any data checking):

``` matlab
% eegplugin_erp() - plot ERP plugin
function eegplugin_erp( fig, try_strings, catch_strings);

% create menu
plotmenu = findobj(fig, 'tag', 'plot');
uimenu( plotmenu, 'label', 'Plot ERP', ...'callback', 'figure; plot(EEG.times, mean(EEG.data,3));');
```


Save the text above as a file, 'eegplugin_erp.m' into the plugin
function sub-directory of EEGLAB (or the EEGLAB directory in which the
function eeglab.m_ is located) and restart EEGLAB (click
[here](http://sccn.ucsd.edu/eeglab/allfunctions/eegplugin_erp.m) to
download this .m file). Then, given an epoched dataset, select the menu
item <font color = brown>Plot \> PLot ERP</font> to plot the ERP average
of all the dataset epochs.

Another, more complete example: To create an extension named 'PCA' that
would apply PCA to your data and store the PCA weights in place of the
ICA weights (Note: Not recommended for most purposes\!), save the Matlab
commands below as file 'eegplugin_pca.m' into the 'plugin'
sub-directory of EEGLAB (or the EEGLAB directory in which **eeglab.m**
is located) and restart EEGLAB (click
[here](http://sccn.ucsd.edu/eeglab/allfunctions/eegplugin_pca.m) to
download this .m file).

``` matlab
% eegplugin_pca() - a pca plug-in
function eegplugin_pca( fig, try_strings, catch_strings);

% create menu
toolsmenu = findobj(fig, 'tag', 'tools');
submenu = uimenu( toolsmenu, 'label', 'Run PCA');

% build command for menu callback\\ cmd = [ '[tmp1 EEG.icawinv] = runpca(EEG.data(:,:));' ];
cmd = [ cmd 'EEG.icaweights = pinv(EEG.icawinv);' ];
cmd = [ cmd 'EEG.icasphere = eye(EEG.nbchan);' ];
cmd = [ cmd 'clear tmp1;' ];

finalcmd = [ try_strings.no_check cmd ];
finalcmd = [ finalcmd 'LASTCOM = ''' cmd ''';' ];
finalcmd = [ finalcmd catch_strings.store_and_hist ];

% add new submenu
uimenu( submenu, 'label', 'Run PCA', 'callback', finalcmd);
```

Note: You may use eegplugin_ functions to append new extension_related
menu items under different EEGLAB menu headings. Above, we add an item
(labeled 'Run PCA') to the <font color=brown>Tools</font> menu by
specifying '' 'tag','tools' '' in the *findobj()* call. If the specified
tag were *import data*, EEGLAB would add the eegplugin_ specified menu
item to the <font color=brown>File \> Import data</font> sub-menu. Using
the tag *import epoch* would add the eegplugin_ specified menu item to
the <font color=brown>File \> Import epoch info</font> sub-menu. The tag
*import event* would add the eegplugin_ specified menu item to the
<font color=brown>File \> Import event info</font> menu. The tag
*export* would add the eegplugin_ specified menu item to the
<font color=brown>File \> Export data</font> menu. Finally, the tag
*plot* would add the eegplugin_ specified menu item to the
<font color=brown>Plot</font> menu. (Note that the tag call should be in
lower case).


After installing the eegplugin_ function above, a new EEGLAB menu item
<font color=brown>Tools \> Run PCA</font> will be created. Use this menu
item to learn the PCA transform for the current EEG dataset. The
resulting PCA decomposition will be stored in place of the ICA
decomposition. (Note: This is possible (if not typically advisable)
since both PCA and ICA are linear decompositions).


See the EEGLAB DIPFIT extension { {File|eegplugin_dipfit.m} } for an
example of a more elaborate extension.

Note: In EEGLAB4.3 we slightly modified how EEGLAB handles extensions.
As a result, later EEGLAB versions might not have been compatible with
earlier plugin functions. Subsequent versions of EEGLAB have and will
support backwards compatibility of extension conventions. In EEGLAB 13,
the term 'plug-in' has been replaced by the more general term
'extension' though the programming syntax remains the same. Also, a new
EEGLAB Extension Manager now helps users download extensions and alerts
current users when extension authors have made a new version available.

## EEGLAB menu integration

As of EEGLAB11, it is possible for the user to control menu behavior
within EEGLAB. EEGLAB can automatically enable or disable (e.g., gray
out and make unresponsive) menu items based on data in memory. This may
result in some extension-related menu items being automatically disabled
under circumstances in which they should not be. In EEGLAB11, we
implemented a new extension menu item activation scheme that makes it
possible to control when an extension's menu item(s) will be active. To
do so, developers must incorporate several keywords in the "userdata"
field of the menu item:

| Keyword        | Default                                | Description                                                                             |
| -------------- | -------------------------------------- | --------------------------------------------------------------------------------------- |
| **epoch**      | { {table|status=on|color=lightgreen} } | set to **off** to disable the menu item when an epoched dataset is being processed      |
| **continuous** | { {table|status=on|color=lightgreen} } | set to **off** to disable the menu item when a continuous dataset is being processed    |
| **startup**    | { {table|status=off|color=orange} }    | set to **on** to enable the menu item at start up when no data have been loaded         |
| **study**      | { {table|status=off|color=orange} }    | set to **on** to enable the menu item when a STUDY is being processed                   |
| **chanloc**    | { {table|status=off|color=orange} }    | when set to **on**, the menu item will be disabled if channel locations are not present |


Keywords should be separated by semicolons. An example of an
extension-elated menu item that is enabled only at startup and when
processing EEGLAB studies is shown below:

``` matlab
   toolsmenu = findobj(fig, 'tag', 'tools');
   uimenu( submenu, 'label', 'My menu', 'callback', mycommand, 'userdata', 'startup:on;study:on');
```

Note that adding **epoch:on** or **continuous:on** would not change the
menu item behavior since these are default behaviors. The following
example would enable the menu item only when processing continuous or
epoched datasets that have channel locations present:

``` matlab
   toolsmenu = findobj(fig, 'tag', 'tools');
   uimenu( submenu, 'label', 'My menu', 'callback', mycommand, 'userdata', 'chanloc:on');
```

Omitting the **userdata** parameter results in the extension menu item
adopting the default behaviors defined in the table above.

## Submitting your plugin

Once you are done with your plugin/extension, you may submit it to this
web [page](http://sccn.ucsd.edu/eeglab/plugin_uploader/upload_form.php).
We will make it appear in the EEGLAB plugin manager for other users to
try.

# Using EEGLAB GUI design functions

The function **supergui()** is the main function used for creating
graphic interfaces in EEGLAB. We will be describing below some basic and
more advanced uses for it:

## Using the supergui function

Supergui was designed to alleviate the burden of manually creating
graphic interface for each function. Instead a series of controls are
defined along with a geometry and the figure is automatically created.
An example is shown below:

``` matlab
  supergui( 'geomhoriz', { 1 1 1 }, 'uilist', { ...
         { 'style', 'text', 'string', 'Hello!' }, { }, ...
         { 'style', 'pushbutton' , 'string', 'OK' } } );
```

This creates the following graphic interface

[center](/Image:Supergui1.jpg "wikilink")

The command line call above contains two main arguments: 'geometry' and
'uilist'. 'geometry' defines the geometry in this case 3 lines { 1 1 1}
(see more complex geometry below). The 'uilist' defines the content for
each of these lines. The first line contains some text "{ 'style',
'text', 'string', 'Hello\!' }". The second line is empty "{ }" and the
third line contains the "OK" button "{ 'style', 'pushbutton' , 'string',
'OK' }".

If you press OK, nothing will happen however because no action has been
associated with this button. To associate an action to a UI control,
simply use the 'callback' command and enter any Matlab command in the
associated string parameter.

``` matlab
  supergui( 'geomhoriz', { 1 1 1 }, 'uilist', { ...
         { 'style', 'text', 'string', 'Hello!' }, { }, ...
         { 'style', 'pushbutton' , 'string', 'OK' 'callback' 'close(gcbf);' } } );
```

Above, we added the 'callback' command "close(gcbf)" which closes the
current figure when users press the "OK" button.

Almost any geometry (but not all as detailed in the advanced section)
may be defined using this scheme. For instance

``` matlab
  supergui( 'geomhoriz', { [1 1] 1 1 }, 'uilist', { ...
         { 'style', 'text', 'string', 'Enter some text' }, ...
         { 'style', 'edit', 'string', 'Hello!' }, { }, ...
         { 'style', 'pushbutton' , 'string', 'OK' 'callback' 'close(gcbf);' } } );
```

[center](/Image:Supergui2.jpg "wikilink")

The first line now has geometry \[1 1\] which means that two UI will
share this line and have the same horizontal extent. Changing \[1 1\] to
\[1 0.5\] as shown below forces the second UI on the line to have only
half the horizontal extent of the first one.

[center](/Image:Supergui3.jpg "wikilink")

In some case, it is convinient to have a UI spam more than one line of
text. This is often the case for listbox for instance. Below we define a
listbox with multiple choice and use the additional command 'geomvert'
to specify the vertical geometry. It is set to \[3 1 1\] which means
that the UI on the first line will span 3 lines of text, and the other
lines will only span one line of text (we have to add carriage returns -
character 10 - to the text of the first UI so this text is aligned with
the listbox).

``` matlab
  supergui( 'geomhoriz', { [1 1] 1 1 }, 'geomvert', [3 1 1], 'uilist', { ...
         { 'style', 'text', 'string', [ 'Make a choice' 10 10 10 ] }, ...
         { 'style', 'listbox', 'string', 'Choice 1|Choice 2|Choice 3' }, { }, ...
         { 'style', 'pushbutton' , 'string', 'OK' 'callback' 'close(gcbf);' } } );
```

[center](/Image:Supergui4.jpg "wikilink")

## Using the inputgui function

Although supergui can be useful, it only creates the GUI and all the
control flow of events needs to be handled by the UIs; i.e., creating a
button "OK", a button "Cancel" and handling the events associated to
these buttons are left to the user. The **inputgui()** function (which
calls the supergui function) helps supplement this by automatically
creating these buttons and also by processing outputs. For instance:

``` matlab
  res = inputgui( 'geometry', { [1 1] }, ...
         'geomvert', [3], 'uilist', { ...
         { 'style', 'text', 'string', [ 'Make a choice' 10 10 10 ] }, ...
         { 'style', 'listbox', 'string', 'Choice 1|Choice 2|Choice 3' } } );
```

[center](/Image:Supergui5.jpg "wikilink")

The "res" output contains the results in this case a cell array
containing a single value from 1 to 3 indicating which choice the user
made (for instance { \[1\] }). The number of elements in this cell array
depends on the number of UIs returning output (in general text and
button do not return output but checkbox, listbox, and edit box do).
Another way to use this function is to set tag for each UI and use the
4th output

``` matlab
  [res userdata err structout] = inputgui( 'geometry', { [1 1] }, ...
         'geomvert', [3], 'uilist', { ...
         { 'style', 'text', 'string', [ 'Make a choice' 10 10 10 ] }, ...
         { 'style', 'listbox', 'string', 'Choice 1|Choice 2|Choice 3' 'tag' 'list' } } );
```

Now the output structure "structout" contains a field named "list" that
will contain the output of the listbox (structout.list = 1 for
instance). This is convenient for creating GUIs, as developers do not
need to remember the order of the output. You may change the order of
lines and you will not have to change any other part of your script.
Note that this is not the case when using the "res" output described at
the beginning of this section.

A complex UI shown below uses this technique. It is inspired by the
pop_newtimef() function.

``` matlab
    g = [1 0.3 0.6 0.34];
    geometry = { g g g g g g g g [1.025 1.27] [1] [1.2 1 1.2]};
    uilist = { ...
      { 'Style', 'text', 'string', 'Channel number', 'fontweight', 'bold'  } ...
      { 'Style', 'edit', 'string', '1' 'tag' 'chan'} {} {} ...
      ...
      { 'Style', 'text', 'string', 'Time limits [min max] (msec)', 'fontweight', 'bold' } ...
      { 'Style', 'edit', 'string', ' ' 'tag' 'tlimits' } ...
      { 'Style', 'popupmenu', 'string', 'Use 50 time points|Use 100 time points' ...
        'tag' 'ntimesout' 'value' 4} { } ...
      { 'Style', 'text', 'string', 'Frequency limits (Hz)', 'fontweight', 'bold' } ...
      { 'Style', 'edit', 'string', ' ' 'tag' 'freqs'  } ...
      { 'Style', 'popupmenu', 'string', 'Use limits, padding 1|Use limits, padding 2' ...
        'tag' 'nfreqs' }  ...
      { 'Style', 'checkbox', 'string' 'Log spaced' 'value' 0 'tag' 'freqscale' } ...
      ...
      { 'Style', 'text', 'string', 'Baseline limits [min max] (msec) (0->pre-stim.)', ...
        'fontweight', 'bold' } ...
      { 'Style', 'edit', 'string', '0' 'tag' 'baseline' } ...
      { 'Style', 'popupmenu',  'string', 'Use divisive baseline|Use standard deviation' ...
        'tag' 'basenorm' } ...
      { 'Style', 'checkbox', 'string' 'No baseline' 'tag' 'nobase' } ...
      { 'Style', 'text', 'string', 'Wavelet cycles [min max/fact] or sequence', ...
        'fontweight', 'bold' } ...
      { 'Style', 'edit', 'string', '3 0.5' 'tag' 'cycle' } ...
      { 'Style', 'popupmenu', 'string', 'Use limits|Use actual seq.' 'tag' 'ncycles' } ...
      { 'Style', 'checkbox', 'string' 'Use FFT' 'value' 0 'tag' 'fft' } ...
      { 'Style', 'text', 'string', 'ERSP color limits [max] (min=-max)', ...
        'fontweight', 'bold' } ...
      { 'Style', 'edit', 'string', ' ' 'tag' 'erspmax'} ...
      { 'Style', 'checkbox', 'string' 'see log power (set)' 'tag' 'scale' 'value' 1} ...
      {} ...
      { 'Style', 'text', 'string', 'ITC color limits [max]', 'fontweight', 'bold' } ...
      { 'Style', 'edit', 'string', ' ' 'tag' 'itcmax'} ...
      { 'Style', 'checkbox', 'string' 'plot ITC phase (set)' 'tag' 'plotphase' } {} ...
      { 'Style', 'text', 'string', 'Bootstrap significance level (Ex: 0.01 -> 1%)', ...
        'fontweight', 'bold' } ...
      { 'Style', 'edit', 'string', ' ' 'tag' 'alpha'} ...
      { 'Style', 'checkbox', 'string' 'FDR correct (set)' 'tag' 'fdr' } {} ...
      { 'Style', 'text', 'string', 'Optional newtimef() arguments (see Help)', ...
        'fontweight', 'bold'} ...
      { 'Style', 'edit', 'string', ' ' 'tag' 'options' } ...
      {} ...
      { 'Style', 'checkbox', 'value', 1, 'string', ...
        'Plot Event Related Spectral Power', 'tooltipstring', ...
        'Plot log spectral perturbation image in the upper panel' 'tag' 'plotersp' } ...
      { 'Style', 'checkbox', 'value', 1, 'string', ...
        'Plot Inter Trial Coherence', 'tooltipstring', ...
        'Plot the inter-trial coherence image in the lower panel' 'tag' 'plotitc' } ...
      { 'Style', 'checkbox', 'value', 0, 'string', ...
        'Plot curve at each frequency' 'tag' 'plotcurve' } ...
      };

      [ tmp1 tmp2 strhalt structout ] = inputgui( geometry, uilist, ...
           'pophelp(''pop_newtimef'');', 'Plot channel time frequency -- pop_newtimef()');
```

Copying and pasting the script above should generate the GUI below. Note
how simply the geometry was defined. The supergui function adapts
automatically the width and height of the window to the containing
elements. Also note the "Help" button which executes the command
"'pophelp(*pop_newtimef*);'" defined in the inputgui command line call.
Upon pressing **'OK**', the fields of the the "structout" structure
contain all the user entry in the GUI.

[center](/Image:Supergui6.jpg "wikilink")

## Advanced GUI design

One limitation of the supergui calling format is that it is not possible
to define random geometries. Any given line needs to span the same
height. There is an advanced calling format that allows to circumvent
that problem.

``` matlab
  supergui('geom', { {2 2 [0 0] [1 2] } { 2 2 [1 0] [2 1] } { 2 2 [1 1] [2 2] } }, ...
           'uilist', { { 'style' 'listbox' 'string' 'cell 1|cell 2' } ...
                       { 'style' 'checkbox' 'string' 'cell 3' } ...
                       { 'style' 'text' 'string' 'cell 4' } });
```

[center](/Image:Supergui7.jpg "wikilink")

This type of interface is not possible using standard calls. The 'geom'
input is detailed in the help section of the supergui function.

[Category:IV. Appendix](/Category:IV._Appendix "wikilink") {
{Backward_Forward|A06:_Maximizing_Memory|A06: Maximizing
Memory|A08:_DIPFIT|A08: DIPFIT} }