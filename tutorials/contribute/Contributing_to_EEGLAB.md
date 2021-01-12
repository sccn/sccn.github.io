---
layout: default
title: Modify EEGLAB code
long_title: Modify EEGLAB code
parent: How to contribute?
grand_parent: Tutorials
---
Contributing to the EEGLAB core code
========================
{: .no_toc }

The main EEGLAB repository is not the place to add new functions. Instead, this is done by creating EEGLAB extensions/plugins. However, it is possible to modify the core code to either fix bugs, or add minor improvements to existing functions. 

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

EEGLAB development model
-------------------

### EEGLAB history

The chief EEGLAB software architects are Arnaud Delorme and Scott Makeig. The predecessor to EEGLAB, the ICA/EEG Toolbox (1997-2001), comprised
functions written by Makeig with Tony Bell, Colin Humphries, Sigurd
Enghoff, Tzyy-Ping Jung, Te-Won Lee, and others, was first released on
the Web in 1997 by Scott Makeig at the Computational Neurobiology
Laboratory of Terrence Sejnowski at The Salk Institute, La Jolla. 

The first version of the integrated EEGLAB toolbox was written there by
Delorme and Makeig with subsequent contributions by many, including
Marissa Westerfield, Jörn Anemüller, Luca Finelli, Robert Oostenveld,
Hilit Serby, Toby Fernsler, Nima Shamlo Bigdeley, Jason Palmer, and many
others. Dedicated beta testers include Andreas Romeyke and his team, who
developed a test suite for EEGLAB, and other advanced users, including
Stefan Debener and Andreus Widmar. 

EEGLAB development is now centered at the Swartz Center for Computational Neuroscience (SCCN) of the Institute
for Neural Computation at the University of California San Diego (UCSD). Core EEGLAB maintenance and development is supported by the US National Institute of Neurological Disorders and Stroke (NINDS). 

The EEGLAB core code cannot be modified by third parties directly. Instead,
users submits [pull requests](/others/Fork_the_EEGLAB_repository.html). EEGLAB core developers then
review the code and add it to the repository.

For third-party developers, we welcome collaborations with users and
open-source developers to expand and improve EEGLAB functions and/or
independently write and release EEGLAB plugin/extension applications
and environments. If you have written plugins for use in your
laboratory, please consider releasing them for use by others, as described on this page.

EEGLAB is under active open-source development. Together with user
developers, we are extending its capabilities to include across-subject
general linear model statistics. User-contributed features and
suggestions are welcome, and we encourage and plan to interconnect EEGLAB
with other MATLAB-compatible toolboxes.

### Open-source model

EEGLAB is an open-source software environment and is available free of
charge to any user.

