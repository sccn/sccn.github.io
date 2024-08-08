import os
import subprocess
import sys
import json

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=False, text=True)
    if result.returncode != 0:
        print(f"Command failed: {command}\nError: {result.stderr}")
    return result

def update_repo(repo, formatted_name, order, plugin_type='readme', plugin_link="https://github.com/sccn"):
    print(f"Updating {repo}...")
    current_dir = os.getcwd()
    repo_path = os.path.join(current_dir, 'github', repo)
    
    if os.path.exists(repo_path):
        os.chdir(repo_path)
        run_command('git pull')
    else:
        run_command(f'git clone {plugin_link}.git {repo_path}')

    if plugin_type == "wiki":
        wiki_repo_path = f"{repo_path}.wiki"
        if os.path.exists(wiki_repo_path):
            os.chdir(wiki_repo_path)
            run_command('git pull')
        else:
            run_command(f'git clone {plugin_link}.wiki.git {wiki_repo_path}')
        
    os.chdir(current_dir)
    script = 'reformat_plugin.py'
    command = f'python {script} {repo_path} {repo} {formatted_name} {plugin_type} {order} {plugin_link}'
    run_command(command)

if __name__ == "__main__":
    # if 'github' not in current directory, create it
    if not os.path.exists('github'):
        os.makedirs('github')
    
    if not os.path.exists('plugins.json'):
        print('Error: plugins.json not found.')
        sys.exit(1)
    plugin_info = json.load(open('plugins.json'))
    plugins = [plugin['name'] for plugin in plugin_info]
    # wiki_plugins = ['SIFT', 'get_chanlocs', 'NFT', 'EEG-BIDS', 'nsgportal', 'clean_rawdata', 'amica', 'LIMO']
    # readme_plugins = ['ARfitStudio', 'roiconnect', 'trimOutlier', 'PACT', 'groupSIFT', 'nwbio', 'ICLabel', 'dipfit', 'eegstats', 'PowPowCAT', 'PACTools', 'zapline-plus', 'fMRIb', 'relica', 'std_dipoleDensity', 'imat', 'viewprops', 'cleanline','NIMA', 'firfilt']
    # ordering = ['ICLabel', 'dipfit', 'EEG-BIDS', 'roiconnect', 'amica', 'cleanline', 'clean_rawdata', 'SIFT', 'zapline-plus', 'eegstats', 'trimOutlier', 'fMRIb', 'imat', 'nwbio', 'NIMA', 'PACT', 'NFT', 'PACTools', 'ARfitStudio', 'PowPowCAT', 'relica', 'std_dipoleDensity', 'viewprops', 'firfilt', 'groupSIFT', 'get_chanlocs', 'nsgportal']
    
    if len(sys.argv) == 1:
        for plugin in plugin_info:
            update_repo(plugin['name'], plugin['name'], plugins.index(plugin['name']), plugin['type'], plugin['link'])
    elif len(sys.argv) == 2:
        plugin_name = sys.argv[1]
        if plugin_name not in plugins:
            print(f"Plugin {plugin_name} not found.")
            sys.exit(1)
        plugin = plugin_info[plugins.index(plugin_name)]
        update_repo(plugin['name'], plugin['name'], plugins.index(plugin['name']), plugin['type'], plugin['link'])
    else:
        print('Usage: python update_plugins.py <plugin_name>')
        sys.exit(1)
