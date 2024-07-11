---
layout: default
title: Using-the-Open-EEGLAB-Portal
long_title: Using-the-Open-EEGLAB-Portal
parent: nsgportal
grand_parent: Plugins
---
There will be two approaches to using the Open EEGLAB Portal: either, through its NSG web interface (http://www.NSGportal.org), or by making use of the NSG command line RESTful interface (NSG-R). This section describes the use of the web interface.

Start by login into the NSG portal. Once logged in, you may upload a **zipped file** containing 1) an EEGLAB script calling 2) one or more data files by name (they should be in or under the same folder as the script). Then click on the "Data" tab and select "Upload data", then upload a file containing your script and data.

<center>
<img src="https://github.com/nucleuscub/pop_nsg_wiki/blob/master/docs/img/500px-NSG3.png" alt="drawing" width="500"/>
</center>

You may download a 3.5-MB sample zip file (containing EEG data and a sample script [HERE](https://sccn.ucsd.edu/mediawiki/images/7/7c/Testingeeglabonnsg.zip). Below is its list of contents:

<center>
<img src="https://github.com/nucleuscub/pop_nsg_wiki/blob/master/docs/img/200px-NSG32.png" alt="drawing" width="200"/>
</center>

The EEGLAB script (test.m) in this upload file is shown below ( try minor alterations for testing purposes)

<center>
<img src="https://github.com/nucleuscub/pop_nsg_wiki/blob/master/docs/img/500px-NSG33.png" alt="drawing" width="500"/>
</center>

Now create a new NSG task. To do this, click on the "Task" tab and select, "Create new task." Click on, "Select input data" and select the zip file you have uploaded above. Click on "Select tool" and select "EEGLAB".

<center>
<img src="https://github.com/nucleuscub/pop_nsg_wiki/blob/master/docs/img/500px-NSG4.png" alt="drawing" width="500"/>
</center>

Then click on "Select parameters". Enter the name of your script. This script must be at the root (top) folder of your zip archive. You may also (optionally) change other NSG settings on this page.

<center>
<img src="https://github.com/nucleuscub/pop_nsg_wiki/blob/master/docs/img/500px-NSG5.png" alt="drawing" width="500"/>
</center>

Finally, press "Save parameters". This will bring you back to the previous screen. You may now press, "Save and Run Task" which will enter the task into the Comet queue. A warning is shown as in the image below. Simply click OK.

<center>
<img src="https://github.com/nucleuscub/pop_nsg_wiki/blob/master/docs/img/300px-NSG6_add.png" alt="drawing" width="350"/>
</center>

Once the task has been run, you will receive an email from NSG (see email for the test job below).


<center>
<img src="https://github.com/nucleuscub/pop_nsg_wiki/blob/master/docs/img/500px-NSG6_3.png" alt="drawing" width="500"/>
</center>

Upon receiving this message, go back to the NSG interface and select the task you ran from the list of tasks, as shown below.

<center>
<img src="https://github.com/nucleuscub/pop_nsg_wiki/blob/master/docs/img/500px-NSG6.png" alt="drawing" width="500"/>
</center>

Select "View" following the heading "Output" (see above): this will bring the output below.

<center>
<img src="https://github.com/nucleuscub/pop_nsg_wiki/blob/master/docs/img/500px-NSG7.png" alt="drawing" width="500"/>
</center>

You may now download the task output, a zip file containing the results of your task. Output files (see listing below) include the Matlab log and error log for your task. If your script saved data files, they will be there. For example, if you use the zip file and script provided above, below (left) is what the unzipped output archive will contain. The figure below (right) is the .jpg image created by the test.m script. Saving output images in Matlab .fig format (instead of .jpg) will allow you to read them into Matlab (for further editing, etc.). Note: The numeric data plotted in a figure can be read from the .fig file structure as well. Alternatively, saving figures in Postscript (e.g., as .epsc) will allow you to edit them in Illustrator.

Note: To save needless transfer time and effort, the uploaded data file itself will not be returned with the output unless your script explicitly saves it under a new name. In future this will also allow you to temporarily store and reuse the uploaded data.

<center>
<img src="https://github.com/nucleuscub/pop_nsg_wiki/blob/master/docs/img/500px-NSG8.png" alt="drawing" width="500"/>
</center>

### Interact with NSG through command line interface NSG-R and the creation of NSG EEGLAB Plugin
As mentioned at the beginning of this page, users can also interact with NSG (and make use of Open EEGLAB Portal) through command line RESTFUL interface NSG-R (R for REST interface). You can use the same credentials when registered for NSG for NSG-R. NSG-R allows users to move away from the browser window and perform computational work more programmatically. However, interacting with NSG-R directly requires some knowledge of web services and appropriate networking tools and libraries (e.g. curl command) which most people are unfamiliar with. Thus we developed an EEGLAB plugin to simplify the process, allowing EEGLAB users to interact with NSG in the familiar MATLAB environment, either through graphical or command line interface. In the next sections of the wiki, we will describe the EEGLAB plugin to NSG and provide hands-on tutorials. For those who are curious about NSG-R, you can read more at this [link](https://www.nsgportal.org/guide.html).