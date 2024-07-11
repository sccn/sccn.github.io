import os
import sys
import shutil

# open a text file ending with .md and append a paragraph to it
def reformat_plugin(dirpath, plugin_name):
    plugins_dir = '/Users/dtyoung/Documents/EEGLAB/sccn.github.io/plugins'
    index_file = os.path.join(plugins_dir, '{plugin_name}.md'.format(plugin_name=plugin_name))
    shutil.copyfile(os.path.join(dirpath, 'README.md'), index_file)
    with open(index_file) as f:
        text = f.read()
        append_text = '''---
layout: default
title: {plugin_name}
long_title: {plugin_name}
parent: Plugins
---
'''.format(plugin_name=plugin_name)
        text = append_text + text
        with open(index_file, 'w') as out:
            out.write(text)


# main
def main():
    if len(sys.argv) != 3:
        print('Usage: python README_plugin.py <plugin_dir_path> <plugin_name>')
        sys.exit(1)
    dirpath = sys.argv[1]
    plugin_name = sys.argv[2]
    reformat_plugin(dirpath, plugin_name)

if __name__ == "__main__":
    main()