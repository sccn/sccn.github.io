---
layout: default
title: NFT
long_title: NFT
parent: NFT
grand_parent: Plugins
---
bem_create_model
----------------

`bem_create_model() - Creates a model structure combining a mesh,  `
`                     conductivity information and BEM parameters.  `

`Usage:  `
`  >> model = bem_create_model(name, mesh, cond, mod);  `

`Inputs:  `
`  name - model name, used as a base filename for matrices  `
`  mesh - mesh structure obtained from BEM_LOAD_MESH  `
`  cond - conductivity values for mesh tissue classes  `
`         vector, starting from first tissue,  `
`         0 is reserved for air  `
`  mod  - index of the modified boundary, for use with IPA. `
`         If mod <= 0, IPA is not used.  `

`Outputs:  `
`  model - model structure with the following fields.  `

`Model Structure:  `
`  name      - name of the model  `
`  mesh      - mesh structure  `
`  cond      - conductivity vector  `
`  mod       - modified boundary information  `
`  node_cond - Average conductivity around a node  `

`Optional Fields:  `
`  ind_mod       - node indices of the modified boundary  `
`  ind_imesh     - node indices of the inner mesh  `
`  ind_imesh_mod - node indices of the modified boundary  `
`                  relative to the inner mesh`

bem_create_session
------------------

`bem_create_session() - Creates a session structure combining a model,  `
`      and sensor data. The session structure contains a model for a `
`      complete head and electrode ’recording session’. Data recorded `
`      using the same set of sensor locations is considered  `
`      to be in the same session.  `

`Usage:  `
`      >> session = bem_create_session(name, model, Smatrix);  `

`Inputs:  `
`  name    - session name, used as a base filename for matrices  `
`  model   - model structure obtained from bem_create_model().  `
`  Smatrix - matrix that defines EEG electrodes in terms of  `
`    the BEM mesh. Each electrode is a weighted sum of the nodes  `
`    of the element. The weights are determined by the element  `
`    shape functions. The format of the Smatrix is as follows:  `
`         [electrode_index node_index weight]  `
`    The rows of the matrix must be sorted by electrode_index  `
`    and there can be more than one row with a given electrode  `
`    index. The Smatrix can be constructed using one of these:  `
`    bem_smatrix_from_nodes() and bem_smatrix_from_points().  `

`Outputs:  `
`  session - session structure with the fields defined in the next section  `

`Session Structure:  `
`  name    - name of the session  `
`  model   - model structure  `
`  Smatrix - EEG sensor information matrix.  `
`  num_electrodes - number of EEG sensors`

bem_generate_eeg_matrices
-------------------------

`bem_generate_eeg_matrices() - Generates BEM matrices for a BEM model.  `

`Usage:  `
`      >> bem_generate_eeg_matrices(model);  `

`Inputs:  `
`  model - model structure generated by BEM_CREATE_MODEL  `

`Notes: The matrices are created using the name given in the model structure  `
`      The following matrices are created on disk, and can be read  `
`      using the bem_load_model_matrix() function  `
`      <model.name>.cmt - BEM coefficient matrix  `
`      <model.name>.dmt - band of Coefficient matrix used by IPA  `
`      <model.name>.imt - inner Coefficient Matrix used by IPA`

bem_generate_eeg_transfer_matrix
--------------------------------

`bem_generate_eeg_transfer_matrix() - Generates EEG transfer matrix.  `

`Usage:  `
`  >> session = bem_generate_eeg_transfer_matrix(session);  `

`Inputs:  `
`  session - session structure generated by BEM_CREATE_SESSION  `

`Outputs:  `
`  session - session object; since it may be modified when  `
`            loading model matrices.  `

`Notes: The matrix is created using the name given in the session structure  `
`      with "tmte" extension for the EEG transfer matrix. It can be loaded  `
`      using the bem_load_transfer_matrix().`

nft_get_config
--------------

`nft_get_config() - Returns the toolbox configuration information  `
`      program path names, defaults, etc. Other toolbox functions call this m-file  `
`      to read their configuration.  `

