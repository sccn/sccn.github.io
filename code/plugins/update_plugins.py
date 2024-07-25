import os
import subprocess
import sys

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=False, text=True)
    if result.returncode != 0:
        print(f"Command failed: {command}\nError: {result.stderr}")
    return result

def update_repo(repo, order, plugin_type='readme'):
    print(f"Updating {repo}...")
    current_dir = os.getcwd()
    repo_path = os.path.join(current_dir, 'github', repo)
    
    if os.path.exists(repo_path):
        os.chdir(repo_path)
        run_command('git pull')
    else:
        run_command(f'git clone https://github.com/sccn/{repo}.git {repo_path}')

    if plugin_type == "wiki":
        wiki_repo_path = f"{repo_path}.wiki"
        if os.path.exists(wiki_repo_path):
            os.chdir(wiki_repo_path)
            run_command('git pull')
        else:
            run_command(f'git clone https://github.com/sccn/{repo}.wiki.git {wiki_repo_path}')
        
    os.chdir(current_dir)
    script = 'reformat_plugin.py'
    command = f'python {script} {repo_path} {repo} {plugin_type} {order}'
    run_command(command)

if __name__ == "__main__":
    # if 'github' not in current directory, create it
    if not os.path.exists('github'):
        os.makedirs('github')
    wiki_plugins = ['SIFT', 'get_chanlocs', 'NFT', 'PACT', 'nsgportal', 'clean_rawdata', 'amica']
    readme_plugins = ['ARfitStudio', 'roiconnect', 'EEG-BIDS', 'trimOutlier', 'groupSIFT', 'nwbio', 'ICLabel', 'dipfit', 'eegstats', 'PowPowCAT', 'PACTools', 'zapline-plus', 'fMRIb', 'relica', 'std_dipoleDensity', 'imat', 'viewprops', 'cleanline','NIMA', 'firfilt']
    ordering = ['ICLabel', 'dipfit', 'EEG-BIDS', 'roiconnect', 'amica', 'cleanline', 'clean_rawdata', 'SIFT', 'zapline-plus', 'eegstats', 'trimOutlier', 'fMRIb', 'imat', 'nwbio', 'NIMA', 'PACT', 'NFT', 'PACTools', 'ARfitStudio', 'PowPowCAT', 'relica', 'std_dipoleDensity', 'viewprops', 'firfilt', 'groupSIFT', 'get_chanlocs', 'nsgportal']
    
    if len(sys.argv) == 1:
        order = 1
        for plugin in wiki_plugins:
            update_repo(plugin, order, 'wiki')
            order += 1
        for plugin in readme_plugins:
            update_repo(plugin, order, "readme")
            order += 1
    elif len(sys.argv) == 2:
        plugin_name = sys.argv[1]
        if plugin_name not in wiki_plugins and plugin_name not in readme_plugins:
            print(f"Plugin {plugin_name} not found.")
            sys.exit(1)

        plugin_type = 'wiki' if plugin_name in wiki_plugins else 'readme'
        plugin_order = ordering.index(plugin_name) + 1

        update_repo(plugin_name, plugin_order, plugin_type)
    else:
        print('Usage: python update_plugins.py <plugin_name>')
        sys.exit(1)
