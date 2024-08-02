---
layout: default
title: Between-Subjects-Categorical-Designs
long_title: Between-Subjects-Categorical-Designs
parent: LIMO
grand_parent: Plugins
---
We replicate here the 1-way ANOVA with familiar, unfamiliar and scrambled faces but split the data in two age groups. Of course, we can take the txt files, edit them and save copies for each group – then in LIMO MEEG we simply use these files. Here, instead, we recompute the subjects model adding in the STUDY design our groups, which will consequently save txt files per group (but not change estimates per subjects). Since some subjects have unspecified age – we create three groups based on the median (figure 35).  

Group 1 is under 26: sub- 3, 8, 15, 16, 17, 18  
Group 2 is above or equal 26: sub- 2, 5, 9, 10, 11, 12, 14  
Group 3: sub- 4, 6, 7, 13, 19 unspecified  

![Figure 35. Edit study](https://github.com/LIMO-EEG-Toolbox/limo_meeg/blob/master/resources/images/35.jpg) 
_Figure 35. Editing STUDY adding groups_

You can update the study using pop_study typing in command line:
```matlab
cd(STUDY.filepath)
[STUDY ALLEEG] = std_editset( STUDY, ALLEEG, 'commands',{{'index',2,'group','1'}, ...
    {'index',7,'group','1'},{'index',14,'group','1'},{'index',15,'group','1'}, ...
    {'index',16,'group','1'},{'index',17,'group','1'},{'index',1,'group','2'}, ...
    {'index',4,'group','2'},{'index',8,'group','2'},{'index',9,'group','2'}, ...
    {'index',10,'group','2'},{'index',11,'group','2'},{'index',13,'group','2'}, ...
    {'index',3,'group','3'},{'index',5,'group','3'},{'index',6,'group','3'}, ...
    {'index',12,'group','3'}, {'index',18,'group','3'}}, 'updatedat','off','rmclust','on');
[STUDY, EEG] = pop_savestudy( STUDY, EEG, 'savemode','resave');
```

Estimate the models, selecting the 1st design with face type only. As before, text files are created, with additionally a split per group of LIMO/Beta/con files. 

From here, we can perform two 2nd level analyses:
- [Between subjects’ ANOVAs with repeated factors](https://github.com/LIMO-EEG-Toolbox/limo_meeg/wiki/9.-Between-subjects%E2%80%99-ANOVAs-with-repeated-factors)
- [Two sample t-tests](https://github.com/LIMO-EEG-Toolbox/limo_meeg/wiki/10.-Two-sample-t-tests)


