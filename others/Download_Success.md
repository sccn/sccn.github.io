---
layout: default
title: EEGLAB Download
nav_exclude: true
search_exclude: true
---
<script>
// Reached only after submitting the download form (which sets this cookie).
// Send direct visitors back to the form.
if (document.cookie.indexOf("eeglabdownload=1") === -1) {
   window.location.href = "/others/How_to_download_EEGLAB.html";
}
</script>

Download EEGLAB
====

Thank you for registering. [Click here](https://sccn.ucsd.edu/eeglab/currentversion/eeglab_current.zip) to download the latest EEGLAB version for MATLAB (if you are using MATLAB 2016a or older, download EEGLAB v2020.0 instead). As of 2019, all new versions are also compiled for Windows and Mac (see below).

EEGLAB is released twice a year and the version name is based on the year. Older EEGLAB versions are available [here](https://sccn.ucsd.edu/eeglab/download/daily/). Revision details are available on the [EEGLAB revision history page](/others/EEGLAB_revision_history.html). If you have a version of MATLAB older than 2014, download EEGLAB version 4.5b [here](https://sccn.ucsd.edu/eeglab/eeglab4.5b.teaching.tar.gz).

To install EEGLAB:

1. Unzip the EEGLAB zip file in the folder of your choice
2. Start MATLAB
3. Change the MATLAB path to the EEGLAB folder you have just uncompressed
4. Type "eeglab" and press enter at the MATLAB prompt

Download EEGLAB development version
------------
Using the development head requires Git, available for free on the Internet. Using the development head is useful to benefit from the latest bug fixes and update your version of EEGLAB daily. Detailed steps to download the EEGLAB development head are available [here](/others/How_to_download_EEGLAB.html).

Download a compiled version of EEGLAB
------------
The EEGLAB compiled version for Windows ([exe](https://sccn.ucsd.edu/eeglab/currentversion/eeglab_compiled_windows.exe)), Mac ([zip](https://sccn.ucsd.edu/eeglab/currentversion/eeglab_compiled_macos.zip)) and Linux Ubuntu ([zip](https://sccn.ucsd.edu/eeglab/currentversion/eeglab_compiled_ubuntu.zip)) does not require MATLAB. Note that as of 2020, we no longer compile for Ubuntu (fewer than 400 downloads/year). If you have access to MATLAB, we recommend the MATLAB version. The links correspond to the latest compiled versions. For older compiled versions, including a version compatible with 32-bit Windows systems (EEGLAB version 7), refer to this [compiled folder](https://sccn.ucsd.edu/eeglab/download/daily/compiled). **Instructions** on how to install the EEGLAB compiled version are available on the [Compiled EEGLAB page](/others/Compiled_EEGLAB.html). **Warning:** messages such as <span style="color:red">Unable to determine if this file contains malware</span> are nothing to worry about &mdash; the files are compressed and contain encrypted MATLAB binaries that antivirus software cannot scan.
