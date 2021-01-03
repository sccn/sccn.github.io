import requests
from bs4 import BeautifulSoup
import urllib.request as urllib
import re
from os import listdir
from os.path import isfile, join


input_path = "/Users/dtyoung/Documents/EEGLAB/sccn.github.io/_site"
host = "https://sccn.github.io"

def getHTMLFiles(path, prefix=""):
    return [prefix + file for file in listdir(path) if re.search(".*\.html$",file)]

files = getHTMLFiles(input_path)
files.extend(getHTMLFiles(input_path + "/workshops", "workshops/"))
files.extend(getHTMLFiles(input_path + "/tutorials", "tutorials/"))
files = list(set(files))
files.sort()
print(files)
with open('link_report.txt', "w") as w:
    w.write("BROKEN LINKS\n")
    for file in files:
        # print(join(input_path, file))
        # with open(join(input_path, file), "r") as f:
        page = requests.get(host + "/" + file)
        if page.status_code == 404:
            w.write("Broken page: " + file + "\n")
        else:
            w.write(file +"\n")
            print(host + "/" + file)
            soup = BeautifulSoup(page.content, 'html.parser')
            urls = soup.find_all('a')
            for link in urls:
                href = link['href']
                if href.startswith('/'):
                    # print(host+href)
                    response = requests.get(host + href)
                    if response.status_code == 404:
                        w.write("\t-" + link.string + ": " + href + "\n")
