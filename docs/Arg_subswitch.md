---
layout: default
title: Arg subswitch
permalink: /docs/Arg_subswitch
parent: Docs
---

Specify a function argument that can be one of several alternative
structs.

**Spec = arg_subswitch(Names,Defaults,Alternatives,Help,Options...)**

The correct struct is chosen according to a selection rule (the mapper).
Accessible to the function as a struct, and visible in the GUI as an
expandable sub-list of arguments (with a drop-down list of alternative
options). The chosen option (usually one out of a set of strings) is
delivered to the Function as the special struct field 'arg_selection'.

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
syntax accepted by the (selected) Source is allowed here, whereas in the
case of positional arguments, the leading arg_norep() arguments of the
source are implicitly skipped.

  - Note: Which one out of the several alternatives should be selected
    is determined via the 'mapper' option. By default, it maps the first
    argument to the Selector, and passes the rest to the matching
    Source.

**Alternatives**

Definition of the switchable option groups. This is a cell array of the
form: { {'selector', Source}, {'selector', Source}, {'selector',
Source}, ...} Each Source is either a function handle (referring to a
function that exposes arguments via an arg_define() clause), or an
in-line cell array of argument specifications, as further explained in
the help of arg_sub(). In the latter case (Source is a cell array), the
option group may also be a 3-element cell array of the form
{'selector',Source,Format} ... where Format is a format specifier as
explained in arg_define().

**Help**

The help text for this argument (displayed inside GUIs), optional.
(default: \[\]).

  - (Developers: Please do \*not\* omit this, as it is the key bridge
    between ease of use and advanced functionality.)
  - The first sentence should be the executive summary (max. 60 chars),
    any further sentencesare a detailed explanation (examples, units,
    considerations). The end of the firstsentence is indicated by a '. '
    followed by a capital letter (beginning of the nextsentence). If
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

  - 'mapper' : A function that maps the value (cell array of arguments
    like Defaults) to a value in the domain of selectors, and a
    potentially updated argument list. The mapper is applied to the
    argument list prior to any parsing (i.e. it faces the raw argument
    list) to determine the current selection, and its second output (the
    potentially updated argument list) is forwarded to the Source that
    was selected, for further parsing.
      - The default mapper takes the first argument in the argument list
        as the Selector and passes the remaining list entries to the
        Source. If there is only a single argument that is a struct with
        a field'arg_selection', this field's value is taken as the
        Selector, and the struct is passed as-is to the Source.

<!-- end list -->

  - 'merge': Whether a value (cell array of arguments) assigned to this
    argument should completely replace all arguments of the default, or
    whether it should instead the two cell arrays should be concatenated
    ('merged'), so that defaults are only selectively overridden. Note
    that for concatenation to make sense, the cell array of Defaults
    cannot be some subset of all allowed positional arguments, but must
    instead either be the full set of positional arguments (and possibly
    some NVPs) or be specified as NVPs in the first place.

# Output Arguments

**Spec**

A cell array, that, when called as spec{1}(reptype,spec{2}{:}), yields a
specification of the argument, for use by arg_define. Technical note:
Upon assignment with a value (via the assigner field), the 'children'
field of the specifier struct is populated according to how the selected
(by the mapper) Source (from Alternatives) parses the value into
arguments. The additional struct field 'arg_selection ' is introduced
at this point.

# Notes

for MATLAB versions older than 2008a, type and shape checking is not
necessarily enforced.


Christian Kothe, Swartz Center for Computational Neuroscience, UCSD



2010-09-24


[Category:V.Plugin Authority.A.Argument
Declaration](/Category:V.Plugin_Authority.A.Argument_Declaration "wikilink")