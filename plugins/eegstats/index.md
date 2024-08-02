---
layout: default
title: eegstats
long_title: eegstats
parent: Plugins
has_children: true
nav_order: 9
---
To view the plugin source code, please visit the plugin's [GitHub repository](https://github.com/sccn/eegstats).

# EEGSTATS plugin for EEGLAB

This plugin computes frequency band power, alpha peak frequency, and alpha asymmetry. It uses the [restingIAF](https://github.com/corcorana/restingIAF) MATLAB code for some computation.

## Do not download GitHub zip file

You will miss the resting IAF code dependency when downloading the zip file. Instead, download the plugin from the EEGLAB extension manager or clone the repository as indicated below.

## Checkout repository

Make sure to copy the submodule when you clone the repository. You may clone the repository in the **plugins** folder of EEGLAB, and the plugin will behave as if you had downloaded it from the EEGLAB plugin manager.

```
git clone --recurse-submodules https://github.com/arnodelorme/eegstats.git
```

## Graphic interface

The plugin may be used from the command line or from its GUI. After installing the plugin using the EEGLAB plugin manager (EEGLAB menu item **File > Manage EEGLAB extensions**), you may load the tutorial dataset "eeglab_data.set" from the "sample_data" folder of eeglab (or simply type "eeglab cont" on the MATLAB command line). Then use EEGLAB menu item **Tools > EEG freq/power statistics** and following UI will pop up. In this UI, you may select frequency ranges of interest, electrodes, and other spectral parameters. You may also select to compute individual alpha frequency or alpha asymmetry between electrodes of your choice. See the [pop_eegstats.m](https://github.com/arnodelorme/eegstats/blob/master/pop_eegstats.m) header for more information.

![](eegstats_gui.png)

Some statistics are then shown on the command line

```
All_channels	FPz	EOG1	F3	Fz	F4	EOG2	FC5	FC1	FC2	FC6	T7	C3	C4	Cz	T8	CP5	CP1	CP2	CP6	P7	P3	Pz	P4	P8	PO7	PO3	POz	PO4	PO8	O1	Oz	O2
4.0-6.0 Hz	10.32874	14.22889	9.67149	12.15102	12.52194	11.41491	8.32056	10.92951	12.55692	12.12547	8.74618	9.27780	11.43005	10.23406	11.97217	5.81186	10.17836	11.12828	10.86633	8.35843	8.59615	10.46200	11.01924	9.80405	5.81822	8.94987	10.24260	9.81776	9.67905	7.94379	7.86885	7.36514	7.68011
8.0-12.0 Hz	14.34564	12.88388	8.29599	14.23616	14.09646	13.61207	9.33680	12.95503	14.09473	13.81112	11.21125	11.13318	14.51065	14.45228	14.24638	7.63537	13.54019	15.94191	16.27163	12.39869	12.74183	16.26172	17.82588	15.80787	10.10653	14.83628	17.25089	17.70982	16.13902	13.31741	14.39267	14.11222	14.18022
18.0-22.0 Hz	1.53140	1.74260	0.55711	3.41521	3.20146	2.81724	0.85928	1.97687	3.33149	3.07455	-0.56236	-0.14296	2.92429	1.89127	2.88576	-3.66506	0.96043	2.88402	2.55589	-0.95219	0.18848	2.11160	2.82488	1.41511	-3.05001	1.16790	2.55386	1.59623	1.61312	-0.32435	0.27099	-0.79813	-0.42993
30.0-45.0 Hz	-4.74193	-3.59272	-2.38355	-3.85762	-4.05003	-4.10457	-2.61030	-4.35485	-3.92142	-4.00219	-6.27543	-4.97281	-4.64989	-5.83781	-4.21922	-6.76074	-5.47909	-5.13860	-5.41030	-6.93733	-4.21273	-5.34485	-5.09403	-5.76578	-6.73008	-3.97376	-4.63646	-5.62076	-5.15805	-5.44294	-4.68207	-5.68633	-5.11051
Peak alpha frequency	9.68	8.50	NaN	9.00	8.50	9.00	NaN	9.00	9.00	9.00	9.00	9.50	9.50	9.50	9.50	9.50	9.50	10.00	10.00	10.00	9.50	10.00	10.00	10.00	9.50	9.50	10.00	10.00	10.00	10.00	10.00	10.00	10.00
Alpha center of gravity	9.36	8.65	8.88	8.94	8.87	8.99	8.97	9.12	8.99	9.05	9.14	9.16	9.45	9.46	9.27	9.13	9.44	9.58	9.56	9.44	9.32	9.64	9.72	9.61	9.39	9.58	9.75	9.83	9.70	9.61	9.71	9.74	9.73
Alpha Asymmetry	0.62408
```

You can also recover these statistics using the command line call (see function help for more information):

```matlab
[power, iafSum, iafChan, freqs] = pop_eegstats(EEG, 'thetarange',[4 6] ,'alpharange',[8 12] , ...
            'otherranges',[18 22;30 45],'averagepower','off','channels','','winsize',2, ...
            'overlap',1,'iaf','on','iafminchan',1,'alphaasymmetry','on','asymchans','F3 F4', ...
            'csvfile','save_these_results.csv');
```

## Group analysis (beta)

The **EEG.etc.eegstats** structure contains the saved EEG spectral statistics. Assuming you have created an EEGLAB study (requires EEGLAB 2024.0 or later version), you may compute EEG statistics on all the datasets (the plugin is compatible with processing an entire EEGLAB STUDY). Then, from the EEGLAB command line, you may recover specific fields for all datasets. You can use the ***std_readdata*** function to read the data from all datasets (this uses the default STUDY design in STUDY.currentdesign -- otherwise, you can also specify the design when calling the ***std_readdata*** function by setting the 'design' parameter).

```matlab
[STUDY,aa,xvals,~,~,~,~,info] = std_readdata(STUDY, ALLEEG, 'customread', 'std_readeegfield', ...
                          'customparams', {{ 'etc', 'eegstats', 'alpha_asymmetry' }}, 'ndim', 1);
```
Then you can perform statistics using EEGLAB building functions. 

```
[~,p] = std_stat(aa, 'groupstats', 'on'), % perform some statistics based on the current STUDY design

p =

  1×1 cell array

    {[0.0345]}
```

Or convert the data to a table, and perform statistics using MATLAB statistics toolbox or using external software. The table below was obtained by applying these commands to a subset of the STERN EEGLAB STUDY available on this [page](https://eeglab.org/tutorials/tutorial_data.html)

```matlab
res = std_cell2table([], [], aa, info, 'design', STUDY.design(2),  'dimensions', {'subjects' 'alpha_asymmetry' })
writetable(res, 'mydata.csv'); % this writes the data to disk

res =

  4×3 table

     condition      subjects    alpha_asymmetry
    ____________    ________    _______________

    {'ignore'  }       1            -1.4385    
    {'ignore'  }       2              1.882    
    {'memorize'}       1            -1.1305    
    {'memorize'}       2             1.9947    
```


## Version history

v1.2 - better STUDY support

v1.1 - better output formating and saving results in EEG structure

v1.0 - initial version
