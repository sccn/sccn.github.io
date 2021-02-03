## Release candidate

1. Check that there is no bug in the unit test cases
2. Change version number and date in eeg_getversion.m
3. Update the revision page
3. Compile as Matlab, check automated update by submitting a new plugin. Remove plugin.
3. Compile as Windows and Mac, and check automated test (menu item "test compiled version")
4. Manually upload and update links in /home/www/eeglab/eeglabversions
5. Edit eeg_getversion, return nothing, and show "RELEASE CANDIDATE"
5. Issue release candidate email to EEGLABLIST list
6. Submit new plugin, and accept it.


## Final candidate

One week later after release candidate.

1. Recompile all executable if any code change
4. Compile as Matlab, check automated update by submitting a new plugin.
5. Accept new plugin and check that update is seen.
6. Final edits in the revision page
7. Send email to EEGLABNEWS list
6. Update the list of web pages of EEGLAB revisions and which version is supported.

## Post release

1. Put back dev as the version
5. Create a new branch for the old version (use GIT)
