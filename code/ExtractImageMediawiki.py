import re
import urllib.request as urllib

sccn_path = "https://sccn.ucsd.edu"
filepath = "download.html"
urllib.urlretrieve("https://sccn.ucsd.edu/wiki/User:Dungt/All_files", filepath)
sccn_path = "https://sccn.ucsd.edu/"
with open(filepath) as f:
    for line in f:
        found = re.search('.*(mediawiki/images.*?(?=\")).*', line)
        if found:
            image_url = sccn_path + found.group(1)
            image_filename = re.search('^.*(?<=\/)(.*)$', found.group(1))
            image_filename = image_filename.group(1)
            image_path = "./output/assets/" + image_filename
            # print(image_url)
            # print(image_filename)
            urllib.urlretrieve(image_url, image_path)
