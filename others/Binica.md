---
layout: default
title: Binica
parent: Other documents
---


Download BINICA binaries: a Compiled C Version of runica()
----------------------------------------------------------

This binary version of the runica() function of Makeig et al. contained
in the EEG/ICA Toolbox originally ran \~12x faster than the MATLAB
version (MATLAB speed has improved since) and may be \~4x more compact.

It uses the logistic infomax ICA algorithm of Bell and Sejnowski, with
natural gradient and extended ICA extensions by Tewon Lee et al.. It was
programmed in MATLAB as runica.m for unsupervised operation by Scott
Makeig at CNL, Salk Institute, La Jolla CA. Sigurd Enghoff translated it
into C++ code and compiled it for multiple platforms. J-R Duann improved
the PCA dimension-reduction and compiled the linux and free_bsd
versions.

Use: To use the function, call with a ".sc" file argument. For
individual applications, copy and modify the sample script "ica.sc".m.
Under UNIX or DOS command line

``` matlab
% ica \< myversion.sc
```
Be sure that the directory that you store the binary file in is in your
search path. e.g., In Unix/Linux add this directory to your root .cshrc
file "setenv path" line.

Outputs: Ica creates two files, "xxx.wts" and "xxx.sph" containing
weights and sphere matrices such that (under Matlab)

``` matlab
>> ICA_activations = wts \* sph \* data;
```


The "xxx" stem in the output files may be specified within the input .sc
parameter file. See the sample .sc file for arguments, and the EEG/ICA
toolbox tutorial for more details.

- [Linux version (works under Red Hat 7 or
8)](ftp://sccn.ucsd.edu/pub/binica/ica_linux.tar.gz). See also OSX
compiled version with GCC below.

- [FreeBSD 4.0](ftp://sccn.ucsd.edu/pub/binica/ica_bsd.tar.gz)

- [Mac OSX PPC](ftp://sccn.ucsd.edu/pub/binica/binica_osx.tgz)
(Recompiled by [William
Beaudot](http://wbeaudot.kybervision.net/main.html) in 2004) or [Recent
compile (April 2016)](/media:linux.zip "wikilink")

- [Mac OSX Intel](/Media:Binica_mac_intel.zip "wikilink") (Recompiled
by [Grega
Repovš](http://psy.ff.uni-lj.si/Osnova/faculty.php?tname=grepovs) in
2009)

- [Win x64 Intel](/media:binica.zip "wikilink"), Windows: (Recompiled
by Ernest Pedapati and Ellen Russo) the source code should compile on
windows architectures (i.e. 32 bit/ AMD).

To use one of these programs from within Matlab (and EEGLAB)

- download the file and place them in the functions/support_files of
the eeglab directory (you may create a subfolder for them or uncompress
them in the function subfolder).
- edit the
[icadefs.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=icadefs.m)
file to specify the file name of the executable you intend to use
(search for variable ICABINARY).
- From the command line, you may use the
[binica.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=binica.m)
function that will call the binary executable. From the EEGLAB graphical
interface, run ICA using the 'binica' option of the Tools → Run ICA
graphic interface (see the tutorial for how to [compute ICA
components](/Chapter_09:_Decomposing_Data_Using_ICA "wikilink")). As a
test, try for example "binica(rand(10,1000))". This is how to use the
algorithm on an EEGLAB dataset.

``` matlab
EEG = pop_runica(EEG,'icatype','binica', 'extended',1,'interupt','on');
```

Older version of the ICA binary are available below (these versions are
not compatible with the Matlab
[binica.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=binica.m)
function and <b>cannot be used directly in Matlab or from EEGLAB</b>
(although see { {Bug\|1604} }); The ica.sc text configuration file
([sample here](ftp://sccn.ucsd.edu/pub/binica/ica_bsd/ica.sc))in the
archive must be edited manually). [SGI Unix (older
version)](ftp://sccn.ucsd.edu/pub/binica/ica_sgi.tar.gz) [Sun Unix
(older version)](ftp://sccn.ucsd.edu/pub/binica/ica_sun.tar.gz) [Windows
PC (95, 98, NT, 2000, XP?. older
version)](ftp://sccn.ucsd.edu/pub/binica/ica_pc.tar.gz)

SOURCE code
-----------

The [Github repository](https://github.com/sccn/binica) (13Mb) contains
the source code, and
[binica_full.zip](ftp://sccn.ucsd.edu/pub/binica/binica_full.zip)
(\~180Mb) source code plus many binaries. This code is distributed under
the GNU GPL license and may not be used for commercial applications. It
is copyrighted by the Salk Institute for biological studies and the
University of San Diego California. This code can usually compile under
most Unix machines. The binary above for Mac OSX also contains a make
file for Mac OSX. Some recommendation below:

- if you uncompress using winzip, deactivate the "tar smart CR/LF"
option in winzip in the menu Option → configuation tab Miscellaneous
- recompile BLAS (folder CLABPACK\\BLAS)
- recompile LABPACK (CLABPACK folder)
For 2 and 3 it is actually better if you find on the Internet the latest
versions of these libraries

- make the ICA binary file by using the makefile in the main
directory
- Modify the icadefs.m Matlab file under EEGLAB so that it points to
your binary (in case you want to call it from Matlab).

- For credits, please quote "binary Infomax ICA by Sigurd Enghoff,
based on the Matlab version of Scott Makeig and collaborators. Makeig S,
Anthony J. Bell, Tzyy-Ping Jung and Terrence J. Sejnowski, Independent
component analysis of electroencephalographic data In: D. Touretzky, M.
Mozer and M. Hasselmo (Eds). Advances in Neural Information Processing
Systems 8:145-151 (1996)."
The README file embedded in the compressed archive also contains
additional details. We would advise to use the GNU C compiler since the
Makefiles should be compatible with it. Please when you have succeeded
compiling it, send us a copy of the exe file (and a small report of how
you did it) so we can put the new file on the Internet.

**Important:** Infomax ICA is under a patent by the Salk Institute and
any commercial product using this type of algorithm (or the recompiled
binary files distributed here) should contact the Salk Institute patent
office.

**Code provided for convenience:** This code is not supported and this
page is provided for convenience only. If you want to add more
documentation (readme file etc...) and guidelines for users or want to
set up a project under sourceforge to support development and
maintenance of BINICA, please feel free to do so. We will not answer
questions regarding the compilation of this code. - Arnaud Delorme,
November 21, 2007.

Cuda version
------------

This Github [repo](https://github.com/fraimondo/cudaica) contains a CUDA
version of the code above for use with NVIDIA GPU processors. A
[fork](https://github.com/sccn/mobilab/tree/master/dependency/cudaica)
by Alejandro Ojeda contains functions to call the CUDA version from
Matlab.