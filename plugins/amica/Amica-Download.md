---
layout: default
parent: AMICA
grand_parent: Plugins
render_with_liquid: false

title: AMICA-Download
long_title: AMICA-Download
---
The information on this page may not be up-to-date, please [visit this
page](https://github.com/japalmer29/amica/wiki/AMICA#download-amica) for detailed
instructions on downloading, installing, and running AMICA.

<font size=3> </font>

**Files**
---------

### Linux/Unix

32 bit

[64 bit](Amica12lnx64.zip)

### Windows

32 bit

[64 bit](https://linkify.me/HxsKynA)

### Mac

[32 bit](Amica12mac32.zip)

[64 bit](Amica12mac64.zip)

To run the mac binary:

1\. Copy the files amica12mac64 and libiomp5.dylib to a directory, like
/users/hans/amica/.

2\. Open a terminal window and type:



$ export DYLD_LIBRARY_PATH=/home/hans/amica (or whatever directory you
used in step 1.)

3\. Copy runamica12.m and loadmodout12.m to a directory in your matlab
path.

4\. In the file runamica12.m, set AMDIR to the directory
(/users/hans/amica) and set AMBIN to amica12mac64.

5\. Test by running matlab and typing:



\>\> runamica12(randn(2,1000),'/users/hans/test/');

<!-- -->



\>\> mods = loadmodout12('/users/hans/test/')

### Sample Data

[Sample datafile (32 channels)](Eeglab_testdat.zip)

**Compiling**
-------------

### Mac

```mv libiomp5dylib /home/me/lib/libiomp5.dylib
export DYLD_LIBRARY_PATH=/home/me/lib

../mpich2/bin/mpif90 -fpp -openmp /Developer/opt/intel/mkl/lib/libmkl_core.a \
/Developer/opt/intel/mkl/lib/libmkl_intel_thread.a /Developer/opt/intel/mkl/lib/libmkl_intel_lp64.a \
amica12.f90 funmod2.f90 -mssse3 -o amica12mac64 -O3

../mpich2/bin/mpif90 -fpp -openmp /Developer/opt/intel/mkl/lib/libmkl_core.a \
/Developer/opt/intel/mkl/lib/libmkl_intel_thread.a /Developer/opt/intel/mkl/lib/libmkl_intel.a \
 amica12.f90 funmod2.f90 -msse3 -o amica12mac32 -O3
```
