---
layout: default
parent: NSGportal
grand_parent: Plugins
render_with_liquid: false

title: Scheme-of-plug-in-functions-call
long_title: Scheme-of-plug-in-functions-call
---
The figure below shows a scheme of function calls in _nsgportal_. In the plug-in there are two main sets, or layers, of functions designated by the prefix _pop__ and _nsg__. The _pop__ functions open a parameter entry window when called with fewer than the required arguments, else run directly without opening a window.  The second class of nsgportal functions with prefix _nsg__ can be called directly from MATLAB command line or from other MATLAB scripts or functions. These functions perform lower-level processing than the pop_ functions. A plug-in function (_eegplugin_nsgportal_) manages the inclusion and appearance of an nsgportal item in the main EEGLAB window menu. 

<center>
<img src="https://github.com/sccn/nsgportal/blob/master/docs/img/nsgportal_scheme_call.png?raw=true" alt="drawing" width="1000"/>
</center>