`Outputs:  `
`  conf - config structure.  `

`Config Structures:  `
`  bem_matrix_program - name of the program that creates EEG matrices.  `
`  asc - name of adaptive skeleton climbing program.  `
`  qslim - name of the coarsening program.  `
`  showmesh - name of the correction and smoothing program.`

bem_load_mesh
-------------

`bem_load_mesh() - Loads a BEM mesh.  `

`Usage:  `
`  >> mesh = bem_load_mesh(name);  `

`Inputs:  `
`  name - mesh name excluding the extension.  `

`Outputs:  `
`  mesh - mesh structure.  `

`Mesh Structure:  `
`  name  - mesh name  `
`  coord - node coordinates  `
`  elem  - elements (connectivity information)  `
`  num_nodes - number of nodes  `
`  num_elements - number of elements  `
`  num_boundaries - number of boundaries  `
`  num_node_elem - number of nodes per element  `
`  num_class - number of tissue classes  `
`  bnd - boundary information array  `
`       [num_elements inner_tissue_class outer_tissue_class]`

bem_load_model_matrix
---------------------

`bem_load_model_matrix() - Loads the BEM matrix with extension ’ext’.  `
`The matrix file name is defined by <model.name>.`<ext>`  `
`Matrix is placed into the model with a field name ’ext’  `

`Usage:  `
`  >> model = bem_load_model_matrix(model, ext);  `

`Inputs:  `
`  model - model structure generated by bem_create_model().  `
`  ext - describes the matrix type. The following types are defined:  `
`    ’cmt’ - BEM Coefficient matrix  `
`    ’dmt’ - band of Coefficient matrix used by IPA  `
`    ’imt’ - inner Coefficient Matrix used by IPA  `
`    ’iinv’ - inverse of the inner coefficient matrix. This matrix is  `
`      computed from ’imt’ if the file does not exist.  `

`Outputs:  `
`  model - model structure.`

bem_load_transfer_matrix
------------------------

`bem_load_transfer_matrix() Loads the BEM transfer matrix with extension ’ext’.  `
`      The matrix file name is defined by <session.name>.`<ext>`.  `
`      Matrix is placed into the session with a field name ’ext’.  `

`Usage:  `
`  >> session = bem_load_transfer_matrix(session, ext);  `

`Inputs:  `
`  session - session structure generated by bem_create_session().  `
`  ext - describes the matrix type. The following type is defined  `
`    ’tmte’ - BEM Transfer matrix.  `

`Outputs:  `
`  session - updated session structure.`

bem_smatrix_from_nodes
----------------------

`bem_smatrix_from_nodes() - Generates Smatrix from nodes of a mesh.  `
`      Smatrix is the sensor information matrix used in  `
`      bem_create_session(). See bem_create_session() for more information.  `

`Usage:  `
`  >> Smatrix = bem_smatrix_from_nodes(mesh, nodes);  `

`Inputs:  `
`  mesh - mesh structure  `
`  nodes - vector of node indices.  `

`Outputs:  `
`  Smatrix - defines one electrode per node. `

bem_solve_dipoles_eeg
---------------------

`bem_solve_dipoles_eeg() - Computes the potential arising from the given dipoles  `
`at the sensor locations defined by the session.  `

`Usage:  `
`  >> [pot, session] = bem_solve_dipoles_eeg(session, dipoles);  `

`Inputs:  `
`  session - session structure defining the model and the sensors.  `
`  dipoles - dipole matrix. Each row defines a dipole as follows:  `
`           [x y z px py pz]  `

`Outputs:  `
`   pot - potentials at the sensors due to simultaneous activation of  `
`         the dipoles.  `
`   session - the updated session structure, in case any matrices are  `
`             loaded, modifying the underlying model.`

bem_solve_lfm_eeg
-----------------

`bem_solve_lfm_eeg() - Computes the LFM arising from given dipoles  `
`at the sensor locations defined by the session.  `

