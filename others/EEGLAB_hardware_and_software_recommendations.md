---
layout: default
title: Hard/software rec.
summary: EEGLAB hardware and software recommendations
parent: Other documents
---


# EEGLAB hardware and software recommendations


Open source spirit
------------------

EEGLAB is an open source software environment and is available free of
charge to any user.

However, EEGLAB requires that you purchase and install the commercial
[Matlab software environment](http://www.mathworks.com/store/). Matlab
version 2008b or later is required; We recommend using the latest
version of Matlab. Matlab and EEGLAB run under Linux/Unix, Mac OS X, or
Windows. Purchasing Matlab can be expensive, though the Matlab student
version is usually priced near $50 US.

We have attempted to remove all dependencies on add-on Matlab toolboxes.
Thus, no additional toolboxes are necessary to run the EEGLAB (10.2 or
higher) core distribution. However, some advanced plug-in toolboxes may
use functions from a specific Matlab toolbox: see their documentation
for details.

Note that all EEGLAB processing functions also can be run under the free
[Octave environment](http://www.gnu.org/software/octave/download.html)
which may be useful when performing batch processing on a large number
of datasets. However, Octave is about 50% slower than Matlab and its
graphic functions are not yet fully Matlab code compatible (see
[here](http://sccn.ucsd.edu/wiki/EEGLAB_and_Octave) for producing
figures under Octave).

Desirable hardware configurations for working with EEGLAB
---------------------------------------------------------

Below we outline hardware and software requirements for EEGLAB and
associated tools. Hardware requirements vary with the size of the
datasets you want to process. We have outlined two levels of hardware
needed for basic and advanced processing respectively. It is also
possible to process data on (some) less powerful platforms but in trying
to use them you may end up spending much of your time trying to avoid
"Out of Memory" errors. EEGLAB works on Windows, Linux, or Mac OS X. No
operating system is better.

**Minimum processing requirements (and/or highly desirable features)**
for processing up to, 32 EEG channels per subject using core EEGLAB
functions only:

-   4 Gb (or more) of RAM (random access memory)
-   At least 200 Gb of available hard drive space (SSD if possible)
-   Latest version of Matlab -- no additional Matlab toolboxes are
    required (but see below)

**Normal processing requirements (and/or highly desirable features)**
for processing 64 or more EEG channels and/or using the most recent
EEGLAB toolboxes:

-   Quad processors cores (4 or more ) are desirable
-   16 Gb or more of RAM (random access memory)
-   At least 1 Tb of SSD (SSD will speed up read/write by a factor of up
    to 5x) or mixed system (SSD 128Gb and large hard drive)
-   The Matlab signal processing, statistics, and optimization
    toolboxes, whose functions are used in some advanced plug-in
    toolboxes.

Notes
-----

-   Although EEGLAB is free, the Matlab software environment that it
    runs on is a commercial product of The Mathworks.



-   For Windows users: Avoid Windows XP which does not work well with
    Matlab because of memory issues.



-   For advanced Mac OSX users: Matlab cannot access what OSX calls
    'inactive memory'. To free it for use by Matlab, on a terminal
    window command line type

```matlab
       * % du -su /*
```
-   For advanced Windows users: It is possible on some platforms to
    start up Matlab with an alternate memory manager using the "–memmgr"
    option. Look
    [here](http://matlab.izmiran.ru/help/techdoc/ref/matlabwindows.html)
    for more information.



-   For Ubuntu linux users: There are often graphics problems when
    Matlab uses OpenGL graphics under Ubuntu. To avoid them, at the
    beginning of each Matlab session enter

``` matlab
       *>> set(0,'DefaultFigureRenderer','painter'); *
```

or

``` matlab
       * >> set(0,'DefaultFigureRenderer','z-buffer')*
``` 
-   For GPU users: EEGLAB functions do not use yet the capabilities of
    GPU (Graphic Processing Unit) boards, which currently have the
    highest performance/cost ratio. However, we have made first attempts
    at porting some functions to work with GPUs -- click
    [here](/GPU "wikilink") for more information.

Printing and editing EEGLAB figures
-----------------------------------

To edit pictures saved from Matlab figures so as to format them for
publication, we advise the following procedure:

-   Export the figure (*myfigure*) from Matlab as a postscript image
    (the *.epsc* format) by typing on the Matlab command line

``` matlab
       * >> print -depsc myfigure.eps*
       * >> print -dpdf -r300 myfigure.pdf`*

``` 

-   Edit the resulting postscript or PDF image file using an editor such
    as Adobe Illustrator.
-   If your vectorized image appears as an uneditable bitmap in the
    postscript editor, change the Matlab renderer to *painter* before
    saving the figure by typing on the Matlab commandline, before saving
    the figure,


``` matlab
        * >> set(gcf, 'renderer', 'painter') *

``` 

-   If you have images with transparent regions, export them using the
    Matlab
    [SVG](http://www.mathworks.com/matlabcentral/fileexchange/7401)
    export tool (PDF above will not work).
-   To ensure that the image you are seeing is the image that is being
    saved and printed, on the Matlab command line type


``` matlab
       *>>set(gcf, 'paperpositionmode', 'auto');*

``` 
-   To change the font of all elements in a figure, try

```matlab 
       * >> setfont(gcf,'fontsize',16);*

``` 
Unfortunately in some recent versions of Matlab, saving vectorized
version of figures has become difficult (artefacts in STUDY scalp
topographies). Let us know if you find better solutions.
