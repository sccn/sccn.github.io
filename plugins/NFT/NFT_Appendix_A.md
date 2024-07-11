---
layout: default
title: NFT_Appendix_A
long_title: NFT_Appendix_A
parent: NFT
grand_parent: Plugins
---
BEM Mesh Format
---------------

The generated BEM mesh is stored on disk as a set of three files: an
element file, a coordinate file, and an information file. All three mesh
files have the same base name, with the file extension specifying the
file type. The file extensions are .bee for the element file, .bec for
the coordinate file and .bei for the information file. All the files are
ASCII text files for easier processing and portability.

The information file (.bei) defines the high level properties of the
mesh. Each mesh consist of one or more boundaries. Since the boundaries
separate tissues, each boundary has an inside and outside tissue type.
The first row of the information file contains information about the
mesh structure. The entries of the first row are the number of
boundaries, the number of nodes, the number of elements, and the number
of nodes per element respectively. For linear meshes there are 3 nodes
per element and for quadratic meshes there are 6 nodes per element. The
following rows of the information file define the boundary information.
Since an element can be a part of only one boundary, the elements of the
mesh are grouped according to the boundary, and from outside to inside.
Therefore, each boundary is a consecutive group of elements. For the
boundary rows, the first column is the boundary index. Second column
gives the number of elements in the boundary. The third and fourth
columns represent the inner and outer tissue class of the boundary.

The tissue class is an integer representing a tissue. This number is
defined per mesh, there is no global assignment of tissue classes at the
moment. The purpose of tissue class is to uniquely define the various
tissues that are represented by the mesh. Since different tissues may
have same or similar conductivities, using a tissue class identifier
provides a better distinction. Furthermore, this scheme makes it
possible to solve the same mesh geometry using different tissue
conductivity values.

The coordinate file (.bec) defines the physical coordinates of the nodes
in the BEM mesh. There is one node per row. The first column is the node
index, and runs from one to the number of nodes in the mesh. The next
three columns represent the x, y, and z coordinates of the node.

The element file (.bee) defines the connectivity of the nodes for each
element. The element file defines one element per row. The first column
is the element index, and runs from one to the number of elements in the
mesh. The next three (linear mesh) or six (quadratic mesh) columns
define the node indexes for the element. Note that the order of nodes
are important, and define the orientation of the element.
