import re
from os import listdir
from os.path import isfile, join

input_path = "/Users/dtyoung/Documents/EEGLAB/eeglab-wiki/mediawiki-to-markdown/output/temp"
output_path = "/Users/dtyoung/Documents/EEGLAB/eeglab-wiki/mediawiki-to-markdown/output/fixed"
sccn_path = "https://sccn.ucsd.edu/githubwiki/files/"

md_files = [file for file in listdir(input_path) if re.search(".*\.md$",file)]
for file in md_files:
    # print(join(input_path, file))
    with open(join(input_path, file), "r") as f:
        with open(join(output_path, file), "w") as out:
            print("file: " + file + "\n")
            for line in f:
                new_line = line
                matched = re.findall('(/mediawiki/images/)(.*?)(.zip|.pdf)', new_line)
                if matched:
                    for match in matched:
                        lowered = match[1].lower() # lowercase file name (w/o extension)
                        new_line = new_line.replace(match[1], lowered)
                        new_line = new_line.replace(match[0], sccn_path)
                        new_line = new_line.replace(' "wikilink"', "")
                        # print(new_line)
                out.write(new_line)
