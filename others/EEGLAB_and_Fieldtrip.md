---
layout: default
title: EEGLAB and FieldTrip
long_title: EEGLAB and FieldTrip
parent: Interoperability
---

EEGLAB and FieldTrip
=========================
{: .no_toc }
<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

History
--------

First a little bit of history. EEGLAB was created in 2000 at The Salk
Institute (La Jolla CA) by Arnaud Delorme and Scott Makeig. EEGLAB was 
fully released in 2002 at the Swartz Center for Computational Neuroscience, 
UCSD (La Jolla, California, USA). 

In 2003-04, the EEGLAB software architect Arnaud
Delorme worked with FieldTrip senior author Robert Oostenveld to provide
basic source localization to EEGLAB via the EEGLAB DIPFIT plugin using
MATLAB code Robert had developed for dipole fitting. Together with many
other functions written at the Donders Institute for Brain, Cognition,
and Behavior (Nijmegen, The Netherlands), the source code contributed by
Robert Oostenveld to DIPFIT served as a basis for FieldTrip, which was
first released by the Donders Institute in 2005. Both packages run on
MATLAB (The Mathworks, Inc.).

Interdependencies
-------------------

EEGLAB and FieldTrip are in part interdependent. For basic source
localization, EEGLAB uses the DIPFIT plugin, which incorporates a
FieldTrip source localization routine. EEGLAB also offers users the
choice of using some FieldTrip statistical routines as well as its own.
The FieldTrip code also includes some EEGLAB functions such as
*topoplot.m* and *runica.m* for performing independent component analysis
decomposition.

EEGLAB and FieldTrip developers meet every year or every
other year to discuss progress in the field and possible collaborations
or new bridges between the two software. 

In the spirit of open-source
programming, we believe that more collaboration is better. Working from
experience with a diversity of approaches allows us to identify and
deal with problematic signal processing issues.

Development philosophies
--------------------------

In practice, the philosophies of EEGLAB and FieldTrip are somewhat
different:

-   FieldTrip is aimed mostly at advanced users and does not have a
    graphic user interface. In contrast, EEGLAB provides a graphic user
    interface (GUI) for data exploration plus a graded path toward
    writing custom analysis scripts using the EEGLAB functions called by
    the EEGLAB GUI.

-   FieldTrip provides limited tools for handling group data. Managing
    group data is intentionally left to the user's choice with a
    rationale that users should not be forced to use any predefined
    scheme for modeling the experimental design. By contrast, EEGLAB 
    provides tools to apply a variety of statistical models and
    sub-models to group experimental data.

-   FieldTrip allows variable-length data epochs. Though EEGLAB supports
    processing of multiple continuous data segments, it is not as
    flexible as FieldTrip in processing data epochs of variable lengths.
    Historically, this difference arose in part because FieldTrip was
    developed to support animal as well as human physiological data
    analysis, whereas EEGLAB development has always focused on the analysis
    of human data.

-   FieldTrip functions provide packaged solutions in which low-level
    processing is hidden and subject to change. Thus, a large number of
    FieldTrip functions that change frequently are hidden in private
    folders. By contract, there are no hidden functions in EEGLAB; users
    have direct access to low-level processing functions, and these are
    fully documented.

-   Any new contribution to FieldTrip adds to the general FieldTrip
    package supported by the Donders Center. In practice, this makes it
    difficult for external developers to contribute code (the FieldTrip
    developers are open about this, though). In EEGLAB, all third party
    contributions are made available as EEGLAB extensions (formerly
    'plugins'). To date, there are more than 120 EEGLAB extensions
    available from many developers, including extensive toolboxes
    ERPLAB, SIFT, LIMO, NFT, MoBILAB, etc. Third-party
    developers maintain full control over their extensions.

-   When you download FieldTrip, you download the *code of the day* (the
    head of the development code), which could contain recently added
    bugs (this might change in the future). EEGLAB
    remains more of a structured package for which additions to core
    functions are carefully considered and controlled to maximize
    stability. EEGLAB's third-party extension (plugin) facility
    provides a free medium for new tool development and publication by
    many groups and individuals.

Which environment should you choose to use?
---------------------------------------------

The choice between either (or both) environments is yours. Some
considerations:

-   If you have little experience with analysis script writing, we
    definitely recommend you try EEGLAB. EEGLAB facilities and
    documentation will also guide you through learning how to write
    scripts, even writing scripts for you based on your menu choices.

-   If you are an advanced programmer, FieldTrip's nested data
    structures might appeal to you. EEGLAB data structures have
    been kept simple on purpose, so beginners do not feel overwhelmed and
    have easy script access to information about their data.

