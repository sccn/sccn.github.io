---
layout: default
title: Arg define
permalink: /docs/Arg_define
parent: Docs
---

Declare function arguments with optional defaults and built-in GUI
support.

'''Struct = arg_define(Values, Specification...)Struct =
arg_define(Format, Values, Specification...) '''

This is essentially a in improved replacement for the parameter
declaration line of a function. Assigns Values (a cell array of values,
typically the "varargin" of the calling function, henceforth named the
"Function") to fields in the output Struct, with parsing implemented
according to a Specification of argument names and their order
(optionally with a custom argument Format description).

By default, values can be a list of a fixed number of positional
arguments (i.e., the typical MATLAB calling format), optionally followed
by a list of name-value pairs (NVPs, e.g., as the format accepted by
figure()), in which, furthermore, instead of any given NVP, a struct may
b epassed as well (thus, one may pass a mix of
'name',value,struct,'name',value,'name',value, ...parameters).
Alternatively, by default the entire list of positional arguments can
instead be be specified as a list of NVPs/structs. Only names that are
allowed by the Specification may be used, if positional syntax is
allowed by the Format (which is the default).

The special feature over hlp_varargin2struct()-like functionality is
that arguments defined via arg_define can be reported to the framework
(if triggered by arg_report()). The resulting specification can be
rendered in a GUI or be processed otherwise.

# Input Arguments

**Format**

Optional format description (default: \[0 Inf\]):

  - If this is a function handle, the function is used to transform the
    Values prior to any other processing into a new Values cell array.
    The function may specify a new (numeric) Format as its second output
    argument (if not specified, this is 0).

<!-- end list -->

  - If this is a number (say, k), it indicates that the first k
    arguments are specified in a positional manner, and the following
    arguments are specified as list of name-value pairs and/or structs.

<!-- end list -->

  - If this is a vector of two numbers \[0 k\], it indicates that the
    first k arguments MAY be specified in a positional manner (the
    following arguments must be be specified as NVPs/structs) OR
    alternatively, all arguments can be specified as NVPs / structs.
    Only names that are listed in the specification may be used as names
    (in NVPs and structs) in this case.

**Values**

A cell array of values passed to the function (usually the calling
function's "varargin"). Interpreted according to the Format and the
Specification.

**Specification...**

The specification of the calling function's arguments; this is a
sequence of arg(), arg_norep(), arg_nogui(), arg_sub(),
arg_subswitch(), arg_subtoggle() specifiers. The special keyword
mandatory can be used in the declaration of default values, which
declares that this argument must be assigned some value via Values
(otherwise, an error is raised before the arg is passed to the
Function).

# Output Arguments

**Struct**

A struct with values assigned to fields, according to the Specification
and Format. If this is not captured by the Function in a variable, the
contents of Struct are instead assigned to the Function's workspace
(default practice).

# See also

arg(), arg_nogui(), arg_norep(), arg_splice(), arg_sub(),
arg_subswitch(), arg_subtoggle()

# Notes

1\) If the Struct output argument is omitted by the user, the arguments
are not returned as a struct but instead directly copied into the
Function's workspace.

2\) Someone may call the user's Function with the request to deliver the
parameter specification, instead of following the normal execution flow.
arg_define() automatically handles this task, except if the user lists
a special argument named 'report_args' is in the Arg-Specification. In
this case, it is the user's task to check whether the field is
non-empty, and if so, terminate the normal execution flow to return
report_args as the Function output. The Function may perform additional
computations in between, as long as a timely delivery of the Struct
remains ensured.

3\) If a struct with a field named 'arg_direct' (set to true) is
passed, all type checking, specification parsing, fallback to default
values and reporting functionality are skipped. This is essentially a
fast path to call a function when all the defaults have previously been
obtained from it via arg_report.

<center>

Christian Kothe, Swartz Center for Computational Neuroscience, UCSD

</center>

<center>

2010-09-24

</center>

[Category:V.Plugin Authority.A.Argument
Declaration](/Category:V.Plugin_Authority.A.Argument_Declaration "wikilink")