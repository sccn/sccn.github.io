import re
from os import listdir,mkdir
from os.path import isfile, join, isdir, dirname, basename, exists

def getFiles(path):
    '''
    Recursively get .md files
    :param path:
    :return:
    '''
    files = []
    for item in listdir(path):
        if re.search(".*\.md$", item):
            files.append(join(path,item))
        elif isdir(join(path, item)):
            files.extend(getFiles(join(path,item)))
    return files
input_path = "/Users/dtyoung/Documents/EEGLAB/sccn.github.io/workshops"
output_path = "/Users/dtyoung/Documents/EEGLAB/eeglab-wiki/mediawiki-to-markdown/output/workshops" # temp output folder

md_files = getFiles(input_path)
for filepath in md_files:
    with open(filepath, "r") as f:
        alter_path = dirname(filepath).replace(input_path, output_path)
        # create subdirectories
        if not exists(alter_path):
            mkdir(alter_path)
        alter_filepath = join(alter_path, basename(filepath))
        with open(alter_filepath, "w") as out:
            print("file: " + alter_filepath + "\n")
            for line in f:
                new_line = line
                matched = re.findall('(font color=)(.*?)(>)', new_line)
                for match in matched:
                    new_line = new_line.replace(match[0], 'span style="color: ')
                    new_line = new_line.replace(match[1] + match[2], match[1] + '">')
                matched = re.search('</font>', new_line)
                if matched:
                    new_line = new_line.replace('</font>', '</span>')
                out.write(new_line)






