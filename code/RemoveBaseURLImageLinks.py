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
                matched = re.search('{{ site.baseurl }}/assets', new_line)
                if matched:
                    new_line = new_line.replace("{{ site.baseurl }}/assets", "/assets")
                matched = re.search('!\\[(\\d*px)\\]', new_line)
                if matched:
                    new_line = new_line.replace(matched.group(1), "")
                out.write(new_line)






