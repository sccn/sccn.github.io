---
layout: default
title: To do before wiki release
parent: Other documents
---

# To do list

- Look at all the plugins and update documentation link (in database) pointing to old wiki pages

- Plugin list

BINICA https://github.com/sccn/binica/wiki

- Replace

plugin by plug-in

*OK* by *Ok*

http with https

ressource with resource

bootstraping with bootstrapping





Open-source model
------------------
EEGLAB is an open-source software environment and is available free of
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

