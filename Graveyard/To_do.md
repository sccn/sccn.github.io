---
layout: default
---
To do before wiki release
====

In progress

- Add google tracking

- EEGLAB: Revisit aspect ratio of GUIs on Windows and Mac

- Plugins: Update all github repositories

- Put Makoto ASR page on the clean_rawdata wiki

- Replace

Printing and editing EEGLAB figures
-----------------------------------

To edit pictures saved from MATLAB figures so as to format them for
publication, we advise the following procedure:

-   Export the figure (*myfigure*) from MATLAB as a postscript image
    (the *.epsc* format) by typing on the MATLAB command line

``` matlab
       * >> print -depsc myfigure.eps*
       * >> print -dpdf -r300 myfigure.pdf`*

``` 

-   Edit the resulting postscript or PDF image file using an editor such
    as Adobe Illustrator.
-   If your vectorized image appears as an uneditable bitmap in the
    postscript editor, change the MATLAB renderer to *painter* before
    saving the figure by typing on the MATLAB commandline, before saving
    the figure,


``` matlab
        * >> set(gcf, 'renderer', 'painter') *

``` 

-   If you have images with transparent regions, export them using the
    MATLAB
    [SVG](http://www.mathworks.com/matlabcentral/fileexchange/7401)
    export tool (PDF above will not work).
-   To ensure that the image you are seeing is the image that is being
    saved and printed, on the MATLAB command line type


``` matlab
       *>>set(gcf, 'paperpositionmode', 'auto');*

``` 
-   To change the font of all elements in a figure, try

```matlab 
       * >> setfont(gcf,'fontsize',16);*

``` 

Unfortunately in some recent versions of MATLAB, saving vectorized
version of figures has become difficult (artefacts in STUDY scalp
topographies). Let us know if you find better solutions.

