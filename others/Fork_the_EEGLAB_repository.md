---
layout: default
title: Fork EEGLAB
parent: Other documents
---

Why fork the repository?
------------------------

Forking (copying) a software repository makes a copy of the repository
that belongs to you. This allows you to experiment and try new things
without affecting the existing code. Once you are done with your
changes, you will be able to transfer them (push them) to the main
repository, if you wish, by using "pull requests" (this could have been
referred to as "push requests" but the software community decided to
name it from the perspective of the main repository, which then is
<em>pulling</em> in your changes). This page will introduce you to the
basics of forking the EEGLAB repository. Github makes the procedure very
simple.

Note:

**This page assumes that you are somewhat familiar with Git and version
control.**

**The EEGLAB main repository is not the place to add new functions. If
you want to add new functionality, write an EEGLAB
[plug-in](/A07:_Contributing_to_EEGLAB "wikilink") instead**

Forking the EEGLAB repository in two steps
------------------------------------------

To fork the EEGLAB repository from Github, follow these two simple
steps:

1.  On Github, go to the [EEGLAB
    repository](https://github.com/eeglabdevelopers/eeglab)
2.  Click **Fork** in the top right corner of the window (See the figure
    below).

![center\|thumb\|700px](/assets/images/Fork_link.jpg)

Once you have executed these two steps you will have successfully
created your own repository of EEGLAB code. At this point you will be
redirected to the new forked repository. The new repository will look
exactly like the EEGLAB repository that you forked, but the forked copy
will be under your username account, in this case *yourgitusername*
![center\|thumb\|700px](/assets/images/Fork_username.jpg)

Working on your forked copy
---------------------------

Once you have created your own fork in Github, you will need to set up
**git** in your computer to start working on your EEGLAB code copy. Then
you will need to clone the new forked repo on your computer.

-   Go to your new forked repo (repository) page in Github. This is the
    same page described in the figure above.
-   Look on the right side of the page for the button **Clone or
    download** and click it.

![center\|thumb\|700px](/assets/images/Clone_link.jpg)

-   Click in the clone HTTPS section to copy the link.

![center\|thumb\|400px](/assets/images/Clone_https_link.jpg)

-   Open a terminal on your computer and type *git clone* and then paste
    and execute the link you copied in the previous step.

`$git clone `[`https://github.com/yourgitusername/eeglab.git`](https://github.com/yourgitusername/eeglab.git)

After following these steps you will have cloned your own local copy of
EEGLAB. You will now be ready to start modifying the code. You can send
back your modified EEGLAB code to github by using "git push."

Issue a "pull request"
----------------------

Once you are satisfied with your code changes, you can go back to Github
and issue a "pull request." Once your changes are evaluated and approved
by the EEGLAB team, they will be merged into the EEGLAB master code.

![center\|thumb\|700px](/assets/images/Pullrequest1.png)

This brings you to a screen where you can select the forked branch you
propose to merge into the master EEGLAB repository. NOTE: Always merge
into the "develop" branch of EEGLAB.

![center\|thumb\|700px](/assets/images/Pullrequest2.png)

Considerations re pull requests
-------------------------------

For expedited approval:

-   If you have added a new feature, make sure it works both from the
    graphic interface and from the Matlab command line. Please send us a
    simple test script to demonstrate this.
-   Run the test cases on the modified function. The test cases are
    available [here](/EEGLAB_test_cases "wikilink"). Find the one(s)
    that test the function you modified and run them.
-   You can never add too much documentation. Make sure you document
    your changes clearly and thoroughly!