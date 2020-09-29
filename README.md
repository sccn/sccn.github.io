# sccn.github.io
Host web content of EEGLAB wiki.
Web: https://sccn.github.io

## Notes for maintainers
* Contents of Workshops and Tutorials pages are stored in the [workshops](https://github.com/sccn/sccn.github.io/tree/master/workshops) and [tutorials](https://github.com/sccn/sccn.github.io/tree/master/tutorials) folders respectively. Use [Github markdown](https://guides.github.com/features/mastering-markdown) to edit and style page content.
* Images are stored in [assets/images](https://github.com/sccn/sccn.github.io/tree/master/assets/images). To link an uploaded image in the page, use path "/assets/images/<image_filename>"
* PDFs and zip files are stored in https://sccn.ucsd.edu/githubwiki/pdfs. These files will be uploaded manually by @dungscout96 for now. In the future we will create a mechanism for users to upload files to sccn server themselves.
* On the Workshops pages, if there's any broken image or file link, it's very likely that the naming of the file is wrong. For some reason file names were capitalized weirdly when exporting from Mediawiki. Check to see if the file exists in either assets/images or https://sccn.ucsd.edu/githubwiki/pdfs (via ssh) and fix filename first before uploading a new file.
* It usually takes few minutes for a pushed commit to go live. It takes some setting-up effort to load the site locally for quick preview of changes:
  * Clone the repository and follow the instructions in https://pmarsceill.github.io/just-the-docs/#getting-started to install Jekyll and update the _config.yml file accordingly. 
  * Ignore _config.yml files when you create new commit. DO NOT push your edited local _config.yml file!
