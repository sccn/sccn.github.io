#!/bin/bash
cd /Users/dtyoung/Documents/EEGLAB/sccn.github.io/code/plugins
git pull --rebase
python update_plugins.py
git add -A && git commit -m "scheduled plugin update"
git push