`Usage:  `
`  >> [pot, session] = bem_solve_lfm_eeg(session, dipoles);  `

`Inputs:  `
`  session - session structure defining the model and the sensors  `
`  dipoles - dipole matrix. Each row defines a dipole as follows:  `
`           [x y z px py pz]  `

`Outputs:  `
`  pot - the LFM at the sensors produced by activation of each dipole,  `
`  session - updated session structure in case any matrices are  `
`            loaded, modifying the underlying model.`

Coregistration
--------------

`Coregistration() - Produces the GUI for co-registration of electrode locations  `
` to the scalp mesh.  `

`Usage:  `
`  >> Coregistration(varargin);  `

`Optional Arguments:  `
`  ’subjectdir’ - (string) Output folder. The results will be saved  `
`   in this folder.  `
`  ’subject’ - (string) Subject name. The subject-specific output files will start  `
`   with this name.  `
`  ’session’ - (string) Session name. The file name for registered electrodes will  `
`   start with this name.`

Forward_Problem_Solution
------------------------

`Forward_Problem_Solution() - Produces the forward model generation GUI.  `

`Usage:  `
`  >> Forward_Problem_Solution(varargin);  `

`Optional Arguments:  `
`  ’subjectdir’ - (string) Output folder. The results will be saved in this folder.  `
`  ’subject’ - (string) Subject name. Subject-specific output files will be saved  `
`   starting with this name.  `
`  ’session’ - (string) Session name. Session-specific output files will be saved  `
`   starting with this name.`

Mesh_generation
---------------

`Mesh_generation() - Produces the mesh generation GUI.  `

`Usage:  `
`  >> Mesh_generation(varargin);  `

`Optional Arguments:  `
`  ’subjectdir’ - (string) Output folder. The results will be saved  `
`   in this folder.  `
`  ’subject’ - (string) Subject name. Output files will start with this name.`

mesh_local_refinement
---------------------

`mesh_local_refinement() - Refines the meshes in a given folder. Loads  `
`Scalp.smf, Skull.smf, Csf.smf, Brain.smf meshes in .smf format and saves  `
`them with the same names.  `

`Usage:  `
`  >> mesh_local_refinement(of, nl, ratio_lmr);  `

`Inputs:  `
`  of - mesh folder  `
`  nl - number of layers (3 or 4)  `
`  ratio_lmr - ratio of local edge length to local distance between meshes`

mesh_final_correction
---------------------

`mesh_final_correction() - Performs mesh correction for Scalp.smf,  `
`Skull.smf, Csf.smf, Brain.smf in a given folder. Saves the meshes with  `
`the same names in .smf format.  `

`Usage:  `
`  >> mesh_final_correction(of, nl);  `

`Inputs:  `
`  of - mesh folder  `
`  nl - number of layers (3 or 4)`

mesh_read_write
---------------

`mesh_read_write() - Reads Scalp, Skull, Csf and Brain meshes in .smf  `
`format in a given folder and writes the total head mesh  bec, bee, bei  `
`format.  `

`Usage:  `
`  >> mesh_read_write(of, mesh_name, nl);  `

`Inputs:  `
`  of - mesh folder  `
`  mesh_name - name of the mesh that will be saved in bec, bee, bei format  `
`  nl - number of layers (3 or 4)`

Segmentation
------------

`Segmentation() - Produces the GUI for running segmentation functions.  `

`Usage:  `
`  >> Segmentation(varargin);  `

`Optional Arguments:  `
`  ’subjectdir’ - (string) Output folder. The results will be saved  `
`   in this folder.  `
`  ’subject’ - (string) Subject name. The output files will start with this name.`

segm_aniso_filtering
--------------------

`segm_aniso_filtering() - Performs anisotropic filtering.  `

`Usage:  `
`  >> [b] = segm_aniso_filtering(out, iter, ts, cond);  `

`Inputs:  `
`  out - input image  `
`  iter - number of iterations  `
`  ts - sampling rate  `
`  cond - diffusion parameter  `

