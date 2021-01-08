---
layout: default
title: Sample dataset description
parent: Reference Topics
grand_parent: Tutorials
---
Sample experiment description <span style="color: green"> - Done</span>
===

In this experiment, there were two types of events "square" and "rt";
"square" events correspond to the appearance of a filled disk in a green
colored square in the display and "rt" to the subject's button press. 

The disk could be presented in any of the five squares on the screen, one
with a green outline and the others with a blue one, distributed along the horizontal
axis. Here we only considered presentation on the left, i.e. positions 1
and 2 as indicated by the *position* field (at about 5.5 degrees and 2.7
degrees of horizontal visual angle, respectively). 

In this experiment, the
subject covertly attended to a selected location on the computer screen
(the green square) and responded with a quick thumb button press only
when the disk was presented at this location. They were to ignore
circles presented at the unattended locations (the blue squares). 

To
reduce the amount of data required to download and process, this dataset
contains only targets (i.e., "square") stimuli presented at the two
left-visual-field attended locations for a single subject. For more
details about the experiment, see [this paper](http://sccn.ucsd.edu/science2002.html).

When using events in an EEGLAB dataset, there are two required event
fields: *type* and *latency*, plus any number of additional user-defined
information fields. It is important to understand here that the names of
the fields were defined by the user creating the dataset, and that it is
possible to create, save, and load as many event fields as desired.

Note also that *type* and *latency* (lowercase) are two keywords
explicitly recognized by EEGLAB and that these fields *must* be defined
by the user unless importing epoch event information (Note: If only
field *latency* is defined, then EEGLAB will create field *type* with a
constant default value of 1 for each event). Unless these two fields are
defined, EEGLAB cannot handle events appropriately to
extract epochs, plot reaction times, etc.
