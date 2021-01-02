---
layout: default
title: EEGLAB Extensions
parent: Other documents
---

# EEGLAB extensions <font color=red>Requires work</font>

EEGLAB extensions or plug-ins allow users to build and publish new data
processing and/or visualization functions using EEGLAB data structures
and conventions. Plug-in functions can be easily used and tested by
selecting the new menu items they introduce into the EEGLAB menus of
users who download them.

EEGLAB v13 and later versions can download and install EEGLAB extensions
(formerly termed *plug-ins*) directly from this page via EEGLAB menu
item <b>Files \> Manage EEGLAB extensions</b>.

Lists of plug-ins / extensions for different EEGLAB versions
------------------------------------------------------------

The way plug-ins are handled has changed through EEGLAB history, leading
to more automation in more recent versions and different systems for
storing and managing plug-ins (the plug-ins themselves are often the
same across the different plug-in management systems). The list of
plug-ins provided below are the same as the list of plug-ins available
through the EEGLAB plug-in manager of the corresponding EEGLAB version.

-   [**See the current list of plug-ins for EEGLAB 2019.1 and later
    versions**](https://sccn.ucsd.edu/eeglab/plugin_uploader/plugin_list_all.php)

<!-- -->

-   [See the list of plug-ins for EEGLAB
    2019.0](/Plugin_list_all "wikilink") (plug-ins on this page are no
    longer updated)

<!-- -->

-   See the [import](/Plugin_list_import "wikilink") and [data
    processing](/Plugin_list_process "wikilink") extensions for EEGLAB
    13.x and 14.x (plug-ins and page no longer updated)

<!-- -->

-   [See plug-ins for EEGLAB 12 and earlier
    versions](/EEGLAB_v12_and_earlier_plugins "wikilink") (plug-ins on
    this page are no longer updated)

To install or update a plug-in
------------------------------

Plug-ins may be installed using the EEGLAB plug-in manager, using menu
item <b>File \> Manage EEGLAB extensions</b>.

Although no longer recommended, plug-ins can still be installed
manually. After downloading the zip file for a plug-in, uncompress the
downloaded plug-in file in the main EEGLAB "plugins"
sub-directory/sub-folder. Remove the old version of the plug-in if it is
present in either directory. Then restart EEGLAB. During start-up,
EEGLAB should print the following on the Matlab command line:

``` matlab
> eeglab: adding plug-in "eegplugin_myplugin" % (see \>\> help
> eegplugin_myplugin)
```

The plug-in will typically have added one or more new items to the
EEGLAB menu (often under the Tools heading).

To uninstall a plug-in
----------------------

Plug-ins can just as easily be removed from the EEGLAB extension
manager. Alternatively, you may simply move or remove its folder from
the EEGLAB plug-ins folder and restart EEGLAB.

To construct and publish a new plug-in
--------------------------------------

See the simple instructions under [How to contribute to
EEGLAB](/A07:_Contributing_to_EEGLAB "wikilink").

To add your plug-in / extension to the EEGLAB extension manager
---------------------------------------------------------------

You may add your extension to the list above so that EEGLAB users can
download it automatically from within EEGLAB. To do this, use [this
form](http://sccn.ucsd.edu/eeglab/plugin_uploader/upload_form.php). If
you just want to upload a new version of your plug-in, you can use this
simplified
[form](http://sccn.ucsd.edu/eeglab/plugin_uploader/version_update.php).

Administrators, these are the maintenance pages to accept [Pending
plug-in
requests](https://sccn.ucsd.edu/eeglab/plugin_uploader/protected/pending_requests.php)
and [Edit plug-in
information](https://sccn.ucsd.edu/eeglab/plugin_uploader/protected/edit_plugin.php).

To access access old versions of a plug-in / extension
------------------------------------------------------

In case you need them, old versions of plug-ins are available for direct
download at
[<http://sccn.ucsd.edu/eeglab/plugins/>](http://sccn.ucsd.edu/eeglab/plugins/).
These cannot be installed through the EEGLAB extension manager. Simply
download the zip file and uncompress it in the eeglab/plugins/ folder
(and make sure you remove any other version of the plug-in you might
have installed).