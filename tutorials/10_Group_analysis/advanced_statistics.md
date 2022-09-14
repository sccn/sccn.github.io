---
layout: default
title: g. Advanced statistics
long_title: e. Advanced statistics
parent: 10. Group analysis
grand_parent: Tutorials 
has_toc: true
---

Study Statistics and Visualization Options
============================================
{: .no_toc }

Advanced statistics are performed in LIMO (Linear Modeling of EEG data), an EEGLAB plugin, primarily developped by Cyril Pernet in collaboration with Arnaud Delorme. 
The [LIMO toolbox](https://limo-eeg-toolbox.github.io/limo_meeg/) allows you to use general linear modeling approaches on an arbitrarilly large 
number of categorical and continuous variables. The EEGLAB team have recently developed a more user friendly interface for LIMO, that directly interfaces EEGLAB variables.
The documentation about the old version of LIMO is available [here](https://github.com/LIMO-EEG-Toolbox/limo_meeg/wiki). You may also refer to the
[LIMO tutorial video series](https://www.youtube.com/embed/videoseries?list=PLXc9qfVbMMN2Vrzte9ul3nrrG8AgB5OkU).

Difference between optimization methods 
- Ordinary Least Square (WLS): This is the simplest and fastest method. Same as using the MATLAB glmfit function.
- Weighted Least Square (WLS): The default. This method attributes some weight to individual trials based their outlier likelyhood.
- Iterated Reweighted Least Square (IRLS): The default. This method attributes some weight to individual trials based their outlier likelyhood.
 
LIMO Faq.
------
These questions were answered by Cyril Pernet.

* **Question: Are the bootstrap only 2nd level or can you do it 1st level as well when you look at a single subject?** Bootstrap statistics are only at the second level.

* **Question: Are contrast only for 2nd level post-hoc on ANOVA analyses?** No, contrast can be calculated at the first level as well.

* **Question: Is there a difference between a paired t-test at the group level between condition 1 and 2, and computing a contrast between condition 1 and 2 at the single subject level, and then computing a one-sample t-test at the group level on that difference?** In theory this is equavalent. However, LIMO uses robust statistics, and uses Yuen t-test at the group level. It is preferable to use the t-test at the group level. 

* **Question: Can I process more than 2 groups of subjects in LIMO?** You can, but you cannot do more than 2 nested groups at the time for second-level statistics.

* **Question: What is the limit in terms of number of 1st-level variables?** There is no limits. You can have as many categorical and continuous variables as you want. 

* **Question: What do I sometimes get errors when using Weighted Least Square (WLS) optimization at the 1st level?** WLS requires that you have more trials than samples. You can reduce the time window or frequency range to decrease the number of samples. This is not a problem with Ordinary Least Square.

