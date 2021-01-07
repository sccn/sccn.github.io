---
layout: default
title: Fork EEGLAB
parent: Other documents
---
Fork EEGLAB <span style="color: green">- DONE</span>
===

The main EEGLAB repository is not the place to add new functions. If
you want to add new functionality, write an EEGLAB
[plugin](/tutorials/misc/Contributing_to_EEGLAB.html) instead.

Why fork the EEGLAB repository?
------------------------
This page assumes that you are somewhat familiar with GitHub, Git, and version control.

Forking (copying) a software repository makes a copy of the repository
that belongs to you. This allows you to experiment
without affecting the existing code. Once you are done with your
changes, you will be able to transfer them (push them) to the main
repository by using *pull requests* (this could have been
referred to as *push requests*, but the software community decided to
name it from the perspective of the main repository, which then is
<em>pulling</em> in your changes). This page will introduce you to the
basics of forking the EEGLAB repository. Github makes the procedure very
simple.

Forking the EEGLAB repository
------------------------------------------

To fork the EEGLAB repository from Github, follow these two simple
steps:

1.  On Github, go to the [EEGLAB
    repository](https://github.com/sccn/eeglab)
2.  Click *Fork* in the top right corner of the window (See the figure
    below).

![center\|thumb\|700px](/assets/images/Fork_link.jpg)

Once you have executed these two steps, you will have successfully
created your own copy of the EEGLAB repository. The new repository will look
exactly like the EEGLAB repository you forked, but the forked copy
will be under your username account.

![center\|thumb\|700px](/assets/images/Fork_username.jpg)

Working on your forked copy
---------------------------

Once you have created your fork in Github, you will need to set up
*git* in your computer to start working on your EEGLAB code copy. Then
you will need to clone the forked repository to your computer.

-   Go to the forked repository page in Github. This is the
    same page described in the figure above.
-   Look on the right side of the page for the button *Clone or
    download* and click it.

![center\|thumb\|700px](/assets/images/Clone_link.jpg)

-   Click in the clone HTTPS section to copy the link.

![center\|thumb\|400px](/assets/images/Clone_https_link.jpg)

-   Open a terminal on your computer and type *git clone* and then paste
    and execute the link you copied in the previous step.

`$git clone `[`https://github.com/yourgitusername/eeglab.git`](https://github.com/yourgitusername/eeglab.git)

After following these steps, you will be ready to start modifying the EEGLAB code.

Issuing a pull request
----------------------

Once you are satisfied with your code changes, commit them to GitHub. Then,  go back to Github
and issue a *pull request*. Once your changes are evaluated and approved
by the EEGLAB team, they will be merged into the EEGLAB master code.

![center\|thumb\|700px](/assets/images/Pullrequest1.png)

This brings you to a screen where you can select the forked branch to merge into the EEGLAB repository. NOTE: Always merge
into the "develop" branch of EEGLAB.

![center\|thumb\|700px](/assets/images/Pullrequest2.png)

Considerations regarding pull requests
-------------------------------

For expedited approval:
-   If you have added a new feature, make sure it works both from the
    graphic interface and from the MATLAB command line. Please send us a
    simple test script to demonstrate this.
-   Run the test cases on the modified function. If possible, add the test case to the [EEGLAB test case repository](https://github.com/sccn/eeglab-testcases).
-   You can never add too much documentation. Make sure you document
    your changes clearly and thoroughly!
-   Issue pull request for single-function changes.
-   Avoid making large numbers of cosmetic changes (indentation, etc.). If there are too many changes, they take a long time to review and are often rejected.