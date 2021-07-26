## Release candidate

1. Check that there is no bug in the unit test cases
3. Update the revision page at https://eeglab.org/others/EEGLAB_revision_history.html
2. Change version number and date in eeg_getversion.m
7. Compile as Windows and Mac, and check automated test (menu item "test compiled version")
8. Manually upload and update links in /home/www/eeglab/eeglabversions (zip archive can have the extension rc for release candidate)
3. Compile as Matlab with rc (release candidate), plugin will automatically be submitted.
4. Check automated install by changing the EEGLAB preferences.
10. Issue release candidate email to EEGLABLIST list with direct link to executables


## Final candidate

One week later after release candidate.

1. Recompile all executable if any code change. Otherwise rename the zip files.
1. Change revision 
6. Accept plugin.
5. Accept new plugin and check that update is seen.
6. Final edits in the revision page
7. Send email to EEGLABNEWS list
6. Update the list of web pages of EEGLAB revisions and which version is supported.
5. Create a new branch for the old version (use GIT)

## Post release

1. Put back dev as the version
