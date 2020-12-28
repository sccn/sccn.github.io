---
layout: default
title: Mex files in EEGLAB
parent: Other documents
---

# Mex files errors and EEGLAB


If you get an error "could not locate mex file" or any related mex file
error, do not blame EEGLAB. EEGLAB itself does not include any
precompiled functions (also called mex functions). However, some
external modules uses mex files for reading binary data file or
performing source localization. Usually, an error indicates the
precompiled file is not available for your platform (it would thus need
to be recompiled, something you can sometimes do yourself - for more
information see below). There are 4 modules in EEGLAB that use mex
files.

-   Fieldtrip functions: If you get an error that some functions in the
    fieldtrip folder cannot be found, refer to the [fieldtrip
    documentation](http://fieldtrip.fcdonders.nl/faq/matlab_complains_about_a_missing_or_invalid_mex_file_what_should_i_do)
    for how to recompile such functions.



-   BIOSIG: some release of BIOSIG contains some updated mex files so
    you might want to check if you have the latest version of BIOSIG.
    Sometimes BIOSIG does not preserve backward compatibility so you may
    experience problem when reading data after updating BIOSIG.



-   ANT plugin: the ANT plugin was made by the ANT company. Contact
    [Maarten](mailto:mvelde@ant-neuro.com) for an updated version of the
    compiled binaries.



-   ERPSS plugin: simply recompile decompresserpss.c (type "mex
    decompresserpss.c")

[Category:EEGLAB](/Category:EEGLAB "wikilink") { {EEGLAB Home} }