---
layout: default
title: Big data
parent: Other documents
---

We have a funded project to run EEGLAB on the Neuroscience Gateway to
run EEGLAB jobs on the San Diego supercomputer. This is a free service
and anybody in the world can use it. See this
[page](/EEGLAB_on_NSG "wikilink") for more information.

In the short term, Octave is the shortest way to using EEGLAB functions
and actually obtain useful results. This
[page](/Running_EEGLAB_on_Octave "wikilink") describes how to use EEGLAB
on Octave.

Deployment of EEGLAB on local supercomputers
--------------------------------------------

When it comes to using supercomputers, Matlab, although quite efficient,
may become incredibly expensive. A single Matlab license may cost $2,100
($1,050 for academia), and with *all* its commercial toolboxes might
come to $145,000 or more. If you have a supercomputer with about 100
processors (as of 2011, this amounts to about $30,000 or 20,000 euros),
you might need to pay the Mathworks about $30,000 to $500,000 to be able
to run Matlab on it (the exact price depends on the number of users on
the cluster, the number of nodes, and the extra toolboxes). This may be
much more than the price of the supercomputer itself! Given that the
Matlab core has not evolved dramatically over the past 10 years, and
still has flaws (lack of consistency of the graphic interface between
platforms; numerical inconsistencies in early version of Matlab 7.0),
free alternatives to Matlab are needed in the Open Source community to
run computation on supercomputers.

We have attempted to tackle this problem and as of June 2018 (EEGLAB
15+), we are currently supporting Octave (v4.4.0) for supercomputing
applications (command line calls only, no graphic support). In our
tests, Octave is about 50% slower than Matlab but this can easily be
compensated by increasing the number of processors assigned to a
specific processing task. Note that EEGLAB functions have not been
parallelized (except a few rare exceptions). Therefore, you are required
to open a Octave/Matlab session on each node and run custom scripts you
write to take advantage of your parallel processing capability. Again,
this [page](/Running_EEGLAB_on_Octave "wikilink") describes how to use
EEGLAB on Octave.

Using EEGLAB with Hadoop
------------------------

Hadoop Mapreduce is a framework for performing computation on large
clusters of computers. There are two steps in Mapreduce job: a mapping
task where a large number of workers (computers) work on a large number
of data lines, and a reduce step, where (usually) a single worker pools
all the mapping results.

Below we provide guidelines for using Elastic Mapreduce on the Amazon
cloud. Note that Elastic Mapreduce is tailored to processing large
quantities of log text files and not binary data. The gain in terms of
processing speed compared to the cost of running such solution remains
unclear if you have a local cluster of computers. In short, you might
spend more time programming the solution and it might cost you more in
terms of bandwidth and storage that if you are running it locally. These
are the steps you should follow. These are new technologies so expertise
in computer science is highly recommended.

