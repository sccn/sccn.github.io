import re
from os import listdir
from os.path import isfile, join
import urllib.request as urllib

def download_image(url, output):
    print(url)
    urllib.urlretrieve(url, output)

# download_image('https://sccn.ucsd.edu/cgi-bin/mathtex.cgi?p_{X}(x)%20\;=\;%20\mathcal{N}(x;%20\mu,%20\sigma^2)%20\;\triangleq\;%20(2\pi)^{-1/2}\sigma^{-1}%20\exp(\mbox{$-\frac{1}{2}$}\hspace{1pt}\sigma^{-2}%20(x-\mu)^2%20)', './test.gif')
sccn_path = "https://sccn.ucsd.edu/wiki/"
input_path = "/Users/dtyoung/Documents/EEGLAB/eeglab-wiki/mediawiki-to-markdown/output/temp"
output_path = "/Users/dtyoung/Documents/EEGLAB/eeglab-wiki/mediawiki-to-markdown/output/fixed_images"
image_path = "/assets/images/"
isPlugin = False

md_files = [file for file in listdir(input_path) if re.search(".*\.md$",file)]
for file in md_files:
    # print(join(input_path, file))
    with open(join(input_path, file), "r") as f:
        with open(join(output_path, file), "w") as out:
            print("file: " + file + "\n")
            for line in f:
                new_line = line
                if not re.search('<center>|</center>', new_line): # this prevents the markdowned image to be converted to html
                    matched = re.findall('(/Image:|/File:|/file:|/image:)(.*?)(.jpg|.png|.gif|.jpeg|.JPG|.PNG|.GIF|.JPEG)', new_line)
                    if matched:
                        for match in matched:
                            image_file = match[1].capitalize() # capitalized file name (w/o extension)
                            new_line = new_line.replace(match[1], image_file)
                            new_line = new_line.replace(match[0], image_path)
                            new_line = new_line.replace(' "wikilink"', "")
                            new_line = new_line.replace("[", "![")
                            if isPlugin:
                                image_file += match[2] # add extension
                                download_image("https://sccn.github.io/assets/images/"+image_file, "/Users/dtyoung/Desktop/eeglab-wiki/amica.wiki/"+image_file)
                    out.write(new_line)




