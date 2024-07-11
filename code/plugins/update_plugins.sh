current_dir=$(pwd)

repo="SIFT"
if cd ../../$repo; then git pull; else git clone https://github.com/sccn/$repo.wiki.git ../../$repo; fi
python Wiki_plugin.py ../../$repo $repo
cd $current_dir

repo="EEG-BIDS"
if cd ../../$repo; then git pull; else git clone https://github.com/sccn/$repo.git ../../$repo; fi
python README_plugin.py ../../$repo $repo
cd $current_dir

repo="roiconnect"
if cd ../../$repo; then git pull; else git clone https://github.com/sccn/$repo.git ../../$repo; fi
python README_plugin.py ../../$repo $repo
cd $current_dir