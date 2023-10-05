---
layout: default
title: Setting up your lab
long_title: EEGLAB data structures
parent: Concepts guide
grand_parent: Tutorials
nav_order: 1
---

In this section, we describe how to set up your EEG lab, with a strong emphasis on obtaining good EEG data quality. 

Data quality is crucial for EEG research. Researchers depend on clean and precise data to draw valid conclusions about brain function and behavior.
If the collected EEG data contains artifacts or noise, it can introduce errors and bias, leading to invalidation of the hypothesis or misleading results. 
EEG recordings are susceptible to various artifacts, including muscle activity, eye blinks, environmental interference, and electrode impedance problems. These artifacts can introduce confounding factors, masking or distorting the true brain signals of interest. High-quality data minimizes the presence of artifacts, enhancing the accuracy of the observed brain activity and reducing confounds.

Cleaning up bad data or removing artifacts is a time-consuming and complex task. Poor data quality increases the workload on researchers, as they have to spend significant time and effort identifying and removing unwanted signals. Importantly, very often, it is not even possible to remove artifacts from EEG data, and doing so can [decrease statistical power](https://www.nature.com/articles/s41598-023-27528-0). By ensuring high-quality data from the beginning, the analysis process becomes more efficient, saving time and resources. 

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

# Pre-registration

Once your study has been funded, you might want to preregister it).

Preregistration in science refers to the practice of specifying the details of a scientific study (e.g., research question, methods, data analysis plan) before the data is collected or analyzed. This approach has several advantages:

1. Reduces biases: Preregistration helps prevent the problem of "HARKing" (Hypothesizing After Results are Known) and other forms of bias. By declaring research plans in advance, researchers reduce the temptation to selectively report or analyze only the results that support their hypotheses, which ensures greater transparency and integrity in scientific research. It does not mean that you cannot conduct exploratory analyses, only that you will need to indicate so in your paper.

2. Reproducibility: Preregistration enhances research reproducibility by providing a clear record of the original study plan. 

3. Eliminates p-hacking and data dredging: Preregistration discourages the practice of p-hacking, which involves selectively analyzing or reporting data until a desired statistically significant result is achieved. It also prevents data dredging or "fishing" for statistically significant patterns by exploring multiple hypotheses or variables without clear a priori reasoning.

4. Methodological transparency: Preregistration promotes transparency by requiring researchers to disclose detailed information about the study design, sample size, data collection procedures, and analysis plans. This transparency allows readers to better evaluate the quality and reliability of the conducted research, reducing the chance of publishing erroneous or misleading findings.

5. Improves study design: The process of preregistration encourages researchers to carefully plan and justify their study aims, methods, and statistical analyses in advance. Often, you will see small things that could be improved in your design as you lay down all the details. This leads to a more thoughtful and robust study design and reduces the likelihood of post hoc changes that might compromise the validity of the results.

6. Reduces publication bias: Preregistration helps combat publication bias, where studies with significant or exciting results tend to be published more often than those with nonsignificant or less interesting findings. By preregistering studies, researchers can diminish this bias, as journals are more open to publishing studies with preregistration records regardless of the obtained results.

