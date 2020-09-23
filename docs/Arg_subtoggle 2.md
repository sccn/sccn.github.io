---
layout: default
title: Arg subtoggle
permalink: /docs/Arg_subtoggle
parent: Docs
---

Specify an argument of a function which is a struct of sub-arguments
that can be disabled.

**Spec = arg_subtoggle(Names,Default,Source,Help,Options...)**

Accessible to the function as a struct, and visible in the GUI as a an
expandable sub-list of arguments (with a checkbox to toggle). The
special field 'arg_selection' (true/false) indicates whether the
argument is enabled or not. The value assigned to the argument
determines whether it is turned on or off, as determined by the mapper
option.

# Input Arguments

**Names**

The name(s) of the argument. At least one must be specified, and if
multiple are

specified, they must be passed in a cell array.

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
syntax accepted by the (selected) Source is allowed here, whereas in the
case of positional arguments, the leading arg_norep() arguments of the
source are implicitly skipped. Note: Whether the argument is turned on
or off is determined via the 'mapper' option. By default, \[\] and 'off'
are mapped to off, whereas {}, non-empty cell arrays and structs are
mapped to on.

**Source**

A source of argument specifications, usually a function handle
(referring to a function which defines arguments via arg_define()).

For convenience, a cell array with a list of argument declarations,
formatted like theSpecification part of an arg_define() clause can be
given, instead. In this case, the effect is the same as specifying
@some_function, for a function implemented as:

function some_function(varargin)
arg_define(Format,varargin,Source{:});

**Help**

The help text for this argument (displayed inside GUIs), optional.
(default: \[\]).

(Developers: Please do \*not\* omit this, as it is the key bridge
between ease of use and advanced functionality.)

The first sentence should be the executive summary (max. 60 chars), any
further sentences are a detailed explanation (examples, units,
considerations). The end of the first sentence is indicated by a '. '
followed by a capital letter (beginning of the next sentence). If
ambiguous, the help can also be specified as a cell array of 2 cells.

**Options...**

Optional name-value pairs to denote additional properties:

  - 'cat' : The human-readable category of this argument, helpful to
    present a list of many parameters in a categorized list, and to
    separate "Core Parameters" from "Miscellaneous" arguments.
    Developers: When choosing names, every bit of consistency with other
    function in the toolbox helps the uses find their way (default:
    \[\]).

<!-- end list -->

  - 'fmt' : Optional format specification for the Source (if it is a
    cell array)
      - (default: \[\]). See arg_define() for a detailed explanation.

<!-- end list -->

  - 'mapper' : A function that maps the argument list (e.g., Defaults)
    to a value in the domain of selectors, and a potentially updated
    argument list. The mapper is applied to the argument list prior to
    any parsing (i.e. it faces the raw argument list) to determine the
    current selection, and its its second output (the potentially
    updated argument list) is forwarded to the Source that was selected,
    for further parsing.
      - The default mapper maps \[\] and 'off' to off, whereas 'on',
        empty ornon-empty cell arrays and structs are mapped to on.

<!-- end list -->

  - 'merge': Whether a value (cell array of arguments) assigned to this
    argument should completely replace all arguments of the default, or
    whether itshould instead the two cell arrays should be concatenated
    ('merged'), so that defaults are only selectively overridden. Note
    that for concatenation to make sense, the cell array of Defaults
    cannot be some subset of all allowed positional arguments, but must
    instead either be the full set of positional arguments (and possibly
    some NVPs) or bespecified as NVPs in the first place.

# Output Arguments

**Spec**

A cell array, that, when called as spec{1}(reptype,spec{2}{:}), yields a
specification of the argument, for use by arg_define. Technical note:
Upon assignment with a value (via the assigner field), the 'children'
field of the specifier struct is populated according to how the selected
(by the mapper) Source parses the value into arguments. The additional
struct field 'arg_selection' is introduced at this point.

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