import re
from os import listdir,mkdir
from os.path import isfile, join, isdir, dirname, basename, exists
import urllib.request as urllib

def download_image(url, output):
    print(url)
    urllib.urlretrieve(url, output)

def getFiles(path):
    files = []
    for item in listdir(path):
        if re.search(".*\.md$", item):
            files.append(join(path,item))
        elif isdir(join(path, item)):
            files.extend(getFiles(join(path,item)))
    return files
# download_image('https://sccn.ucsd.edu/cgi-bin/mathtex.cgi?p_{X}(x)%20\;=\;%20\mathcal{N}(x;%20\mu,%20\sigma^2)%20\;\triangleq\;%20(2\pi)^{-1/2}\sigma^{-1}%20\exp(\mbox{$-\frac{1}{2}$}\hspace{1pt}\sigma^{-2}%20(x-\mu)^2%20)', './test.gif')
sccn_path = "https://sccn.ucsd.edu/wiki/"
input_path = "/Users/dtyoung/Documents/EEGLAB/sccn.github.io/workshops"
output_path = "/Users/dtyoung/Documents/EEGLAB/eeglab-wiki/mediawiki-to-markdown/output/workshops"
image_path = "/assets/images/"
isPlugin = False

md_files = getFiles(input_path)
for filepath in md_files:
#     # print(join(input_path, file))
    with open(filepath, "r") as f:
        alter_path = dirname(filepath).replace(input_path, output_path)
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
                    print(new_line)
                    new_line = new_line.replace(matched.group(1), "")
                        # image_file = match[1].capitalize() # capitalized file name (w/o extension)
#                             new_line = new_line.replace(match[1], image_file)
#                             new_line = new_line.replace(match[0], image_path)
#                             new_line = new_line.replace(' "wikilink"', "")
#                             new_line = new_line.replace("[", "![")
#                             if isPlugin:
#                                 image_file += match[2] # add extension
#                                 download_image("https://sccn.github.io/assets/images/"+image_file, "/Users/dtyoung/Desktop/eeglab-wiki/amica.wiki/"+image_file)
                out.write(new_line)