Overall, preregistration in science promotes transparency, reduces biases, enhances reproducibility, and improves the overall quality of research, contributing to the advancement of knowledge and scientific progress. There are also now 100 journals that publish study protocols before the manuscript is published (see the bottom of this [page](https://hsls.libguides.com/scholarly-communication/where-should-i-publish) for more information). 

The added advantage of pre-registration is **decreased stress** for the researcher. You have already planned everything, and most journals (including prestigious ones) will publish negative results (especially if they published your protocol). 

# Which EEG system to use

There are several reputable EEG (electroencephalography) research systems available on the market. Most are being made by companies that have been there for decades. 

*. BrainAmp series by Brain Products: Known for its high system, these systems offer various amplifier options and software solutions. Offers a convenient way to check the impedance on the cap with LEDs.

*. BioSemi ActiveTwo: This active electrode system provides excellent signal quality, low noise, and is known for its ease of use. Because this company only offers one system and provides no analysis software, it is often cheaper than other solutions. This company is known for its CMS/DRL noise reduction (see below) although other companies use it too. It is also known for not directly measuring electrode impedance (instead using a custom offset) and this annoys a lot of researchers.

*. Neuroscan by Compumedics: This is the oldest company, comparable to Brainamps, with more focus on clinical research.

*. g.Nautilus by g.tec: A wireless and mobile EEG system designed for neurofeedback and brain-computer interface (BCI) applications. 

*. ANT Neuro: A company created more than two decades ago like BrainAmps. 

*. EGI/Magstim (formerly Philips Neuro): Known for its water-based electrode system (as compared to gel-based), this company has changed hands several times. The hardware is solid and their gel caps are considered some of the best in the industry. Innovation at this company has slowed down in the past decade since it changed hands twice. However, BIOSEMI is still using the same amplifiers. EEG does not evolve that fast.

We have personally worked with all of these systems. Collecting EEG data is not rocket science, and the quality of the data is likely more linked to the cap than the EEG amplifier which use decade old technology.

# Active vs. passive electrode

Active and passive EEG electrodes are two types of electrodes used in electroencephalography (EEG) to measure brain activity. Here are the key differences between active and passive EEG electrodes:

1. Design: 
   - Active electrodes: These electrodes have built-in amplification circuitry, which amplifies the weak electrical signals received from the brain before transmitting them to the EEG recording system. 
   - Passive electrodes: These electrodes do not have built-in amplification circuitry and directly transmit the low voltage electrical signals from the brain to the EEG recording system.

2. Noise Reduction: 
   - Active electrodes: Due to their built-in amplification circuitry, active electrodes can amplify the weak brain signals closer to the scalp, minimizing the effect of noise and interferences. 
   - Passive electrodes: Since they lack amplification circuitry, passive electrodes are vulnerable to picking up more noise and interferences, which can affect the quality of the recorded EEG signals.

3. Input Impedance: 
   - Active electrodes: They typically have a very high input impedance, meaning they draw very little current from the scalp, reducing the contact impedance between the electrode and the scalp. 
   - Passive electrodes: These electrodes often have higher contact impedance, as they do not have acamplification circuitry. This can result in a higher contact impedance and potentially lead to signal distortions.

4. Signal Quality: 
   - Active electrodes: With their built-in amplification circuitry and low noise characteristics, active electrodes tend to provide higher signal quality and better signal-to-noise ratio compared to passive electrodes. 
   - Passive electrodes: Due to their susceptibility to noise and interferences, passive electrodes may have lower signal quality and a lower signal-to-noise ratio.

5. Complexity and Cost: 
   - Active electrodes: Active electrodes are typically more complex and sophisticated, as they require additional circuitry for signal amplification. This complexity can lead to higher manufacturing costs. 
   - Passive electrodes: Passive electrodes are simpler in design and do not require additional amplification circuitry, making them less complex and cheaper to manufacture.

6. Scalp Preparation: 
   - Active electrodes: Since active electrodes have a higher input impedance, they typically require less scalp preparation, such as cleaning or application of conductive gel, to ensure good electrical contact. 
   - Passive electrodes: Due to a potentially higher contact impedance, passive electrodes may require more thorough scalp preparation, including cleaning and gel application, to achieve optimal electrical contact.

In summary, active electrodes have built-in amplification circuitry, provide better noise reduction, higher signal quality, and have higher input impedance compared to passive electrodes. However, they are more complex and expensive. Passive electrodes, on the other hand, lack built-in amplification circuitry and may pick up more noise and interferences, resulting in lower signal quality. They are simpler and cheaper but require more thorough scalp preparation for optimal contact.
In practice, in the last decade, most of the EEG manufacturers sell active electrode systems, and they should be prefered for most applications.

## What is CMS/DRL correction?

CMS/DRL correction stands for common mode sense/difference mode sense-driven reference level correction. It is a technique used to reduce the influence of common mode noise on the recorded brain signals.

EEG signals are susceptible to various types of noise, including common mode noise, which refers to noise that is present on both the active electrode (recording electrode on the scalp) and the reference electrode. This common noise can interfere with the accurate measurement of brain activity.

CMS/DRL correction involves using additional electrodes placed on the subject's body (or on the scalp) to measure the common mode and difference mode signals. The common mode signal represents the noise present on both the active and reference electrodes, while the difference mode signal represents the actual brain signal of interest.

By utilizing these extra electrodes, the CMS/DRL correction technique effectively subtracts the common mode noise from the recorded EEG signal, leaving primarily the brain activity. This correction helps improve the signal quality and increases the accuracy of EEG analysis by reducing the impact of external interference and noise sources.

Overall, CMS/DRL correction is a valuable method for enhancing the signal-to-noise ratio and obtaining more reliable EEG measurements. The Biosemi company is known for this system although it might also be used by other companies (the Muse system also uses it). This type of correction is not needed when the EEG signal is recorded in a faraday cage. 

# Dry vs. wet electrodes

Dry electrode versus "wet" cap vs "water-based" cap. Dry electrodes and "wet" caps are both types of electrodes used in electroencephalography (EEG) to measure brain activity. However, they differ in terms of their contact with the scalp and the use of conductive materials.

*. Dry electrodes: 
- Dry electrodes do not require the use of conductive gels or creams to establish contact with the scalp.
- They are typically made of carbon or metal and have a system built within the electrode to improve conductivity.
- Advantages:
  - Easy to use and less messy compared to wet electrodes.
  - Faster setup time as there is no need to apply conductive gels.
- Disadvantages:
  - Generally, lower signal quality due to reduced contact with the scalp.
  - Sometimes rigid so heavier
  - More susceptible to environmental noise and movement artifacts.
  - Reduced signal stability over long periods of time.
  - increased pressure to keep contact that can lead to subject headaches

*. "Wet" caps (also known as gel electrodes):
- "Wet" caps use conductive gels or creams to establish a good electrical connection between the electrode and the scalp.
- These caps consist of several electrodes embedded in a flexible cap or a headgear.
- Advantages:
  - Better contact with the scalp resulting in higher signal quality and reduced noise.
  - More stable signals
- Disadvantages:
  - Takes time to set up (about 30 minute to 1 hour)
  - Subjects have gel in their hair and often need to wash their hair at the end of the experiment
  - Require time-consuming cleaning process

*. "Water-based" caps (e.g. EGI company or Emotiv):
- "water-based" caps use saline water instead of conductive gels or creams to establish an electrical connection between the electrode and the scalp.
- These caps consist of several electrodes embedded in a flexible cap or a headgear.
- Advantages:
  - Quick set up time
  - Subject may have slightly wet hair at the end of the experiment, but might not need to wash their hair right away
- Disadvantage:
  - Water bridges can form (direct connection between two channels) which can create later problems during data analysis. This is especially a problem for high-density systems (128 channels or more).
  - Electrodes dry up and may need to be re-wet every 20 minutes

In general, because data quality is essential, research should be conducted with a wet gel-based system. Then, in case this is not possible, a water-based system is the second best choice (for example, in clinical applications or applications with kids). Dry electrodes are the last choice, although it makes sense to use them when embedded in an audio headset, a VR system, or an earbud. 

What about consumer-grade EEG systems, for example:

5. Emotiv Epoc+: A 16-channel consumer-grade EEG system that offers a more affordable and accessible option. It is suitable for basic brain activity monitoring and is often used in gaming and entertainment applications.

This is by no means an exhaustive list, and there are many other reputable EEG systems available. The best choice ultimately depends on the specific requirements, budget, research needs, and intended application of the EEG system.

# Maximizing EEG data quality


Most of these items are true for most

Using the syringe filled with gel, pushing down on the electrode well (so the gel doesn’t spread to other parts of the cap), part the participant’s hair with the needle until you reach the skin. Then squeeze a small amount of gel into each well. Press firmly but not so firmly that the subject experiences pain
DO NOT PUT TOO MUCH GEL IN, otherwise the gel will spread between electrode wells across the scalp, merging multiple distinct EEG signals into one
Once all the wells have been filled, take the cable banks and match the number on the cable electrode to the electrode well label; pop them in one by one using one cable per colored section
The letters on the cable bank do not have to match the letters on the electrode well labels (if bank A is unavailable, bank E can be used in place of bank A)
Any other cable bank letter can be substituted as long as the numbers match up (cable E1 can go into electrode well A1 on the cap, cable E2 into A2, etc.)
Checking impedances
Connect the banks to the top of the amplifier in the order that they are attached on the cap (section A on the cap, then section B, then section C etc.)
Do not follow the alphabetical order of the cable bank designation because they might not correspond to the letter of the section on the cap
Connect the other end of the USB cable that’s plugged into the receiver to the far right monitor used for the control computer
On the Desktop, open ActiView, a BioSemi data viewing and recording software, on the control computer
Press Start at the top left to view the live streaming EEG data
