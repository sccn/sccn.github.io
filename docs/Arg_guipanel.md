---
layout: default
title: Arg guipanel
permalink: /docs/Arg_guipanel
parent: Docs
---

Create a uipanel that displays an argument property inspector for a
Function.

'''Handle = arg_guipanel(Options ...)Handle = arg_guipanel(Parent,
Options ...) '''

The handle supports the method .GetPropertySpecification(), by means of
which the edited argument specification can be retrieved. This result
can be turned into a valid Function argument using arg_tovals().
Additional Parameters may be passed to the Function, in order to
override some of its defaults.

# Input Arguments

**Parent**

optional parent widget

**Options**

name-value pairs; possible names are:

  - 'Function' : the function for which to display arguments

<!-- end list -->

  - 'Parameters' : cell array of parameters to the function

<!-- end list -->

  - 'Position' : position of the panel within the parent widget

# Output Arguments

**Handle**

handle to the panel; supports .GetPropertySpecification() to obain the
edited specification


Christian Kothe, Swartz Center for Computational Neuroscience, UCSD



2010-10-24


[Category:V.Plugin Authority.A.Argument
Declaration](/Category:V.Plugin_Authority.A.Argument_Declaration "wikilink")