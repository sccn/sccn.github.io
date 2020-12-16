---
layout: default
title: delete dataset
parent: z. additional
grand_parent: Tutorials
---
Deleting a Dataset from Memory
-------------------------------

To delete the newly created second dataset, select
<span style="color: brown">File → Clear dataset(s)</span> or
<span style="color: brown">Edit → Delete dataset(s)</span> and enter the
dataset index, "2" as shown below, and press *OK*.


![Image:Delete.png]({{ site.baseurl }}/assets/images/Delete.png)


The second dataset will now be removed from the EEGLAB/Matlab
workspace. (Note: It is not necessary to switch back to the first
dataset before deleting the second. It is also possible to delete
several datasets at once from this window by entering their indices
separated by spaces.)

Storing a dataset
-----------------
Note that **storing the new dataset in Matlab memory does not
automatically store it permanently on disk**. 
To do this, select
<span style="color: brown">File → Save current dataset</span>. 

You may recover the previous dataset
using the <span style="color: brown">Dataset</span> top menu.