However, EEGLAB requires that you purchase and install the commercial
[MATLAB software environment](http://www.mathworks.com/store/). MATLAB
version 2008b or later is required; We recommend using the latest
version of MATLAB. MATLAB and EEGLAB run under Linux/Unix, Mac OS X, or
Windows. Purchasing MATLAB can be expensive, though the MATLAB student
version is usually priced near $50 US.

We have attempted to remove all dependencies on add-on MATLAB toolboxes.
Thus, no additional toolboxes are necessary to run the EEGLAB core distribution. However, some advanced plugin toolboxes may
use functions from a specific MATLAB toolbox: see their documentation
for details.

Note that all EEGLAB processing functions (not its graphic interface) also can be run under the free
[Octave environment](http://www.gnu.org/software/octave/download.html). EEGLAB also exists as a compiled program that does not require MATLAB.

### License and credits

EEGLAB is distributed under the [BSD
    license](https://opensource.org/licenses/BSD-2-Clause). Any
    contributed functions we add to EEGLAB will be made available for
    free commercial and non-commercial use under this license.

Contributors are acknowledged on GitHub, which record commits made to the main source code. 

Consider writing an *extension* or *plugin* option, as described
in the section below. EEGLAB extensions allow authors to flexibly
incorporate new functions into the EEGLAB menu of every user who has
downloaded the extension. The authors also retain all commercial rights to the functions they write.

### Code of conduct

We strive to follow a code of conduct emphasizing community,
collaboration, respect, and responsibility first outlined by the [Ubuntu
community](https://ubuntu.com/community/code-of-conduct).

### Using GIT to contribute code

To contribute code to the EEGLAB core code, fork the code and create a
pull request as indicated below. You will need a Github account
to perform these operations but do not require any special permission
from us.

Forking the EEGLAB repository
---

The main EEGLAB repository is not the place to add new functions. If
you want to add new functionality, write an EEGLAB
[plugin](/tutorials/misc/Contributing_to_EEGLAB.html) instead.

### Why fork the EEGLAB repository?
This page assumes that you are somewhat familiar with GitHub, Git, and version control.

Forking (copying) a software repository makes a copy of the repository
that belongs to you. This allows you to experiment
without affecting the existing code. Once you are done with your
changes, you will be able to transfer them (push them) to the main
repository by using *pull requests* (this could have been
referred to as *push requests*, but the software community decided to
name it from the perspective of the main repository, which then is
<em>pulling</em> in your changes). This page will introduce you to the
basics of forking the EEGLAB repository. Github makes the procedure very
simple.

### Forking the EEGLAB repository

To fork the EEGLAB repository from Github, follow these two simple
steps:

1.  On Github, go to the [EEGLAB
    repository](https://github.com/sccn/eeglab)
2.  Click *Fork* in the top right corner of the window (See the figure
    below).

![center\|thumb\|700px](/assets/images/Fork_link.jpg)

Once you have executed these two steps, you will have successfully
created your own copy of the EEGLAB repository. The new repository will look
exactly like the EEGLAB repository you forked, but the forked copy
will be under your username account.

![center\|thumb\|700px](/assets/images/Fork_username.jpg)

### Working on your forked copy

Once you have created your fork in Github, you will need to set up
*git* in your computer to start working on your EEGLAB code copy. Then
you will need to clone the forked repository to your computer.

-   Go to the forked repository page in Github. This is the
    same page described in the figure above.
-   Look on the right side of the page for the button *Clone or
    download* and click it.

![center\|thumb\|700px](/assets/images/Clone_link.jpg)

-   Click in the clone HTTPS section to copy the link.

![center\|thumb\|400px](/assets/images/Clone_https_link.jpg)

-   Open a terminal on your computer and type *git clone* and then paste
    and execute the link you copied in the previous step.

`$git clone `[`https://github.com/yourgitusername/eeglab.git`](https://github.com/yourgitusername/eeglab.git)

After following these steps, you will be ready to start modifying the EEGLAB code.

### Issuing a pull request

Once you are satisfied with your code changes, commit them to GitHub. Then,  go back to Github
and issue a *pull request*. Once your changes are evaluated and approved
by the EEGLAB team, they will be merged into the EEGLAB master code.

![center\|thumb\|700px](/assets/images/Pullrequest1.png)

This brings you to a screen where you can select the forked branch to merge into the EEGLAB repository. NOTE: Always merge
into the "develop" branch of EEGLAB.

![center\|thumb\|700px](/assets/images/Pullrequest2.png)

### Considerations regarding pull requests

For expedited approval:
-   If you have added a new feature, make sure it works both from the
    graphic interface and from the MATLAB command line. Please send us a
    simple test script to demonstrate this.
-   Run the test cases on the modified function. If possible, add the test case to the [EEGLAB test case repository](https://github.com/sccn/eeglab-testcases).
-   You can never add too much documentation. Make sure you document
    your changes clearly and thoroughly!
-   Issue pull request for single-function changes.
-   Avoid making large numbers of cosmetic changes (indentation, etc.). If there are too many changes, they take a long time to review and are often rejected.