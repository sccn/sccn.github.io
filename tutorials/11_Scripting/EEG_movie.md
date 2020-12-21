---
layout: default
title: EEG movies
parent: 11. Write scripts
grand_parent: Tutorials
---
Creating scalp topography animations
=========

The script used on this page is available at [make_eeg_movie.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=make_eeg_movie.m)

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

Using the eegmovie function to make 2-D scalp topography animations
------------------
A simple way to create scalp map animations is to use the (limited)EEGLAB function [eegmovie.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eegmovie.m) from the command line. For
instance, to make a movie of the latency range -100 ms to 600 ms, type:

```matlab
%% Simple 2-D movie
eeglab; close; % add path
eeglabp = fileparts(which('eeglab.m'));
EEG = pop_loadset(fullfile(eeglabp, 'sample_data', 'eeglab_data_epochs_ica.set'));

% Above, convert latencies in ms to data point indices
pnts1 = round(eeg_lat2point(-100/1000, 1, EEG.srate, [EEG.xmin EEG.xmax]));
pnts2 = round(eeg_lat2point( 600/1000, 1, EEG.srate, [EEG.xmin EEG.xmax]));
scalpERP = mean(EEG.data(:,pnts1:pnts2),3);

% Smooth data
for iChan = 1:size(scalpERP,1)
    scalpERP(iChan,:) = conv(scalpERP(iChan,:) ,ones(1,5)/5, 'same');
end

% 2-D movie
figure; [Movie,Colormap] = eegmovie(scalpERP, EEG.srate, EEG.chanlocs, 'framenum', 'off', 'vert', 0, 'startsec', -0.1, 'topoplotopt', {'numcontour' 0});
seemovie(Movie,-5,Colormap);

% save movie
vidObj = VideoWriter('erpmovie2d.mp4', 'MPEG-4');
open(vidObj);
writeVideo(vidObj, Movie);
close(vidObj);
```

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/A9HcbFtTWKc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>

Below, we use the same function to plot the ERP on a 3-D head plot.

Using the eegmovie function to make 3-D scalp topography animations
------------------

Run the script above first. The script below creates a 3-D head plot movie.

```matlab
%% Simple 3-D movie
% Use the graphic interface to coregister your head model with your electrode positions
headplotparams1 = { 'meshfile', 'mheadnew.mat'       , 'transform', [0.664455     -3.39403     -14.2521  -0.00241453     0.015519     -1.55584           11      10.1455           12] };
headplotparams2 = { 'meshfile', 'colin27headmesh.mat', 'transform', [0          -13            0          0.1            0        -1.57         11.7         12.5           12] };
headplotparams  = headplotparams1; % switch here between 1 and 2

% set up the spline file
headplot('setup', EEG.chanlocs, 'STUDY_headplot.spl', headplotparams{:}); close
 
% check scalp topo and head topo
figure; headplot(scalpERP(:,end-50), 'STUDY_headplot.spl', headplotparams{:}, 'maplimits', 'absmax', 'lighting', 'on');
figure; topoplot(scalpERP(:,end-50), EEG.chanlocs);
figure('color', 'w'); [Movie,Colormap] = eegmovie( scalpERP, EEG.srate, EEG.chanlocs, 'framenum', 'off', 'vert', 0, 'startsec', -0.1, 'mode', '3d', 'headplotopt', { headplotparams{:}, 'material', 'metal'}, 'camerapath', [-127 2 30 0]); 
seemovie(Movie,-5,Colormap);

% save movie
vidObj = VideoWriter('erpmovie3d1.mp4', 'MPEG-4');
open(vidObj);
writeVideo(vidObj, Movie);
close(vidObj);
```

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/rwo1ufsuQ6w" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>

In the script above, change the line "headplotparams  = headplotparams1;" to "headplotparams  = headplotparams2;" to switch between headmodels.

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/6iuGt7FzX30" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>

It is also possible to create frames for movies as shown in the next section.

Creating movie from frames
------------
Another solution here is assemble a series of images into a movie. For
example, type:

``` matlab
%% Using topoplot to make movie frames
vidObj = VideoWriter('erpmovietopoplot.mp4', 'MPEG-4');
open(vidObj);
counter = 0;
for latency = -100:10:600 %-100 ms to 1000 ms with 10 time steps
    figure; pop_topoplot(EEG,1,latency, 'My movie', [] ,'electrodes', 'off'); % plot'
    currFrame = getframe(gcf);
    writeVideo(vidObj,currFrame);
    close;  % close current figure
end
close(vidObj);
```
