---
layout: default
title: BCIchapter
permalink: /docs/BCIchapter
parent: Docs
---

This is the data and code associated with the book chapter:

The data from the BCI competition III is in the three .mat files. The
data is described
[here](http://www.bbci.de/competition/iii/desc_IVb.html).

data_set_IVb_al_train

There are two ways to train the BCI, either automatic & ad hoc or
manually tuned to the subject. eval_bcicomp used the ad hoc way. As you
will see, the alternative manually tuned version gives you spatial
filters which better reveal the dipole for foot movement (centrally
located) than the ad hoc way. S o if you want to include the spatial
filter plots, you might want to use use the second code path.

1\. A brief and simple one (ad hoc & not much to explain)

` load data_set_IVb_al_train`
` `
` [S,T,w,b] = train_bci(single(cnt), nfo.fs, ...`
`   sparse(1,mrk.pos,(mrk.y+3)/2),[0.5 3.5],@(f)f>7&f<30,3,200);`

\-\> this yields the spatial filter spatial_filter_S.pdf, the temporal
filter spectral_filter_T.pdf, and the prediction prediction.pdf.

2\. One which uses a spectral filter (flt) manually tuned to the dataset
in question: load data_set_IVb_al_train

` flt = @(f)(f>7&f<30).*(1-cos((f-(7+30)/2)/(7-30)*pi*4));`
` [S,T,w,b] = train_bci(single(cnt), nfo.fs, ...`
`   sparse(1,mrk.pos,(mrk.y+3)/2),[0.5 3.5],flt,3,300);`

\-\> this yields the spatial_filter_S2.pdf, spectral_filter_T.pdf
and prediction2.pdf.

For the manual tuning, one can either use BCILAB, or, I guess, EEGLAB. I
used neither and just specified a two-peaked spectral filter from my
prior experience with our own b enchmarking data. pre_post_flt.pdf
shows how T transforms the six EEG components produced by CSP, during
test_bci. It has essentially no latency.