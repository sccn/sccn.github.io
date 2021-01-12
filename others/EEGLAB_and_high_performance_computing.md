---
layout: default
title: EEGLAB and HPC
long_title: EEGLAB and High Performance Computing
parent: Interoperability
---
EEGLAB and high-performance computing
====
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

EEGLAB and the Neuroscience Gateway
---
We have a funded project to run EEGLAB on the San Diego supercomputer via the Neuroscience Gateway (NSG). This is a free service for academia worldwide. The documentation for using EEGLAB on NSG is available on the [NSGportal GitHub wiki](https://github.com/sccn/nsgportal/wiki).


Deep learning and EEGLAB
----
Deep learning is popular and deep learning applied to EEG data is increasing at a rapid pace. We recommend using EEGLAB to prepare data for deep learning and machine learning. EEGLAB data epochs may be concatenated either in MATLAB or Python (EEGLAB datasets may be read in Python using the *loadmat* function of the *scipy* librairy) and used as input for deep learning networks. In MATLAB, assuming multiple datasets are loaded in EEGLAB with the same number of channels and the same number of samples per epochs, type:

```matlab
X = cat(3, ALLEEG.data); % concatenate trials
X = permute(X, [3 1 2]);
X = reshape(X, size(X,1), size(X,2)*size(X,3));
```

Now, X contains feature vectors (one row per EEG data epoch) ready to be used for deep learning or machine learning applications.

Running EEGLAB on GPUs (Graphic Processing Units)
---

### Introduction

GPU-based processing is promising in MATLAB.
The recent enthusiasm for using GPU (Graphical Processing Unit)
computational capabilities led us to try the freely available GPU
solution for MATLAB. Computing using the GPU usually only involves
recasting variables and requires minor changes to MATLAB scripts or
functions.

One of our servers is a Quad Core Intel™ Xeon W3550 3.0GHz, 8M L3,
4.8GT/s, Turbo and has a One nVidia GTX Titan (2688 CUDA cores),
although it is unclear if MATLAB uses all the CUDA cores (based on the
MATLAB message below). All the tests on this page compared the central
processor with the GPU unit. When typing "gpuDevice" on the MATLAB
command line, the following message appears

``` matlab
gpuDevice

ans =

  CUDADevice with properties:

                      Name: 'GeForce GTX TITAN'
                     Index: 1
         ComputeCapability: '3.5'
            SupportsDouble: 1
             DriverVersion: 10.2000
            ToolkitVersion: 10
        MaxThreadsPerBlock: 1024
          MaxShmemPerBlock: 49152
        MaxThreadBlockSize: [1024 1024 64]
               MaxGridSize: [2.1475e+09 65535 65535]
                 SIMDWidth: 32
               TotalMemory: 6.3787e+09
           AvailableMemory: 5.3827e+09
       MultiprocessorCount: 14
              ClockRateKHz: 875500
               ComputeMode: 'Default'
      GPUOverlapsTransfers: 1
    KernelExecutionTimeout: 0
          CanMapHostMemory: 1
           DeviceSupported: 1
            DeviceSelected: 1
```

### Basic matrix computation using GPUs provided a major speedup

``` matlab
GPUstart;

EEG = pop_loadset('sample_data/eeglab_data_epochs_ica.set');
data = [EEG.data(:,:)];
data = [data data data data data data ];
data = [data data data data data data ];
data2 = gpuArray(data);

tic; tmp = power(complex(data2), complex(1.3,0)); toc
Elapsed time is 0.000393 seconds

tic; tmp = data.^1.3; toc
Elapsed time is 0.689292 seconds
```

Raising each value in the EEG data matrix to a fractional power (1.3)
using the GPU rather than the central processor produced a 2000x speed
increase.

### Running non-parametric statistics on GPUs speeds up processing 50 times

We modified the repeated-measures ANOVA function to be GPU compatible (all the MATLAB GPU functions used here are made available at the bottom
of this page).

``` matlab
c = { single(rand(400,800,100)) single(rand(400,800,100)); ...
          single(rand(400,800,100)) single(rand(400,800,100))};
tic; [FC FR FI dfc dfr dfi] = anova2_cell(c); toc
Elapsed time is 0.24665 seconds.

c = { gpuArray(single(rand(400,800,100))) gpuArray(single(rand(400,800,100))); ...
      gpuArray(single(rand(400,800,100))) gpuArray(single(rand(400,800,100)))};
tic; [FC FR FI dfc dfr dfi] = anova2_cell_gpu(c); GPUsync; toc
Elapsed time is 0.005052 seconds.
```

The GPU computation appeared to be about 50 times faster than when using
the main CPUs. For smaller matrices, the difference between the GPU and CPU code implementations
might be smaller.

### Using GPUs for time-frequency decomposition provides a 10x speedup

``` matlab
EEG = pop_loadset('sample_data/eeglab_data_epochs_ica.set');
data2 = EEG.data;
tic; timefreq(data2, EEG.srate, 'cycles', 0); toc
Elapsed time is 0.3517511 seconds.

data = gpuArray([EEG.data(:,:)]);
tic; timefreq_gpu(data, EEG.srate, 'cycles', 0); toc
Elapsed time is 0.038354 seconds.
```

Here we did observe a (10x) speedup from performing the time-frequency
wavelet decompositions on the GPU rather than the CPU. Note that we run
each function several times, so memory allocation does not affect the result (the first iteration on GPU is sometimes slow). Note also that
the code above uses the FFT function, which automatically uses parallel
computation on the main processor (which has 4 cores), so the advantage
of using GPU likely to be about 40x compared to a single-core CPU.

### Conclusions concerning GPU Computing in MATLAB

When we ran our first tests in 2010, there were 3 options on the market:
GPUmat (free), Jacket (commercial), and the Parallel Computing Toolbox
of MATLAB (commercial). Overall, we were disappointed with the performance improvements.

As of 2020 (the date at which these tests were run), GPU solutions have been vastly optimized, and we
now observe major speedup for all solutions. It appears that our GPU is
compatible with double-precision numbers, although we have not tested that
solution.

The EEGLAB-compatible GPU functions we tested are available
[here](https://github.com/sccn/eeglab_gpu_func). Note that these functions are
not fully functional (they only work under a limited set of conditions
as tested above) and thus are only made available for exploratory
testing purposes.

What if MATLAB is not available for my computing resource
--------------------------------------------

When it comes to using supercomputers or Singularity, MATLAB, although quite efficient,
may not be available (check with your local supercomputer, because it often is). As of 2019 (EEGLAB 2019), we are currently supporting Octave (v4.4.0) for supercomputing
applications. You may refer to 
this [page](/others/Running_EEGLAB_on_Octave) for how to use
EEGLAB on Octave. In the short term, Octave may be the simplest way to using EEGLAB functions and actually obtain useful results.

Using EEGLAB with Hadoop
------------------------
Hadoop Mapreduce is a framework for performing computation on large
clusters of computers. There are two steps in Mapreduce job: a mapping
task where many workers (computers) work on a large number
of data lines, and a reduce step, where (usually) a single worker pools all the mapping results. This section was written in 2013 and updated in 2021.

Below we provide guidelines for using Elastic Mapreduce on the Amazon
cloud. Note that Elastic Mapreduce is tailored to processing large
quantities of log text files and not binary data. The gain in terms of
processing speed compared to the cost of running such a solution remains
unclear if you have a local cluster of computers. In short, you might
spend more time programming the solution, and it might cost you more in
terms of bandwidth and storage than if you were running it locally. These
are the steps you should follow. Expertise
in computer science is highly recommended.

-   Installing Hadoop command-line interface. First, install the [Command
    Line Interface](http://aws.amazon.com/developertools/2264) to
    Elastic Mapreduce. This will allow you to configure and run jobs on
    the Amazon cloud. You will also need to create an [AWS
    account](http://aws.amazon.com/). Hadoop will need to run in
    streaming mode, where the data is simply streamed to any executable.
    It might also be possible to run Hadoop in native Java mode and
    compile MATLAB code using the Java builder (this is
    more complex than using the streaming mode).

-   Transfer your data to Amazon storage cloud (the Amazon storage cloud
    is named S3). Note that your data
    should be formatted in strings of characters. <b>If you want to
    process raw EEG data, you will have to serialize it in text</b>,
    with each channel representing one row of text (Hadoop may also process binary data, although we have not tried that feature). There is no
    limit to the length of a line of text. However, one must remember
    the overhead in terms of both signal processing and bandwidth
    associated with processing text. If you have 128 channels and 100
    data files, this corresponds to 12,800 processing Hadoop steps. If
    you can allocate 1,000 workers to the task, this means that each
    worker will process about 13 channels, a potential speedup of about
    1,000 on your task. To minimize bandwidth overhead, you might want to
    transfer the compressed binary data to S3, then have a local amazon
    EC2 amazon node uncompress it and put it back to S3 (this is because
    EC2 nodes bandwidth with S3 is free).

-   Solution 1 (easiest to implement) using Octave. EEGLAB command line
    code is compatible with
    [Octave](/others/Running_EEGLAB_on_Octave). Octave may be
    installed relatively easyly on each of the nodes using the
    bootstrapping method (a method to automatically install software on
    each of the nodes). The command to automatically install Octave on
    EC2 Amazon nodes is *sudo yum –y install octave --enablerepo=epel*

    Hadoop communicates with workers through STDIN and STDOUT pipes. For your main MATLAB script, you might want to add the following
    at the beginning of the main script. This will make it executable and
    will allow it to process data on STDIN. You may
    write the output of your data processing using the *printf* or *disp* MATLAB
    commands. 

    ``` matlab
    #!/usr/bin/octave -qf
    Q = fread(stdin); %Standard Octave / MATLAB code from here on
    ```

-   Solution 2, compiling MATLAB code. Compiling MATLAB code is the most
    efficient solution as MATLAB compiled code is often 2 to 4 times
    faster than Octave code, and compiled code does not require a MATLAB
    license. If you compile MATLAB code on your local Unix workstation,
    you will need to make sure to use an Amazon AMI (virtual machine
    image) with the same set of libraries so that your code can run on
    that machine. You will need to pick an AMI that is compatible with
    Hadoop as well. Also, MATLAB does not have a simple mechanism
    allowing it to read from STDIN. The easiest solution is to use third-party compiled Mex files to do so (for example, see
    [popen](http://www.mathworks.com/matlabcentral/fileexchange/13851-popen-read-and-write)).
    Another solution is to have a shell command write STDIN on disk,
    then call the MATLAB executable (although this might impair
    performance).

-   Reduce step: once all the workers have computed what they had to
    compute (spectral power for example), the reduce step may write it
    back on S3 Amazon storage (and also do futher processing if
    necessary such as grouping back channels belonging to the same
    subject).

-   Running Hadoop: using the AWS command-line interface, type something
    like the following.

    ``` matlab
    elastic-mapreduce --create --stream --input s3n://Arno/myEEGserializedtextfiles/ \
    --mapper s3://Arno/process_octave \
    --reducer s3://Arno/reducer.py \
    --output s3n://Arno/output --debug --verbose \
    --log-uri s3n://Arno/logs --enable-debugging \
    --bootstrap-action s3n://Arno/install_octave
    ```

- Note the reduce step can be written in any programming language that
takes data from STDIN and writes to STDOUT. The reduce step will usually
not require to run EEGLAB commands. It is simply about pooling data from
the workers and summarizing it. In this case, we used a Python custom
program, but it could have also been Octave/MATLAB since
Octave is installed on each of the workers. The exact content of your
code will depend on what task you are interested in doing.

The solution outlined above should only be tried when dealing with
a huge amount of data that no local processor or cluster can handle.
 It is therefore
best suited when bootstrapping data is required (lots of computation on
little data). Please send us your comments and new solutions at <eeglab@sccn.ucsd.edu>.

