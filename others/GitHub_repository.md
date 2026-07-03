---
layout: default
title: GitHub repository
long_title: GitHub repository
parent: Download EEGLAB
nav_order: 2
---
Cloning EEGLAB from GitHub
====
Since 2014, it is possible to use GIT to download the latest
development version of EEGLAB from GitHub at any time - this version is
more recent than the [ZIP release](/others/How_to_download_EEGLAB.html). Because of our development scheme, the
latest version of EEGLAB is usually the most stable. We recommend
using [SourceTree](https://www.sourcetreeapp.com/) to visualize branches.
Clone the [EEGLAB GitHub
repository](https://github.com/sccn/eeglab.git) as you would do with any
standard git package. When cloning, make sure you use the
*--recurse-submodule* option. Otherwise, important EEGLAB plugins will not be downloaded and EEGLAB will not be fully functional.

```
git clone --recurse-submodules https://github.com/sccn/eeglab.git
```

Accessing branches
------------------

The Master branch is a copy of the latest ZIP release. The *develop*
branch is the latest stable code with updates and bug fixes. Most likely,
you will want to use the *develop* branch, which is the branch cloned by default.

All other branches refer to previous versions of EEGLAB or unstable code
that is under intensive development. To update the EEGLAB code using the
latest development sources, simply right click on the EEGLAB folder and
select *git pull*.

Contributing code to EEGLAB
------------------

To contribute code to EEGLAB, fork the code and create a pull request, as
indicated on this [page](/tutorials/contribute/Contributing_to_EEGLAB.html#forking-the-eeglab-repository). This other
[page](/tutorials/contribute) contains additional
information on how to contribute to EEGLAB.

Prior repository systems
------------------

EEGLAB was first under RCS (2002-2005), then under CVS (2005-2010), and
finally under SVN (2010-2014) before migrating to GIT (2014-). All
commit messages have been preserved in the migration process.
