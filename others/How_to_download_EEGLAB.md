---
layout: default
title: Download EEGLAB
long_title: Download EEGLAB
parent: Download EEGLAB
nav_order: 1
---
Download EEGLAB
====

Fill in the form below to download the latest stable version of EEGLAB. The rest of this page describes how to download the development version of EEGLAB, and is recommended for advanced EEGLAB users only. In the video, we outline the different options for running EEGLAB.

<!-- Set the download cookie so the Download_Success page can be accessed after submitting -->
<script>document.cookie = "eeglabdownload=1;path=/;max-age=604800";</script>

<form class="form" method="post" name="icaform" onsubmit="return checkFields();" action="https://sccn.ucsd.edu/eeglab/downloadeeglab.php">
  <p>Your name:<br>
  <input name="username" type="text" value="" size="40"></p>
  <p>Your email address:<br>
  <input name="email" type="text" value="" size="40"></p>
  <p>Your research area (and comments):<br>
  <textarea name="comments" cols="40" rows="4" wrap="soft"></textarea></p>
  <p><label><input type="checkbox" name="eeglabnews"> Invite me to receive email notification of major updates.</label><br>
  <label><input type="checkbox" name="eeglablist"> Invite me to the (moderated) EEGLAB email discussion list.</label><br>
  <label><input type="checkbox" name="agree"> I accept the terms of the <a href="https://github.com/sccn/eeglab/blob/develop/eeglablicense.txt" target="_blank">BSD license</a>.</label></p>
  <p><input type="submit" value="Submit"></p>
</form>

<script>
// Validate the download form before submission
function checkFields() {
    var form = document.icaform;
    if (form.username.value === "" || form.email.value === "") {
        alert("Please enter your name and email address.");
        return false;
    }
    if (!form.agree.checked) {
        alert("Check the box to agree to the BSD license terms.");
        return false;
    }
    return true;
}
</script>

**Disclaimer:** EEGLAB is a toolbox written and released for neuroimaging research purposes only with no guarantee of suitability for any particular purpose. EEGLAB, or data obtained from EEGLAB, should not under any circumstances be used for clinical purposes.

**Privacy:** SCCN will not distribute email addresses or other information contributed by those who download our software to anyone for any purpose other than personal correspondence or message distribution via user-requested email lists. Please check your SPAM/Junk Email folder for a confirmation reply from our mailing lists, and mark it as *not spam*.

EEGLAB versions
------------
MATLAB comes in different versions across operating systems, and EEGLAB in different versions as well. We recommend using the latest version of EEGLAB with a recent — though not necessarily the most recent — version of MATLAB, on any platform (Windows, macOS, Linux), as there are no dramatic differences between them. The video below gives more details.

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/NhKc0arEcbs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>

Download the EEGLAB ZIP file archive
------------
The form above downloads EEGLAB in ZIP format (the latest release). Older versions are available in the [EEGLAB download archive](https://sccn.ucsd.edu/eeglab/download/daily/). The [EEGLAB revision history page](/others/EEGLAB_revision_history.html) describes changes between EEGLAB versions.

Please do NOT download the zip file from the [EEGLAB GitHub repository](https://github.com/sccn/eeglab.git) as it is missing important EEGLAB plugins not included in the EEGLAB code base. If you want to use the development version of EEGLAB, clone it and include submodules as explained on the [GitHub repository](/others/GitHub_repository.html) page.

