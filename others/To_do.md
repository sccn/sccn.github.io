---
layout: default
title: To do before wiki release
parent: Other documents
---

# To do list

- Look at all the plugins and update documentation link (in database) pointing to old wiki pages

- Plugin list

BINICA https://github.com/sccn/binica/wiki

- Add google tracking

- Make sure all pages have {: .no_toc }

- Revisit aspect ratio of GUIs on Windows and Mac

- search for wikilinks

- Correct section 5 to 8 with Grammarly

- Create git-annex repository for test cases

- Add readme to FIRFILT

- Replace

carthesian with cartesian

plugin by plug-in

*OK* by *Ok*

http with https

ressource with resource

bootstraping with bootstrapping

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
