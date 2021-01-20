import requests
from bs4 import BeautifulSoup
import urllib.request as urllib
import re
from os import listdir
from os.path import isfile, isdir, join


input_path = "/Users/dtyoung/Documents/EEGLAB/sccn.github.io/_site"
host = "https://eeglab.org"

def getHTMLFiles(path, prefix=""):
    files = [join(prefix, file) for file in listdir(path) if re.search(".*\.html$",file)]
    for folder in [f for f in listdir(path) if isdir(join(path, f))]:
        files.extend(getHTMLFiles(join(path, folder), join(prefix, folder)))
    return files

files = getHTMLFiles(input_path)
files.extend(getHTMLFiles(input_path + "/workshops", "workshops/"))
files = getHTMLFiles(input_path + "/tutorials", "tutorials/")
files.extend(getHTMLFiles(input_path + "/download", "download/"))
files.extend(getHTMLFiles(input_path + "/news", "news/"))
files.extend(getHTMLFiles(input_path + "/others", "others/"))
files.extend(getHTMLFiles(input_path + "/support", "support/"))
files = list(set(files))
files.sort()
print(files)
with open('link_report.txt', "w") as w:
    w.write("BROKEN or NOT UPDATED LINKS\n")
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
                try:
                    href = link['href']
                    if href.startswith('/'):
                        # print(host+href)
                        response = requests.get(host + href)
                        if href.startswith("http://sccn.ucsd.edu/wiki") or response.status_code == 404:
                            w.write("\t-" + link.string + ": " + href + "\n")
                    elif href.startswith("http://sccn.ucsd.edu/wiki"):
                            w.write("\t-" + link.string + ": " + href + "\n")
                except Exception:
                    print(link)

