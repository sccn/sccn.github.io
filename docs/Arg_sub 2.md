---
layout: default
title: Arg sub
permalink: /docs/Arg_sub
parent: Docs
---

Specify an argument of a function which is a structure of sub-arguments.

**Spec = arg_sub(Names,Defaults,Source,Help,Options...)**

Delivered to the function as a struct, and visible in the GUI as a an
expandable sub-list of arguments. A function may have an argument which
itself consists of several arguments. For example, a function may be
passing the contents of this struct as arguments to another function, or
may just collect several arguments into sub-fields of a single struct.
Differs from the default arg() function by allowing, instead of the
Range, either a Source function which exposes a list of arguments
(itself using arg_define), or a cell array with argument
specifications, identical in format to the Specification part of an
arg_define() clause.

# Input Arguments

**Names**

The name(s) of the argument. At least one must be specified, and if
multiple are specified, they must be passed in a cell array.

  - The first name specified is the argument's "code" name, as it should
    appear in the function's code (= the name under which arg_define()
    returns it to the function).

<!-- end list -->

  - The second name, if specified, is the "Human-readable" name, which
    is exposed in the GUIs (otherwise the code name is displayed).

<!-- end list -->

  - Further specified names are alternative names for the argument
    (e.g., for backwards compatibility with older function
    syntaxes/parameter names).

**Defaults**

A cell array of arguments to override defaults for the Source; all
syntax accepted by the Source is allowed here, whereas in the case of
positional arguments, the leading arg_norep() arguments of the source
are implicitly skipped. If empty, the defaults of the Source are
unaffected.

**Source**

A source of argument specifications, usually a function handle
(referring to a function which defines arguments via arg_define()).

  - For convenience, a cell array with a list of argument declarations,
    formatted like the Specification part of an arg_define() clause can
    be given, instead. In this case, the effect is the same as
    specifying @some_function, for a function implemented as:
      - function some_function(varargin)
        arg_define(Format,varargin,Source{:});

**Help**

The help text for this argument (displayed inside GUIs), optional.
(default: \[\]).

  - (Developers: Please do \*not\* omit this, as it is the key bridge
    between ease of use and advanced functionality.)

<!-- end list -->

  - The first sentence should be the executive summary (max. 60 chars),
    any further sentences are a detailed explanation (examples, units,
    considerations). The end of the first sentence is indicated by a '.
    ' followed by a capital letter (beginning of the next sentence). If
    ambiguous, the help can also be specified as a cell array of 2
    cells.

**Options...**

Optional name-value pairs to denote additional properties:

  - 'cat' : The human-readable category of this argument, helpful to
    present a list of many parameters in a categorized list, and to
    separate "Core Parameters" from "Miscellaneous" arguments.
      - Developers: When choosing names, every bit of consistency with
        other function in the toolbox helps the uses find their way
        (default: \[\]).

<!-- end list -->

  - 'fmt': Optional format specification for the Source (if it is a cell
    array)
      - (default: \[\]). See arg_define() for a detailed explanation.

<!-- end list -->

  - 'merge': Whether a value (cell array of arguments) assigned to this
    argument should completely replace all arguments of the default, or
    whether instead the two cell arrays should be concatenated
    ('merged'), so that defaults are only selectively overridden.
      - Note that for concatenation to make sense, the cell array of
        Defaults cannot be some subset of all allowed positional
        arguments, but must instead either be the full set of positional
        arguments (and possibly some NVPs) or be specified as NVPs in
        the first place.

# Output Arguments

**Spec**

A cell array, that, when called as spec{1}(reptype,spec{2}{:}), yields a
specification of the argument, for use by arg_define.

  - Technical note: Upon assignment with a value (via the assigner
    field), the 'children' field of the specifier struct is populated
    according to how the Source parses the value into arguments.

# Notes

for MATLAB versions older than 2008a, type and shape checking is not
necessarily enforced.

<center>

Christian Kothe, Swartz Center for Computational Neuroscience, UCSD

</center>

<center>

2010-09-24

</center>

[Category:V.Plugin Authority.A.Argument
Declaration](/Category:V.Plugin_Authority.A.Argument_Declaration "wikilink")