-   If you want maximum control over your processing pipeline, you might
    also want to choose EEGLAB since it gives you ready access to
    low-level processing functions and has in-depth documentation. Also,
    if you want to maximize the probability that your code will continue
    to work in future revisions of the software, again EEGLAB might be
    the best option.

-   If you want to publish MATLAB code for new functions or toolboxes,
    EEGLAB extensions provide a sure way to make your code known and
    available for widespread, easy use and testing -- even directly from
    the EEGLAB GUI of users who download your extensions. The EEGLAB
    Extension Manager will also allow you to help users maintain current
    versions of your extensions.

-   Both EEGLAB and FieldTrip can be added to the MATLAB path and run
    together. Some functions are available to convert between data
    structures of both toolboxes, such as the EEGLAB *eeglab2fieldtrip.m*
    and the *fieldtrip2eeglab.m* functions - note that these functions
    focus on converting specific structure of data (FieldTrip has
    several of them) and are not meant to be all-purpose functions.
    EEGLAB can also import data from FILE-IO, which is compatible with
    MATLAB files saved by FieldTrip. There is a notable function name
    conflict when using both EEGLAB and FieldTrip together -- the
    *topoplot.m* function is present in both toolboxes (EEGLAB will handle the conflict for you).

Converting between EEGLAB and FieldTrip data structures
--------------------------------------------------------

In practice, it is easy to use both EEGLAB and FieldTrip at the same
time and to convert back and forth between data structures.

To import FieldTrip data structures into EEGLAB, you may use the
*pop_fileio* function of EEGLAB or the *fieldtrip2eeglab*  function (the
result is the same since fieldtrip2eeglab calls *pop_fileio*).

``` matlab
EEG = pop_fileio(hdr, dat, events);
```

or

``` matlab
EEG = fieldtrip2eeglab(hdr, dat, events);
```

To import EEGLAB datasets in FieldTrip is to read EEGLAB datasets using
the file File-IO interface either using the standard FILE-IO interface
or using the low-level EEGLAB reading function of FILE-IO as below.

``` matlab
hdr = ft_read_header( EEGLABFILE );
data = ft_read_data( EEGLABFILE, 'header', hdr );
events = ft_read_event( EEGLABFILE, 'header', hdr );
```

A legacy function *eeglab2fieldtrip* also exists although it is mostly
used internally in EEGLAB to convert EEGLAB datasets to FieldTrip for
source localization purposes (DIPFIT). It is not recommended to use that
function although it might still work for your application.

Performing advanced source localization using DIPFIT/FieldTrip
---------------------------------------------------------------

The [source localization section](/tutorials/09_source/EEG_sources)
of the tutorial describes how to use FieldTrip functions to localize sources underlying EEG activity and ICA components.

Wrap up your FieldTrip scripts into EEGLAB plugin menu items
----------------------------------------------------------------

Because of our historical collaboration,
EEGLAB channel locations may be conveniently aligned with FieldTrip
head models from the EEGLAB graphic interface, allowing you to leverage the full capabilities of FieldTrip source reconstruction methods on EEGLAB
datasets as outlined in the
[source localization section](/tutorials/09_source/EEG_sources.html#advanced-source-reconstruction-using-dipfitfieldtrip) of the tutorial.

We have created the template [erpsource](https://github.com/sccn/erpsource) EEGLAB plugin that takes EEGLAB data as input, performs the
coregistration with a standard FieldTrip BEM model, and apply eLoreta
for ERP analysis (also based on the previous
[section](/tutorials/09_source/EEG_sources.html#advanced-source-reconstruction-using-dipfitfieldtrip)).
We believe this template could be modified by some of you to create
other plugins.

The long term sustainability of EEGLAB and FieldTrip relies on the
contribution of new methods by the community for advanced MEEG
processing. Making your FieldTrip code available as an EEGLAB plugin
(there are more than 120 plugins to date) will make it visible to the
EEGLAB community. 

You can submit a plugin on this [web page](https://sccn.ucsd.edu/eeglab/plugin_uploader/upload_form.php) and,
once approved, it becomes instantaneously visible by all EEGLAB users
and available directly in the EEGLAB graphic interface (according to our
statistics on Mixpanel in 2019, 150,000 to 200,000 EEGLAB sessions are
started each month from about 10,000 to 20,000 unique users). Plugins
are ranked by the number of downloads, and there is also a rating/commenting
system in place for each plugin. The quarterly EEGLAB newsletter sent to
15,000 researchers also features new plugins upon request from their
author.

Do not hesitate to contact [us](mailto:eeglab@sccn.ucsd.edu) if you have
questions.
