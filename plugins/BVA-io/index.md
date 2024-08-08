---
layout: default
title: BVA-io
long_title: BVA-io
parent: Plugins
render_with_liquid: false
nav_order: 28
---
To view the plugin source code, please visit the plugin's [GitHub repository](https://github.com/sccn/bva-io).

# BVA-io for Brain Vision Analyzer format

This repository is a plugin for EEGLAB to import/export
Brain Vision Analyzer EEG data files.

# Version history
v1.73 - Writing data now in MULTIPLEXED format as a new option; show warning when VMRK file is missing

v1.72 - Avoid crashing when event file is absent

v1.71 - Allow to import .ahdr files

v1.7 - Better handling of VMRK and EEG file non-consistant witht the header VHDR file; allow empty marker info section; allow importing truncated binary file
