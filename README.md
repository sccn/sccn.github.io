# sccn.github.io
Host web content of EEGLAB wiki.
Live page: https://sccn.github.io

## Notes for maintainers
* Contents of Workshops and Tutorials pages are stored in the [workshops](https://github.com/sccn/sccn.github.io/tree/master/workshops) and [tutorials](https://github.com/sccn/sccn.github.io/tree/master/tutorials) folders respectively. Use [Github markdown](https://guides.github.com/features/mastering-markdown) to edit and style page content.
* Images are stored in [assets/images](https://github.com/sccn/sccn.github.io/tree/master/assets/images). To link an uploaded image in the page, use path "/assets/images/<image_filename>"
* PDFs and zip files are stored in https://sccn.ucsd.edu/githubwiki/files/<file_name>. These files will be uploaded manually by @dungscout96 for now. In the future we will create a mechanism for users to upload files to sccn server themselves.
* On the Workshops pages, if there's any broken image or file link, it's very likely that the naming of the file is wrong. For some reason file names were capitalized weirdly when exporting from Mediawiki. Check to see if the file exists in either assets/images or https://sccn.ucsd.edu/githubwiki/files and fix filename first before uploading a new file.
* It usually takes few minutes for a pushed commit to go live. See instructions below if you want to set up Jekyll and quickly load changes locally on your laptop.

### To run the site locally on your laptop
* Install Jekyll following the instruction: https://jekyllrb.com/docs/installation/. (See [here](https://jekyllrb.com/docs/installation/macos/) for mac)
* Clone the repository: ``git clone https://github.com/sccn/sccn.github.io.git; cd sccn.github.io``
* Run ``bundle install`` to download theme and its dependencies
* Open *_config.yml* and change the line ``remote_theme: pmarsceill/just-the-docs`` to ``theme: "just-the-docs"``. **Don't commit this change to remote!**
* Run ``bundle exec jekyll serve`` and the site should be live at http://localhost:4000/
