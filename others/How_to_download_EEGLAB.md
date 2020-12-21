---
layout: default
title: How to download EEGLAB
parent: Other documents
---

# How to download EEGLAB

This page describe how to download the development version of EEGLAB.
This version contains the latest development. It is recommended for EEG
advanced users.

ZIP download
------------

EEGLAB download in ZIP format is available at [EEGLAB download
link](https://sccn.ucsd.edu/eeglab/download.php). This includes the
latest release as well as old versions.

Getting the latest development copy using any GIT Client (Windows, etc...)
--------------------------------------------------------------------------

Since the end of 2014, it is possible to use GIT to download the latest
development version of EEGLAB from Github at any time - this version is
more recent that the ZIP above. Because of our development scheme, the
latest version of EEGLAB is usually the most stable. We recommend
[sourcetree](https://www.sourcetreeapp.com/) to visualize branches.
Simply clone the [EEGLAB GitHub
repository](https://github.com/sccn/eeglab.git) as you would do with any
standard git package. When cloning make sure you use the the option
**--recurse-submodule** (git clone --recurse-submodule
git@github.com:eeglabdevelopers/eeglab.git) otherwise the firfilt plugin
- which is the default filtering plugin - will not be downloaded and
will not be functional.

Accessing branches
------------------

The Master branch is a copy of the latest ZIP release. The *develop*
branch is the latest stable code with updates and bug fixes. Most likely
you will want to use this branch.

All other branches refer to previous version of EEGLAB or unstable code
that is under intensive development. To update the EEGLAB code using the
latest development sources, simply right click on the EEGLAB folder and
select "git pull".

Contributing code to EEGLAB
---------------------------

To contribute code to EEGLAB, fork the code and create a pull request as
indicated on this [page](/Fork_the_EEGLAB_repo "wikilink"). This other
[page](/A07:_Contributing_to_EEGLAB "wikilink") contains other
information on how to contribute to EEGLAB.

Prior repository systems
------------------------

EEGLAB was first under RCS (2002-2005), then under CVS (2005-2010), and
finally under SVN (2010-2014) before migrating to GIT (2014-). All the
revision message have been preserved in the migration process. It is
however not possible to access the RCS, CVS, and SVN repositories since
they refer to obsolete versions of EEGLAB.