-   Installing Hadoop command line interface. First install the [Command
    Line Interface](http://aws.amazon.com/developertools/2264) to
    Elastic Mapreduce. This will allow you to configure and run jobs on
    the Amazon cloud. You will also need to create an [AWS
    account](http://aws.amazon.com/). Hadoop will need to run in
    streaming mode, where the data is simply streamed to any executable.
    It might also be possible to run Hadoop in native Java mode and
    compile Matlab code using the Java builder (this is probably much
    more complex than using the streaming mode though).

<!-- -->

-   Transfer your data to Amazon storage cloud (the Amazon storage cloud
    is named S3). A useful tool to do this is the
    [s3cp](https://github.com/aboisvert/s3cp) tools. Note that your data
    should be formatted in strings of characters. <b>If you want to
    process raw EEG data, you will have to serialize it in text</b>,
    with each channel for example representing one line. There is no
    limit to the length of a line of text. However, one must remember
    the overhead in terms of both signal processing and bandwidth
    associated with processing text. If you have 128 channels and 100
    data files, this corresponds to 12800 processing hadoop steps. If
    you can allocate 1000 workers to the task, this means that each
    worker will process about 13 channels, a potential speedup of about
    1000 on your task. To minimize bandwidth overhead, you might want to
    transfer the compressed binary data to S3, then have a local amazon
    EC2 amazon node uncompress it and put it back to S3 (this is because
    EC2 nodes bandwidth with S3 is free). If you are dealing with
    Terabytes of data, this task can take a long time (as S3 is
    configured to have a very slow reading latency and very high writing
    latency). There are tools to copy data in parallel to S3.

<!-- -->

-   Solution 1 (easiest to implement) using Octave. EEGLAB command line
    code is compatible with
    [Octave](/Running_EEGLAB_on_Octave "wikilink"). Octave may be
    installed relatively easy on each of the nodes using the
    bootstraping method (a method to automatically install software on
    each of the nodes). The command to automatically install Octave on
    EC2 Amazon nodes is:

``` matlab
sudo yum –y install octave --enablerepo=epel
```

Then, for your main Matlab script, you might want to add the following
at the beginning of the main script. This will make it executable and
will allow it to process data on STDIN.

``` matlab
#!/usr/bin/octave -qf
Q = fread(stdin); %Standard Octave / MATLAB code from here on
```

Hadoop communicate with workers through STDIN and STDOUT pipes. You may
write the output of your data processing using the printf or disp Matlab
commands.

-   Solution 2, compiling Matlab code. Compiling Matlab code is the most
    efficient solution as Matlab compiled code is often 2 to 4 times
    faster than Octave code and compiled code does not require a Matlab
    licence. If you compile Matlab code on your local Unix workstation,
    you will need to make sure to use an Amazon AMI (virtual machine
    image) with the same set of librairies so that your code can run on
    that machine. You will need to pick an AMI that is compatible with
    Hadoop as well. Also, Matlab does not have a simple mechanism
    allowing it to read from STDIN. The easiest solution is to use third
    party compiled Mex files to do so (see for example
    [popen](http://www.mathworks.com/matlabcentral/fileexchange/13851-popen-read-and-write)).
    Another solution is to have a shell command write STDIN on disk,
    then call the Matlab executable (although this might impair
    performance).

<!-- -->

-   Reduce step: once all the worker have computed what they had to
    compute (spectral power for example), the reduce step may write it
    back on S3 Amazon storage (and also do futher processing if
    necessary such as grouping back channels belonging to the same
    subject).

<!-- -->

-   Running Hadoop: using the AWS command line interface, type something
    like the following.

``` matlab
elastic-mapreduce --create --stream --input s3n://Arno/myEEGserializedtextfiles/ \
--mapper s3://Arno/process_octave \
--reducer s3://Arno/reducer.py \
--output s3n://Arno/output --debug --verbose \
--log-uri s3n://Arno/logs --enable-debugging \
--bootstrap-action s3n://Arno/install_octave
```

Note the reduce step can be written in any programming language that
takes data from STDIN and writes to STDOUT. The reduce step will usually
not require to run EEGLAB commands. It is simply about pooling data from
the workers and summarizing it. In this case, we used Python custom
program (reducer.py) but it could have also been Octave/Matlab since
Octave is installed on each of the workers. The exact content of your
code will depend on what task you are interested in doing.

The solution outlined above should only be tried when dealing with
gigantic amount of data that no local processor or cluster can handle.
It is costly (mostly in terms of Amazon storage as storing 10 Terabytes
of data will cost you about $800 per month as of 2013). It is therefore
best suited when bootstraping data is required (lots of computation on
little data). Send us your comments at <eeglab@sccn.ucsd.edu>.

------------------------------------------------------------------------

<div align=right>

**Return to [EEGLAB Wiki Home](/EEGLAB "wikilink")**

</div>

[Category:EEGLAB](/Category:EEGLAB "wikilink")
