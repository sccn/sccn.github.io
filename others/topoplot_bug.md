In EEGLAB 2024.0,l we modified the topoplot function for Octave compatibility, where the meshgrid function was used to precompute point coordinates (this is the [code change](https://github.com/sccn/eeglab/commit/fb2b77e1db70c025b7898f18af895e59aba7bbc1) to fix the issue). This is because Octave griddata function is not as powerful as the MATLAB one and requires this extra step.

However, the coordinates were inverted, resulting in the bug below. This is a subtle mirroring issue in which the image is flipped along the diagonal.

![scalp_topo](https://github.com/sccn/sccn.github.io/assets/1872705/0e9003b5-203e-431c-ada5-6bf1c31a2051)

Unfortunately, this issue affects all topoplot performed with EEGLAB 2024.0.
