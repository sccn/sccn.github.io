---
layout: default
title: EEGLAB Extensions
parent: Other documents
---
EEGLAB extensions and plug-ins <span style="color: green"> - Done</span>
====

EEGLAB extensions or plug-ins allow users to build and publish new data
processing and/or visualization functions using EEGLAB data structures
and conventions. Plug-in functions can be easily used and tested by
selecting the new menu items they introduce into the EEGLAB menus.

EEGLAB v13 and later versions can download and install EEGLAB *plug-ins* directly from this page via EEGLAB menu
item <span style="color: brown">File → Manage EEGLAB extensions</span>.

Lists of plug-ins for different EEGLAB versions
-----------------------------
The way plug-ins are handled has changed through EEGLAB history, leading
to more automation in more recent versions and different systems for
storing and managing plug-ins (the plug-ins themselves are often the
same across the different plug-in management systems). The list of
plug-ins provided below are the same as the list of plug-ins available
through the EEGLAB plug-in manager of the corresponding EEGLAB version.

-   [See the current list of plug-ins for EEGLAB 2019.1 and later
    versions](https://sccn.ucsd.edu/eeglab/plugin_uploader/plugin_list_all.php)
-   [See the list of plug-ins for EEGLAB
    2019.0](https://sccn.ucsd.edu/wiki/Plugin_list_all) (plug-ins on this page are no
    longer updated)
-   See the [import](https://sccn.ucsd.edu/wiki/Plugin_list_import) and [data processing](https://sccn.ucsd.edu/wiki/Plugin_list_process) extensions for EEGLAB
    13.x and 14.x (plug-ins and page no longer updated)

To install or update a plug-in
------------------------------

Plug-ins may be installed using the EEGLAB plug-in manager, using menu
item <span style="color: brown">File → Manage EEGLAB extensions</span>.

Although no longer recommended, plug-ins can still be installed
manually. After downloading the zip file for a plug-in, uncompress the
downloaded plug-in file in the main EEGLAB "plugins"
sub-directory. Remove the old version of the plug-in if it is
present in the directory. Then restart EEGLAB. During start-up,
EEGLAB should print the following on the Matlab command line:

``` matlab
> eeglab: adding plug-in "eegplugin_myplugin" % (see >> help eegplugin_myplugin)
```

The plug-in will typically have added one or more new items to the
EEGLAB menus (often under the *Import data* or *Tools* headings).

To uninstall a plug-in
----------------------

Plug-ins can just as easily be removed from the EEGLAB extension
manager. Alternatively, you may move or remove its folder from
the EEGLAB plug-ins folder and restart EEGLAB.

To contribute a new plug-in
--------------------------------------

See the simple instructions under [How to contribute to
EEGLAB](/A07:_Contributing_to_EEGLAB "wikilink") to create EEGLAB compatible code.

Then, you may add your extension to the list above so that EEGLAB users can
download it automatically from within EEGLAB. To do this, use [this
form](http://sccn.ucsd.edu/eeglab/plugin_uploader/upload_form.php). If
you want to upload a new version of your plug-in, you can use 
[this simplified form](http://sccn.ucsd.edu/eeglab/plugin_uploader/version_update.php).

Administrators, these are the maintenance pages to accept [Pending
plug-in
requests](https://sccn.ucsd.edu/eeglab/plugin_uploader/protected/pending_requests.php)
and [Edit plug-in
information](https://sccn.ucsd.edu/eeglab/plugin_uploader/protected/edit_plugin.php).

To access old versions of a plug-in / extension
------------------------------------------------------

In case you need them, old versions of plug-ins are available for direct
download at
[http://sccn.ucsd.edu/eeglab/plugins/](http://sccn.ucsd.edu/eeglab/plugins/).
These cannot be installed through the EEGLAB extension manager. Simply
download the zip file and uncompress it in the *eeglab/plugins/* folder
(and make sure you remove any other version of the plug-in you might
have installed).