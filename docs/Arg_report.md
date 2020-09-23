---
layout: default
title: Arg report
permalink: /docs/Arg_report
parent: Docs
---

Report information of a certain Type from the given Function.

**Result = arg_report(Type,Function,Arguments)**

# Input Arguments

**Type**

Type of information to report, can be one of the following:

  - 'rich' : Report a rich declaration of the function's arguments as a
    struct array, with fields as in arg_specifier.

<!-- end list -->

  - 'lean' : Report a lean declaration of the function's arguments as a
    struct array, with fields as in arg_specifier, like rich, but
    excluding the alternatives field.

<!-- end list -->

  - 'vals' : Report the values of the function's arguments as a struct,
    possibly with sub-structs.

<!-- end list -->

  - 'handle': Report function handles to scoped functions within the
    Function (i.e.,subfunctions). The named of those functions are
    listed as a cell string arrayin place of Arguments.

<!-- end list -->

  - 'properties': Report properties of the function, if any.

**Function**

a function handle to a function which defines some arguments (via
arg_define)

**Arguments**

cell array of parameters to be passed to the function; depending on the
function's implementation, this can affect the current value assignment
(or structure) of the parameters being returned If this is not a cell,
it is automatically wrapped inside one (note: to specify the first
positional argument as \[\] to the function, always pass it as {\[\]};
this is only relevant if the first argument's default is non-\[\]).

# Output Arguments

**Result**

the reported data.

# Notes

In all cases except 'properties', the Function must use arg_define() to
define its arguments.


Christian Kothe, Swartz Center for Computational Neuroscience, UCSD



2010-09-24


[Category:V.Plugin Authority.A.Argument
Declaration](/Category:V.Plugin_Authority.A.Argument_Declaration "wikilink")