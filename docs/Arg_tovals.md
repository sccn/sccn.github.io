---
layout: default
title: Arg tovals
permalink: /docs/Arg_tovals
parent: Docs
---

Convert a 'rich' argument report into a 'vals' report.

**Vals = arg_tovals(Rich)**

# Input Arguments

**Rich**

a 'rich' argument report, as obtained via
arg_report('rich',some_function)

**Direct**

whether to endow the result with an 'arg_direct' flag set to true,
which indicates to the function taking the Vals struct that the contents
of the struct directly correspond to workspace variables of the
function. If enabled, contents of Vals must be changed with care - for
example, removing/renaming fields will likely lead to errors in the
function. (default: true)

# Output Arguments

**Vals**

a 'vals' argument report, as obtained via
arg_report('vals',some_function) this data structure can be used as a
valid argument to some_function.


Christian Kothe, Swartz Center for Computational Neuroscience, UCSD



2010-10-18


[Category:V.Plugin Authority.A.Argument
Declaration](/Category:V.Plugin_Authority.A.Argument_Declaration "wikilink")