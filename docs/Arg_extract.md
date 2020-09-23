---
layout: default
title: Arg extract
permalink: /docs/Arg_extract
parent: Docs
---

Extract arguments from Args; simple version, see notes.

**Value = arg_extract(Args,Names,Position,Default)**

# Input Arguments

**Args**

the varargin of the calling function

**Names**

name by which the argument is referenced, or a cell array of names

**Position**

the 1-based position of the argument, if it can be listed positionally,
or \[\]if not (default: \[\])

**Default**

optional default value, if the argument was not given

(can only be specified if position is \[\], see notes)

# Output Arguments

**Value**

The extracted value

# Notes

This version of arg_extract assumes that the argument of interest, if
it can be specified positionally, must be contained in Args (i.e.,
either by name, or by position). To enforce this, no Default can be
assigned if the listed Position is non-empty.

The second limitation is on the allowed values of all arguments in Args:
No struct-typed argument may contain any of the Names as a valid field
name, and no string-typed argument may allow any of the Names as its
value; otherwise, these fields may be accidentally picked out by
arg_extract.

# Examples

``` Matlab
% extract the ALLEEG argument (by name or position)
x = arg_extract(varargin,'ALLEEG',1) ;

% extract the sampling rate argument (by name, give an error if missing)
x = arg_extract(varargin,{'srate','SamplingRate'});

% extract the sampling rate argument (by name, and fall back to some default if missing)
x = arg_extract(varargin,{'srate','SamplingRate'},[],200);
```


Christian Kothe, Swartz Center for Computational Neuroscience, UCSD



2010-09-24


[Category:V.Plugin Authority.A.Argument
Declaration](/Category:V.Plugin_Authority.A.Argument_Declaration "wikilink")