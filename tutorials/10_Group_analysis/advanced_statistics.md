---
layout: default
title: g. Advanced statistics
long_title: e. Advanced statistics
parent: 10. Group analysis
grand_parent: Tutorials 
has_toc: true
---

![kids-under-construction-clipart-1050_450-1024x439-1](https://user-images.githubusercontent.com/1872705/190218156-204dee28-4774-4fa6-831b-174d60c93ac5.png)

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

* **Question: What do I sometimes get errors when using Weighted Least Square (WLS) optimization at the 1st level?** WLS requires that you have more trials than samples. You can reduce the time window or frequency range to decrease the number of samples. This is not a problem with Ordinary Least Square.

* **Question: I have 2 sessions per subject and a continuous var (questionnaire) for each session. How do I calculate the interaction between sessions and the continuous var?** You would want to use repeated measure ANOVA with covariate but this is not in LIMO right now (maybe check old_rep_ANOVA.m). An ANCOVA could be used but you would loose the fact that the sessions are paired accross subject. For an ANCOVA, you would want to store a text file that contains an extra column with the product for the interaction. If you have 2 sessions and a continuous variable with x1 to x4, the last column could contain (-x1, -x2, x3, x4). In theory you would have a text file with 2 categorical variables, one continuous variable and 1 interaction. For example if x1=1, x2=2, x3=3 and x4=4, the text file would contain
```
1  0  1  -1
1  0  2  -2
0  1  3  3
0  1  4  4
```
> However, in practice, since it is difficult to know which variables are categorical and which are continuous without asking the user, you will need to select 2 list of betas, one for session 1 and one for session 2, and your covariate file will contain
</blockquote>

```
1  -1
2  -2
3  3
4  4
```

> The function [limo_split_continuous.m](https://github.com/LIMO-EEG-Toolbox/limo_tools/blob/master/limo_split_continuous.m) may be used to create interaction terms with continuous variables.


