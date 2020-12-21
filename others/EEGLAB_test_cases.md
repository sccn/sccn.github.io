---
layout: default
title: EEGLAB test cases
parent: Other documents
---

# EEGLAB test cases

## What is a unit testing test case?

A test case is a small function or function call built to test a
specific function call - here an EEGLAB function. We aim to have at
least one test case per function, though for many EEGLAB functions many
more test cases may be required to test the whole range of available GUI
and command line options (and their combinations).

There are different types of test cases. Some test cases simply test
that a given function does not crash when using specific combinations of
input parameters. This constitutes the majority of EEGLAB tests for
functions with graphical outputs. Some other test cases run a given
function and test if the output is numerically accurate.

## EEGLAB test case repository

Our test cases do not cover all the possible usage of EEGLAB functions.
We estimate that our about 5,000 test cases cover about 10% of all
possible function call variations.

Test cases are stored in a SVN repository: [https://sccn.ucsd.edu/svn/eeglab-testcases/trunk](https://sccn.ucsd.edu/svn/eeglab-testcases/trunk)

The total size of the unit testing package above is currently (5/11)
1.76 GB. After downloading the code (perhaps to a directory/folder you
name "/unittesting"), move to this folder in MATLAB and run the
<b>runlocal</b> function. This will execute all the tests. At the end of
the testing (usually about 15 minutes), a list of any functions that
have failed will be returned. For example, if bugs have crept into two
functions 'decompresserpss' and 'pop_epoch', the 'runlocal' output might
be:

```

function /Users/arno/eeglab-testcases/trunk/unittesting_binary/pop_read_erpss/test_pop_read_erpss.m
    msg Error using ==> read_erpss at 245
 decompresserpss function error (see message above)
 *********************************************
 function /Users/arno/eeglab-testcases/trunk/unittesting_general/unittesting_popfunc/pop_epoch/test_pop_epoch.m
    msg Error using ==> pop_epoch at 123
 ??? Index exceeds matrix dimensions.
 *********************************************
```


You may then go to each folder containing a function that failed and
call the function from the command line. For instance

```

>> cd /Users/arno/eeglab-testcases/trunk/unittesting_binary/pop_read_erpss
>> test_pop_read_erpss

```

The function should again fail, making it possible to debug it 'on the
spot' if you wish.

Note that the sample errors above are simply provided as examples. All
the (nearly 5,000) test cases contained in the repository have been
verified to work under several versions of Matlab 7.x running under
Windows, Mac OSX, and Linux.

### EEGLAB test case sub-repositories

Since the test case repository above is quite large (1.76 GB), we have
separated the test cases into sub-folders that may be run independently.
In each case you must check out the folder [https://sccn.ucsd.edu/svn/eeglab-testcases/trunk/unittesting_common](https://sccn.ucsd.edu/svn/eeglab-testcases/trunk/unittesting_common)

This small folder (only 0.1 MB) contains common code required to apply
the test cases. You may then check out any of the following folders
below. Note that their parent folder (perhaps name it "/unittesting")
must also contain "/unittesting_common" (above):

[https://sccn.ucsd.edu/svn/eeglab-testcases/trunk/unittesting_general](https://sccn.ucsd.edu/svn/eeglab-testcases/trunk/unittesting_general)

Though this repository contains tests for all the signal processing
functions in EEGLAB (90% of all tests), it is only 18 MB in size. After
downloading the folder, run the <b>runlocal</b> function contained in
it.

[https://sccn.ucsd.edu/svn/eeglab-testcases/trunk/unittesting_studyfunc](https://sccn.ucsd.edu/svn/eeglab-testcases/trunk/unittesting_studyfunc)

This folder contains all the test cases for functions that deal with
EEGLAB studies. Because it contains a test STUDY with anonymized data
for several test subjects, this folder is larger (1.2 GB). After
downloading this folder (again putting it under "/unittesting"), run the
<b>runlocal</b> function contained in it.

[https://sccn.ucsd.edu/svn/eeglab-testcases/trunk/unittesting_binary](https://sccn.ucsd.edu/svn/eeglab-testcases/trunk/unittesting_binary)

This folder contains test cases for reading binary data files in several
formats. Because it contains several anonymized binary test data files,
this folder is also large (500 MB). After downloading this folder (under
"/unittesting"), run the <b>runlocal</b> function contained in it.

## Adding new test cases

Contributing new test cases is very useful both for us the EEGLAB
developers and for the EEGLAB user community in general, because unit
testing helps insure that the EEGLAB code base remains stable. You may
want to add test cases for your own functions or scripts, to insure they
continue to give the same output. Or you may want to add test cases for
functions you call with non-standard combinations of options. If you
have test cases for EEGLAB functions that you might contribute to our
repository, contact us at eeglab@sccn.ucsd.edu. We will create a SVN
account for you so you can check your code into the test case
repository.

What is an ideal test case? An ideal test case runs an EEGLAB function
with some (useful) combination of input parameters and also checks that
the function output is correct. This might involve saving
verified-to-be-correct output data in a file and comparing the test case
output to the data in the file. However, nearly always 'some test is
better than no test.' Therefore, even if your test does not yet check
function output, we will be happy to add it to our test case suite.
Ideally, your tests should use the same test input data provided in the
test case repository, or the tutorial data that is distributed with
EEGLAB in the "sample_data" folder.

## Adding EEGLAB scripts to unit testing

If you have complex scripts calling standard MATLAB and EEGLAB functions
that you want to ensure will continue to be supported in future EEGLAB
releases, send us the script and associated data to
eeglab@sccn.ucsd.edu.

<i>To date, most test-case functions were contributed by Arnaud Delorme,
Ke Tang, Andreas Romeyke, and Ronny Lindner.</i>