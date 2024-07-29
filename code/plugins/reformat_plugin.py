import os
import sys
import shutil

# open a text file ending with .md and append a paragraph to it
def reformat_wiki_pages(filepath, filename, parent, output_file, wiki_input_dir=""):
    append_text = '''---
layout: default
title: {filename}
long_title: {filename}
parent: {parent}
grand_parent: Plugins
'''.format(filename=filename, parent=parent)

    if parent == "nsgportal":
        pages = []
        # load _Sidebar.md and extract all links from markdown file
        with open(os.path.join(wiki_input_dir, '_Sidebar.md')) as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('*'):
                    # extract text between square brackets
                    page = line[line.find('(')+1:line.find(')')]
                    pages.append(page)
        if filename in pages:
            order = pages.index(filename)
            append_text += 'nav_order: {order}\n'.format(order=order)
    
    append_text += '---\n'

    with open(filepath) as f:
        text = f.read()
        text = append_text + text
        with open(output_file, 'w') as out:
            out.write(text)

def reformat_plugin_dir(plugin_input_dir, plugin_name, order, plugin_type='wiki'):
    # plugins_output_dir = '/Users/dtyoung/Documents/EEGLAB/sccn.github.io/plugins'
    plugin_output_dir = os.path.join('../../plugins', plugin_name)
    if not os.path.exists(plugin_output_dir):
        os.makedirs(plugin_output_dir)

    # copy image directory from input to output dir
    if os.path.exists(os.path.join(plugin_input_dir, 'images')):
        shutil.copytree(os.path.join(plugin_input_dir, 'images'), os.path.join(plugin_output_dir, 'images'), dirs_exist_ok=True)
    # copy all .jpg and .png files from input to output dir
    for file in os.listdir(plugin_input_dir):
        if file.endswith('.jpg') or file.endswith('.png'):
            shutil.copyfile(os.path.join(plugin_input_dir, file), os.path.join(plugin_output_dir, file))
    
    # if plugin is 'imat', copy the Docs directory recursively to the output directory
    if plugin_name == 'imat':
        shutil.copytree(os.path.join(plugin_input_dir, 'Docs'), os.path.join(plugin_output_dir, 'Docs'), dirs_exist_ok=True)

    index_file = os.path.join(plugin_output_dir, 'index.md')
    shutil.copyfile(os.path.join(plugin_input_dir, 'README.md'), index_file)
    with open(index_file) as f:
        text = f.read()
        append_text = '''---
layout: default
title: {plugin_name}
long_title: {plugin_name}
parent: Plugins
has_children: true
nav_order: {order}
---
To view the plugin source code, please visit the plugin's [GitHub repository](https://github.com/sccn/{plugin_name}).

'''.format(plugin_name=plugin_name, order=order)
        text = append_text + text
        with open(index_file, 'w') as out:
            out.write(text)

    if plugin_type == 'wiki':
        wiki_plugin_input_dir = plugin_input_dir + '.wiki'

        # copy image directory from input to output dir
        if os.path.exists(os.path.join(wiki_plugin_input_dir, 'images')):
            shutil.copytree(os.path.join(wiki_plugin_input_dir, 'images'), os.path.join(plugin_output_dir, 'images'), dirs_exist_ok=True)
        # copy all .jpg and .png files from wiki input to output dir
        for file in os.listdir(wiki_plugin_input_dir):
            if file.endswith('.jpg') or file.endswith('.png'):
                shutil.copyfile(os.path.join(wiki_plugin_input_dir, file), os.path.join(plugin_output_dir, file))


        for root, dirs, files in os.walk(wiki_plugin_input_dir):
            for file in files:
                if file.endswith('.md') and not file.startswith('index') and not file.startswith('Home'):
                    reformat_wiki_pages(os.path.join(wiki_plugin_input_dir, file), file.strip('.md'), plugin_name, os.path.join(plugin_output_dir, file), wiki_plugin_input_dir)
# main
def main():
    if len(sys.argv) != 5:
        print('Usage: python test.py <plugin_dir_path> <plugin_name> <plugin_type> <nav_order>')
        sys.exit(1)
    dirpath = sys.argv[1]
    plugin_name = sys.argv[2]
    plugin_type = sys.argv[3]
    order = sys.argv[4]
    reformat_plugin_dir(dirpath, plugin_name, order, plugin_type)

if __name__ == "__main__":
    main()
