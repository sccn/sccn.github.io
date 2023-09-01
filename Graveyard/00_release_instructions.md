## Release candidate

1. Check that there is no bug in the unit test cases
2. Update the revision page at https://eeglab.org/others/EEGLAB_revision_history.html
3. Change version number and date in eeg_getversion.m
4. Compile as Windows and Mac, and check automated test (menu item "test compiled version")
5. Manually upload and update links in /home/www/eeglab/eeglabversions (zip archive can have the extension rc for release candidate)
6. Compile as Matlab with rc (release candidate), plugin will automatically be submitted.
7. Check automated install by changing the EEGLAB preferences.
8. Create a new branch for the old version (use GIT)
9. Issue release candidate email to EEGLABLIST list with direct link to executables


## Final candidate

One week later after release candidate.

1. Recompile all executable if any code change. Otherwise rename the zip files.
2. Change revision 
3. Accept plugin.
4. Accept new plugin and check that update is seen.
5. Download Fieldtrip and Picard and run "test_compiled_version" script
6. Final edits in the revision page
7. Unpate links in /home/arno/www/eeglab/currentversion
8. Send email to EEGLABNEWS list

## Post release

1. Put back dev as the version
