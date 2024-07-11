---
layout: default
title: Chapter_05_NFT_Commands_and_Functions
long_title: Chapter_05_NFT_Commands_and_Functions
parent: NFT
grand_parent: Plugins
---
This section summarizes the MATLAB commands and data structures used for
each stage of head modeling using the NFT toolbox. The function
reference can be found in Appendix B

Function Naming and Style
-------------------------

The toolbox functions have names all lowercase, words separated by
underscore. The GUI function names start with capital letters. The user
interface functions all begin with the name of the module, such as
bem_, mesh_, segm_, warping_ while utility functions are prefixed by
util, for instance BEM utility functions start with utilbem_. All
functions have help sections describing the usage, inputs and outputs,
compatible with the help2html() conventions. They also include a license
block.

In user interface functions (bem_, etc.) the input arguments are
validated before use. The utility functions, which are mostly used
internally do minimal validation.

Segmentation Functions
----------------------

The main user interface for the segmentation is initiated using
[Segmentation()](NFT_Appendix_B#Segmentation "wikilink") command which
opens up the GUI for segmentation.

While most of the BEM matrix generation functionality can be initiated
from the GUI interface, each operation can also be performed through
matlab functions. After loading the MR image the following functions are
called respectively:
[segm_aniso_filtering()](NFT_Appendix_B#segm_aniso_filtering "wikilink"),
[segm_scalp()](NFT_Appendix_B#segm_scalp "wikilink"),
[segm_brain()](NFT_Appendix_B#segm_brain "wikilink"),
[segm_outer_skull()](NFT_Appendix_B#segm_outer_skull "wikilink"),
[segm_inner_skull()](NFT_Appendix_B#segm_inner_skull "wikilink"),
[segm_final_skull()](NFT_Appendix_B#segm_final_skull "wikilink").

Mesh Generation Functions
-------------------------

The main user interface for mesh generation is initiated using
[Mesh_generation()](NFT_Appendix_B#Mesh_generation "wikilink") command
which opens up the GUI for mesh generation. The function loads the
segmentation and generates meshes for scalp, skull, CSF and brain. If
the user wants to refine the meshes locally,
[mesh_local_refinement()](NFT_Appendix_B#mesh_local_refinement "wikilink")
function is called. The topology of the generated meshes are checked by
[mesh_final_correction()](NFT_Appendix_B#mesh_final_correction "wikilink"),
and finally, the total head mesh is written in the format described in A
using the function
[mesh_read_write()](NFT_Appendix_B#mesh_read_write "wikilink").

Co-registration Functions
-------------------------

The main user interface for the co-registration of electrode locations
with MR images is initiated using Coregistration() command which opens
up the GUI for co-registration.

Warping Functions
-----------------

The main user interface for the warping of a template head model is
initiated using
[Warping_mesh()](NFT_Appendix_B#Warping_mesh "wikilink") command which
opens up the GUI for warping functions. After loading the electrode
locations the MNI mesh is loaded. Using
[warping_main_function()](NFT_Appendix_B#warping_main_function "wikilink")
function the warping parameters and the warped mesh are calculated.

Forward Model Generation Functions
----------------------------------

The main user interface for the forward model generation is initiated
using
[Forward_Problem_Solution()](NFT_Appendix_B#Forward_Problem_Solution "wikilink")
command. While most of the BEM matrix generation functionality can be
initiated from the GUI interface, each operation also be performed
through matlab functions.

The functions used by the BEM module are used for creating the BEM
structures, running the solver to generate the model matrices, and
solving for single or multiple dipoles.

The state of the forward solution is stored in the structures, and no
global variables are used by the toolbox. Since the contents of the
structure arguments may change during a function call, most interface
functions return the structure so that the changes can be preserved
(MATLAB has no OUT arguments).

### Mesh Functions

A set of mesh files can be loaded with the
[bem_load_mesh()](NFT_Appendix_B#bem_load_mesh "wikilink") function
which returns a mesh structure.

### Model Functions

The model structure which combines the mesh, conductivities and solver
IPA parameters is obtained using the
[bem_create_model()](NFT_Appendix_B#bem_create_model "wikilink")
function. Once the model structure is obtained, it is possible to invoke
the solver using the
[bem_generate_eeg_matrices()](NFT_Appendix_B#bem_generate_eeg_matrices "wikilink")
function to generate the BEM matrices. Individual matrices can be loaded
into the model structure using the
[bem_load_model_matrix()](NFT_Appendix_B#bem_load_model_matrix "wikilink")
function.

### Session Functions

The session structure is used for solving the forward problem at a given
set of sensors. The structure is created using
[bem_create_session()](NFT_Appendix_B#bem_create_session "wikilink")
from a model and a list of sensors. The list of sensors can be generated
from a list of nodes using the
[bem_smatrix_from_nodes()](NFT_Appendix_B#bem_smatrix_from_nodes "wikilink")
function.

The transfer matrix for the sensors specified in the session can be
generated using the
[bem_generate_eeg_transfer_matrix()](NFT_Appendix_B#bem_generate_eeg_transfer_matrix "wikilink")
function which computes and saves the transfer matrix. The computed
transfer matrix can be loaded into the session structure using the
[bem_load_transfer_matrix()](NFT_Appendix_B#bem_load_transfer_matrix "wikilink")
function.

There are two functions for obtaining forward solutions. The
[bem_solve_dipoles_eeg()](NFT_Appendix_B#bem_solve_dipoles_eeg "wikilink")
function computes the sensor potentials due to the activation of a
number of dipoles. The
[bem_solve_lfm_eeg()](NFT_Appendix_B#bem_solve_lfm_eeg "wikilink")
function is suitable for generating a Lead Field Matrix since it returns
a matrix of single dipole solutions.

### Utility Functions

The utility functions are used internally by the functions described
above.

The external user configuration can be returned using the
[NFT_get_config()](NFT_Appendix_B#NFT_get_config "wikilink") function.
This m-file can be edited manually to specify run-time options for the
toolbox. User interface functions call this function to get
configuration variables as needed.

The
[utilbem_compute_cond()](NFT_Appendix_B#utilbem_compute_cond "wikilink")
and
[utilbem_compute_indices()](NFT_Appendix_B#utilbem_compute_indices "wikilink")
functions compute conductivity and index information from the mesh.
These functions are called by
[bem_create_model()](NFT_Appendix_B#bem_create_model "wikilink") and
the results are stored in the model structure.

There are two utility functions for computing source (right-hand-side)
vectors.
[utilbem_multilayer_rhs()](NFT_Appendix_B#utilbem_multilayer_rhs "wikilink")
is used for IPA and
[utilbem_pot_unbound()](NFT_Appendix_B#utilbem_pot_unbound "wikilink")
is used without IPA.