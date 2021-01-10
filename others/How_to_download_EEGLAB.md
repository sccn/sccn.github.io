---
layout: default
title: Download EEGLAB
parent: Other documents
---
Download EEGLAB <span style="color: green">- DONE</span>
====

Go to the [EEGLAB download
page](https://sccn.ucsd.edu/eeglab/download.php) to download the latest stable version of EEGLAB. The rest of this page describes how to download the development version of EEGLAB, and is recommended for advanced EEGLAB users only.

Download the EEGLAB ZIP file archive
------------
EEGLAB download in ZIP format is available on the [EEGLAB download
page](https://sccn.ucsd.edu/eeglab/download.php). This includes the
latest release as well as old versions. The [EEGLAB revision history page](/others/EEGLAB_revision_history.html) describes changes between EEGLAB versions.

Please do NOT download the zip file from the [EEGLAB GitHub repository](https://github.com/sccn/eeglab.git) as it is missing important EEGLAB plugins not included in the EEGLAB code base. If you want to use the development version of EEGLAB, clone it and include submodules as explained below.

Cloning EEGLAB from GitHub
------------------
Since 2014, it is possible to use GIT to download the latest
development version of EEGLAB from GitHub at any time - this version is
more recent than the ZIP above. Because of our development scheme, the
latest version of EEGLAB is usually the most stable. We recommend
using [SourceTree](https://www.sourcetreeapp.com/) to visualize branches.
Clone the [EEGLAB GitHub
repository](https://github.com/sccn/eeglab.git) as you would do with any
standard git package. When cloning, make sure you use the
*--recurse-submodule* option. Otherwise, important EEGLAB plugins will not be downloaded and EEGLAB will not be fully functional.

```
git clone --recurse-submodules https://github.com/sccn/eeglab.git
```

### Accessing branches

The Master branch is a copy of the latest ZIP release. The *develop*
branch is the latest stable code with updates and bug fixes. Most likely,
you will want to use the *develop* branch, which is the branch cloned by default.

All other branches refer to previous versions of EEGLAB or unstable code
that is under intensive development. To update the EEGLAB code using the
latest development sources, simply right click on the EEGLAB folder and
select *git pull*.

### Contributing code to EEGLAB

To contribute code to EEGLAB, fork the code and create a pull request, as
indicated on this [page](/others/Fork_the_EEGLAB_repository.html). This other
[page](/tutorials/misc/Contributing_to_EEGLAB.html) contains other
information on how to contribute to EEGLAB.

### Prior repository systems

EEGLAB was first under RCS (2002-2005), then under CVS (2005-2010), and
finally under SVN (2010-2014) before migrating to GIT (2014-). All
commit messages have been preserved in the migration process.

