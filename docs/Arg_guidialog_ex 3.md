---
layout: default
title: Arg guidialog ex
permalink: /docs/Arg_guidialog_ex
parent: Docs
---

Create an input dialog that displays input fields for a Function and
Parameters.

**Parameters = arg_guidialog(Function, Options...)**

The Parameters that are passed to the function can be used to override
some of its defaults. The function must declare its arguments via
arg_define. In addition, only a Subset of the function's specified
arguments can be displayed.

# Input Arguments

**Function**

the function for which to display arguments

**Options...**

optional name-value pairs; possible names are:

  - 'Parameters' : cell array of parameters to the Function to override
    some of its defaults.

<!-- end list -->

  - 'Subset' : Cell array of argument names to which the dialog shall be
    restricted; these arguments may contain . notation to index into
    arg_sub and the selected branch(es) of
    arg_subswitch/arg_subtoggle specifiers. Empty cells show up in the
    dialog as empty rows.

<!-- end list -->

  - 'Title' : title of the dialog (by default: functionname())

# Output Arguments

**Parameters**

a struct that is a valid input to the Function.

<center>

Christian Kothe, Swartz Center for Computational Neuroscience, UCSD

</center>

<center>

2010-10-24

</center>

[Category:V.Plugin Authority.A.Argument
Declaration](/Category:V.Plugin_Authority.A.Argument_Declaration "wikilink")