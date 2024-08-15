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

    # write index file
    with open('../../plugins/index.md', 'w') as index_file:
        text = '''---
layout: default
title: Plugins
has_children: true
has_toc: true
nav_order: 7
---
# EEGLAB plugin documentation

Below is a list of plugins that have documentation copied from GitHub. Please note that this is only a small subset of all EEGLAB plugins, as not all plugin documentation is compatible with visualization and search functionalities on the EEGLAB website. The complete list of plugins can be found [here](https://sccn.ucsd.edu/eeglab/plugin_uploader/plugin_list_all.php).

'''
        for cat in ['import', 'processing']:
            text += f'## {cat.capitalize()}\n'
            for plugin in [plugin for plugin in plugin_info if plugin['cat'] == cat]:
                text += f'* [{plugin["name"]}](/plugins/{plugin["name"]}): {plugin["desc"]}\n'
            
            text += '\n'
        
        index_file.write(text)

    
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