`Outputs:  `
`  b - output image`

segm_scalp
----------

`segm_scalp() - Performs scalp segmentation  `

`Usage:  `
`  >> [Sca] = segm_scalp(b);  `

`Inputs:  `
`  b - input image (filtered MR image)  `

`Outputs:  `
`  Sca - scalp mask`

segm_brain
----------

`segm_brain() - Performs brain segmentation  `

`Usage:  `
`  >> [Bra] = segm_brain(b,Sca, sli, WMp,sl, st);  `

`Inputs:  `
`  b - input image (filtered MR image)  `
`  sli - lowest point for cerebellum  `
`  WMp - white matter point  `
`  sl,st - fill level and threshold for watershed segmentation  `

`Outputs:  `
`  Bra - brain mask`

segm_outer_skull
----------------

`segm_brain() - Performs outer skull segmentation  `

`Usage:  `
`  >> [Sk_out, X_dark] = segm_outer_skull(b, Sca, Bra, sli_eyes);  `

`Inputs:  `
`  b - input image (filtered MR image)  `
`  Sca - scalp mask`
`  Bra - brain mask`
`  sli_eyes - slice of the eyes`

`Outputs:  `
`  Sk_out - outer skull mask`
`  X_dark - dark regions of b`

segm_inner_skull
----------------

`segm_inner_skull() - Performs inner skull segmentation  `

`Usage:  `
`  >> Sk_in = segm_inner_skull(b, Sk_out, X_dark, Bra);  `

`Inputs:  `
`  b - imput image (filtered MR image)  `
`  Sk_out - outer skull mask  `
`  X_dark - dark regions of b  `
`  Bra - Brain mask  `

`Outputs:  `
`  Sk_in - inner skull mask  `

segm_final_skull
----------------

`segm_final_skull() - Corrects scalp and outer skull masks wrt inner  `
`                  skull mask  `

`Usage:  `
`  >> [Sca, Sk_out] = segm_final_skull(Sca, Sk_out, Sk_in, WMp);  `

`Inputs:  `
`  Sca    - scalp mask  `
`  Sk_out - outer skull mask  `
`  Sk_in  - inner skull mask  `
`  WMp    - white matter point  `

`Outputs:  `
`  Sca    - scalp mask  `
`  Sk_out - outer skull mask`

utilbem_compute_cond
--------------------

`utilbem_compute_cond() - Computes the average conductivity  `
`    around a node to be used in BEM computations.  `

`Usage:  `
`  >> cond = utilbem_compute_cond(Coord, Elem, layers, sigma)  `

`Inputs:  `
`   Coord  - node coordinate matrix  `
`   Elem   - element connectivity matrix  `
`   layers - mesh boundary information  `
`   sigma  - vector of element conductivities  `

`Outputs:  `
`   cond - average conductivity for each node (vector)  `

`Note: The average conductivity is normally the average of the inner and outer  `
`   conductivities of the layer that a node belongs to. However, for  `
`   meshes with intersecting boundaries there may be three or more tissues  `
`   around a node. This function also handles this general case.`

utilbem_compute_indices
-----------------------

`utilbem_compute_indices() - When the Isolated Problem Approach (IPA) is used,  `
`    the BEM equations are modified to reduce the numerical errors due to  `
`    the low conductivity skull layer.  For this purpose an "inner mesh"  `
`    is defined consisting of skull and the inner layers. This function  `
`    computes the node indices corresponding to these layers to be used  `
`    in BEM computations.  `

`Usage:  `
`  >> [indMsh, indMod, indMshMod] = utilbem_compute_indices(Coord, Elem, layers, mod);  `

`Inputs:  `
`   Coord  - node coordinate matrix  `
`   Elem   -  element connectivity matrix  `
`   layers - mesh boundary information  `
`   mod    - index of the boundary modified for IPA.  `

