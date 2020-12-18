---
layout: default
title: EEGLAB Menu Functions
parent: Other documents
---

In EEGLAB, all menu items call stand-alone functions. The correspondence
is indicated below. *Note that this part of the documentation is not
totally up to date. Some recently added menus might be missing.*

#### File


**Import data**


From ASCII/float file or Matlab array --
[pop_importdata()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_importdata.m)

From continuous or seg. EGI .RAW file --
[pop_readegi()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_readegi.m)

From Multiple seg. EGI .RAW files --
[pop_readsegegi()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_readsegegi.m)

From BCI2000 ASCII file -- pop_loadbci()

From Snapmaster .SMA file --
[pop_snapread()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_snapread.m)

From Neuroscan .CNT file --
[pop_loadcnt()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_loadcnt.m)

From Neuroscan .EEG file --
[pop_loadeeg()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_loadeeg.m)

From Biosemi .BDF file --
[pop_biosig()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_biosig.m)

From .EDF file --
[pop_biosig()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_biosig.m)

From ANT EEProbe .CNT file -- pop_loadeep()

From ANT EEProbe .AVR file -- pop_loadeep_avg()

From .BDF file (backup function) -- pop_readbdf()

From Brain Vis. Rec. .VHDR file -- pop_loadbv.m

From Brain Vis. Anal. Matlab file -- pop_loadbva()

From CTF Folder (MEG) -- 'ctf_folder'

From ERPSS .RAW or .RDF file -- pop_read_erpss()

From INStep .ASC file -- pop_loadascinstep()

From 4D .M4D pdf file -- pop_read4d()

From other formats using FILEIO --
[pop_fileio()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_fileio.m)

From other formats using BIOSIG --
[pop_biosig()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_biosig.m)

From Matlab array or ASCII file --
[pop_importepoch()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_importepoch.m)

From Neuroscan .DAT file --
[pop_loaddat()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_loaddat.m)

<!-- -->


**Import event info**


From Matlab array or ASCII file --
[pop_importevent()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_importevent.m)

From data channel --
[pop_chanevent()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_chanevent.m)

From Presentation .LOG file --
[pop_importpres()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_importpres.m)

From Neuroscan .EV2 file --
[pop_importev2()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_importev2.m)

'''Export '''


Data and ICA to text file --
[pop_export()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_export.m)

Weight matrix to text file --
[pop_expica()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_expica.m)

Inverse weight matrix to text file --
[pop_expica()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_expica.m)

Data to EDF/BDF/GDF file --
[pop_writeeeg()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_writeeeg.m)

Write Brain Vis. exchange format file -- --

Load existing dataset --
[pop_loadset()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_loadset.m)

Save current dataset --
[pop_saveset()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_saveset.m)

Save datasets --
[pop_saveset()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_saveset.m)

Clear dataset(s) --
[pop_delset()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_delset.m)

'''Create Study '''


Using all loaded datasets --
[pop_study()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_study.m)

Browse for datasets --
[pop_study()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_study.m)

Load existing study --
[pop_loadstudy()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_loadstudy.m)

Save current study --
[pop_savestudy()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_savestudy.m)

Save current study as --
[pop_savestudy()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_savestudy.m)

Clear study --
[pop_delset()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_delset.m)

Maximize memory --
[pop_editoption()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_editoptions.m)

**History Scripts**


Save dataset history script --
[pop_saveh()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_saveh.m)

Save session history script --
[pop_saveh()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_saveh.m)

Run Script -- -- --

Quit

#### Edit


Dataset info --
[pop_editset()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_editset.m)

Event fields --
[pop_editeventfield()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_editeventfield.m)

Event values --
[pop_editeventvals()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_editeventvals.m)

About this dataset --
[pop_comments()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_comments.m)

Channel locations --
[pop_chanedit()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_chanedit.m)

Select data --
[pop_select()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_select.m)

Select data using events --
[pop_rmdat()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_rmdat.m)

Select epochs or events --
[pop_selectevent()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_selectevent.m)

Copy current dataset --
[pop_copyset()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_copyset.m)

Append datasets --
[pop_mergeset()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_mergeset.m)

Delete dataset(s) --
[pop_delset()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_delset.m)

#### Tools


Change sampling rate --
[pop_resample()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_resample.m)

*' Filter the data*'


Basic FIR filter --
[pop_eegfilt()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_eegfilt.m)

Short IIR filter --
[pop_iirfilt()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_iirfilt.m)

Re-referencing --
[pop_reref()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_reref.m)

Interpolate electrodes -- --

Reject continuous data by eye --
[pop_eegplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_eegplot.m)

Extract epochs --
[pop_epoch()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_epoch.m)

Remove baseline --
[pop_rmbase()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_rmbase.m)

Run ICA --
[pop_runica()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_runica.m)

Remove components --
[pop_subcomp()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_subcomp.m)

Automatic channel rejection --
[pop_rejchan()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_rejchan.m)

Automatic epoch rejection --
[pop_autorej()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_autorej.m)

*' Reject data epochs*'


Reject data (all methods) --
[pop_rejmenu()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_rejmenu.m)

Reject by inspection --
[pop_eegplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_eegplot.m)

