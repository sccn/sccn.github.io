import os
import sys
import shutil

def clean_filename(filename):
    filename = filename.replace(' ', '_')
    filename = filename.replace('(', '')
    filename = filename.replace(')', '')
    filename = filename.replace(',', '')
    filename = filename.replace(';', '')
    filename = filename.replace(':', '')
    filename = filename.replace('/', '')
    return filename
# open a text file ending with .md and append a paragraph to it
def reformat_wiki_pages(filepath, filename, parent, output_file, wiki_input_dir=""):
    append_text = '''---
layout: default
parent: {parent}
grand_parent: Plugins
render_with_liquid: false
'''.format(filename=filename, parent=parent)

    print(f"Reformatting {filename} of {parent}...")
    if parent in ["nsgportal"]:
        pages = []
        titles = []
        # load _Sidebar.md and extract all links from markdown file
        with open(os.path.join(wiki_input_dir, '_Sidebar.md')) as f:
            lines = f.readlines()
            for line in lines:
                if '(' in line:
                    # extract text between square brackets
                    # find the first '(' after the square brackets
                    page = line[line.find('(', line.find(']'))+1:line.rfind(')')]
                    if parent == "LIMO":
                        page = page.replace('https://github.com/LIMO-EEG-Toolbox/limo_meeg/wiki/', '')
                        page = clean_filename(page)
                    title = line[line.find('[')+1:line.find(']')]
                    pages.append(page)
                    titles.append(title)
        pages = list(map(str.lower, pages))
        filename = clean_filename(filename)
        if filename.lower() in pages:
            order = pages.index(filename.lower())
            title = titles[order]
            append_text += '''
title: {title}
long_title: {title}
'''.format(title=title)

            append_text += 'nav_order: {order}\n'.format(order=order+1)
    else:   
        append_text += '''
title: {filename}
long_title: {filename}
'''.format(filename=filename)
    
    append_text += '---\n'

    with open(filepath) as f:
        text = f.read()
        if parent == "LIMO":
            text = format_text_limo(text)
        text = append_text + text
        outputfilename = clean_filename(os.path.basename(output_file))
        outputfilepath = os.path.dirname(output_file)

        with open(f"{outputfilepath}/{outputfilename}", 'w') as out:
            out.write(text)

def format_text_limo(text):
    # find in the text the line containing ```matlab and append a line before it
    text = text.replace('https://github.com/', 'https://raw.githubusercontent.com/')
    text = text.replace('blob/', '')

    return text

def reformat_plugin_dir(plugin_input_dir, plugin_name, formatted_name, order, link, plugin_type='wiki'):
    # plugins_output_dir = '/Users/dtyoung/Documents/EEGLAB/sccn.github.io/plugins'
    plugin_output_dir = os.path.join('../../plugins', plugin_name)
    if not os.path.exists(plugin_output_dir):
        os.makedirs(plugin_output_dir)

    # copy image directory from input to output dir
    if os.path.exists(os.path.join(plugin_input_dir, 'images')):
        shutil.copytree(os.path.join(plugin_input_dir, 'images'), os.path.join(plugin_output_dir, 'images'), dirs_exist_ok=True)
    # copy all .jpg and .png files from input to output dir
    for file in os.listdir(plugin_input_dir):
        if file.endswith(('.png', '.jpg', '.gif')):
            shutil.copyfile(os.path.join(plugin_input_dir, file), os.path.join(plugin_output_dir, file))
    
    # if plugin is 'imat', copy the Docs directory recursively to the output directory
    if plugin_name == 'imat':
        shutil.copytree(os.path.join(plugin_input_dir, 'Docs'), os.path.join(plugin_output_dir, 'Docs'), dirs_exist_ok=True)

    index_file = os.path.join(plugin_output_dir, 'index.md')
    shutil.copyfile(os.path.join(plugin_input_dir, 'README.md'), index_file)
    append_text = '''---
layout: default
title: {plugin_name}
long_title: {plugin_name}
parent: Plugins
render_with_liquid: false'''.format(plugin_name=formatted_name)

    if plugin_type == 'wiki':
        append_text += '\nhas_children: true'
        wiki_plugin_input_dir = plugin_input_dir + '.wiki'

        # copy image directory from input to output dir
        if os.path.exists(os.path.join(wiki_plugin_input_dir, 'images')):
            shutil.copytree(os.path.join(wiki_plugin_input_dir, 'images'), os.path.join(plugin_output_dir, 'images'), dirs_exist_ok=True)
        # copy all .jpg and .png files from wiki input to output dir
        for file in os.listdir(wiki_plugin_input_dir):
            if file.endswith('.jpg') or file.endswith(('.png', '.jpg', '.gif')):
                shutil.copyfile(os.path.join(wiki_plugin_input_dir, file), os.path.join(plugin_output_dir, file))


        for root, dirs, files in os.walk(wiki_plugin_input_dir):
            for file in files:
                if file.endswith('.md') and not file.startswith('index') and not file.startswith('Home'):
                    reformat_wiki_pages(os.path.join(wiki_plugin_input_dir, file), file.replace('.md', ''), formatted_name, os.path.join(plugin_output_dir, file), wiki_plugin_input_dir)
    

    with open(index_file) as f:
        append_text += '''
nav_order: {order}
---
To view the plugin source code, please visit the plugin's [GitHub repository]({link}).

'''.format(link=link, order=order)
        text = f.read()
        text = append_text + text

        if plugin_name == 'LIMO':
            with open(os.path.join(wiki_plugin_input_dir, 'Home.md')) as f:
                text += f.read()

        with open(index_file, 'w') as out:
            out.write(text)
# main
def main():
    if len(sys.argv) != 7:
        print('Usage: python reformat_plugin.py <plugin_dir_path> <plugin_name> <formatted_name> <plugin_type> <nav_order> link')
        sys.exit(1)
    dirpath = sys.argv[1]
    plugin_name = sys.argv[2]
    formatted_name = sys.argv[3]
    plugin_type = sys.argv[4]
    order = sys.argv[5]
    link = sys.argv[6]
    reformat_plugin_dir(dirpath, plugin_name, formatted_name, order, link, plugin_type)

if __name__ == "__main__":
    main()
