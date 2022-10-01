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
These questions were compiled by Arnaud Delorme. Most of the answers are from Cyril Pernet, the main author of LIMO.

* **Question: Are the bootstrap only 2nd level, or can you do it 1st level as well when you look at a single subject?** Bootstrap statistics are only at the second level.

* **Question: Are contrast only for 2nd level post-hoc on ANOVA analyses?** No, contrast can be calculated at the first level as well.

* **Question: Is there a difference between (A) computing a paired t-test at the group (2nd) level between two level 1 beta parameters (conditions 1 and 2), and (B) computing a contrast between conditions 1 and 2 at the (1st) single subject level (difference of the two betas), and then computing a one-sample t-test at the group level on that difference?** In theory, this is equivalent. However, LIMO uses robust statistics and uses Yuen t-test at the group level, so it is preferable to use the t-test at the group level (solution A).

* **Question: Can I process more than two groups of subjects in LIMO?** You can, but you cannot do more than two nested groups at a time for second-level statistics.

* **Question: What is the limit in terms of the number of 1st-level variables?** There are no limits. You can have as many categorical and continuous variables as you want. 

* **Question: What do I sometimes get errors when using Weighted Least Square (WLS) optimization at the 1st level?** WLS requires that you have more trials than samples. You can reduce the time window or frequency range to decrease the number of samples. This is not a problem with Ordinary Least Square. IRLS (Iterated Reweighted Least Square) is the best method but is likely not to be used in practice because it is too slow compared to WLS, and the gain is minimal.

* **Question: I have two sessions per subject and a continuous var (questionnaire) for each session. How do I calculate the interaction between sessions and the continuous var?** You would want to use repeated measure ANOVA with covariate, but this is not in LIMO right now (maybe check old_rep_ANOVA.m). An ANCOVA could be used, but you would lose the fact that the sessions are paired across subjects. For an ANCOVA, you would want to store a text file that contains an extra column with the product for the interaction. If you have two sessions and a continuous variable with x1 to x4, the last column could contain (-x1, -x2, x3, x4). In theory, you would have a text file with two categorical variables, one continuous variable, and one interaction. For example, if x1=1, x2=2, x3=3, and x4=4, the text file would contain
```
1  0  1  -1
1  0  2  -2
0  1  3  3
0  1  4  4
```
> However, in practice, since it is difficult to know which variables are categorical and which are continuous without asking the user, you will need to provide 2 lists of betas, one for session 1 and one for session 2, and your covariate file will contain:
```
1  -1
2  -2
3  3
4  4
```
> If a continuous variable is at the first level (reaction time, for example), the function [limo_split_continuous.m](https://github.com/LIMO-EEG-Toolbox/limo_tools/blob/master/limo_split_continuous.m) may also be used to split a continuous variable for each categorical variable at the 1st level. So if you have one continuous variable, you will get 2 beta parameters, one for session 1 and one for session 2 (this can be done from the LIMO GUI - first LIMO menu in EEGLAB). Then the interaction term between sessions and the continuous variable can then be calculated at the second level using an ANCOVA.

* **Question: I have reaction time in a go-nogo task where 50% of the stimuli are target stimuli, and the other 50% are distractors (subjects are not supposed to respond to distractors). I want to analyze correct responses (response on the go target trials and no response on no-go non-target trials). Is there a way to include the reaction time as a covariate even though I do not have reaction time for distractors?** Yes, this is totally possible. This would be a level 1 analysis across trials. For distractors, you would set the reaction time to 0, which means these trials will be ignored for the covariate analysis with reaction time. However, you would not be able to compute the interaction between reaction time and trial type since you do not have reaction time for distractors. At the second level, you can perform a paired t-test on the trial type (target vs. distractor) and a one-sample t-test on the reaction time beta parameter.

* **Question: I have 9 types of visual stimuli, 3 types of faces, and 3 repetitions for each stimulus (presentations 1, 2 and 3). I want to look at the differences between faces. What is the best way of doing that in LIMO?** If you have a variable in EEGLAB that contains the type of face (irrespective of the repetition), you could use that at the first level, then perform an ANOVA between the three types of faces at the second level. However, a better solution is to enter both face type and repetition at the first level (to obtain a total of 9 betas), then build three contrasts to group (meaning compute the average) the betas for the 3 repetitions for the 3 types of face, and then compute an ANOVA at the 2nd level to compare the 3 contrasts. In EEGLAB, you can group the types of faces when creating a STUDY design, and the contrasts will be created automatically. The advantage of this solution is that repetition is included in the model, and so variation of the signal due to repetitions is accounted for. The third solution is to use repetition and face for the 1st level model (so 9 betas), perform a 2-way ANOVA at the 2nd level (Faces x Repetition), and then look at the main effect for faces. However, if you are not interested in repetitions, this solution is suboptimal, as the two-way ANOVA will decrease statistical power when compared to the one-way one. 
* 
* The best way to do that in LIMO is to create a 1st level contrast 