Reject extreme values --
[pop_eegthresh()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_eegthresh.m)

Reject by linear trend/variance --
[pop_rejtrend()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_rejtrend.m)

Reject by probability --
[pop_jointprob()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_jointprob.m)

Reject by kurtosis --
[pop_rejkurt()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_rejkurt.m)

Reject by spectra --
[pop_rejspec()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_rejspec.m)

Reject marked epochs --
[pop_rejepoch()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_rejepoch.m)

*' Reject using ICA*'


Reject components by map --
[pop_selectcomps()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_selectcomps.m)

Reject data (all methods) --
[pop_rejmenu()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_rejmenu.m)

Reject by inspection --
[pop_eegplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_eegplot.m)

Reject extreme values --
[pop_eegthresh()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_eegthresh.m)

Reject by linear trend/variance --
[pop_rejtrend()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_rejtrend.m)

Reject by probability --
[pop_jointprob()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_jointprob.m)

Reject by kurtosis --
[pop_rejkurt()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_rejkurt.m)

Reject by spectra --
[pop_rejspec()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_rejspec.m)

Reject marked epochs --
[pop_rejepoch()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_rejepoch.m)

Run ICA

*' Locate dipoles using DIPFIT 2.x*'


Head model and settings --
[pop_dipfit_settings()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_settings.m)

Coarse fit (grid scan) -- -- --

Fine fit (iterative) --
[pop_dipfit_nonlinear()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_nonlinear.m)

Autofit (coarse fit, fine fit & plot) -- -- --

Plot component dipoles -- -- --

#### Plot


*' Channel locations*'


By name --
[topoplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=topoplot.m)

By number --
[topoplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=topoplot.m)

Channel data (scroll) --
[pop_eegplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_eegplot.m)

Channel spectra and maps --
[pop_spectopo()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_spectopo.m)

Channel properties --
[pop_prop()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_prop.m)

Channel ERP image --
[pop_erpimage()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_erpimage.m)

*' Channel ERPs*'


With scalp maps --
[pop_timtopo()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_timtopo.m)

In scalp array --
[pop_plottopo()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_plottopo.m)

In rect. array --
[pop_plotdata()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_plotdata.m)

*' ERP maps*'


As 2-D scalp maps --
[pop_topoplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_topoplot.m)

As 3-D head plots --
[pop_headplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_headplot.m)

Sum/Compare ERPs --
[pop_comperp()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_comperp.m)

Component activations (scroll) --
[pop_eegplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_eegplot.m)

Component spectra and maps --
[pop_spectopo()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_spectopo.m)

*' Component maps*'


As 2-D scalp maps --
[pop_topoplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_topoplot.m)

As 3-D head plots --
[pop_headplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_headplot.m)

Component properties --
[pop_prop()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_prop.m)

Component ERP image --
[pop_erpimage()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_erpimage.m)

*' Component ERPs*'


With component maps --
[pop_envtopo()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_envtopo.m)

With comp. maps (compare) --
[pop_envtopo()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_envtopo.m)

In rectangular array --
[pop_plotdata()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_plotdata.m)

Sum/Compare comp. ERPs --
[pop_comperp()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_comperp.m)

*' Data statistics*'


Channel statistics --
[pop_signalstat()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_signalstat.m)

Component statistics --
[pop_signalstat()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_signalstat.m)

Event statistics --
[pop_eventstat()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_eventstat.m)

*' Time-frequency transforms*'


Channel time-frequency --
[pop_timef()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_timef.m)

Channel cross-coherence --
[pop_crossf()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_crossf.m)

Component time-frequency --
[pop_timef()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_timef.m)

Component cross-coherence --
[pop_crossf()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_crossf.m)

#### Study


Edit study info --
[pop_study()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_study.m)

Precompute channel measures --
[pop_precomp()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_precomp.m)

Plot channel measures --
[pop_chanplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_chanplot.m)

Precompute component measures --
[pop_precomp()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_precomp.m)

Build preclustering array --
[pop_preclust()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_preclust.m)

Cluster components --
[pop_clust()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_clust.m)

Edit/plot clusters --
[pop_clustedit()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_clustedit.m)

#### Datasets


Current/Active Datasets (listed as selectable items) -- -- --

Select multiple datasets -- -- --

Select the study set -- -- --

#### Help


About EEGLAB --
[eeglab()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeglab.m)

About EEGLAB Help --
[eeg_helphelp()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_helphelp.m)

EEGLAB menus --
[eeg_helpmenu()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_helpmenu.m)

*' EEGLAB functions*'


Toolbox functions -- -- --

Signal processing functions --
[eeg_helpsigproc()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_helpsigproc.m)

Interactive pop_functions --
[eeg_helppop()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_helppop.m)

*' EEGLAB advanced*'


Dataset structure --
[eeg_checkset()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_checkset.m)

Admin functions --
[eeg_helpadmin()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_helpadmin.m)

Web tutorial -- -- --

Email EEGLAB -- -- --

<div align=right>

Return to [EEGLAB Wiki](/EEGLAB "wikilink")
Return to [SCCN Wiki Home](/Main_Page "wikilink")

</div>

[Category:EEGLAB](/Category:EEGLAB "wikilink")