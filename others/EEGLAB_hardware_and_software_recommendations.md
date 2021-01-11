---
layout: default
title: Hard/software requirements
summary: EEGLAB hardware and software recommendations
parent: Download EEGLAB
---
EEGLAB hardware and software requirements <span style="color: green"> - Done</span>
====

Desirable hardware configurations for working with EEGLAB
---------------------------------------------------------

Below we outline hardware and software requirements for EEGLAB and
associated tools. Hardware requirements vary with the size of the
datasets you want to process. We have outlined two levels of hardware
needed for basic and advanced processing, respectively. It is also
possible to process data on (some) less powerful platforms, but in trying
to use them, you may end up spending much of your time trying to avoid
"Out of Memory" errors. EEGLAB works on Windows, Linux, or Mac OS X. No
operating system is better.

**Minimum processing requirements (and/or highly desirable features)**
for processing up to 32 EEG channels per subject using core EEGLAB
functions only:

-   8Gb of RAM (random access memory)
-   At least 200 Gb of available hard drive space (SSD if possible)
-   Newest version of MATLAB -- no additional MATLAB toolboxes are
    required (but see below)

**Normal processing requirements (and/or highly desirable features)**
for processing 64 or more EEG channels and/or using the most recent
EEGLAB toolboxes:

-   Quad processors cores (4 or more are desirable) 
-   16 Gb or more of RAM (random access memory)
-   At least 1 Tb of SSD (SSD will speed up read/write by a factor of up
    to 5x) or mixed system (SSD 128Gb and large hard drive)
-   Newest version of MATLAB and the MATLAB signal processing, statistics, and optimization
    toolboxes, whose functions are used in some advanced EEGLAB plugins.

Notes
-----

-   Although EEGLAB is free, the MATLAB software environment that it
    runs on is a commercial product of The Mathworks. Often, your school might have negotiated access ([check here](https://www.mathworks.com/academia/tah-support-program/eligibility.html)). EEGLAB also works on the free Octave environment (command-line only), and you may also download a compiled version of EEGLAB that does not require a MATLAB license. 
    
-   For Ubuntu linux users: There are often graphics problems when
    MATLAB uses OpenGL graphics under Ubuntu. To avoid them, at the
    beginning of each MATLAB session enter

    ``` matlab
    >> set(0,'DefaultFigureRenderer','painters');
    ```

-   For GPU users: EEGLAB functions do not currently use GPUs' capabilities (Graphic Processing Unit), which currently have the
    highest performance/cost ratio. However, we have made the first attempts
    at porting some functions to work with GPUs -- click
    [here](/others/EEGLAB_and_high_performance_computing.html#running-eeglab-on-gpus-graphic-processing-units) for more information.
