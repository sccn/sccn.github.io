import re
from os import listdir
from os.path import isfile, join

sccn_path = "https://sccn.ucsd.edu/wiki/"
input_path = "/Users/dtyoung/Documents/EEGLAB/eeglab-wiki/mediawiki-to-markdown/output/fixed_images"
output_path = "/Users/dtyoung/Documents/EEGLAB/eeglab-wiki/mediawiki-to-markdown/output/fixed"
function_path = "http://sccn.ucsd.edu/eeglab/locatefile.php?file="

md_files = [file for file in listdir(input_path) if re.search(".*\.md$",file)]
for file in md_files:
    # print(join(input_path, file))
    with open(join(input_path, file), "r") as f:
        with open(join(output_path, file), "w") as out:
            print("file: " + file + "\n")
            for line in f:
                new_line = line
                matched = re.findall('({ {File\\\\\\||{ {File\\|)(.*?)(} })', new_line)
                if matched:
                    for match in matched:
                        new_line = new_line.replace(match[0], "[{}]({}".format(match[1],function_path))
                        new_line = new_line.replace(match[2], ")")
                out.write(new_line)