`Outputs:  `
`   indMsh - coordinate indices of inner mesh nodes (vector).  `
`   indMod - coordinate indices of modified boundary nodes (vector).  `
`   indMshMod - Coordinate indices of modified boundary relative to inner  `
`               mesh.`

utilbem_multilayer_rhs
----------------------

`utilbem_multilayer_rhs() - Computes the Right-Hand-Side of the  `
`    BEM matrix equation when IPA (Isolated Problem Approach) is  `
`    used. The RHS vector corrected by IPA reduces numerical errors  `
`    in computation due to the low conductivity skull layer.  `

`Usage:  `
`  >> RHS = utilbem_multilayer_rhs(Coord, cond, indMod, indMsh, indMshMod,  `
`   iinv, dmt, s2, s3, dip);  `

`Inputs:  `
`   Coord     - node coordinate matrix  `
`   cond      - average conductivity for each node (vector)  `
`               as computed by utilbem_compute_cond()  `
`   indMod    - coordinate indices of modified boundary nodes (vector).  `
`   indMsh    - coordinate indices of inner mesh nodes (vector).  `
`   indMshMod - coordinate indices of modified boundary relative to inner mesh.  `
`               The indices are computed by utilbem_compute_indices()  `
`   iinv      - inverse inner matrix.  `
`   dmt       - sub coefficient matrix (# of nodes) x (# of mod. boundary nodes).  `
`   s2        - outer conductivity of the modified layer.  `
`   s3        - inner conductivity of the modified layer  `
`   dip       - dipole parameters [x y z px py pz]  `

`Outputs:  `
`   RHS - The right-hand-side of the BEM matrix equation for a given  `
`   dipole.`

utilbem_pot_unbound
-------------------

`utilbem_pot_unbound() - Computes the unbounded potential at the  `
`    given coordinates due to a single dipole. The result is  `
`    weighted by the average conductivity around the node.  `

`Usage:  `
`  >> pot = utilbem_pot_unbound(Coord, cond, dip)  `

`Inputs:  `
`   Coord - node coordinate matrix  `
`   cond  - average conductivity for each node (vector)  `
`          as computed by utilbem_compute_cond()  `
`   dip   - dipole [x y z px py pz]  `

`Outputs:  `
`   pot - node potentials for the homogeneous model  `

`Notes: When IPA is not used the weighted potential `
`   is the  Right-Hand-Side of the BEM matrix equation.`

Warping_mesh
------------

`Warping_mesh() - Produces the GUI for warping of a template head model  `
`        to measured electrode locations.`

`Usage:  `
`  >> Warping_mesh(varargin);  `

`Optional Arguments:  `
`  ’subjectdir’ - (string) Output folder. The results will be saved  `
`   in this folder.  `
`  ’subject’ - (string) Subject name. Subject-specific output files will be saved  `
`   starting with this name.  `
`  ’session’ - (string) Session name. Session-specific output files will be saved  `
`   starting with this name.`

warping_main_function
---------------------

`warping_main_function() - Main warping function.  `

`Usage:  `
`  >> [Ptm, ind, Cscalp_w,Cskull_w,CCSF_w,W,A,e,LMm2] =  `
`  warping_main_function(Cscalp, Escalp, Cskull, CCSF,LMm, Fm, Fd, pos);  `

`Inputs:  `
`  Cscalp, Escalp - scalp mesh  `
`  Cskull         - coordinates of skull mesh  `
`  CCSF           - coordinates of CSF mesh  `
`  LMm            - landmarks on the template mesh  `
`  Fm             - fiducials of the template mesh  `
`  Fd             - fiducials from the digitizer data  `
`  pos            - electrode locations  `

`Outputs:  `
`  Ptm      - electrode locations on the mesh  `
`  ind      - index of the electrodes on the mesh  `
`  Cscalp_w - warped scalp mesh coordinates  `
`  Cskull_w - warped skull mesh coordinates  `
`  CCSF_w   - warped CSF mesh coordinates  `
`  W, A, e  - warping transform parameters  `
`  LMm2     - warped landmarks  `
