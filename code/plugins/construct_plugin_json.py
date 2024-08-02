import json
ordering = ['ICLabel', 'dipfit', 'EEG-BIDS', 'roiconnect', 'amica', 'cleanline', 'clean_rawdata', 'SIFT', 'zapline-plus', 'eegstats', 'trimOutlier', 'fMRIb', 'imat', 'nwbio', 'NIMA', 'PACT', 'NFT', 'PACTools', 'ARfitStudio', 'PowPowCAT', 'relica', 'std_dipoleDensity', 'viewprops', 'firfilt', 'groupSIFT', 'get_chanlocs', 'nsgportal']
naming = ['ICLabel', 'dipfit', 'EEG-BIDS', 'roiconnect', 'amica', 'cleanline', 'clean_rawdata', 'SIFT', 'zapline-plus', 'eegstats', 'trimOutlier', 'fMRIb', 'imat', 'nwbio', 'NIMA', 'PACT', 'NFT', 'PACTools', 'ARfitStudio', 'PowPowCAT', 'relica', 'std_dipoleDensity', 'viewprops', 'firfilt', 'groupSIFT', 'get_chanlocs', 'nsgportal']
wiki_plugins = ['SIFT', 'get_chanlocs', 'NFT', 'EEG-BIDS', 'nsgportal', 'clean_rawdata', 'amica', 'LIMO']
readme_plugins = list(set(ordering) - set(wiki_plugins))

plugin_json = []
for plugin in ordering:
     ptype = 'wiki' if plugin in wiki_plugins else 'readme'
     link = f'https://github.com/sccn/{plugin}'
     plugin_json.append({'plugin': plugin, 
                         'name': naming[ordering.index(plugin)],
                         'type': ptype, 
                         'link': link})

with open('plugins.json', 'w') as out:
    json.dump(plugin_json, out, indent=2)