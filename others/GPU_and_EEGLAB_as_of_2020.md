---
layout: default
title: EEGLAB and GPU
parent: Other documents
---

### Introduction

GPU-based processing is promising in MATLAB. There used to be several
options although currently the default is the Matlab supported solution.
The recent enthusiasm for using GPU (Graphical Processing Unit)
computational capabilities led us to try the freely available GPU
solution for Matlab. Computing using the GPU usually only involves
recasting variables and requires minor changes to Matlab scripts or
functions.

One of our servers is a Quad Core Intel™ Xeon W3550 3.0GHz, 8M L3,
4.8GT/s, Turbo and has a One nVidia GTX Titan (2688 CUDA cores),
although it is unclear if Matlab uses all the CUDA cores (based on the
Matlab message below). All the tests on this page compared the central
processor with the GPU unit. When typing "gpuDevice" on the Matlab
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

### Basic matrix computation using GPUs provided a major speed-up

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

### Running non-parametric statistics on GPUs speeded up processing 50 times

We modified the repeated-measures ANOVA function to be GPU compatible.
(All the Matlab GPU functions we used are made available at the bottom
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
the main CPUs. For smaller matrices, the difference between the GPU code
might be smaller.

### Using GPUs for time-frequency decomposition gave a 10x speed-up

``` matlab
EEG = pop_loadset('sample_data/eeglab_data_epochs_ica.set');
data2 = EEG.data;
tic; timefreq(data2, EEG.srate, 'cycles', 0); toc
Elapsed time is 0.3517511 seconds.

data = gpuArray([EEG.data(:,:)]);
tic; timefreq_gpu(data, EEG.srate, 'cycles', 0); toc
Elapsed time is 0.038354 seconds.
```

Here we did observe a (10x) speed-up from performing the time-frequency
wavelet decompositions on the GPU rather than the CPU. Note that we run
each function several times, so memory allocation does not affect too
much the result. The first run on GPU is sometimes slow. Note also that
the code above uses the FFT function which automatically uses parallel
computation on the main processor (which has 4 cores) so the advantage
of using GPU is decreased.

### Conclusions concerning GPU Computing in MATLAB

<i>Arnaud Delorme - March 2020</i>

When we run our first tests in 2010, there were 3 options on the market:
GPUmat (free), Jacket (commercial), and the Parallel Computing Toolbox
of MATLAB (commercial). Overall, we were relatively disappointed with
GPU solutions. Even if Jacket proves more efficient than other options,
we can only expect an additional speed-up of about 5-20% compared to
GPUmat. This is far from the 100x speed-up that we were hearing about
when GPU cards came out. However, a 3x speed up was still welcomed.

As of 2020 though, the GPU solution have been vastly optimized and we
now observe major speed up for all solutions. It appears that our GPU is
compatible with double precision, although we have not tested that
solution.

The EEGLAB-compatible GPU functions we tested are available
[here](/media:Gpu_funcs2.zip "wikilink"). Note that these functions are
not totally functional (they only work under a limited set of conditions
as tested above) and thus are only made available for exploratory
testing purposes.
