import os
import sys

# open a text file ending with .md and append a paragraph to it
# Usage: python test.py <filename>.md
def append_to_file(filepath, filename, parent):
    with open(filepath) as f:
        text = f.read()
        append_text = '''---
layout: default
title: {filename}
long_title: {filename}
parent: {parent}
grand_parent: Plugins
---
'''.format(filename=filename, parent=parent)
        text = append_text + text
    with open(filepath, 'w') as out:
        out.write(text)

def reformat_plugin_dir(dirpath, plugin_name):
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            if file.endswith('.md') and not file.startswith('index') and not file.startswith('Home'):
                append_to_file(os.path.join(root, file), file.strip('.md'), plugin_name)

# main
def main():
    if len(sys.argv) != 3:
        print('Usage: python test.py <plugin_dir_path> <plugin_name>')
        sys.exit(1)
    dirpath = sys.argv[1]
    plugin_name = sys.argv[2]
    reformat_plugin_dir(dirpath, plugin_name)

if __name__ == "__main__":
    main()