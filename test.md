---
layout: default
nav_exclude: true
---
{%- assign cmd = "eeglabp = fileparts(which('eeglab.m')); open(fullfile(eeglabp, 'tutorial_scripts', 'LiveScripts', 'dipfit_source_reconstruction.mlx'));" -%}
{% include modal.html command=cmd %}
