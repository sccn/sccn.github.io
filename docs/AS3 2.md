---
layout: default
title: AS3
permalink: /docs/AS3
parent: Docs
---

[category:arno](/category:arno "wikilink")

This page contains some hints for writing AS3 Flash code.

AS3 code may be attached to scenes or frames, or may be independent of
frames. Advanced programmers advise not to program in frames.

AS3 code may be edited in Flash or in Flex (Eclipse like).

If programming in Frames and still want to declare class or share
variables between frames:

  - Create a DocumentClass.as document in a folder named for example
    "scripts"
  - Add this script to the "Class" field of the document (Document
    properties)
  - You will have to import all packages used in your document (this is
    no longer done automatically)
  - You will also have to click the properties in the AS3 settings so
    that all objects are automatically declared (go to Publish Settings,
    click on the Flash tab then the AS3 button, then the checkbox
    "Automatically Declare Stage Instances")
  - I guess each Frame/Scene is now like a separate class
  - Note that new variable for the parent class (DocumentClass) may be
    created dynamically (example DocumentClass.mynewvar = 0). This
    automatically creates a static variable accessible from all scenes.