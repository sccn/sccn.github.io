---
layout: default
title: Arg toworkspace
permalink: /docs/Arg_toworkspace
parent: Docs
---

Copy the arguments in the given Struct into the workspace of the calling
function.

**arg_toworkspace(Struct,Yield)**

# Input Arguments

**Struct**

an argument structure, as produced by arg_define

**Yield**

When true, this function reports ("yields") the field 'report_args' to
the framework, given that it is non-empty.

# Implementation Note

The Yield functionality is implemented by means of an exception that is
recognized by arg_report().

<center>

Christian Kothe, Swartz Center for Computational Neuroscience, UCSD

</center>

<center>

2010-09-24

</center>

[Category:V.Plugin Authority.A.Argument
Declaration](/Category:V.Plugin_Authority.A.Argument_Declaration "wikilink")