import re
from os import listdir
from os.path import isfile, join

def reformat(math_string):
    new_string = math_string.replace("\\\\", '\\')
    new_string = new_string.replace("\\begin{eqnarray\*}","")
    new_string = new_string.replace("\\end{eqnarray\*}","")
    new_string = new_string.replace("\\parstyle","")
    new_string = new_string.strip()

    return new_string


input_path = "/Users/dtyoung/Documents/EEGLAB/eeglab-wiki/mediawiki-to-markdown/output/temp"
output_path = "/Users/dtyoung/Documents/EEGLAB/eeglab-wiki/mediawiki-to-markdown/output/fixed"
latex_server = "https://latex.codecogs.com/svg.latex?"

md_files = [file for file in listdir(input_path) if re.search(".*\.md$",file)]
for file in md_files:
    with open(join(input_path, file), "r") as f:
        with open(join(output_path, file), "w") as out:
            print("file: " + file + "\n")
            math_string = ""
            inMath = False
            for line in f:
                new_line = line
                if inMath:
                    matched_end = re.search('(.*)(</m>|</math>)', new_line)
                    if matched_end:
                        inMath = False
                        math_string += matched_end.group(1)
                        new_line = f'<img src="{latex_server}{math_string}">'
                        new_line = reformat(new_line)
                        math_string = ""
                    else:
                        math_string += new_line
                else:
                    matched_start = re.findall('(<m>|<math>)(.*?)', new_line)
                    if matched_start:
                        if len(matched_start) > 1:
                            matched = re.findall('(<m>|<math>)(.*?)(</m>|</math>)', new_line)
                            for match in  matched:
                                math_string += match[1]
                                new_line = new_line.replace(match[0] + match[1] + match[2], f'<img src="{latex_server}{math_string}">')
                                print(new_line)
                                math_string = ""
                            inMath = False
                            new_line = reformat(new_line)
                        else:
                            matched_start = re.search('(<m>|<math>)(.*)', new_line)
                            matched_end = re.search('(.*)(</m>|</math>)', new_line)
                            inMath = True
                            if matched_end:
                                inMath = False
                                matched = re.search('(<m>|<math>)(.*)(</m>|</math>)', new_line)
                                if matched:
                                    math_string += matched.group(2)
                                    new_line = re.sub('(<m>|<math>)(.*)(</m>|</math>)', f'<img src="{latex_server}{math_string}">', new_line)
                                    new_line = reformat(new_line)
                                    print(new_line)
                                    math_string = ""
                            else:
                                math_string += matched_start.group(2)
                if not inMath:
                    out.write(new_line)
