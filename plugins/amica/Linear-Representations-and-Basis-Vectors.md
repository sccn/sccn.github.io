---
layout: default
title: amica
long_title: amica
parent: amica
grand_parent: Plugins
---
<font size=3> This page describes basic linear algebra concepts related
to linear representations in vector spaces. </font>

**Basis Vectors**
-----------------

<font size = 3>

Originally we are given the recorded data in the channel space, say with
<img src="https://latex.codecogs.com/svg.latex?n"> channels, and <img src="https://latex.codecogs.com/svg.latex?T"> samples (i.e. time points, frames). Thedata can be thought of as a collection of <img src="https://latex.codecogs.com/svg.latex?T"> vectors in<img src="https://latex.codecogs.com/svg.latex?n">-dimensional space, each of which in the case of EEG is asnapshot of the electric potential at the electrodes (relative to a
given reference) at a particular time point.

The data can also be thought of as a collection of <img src="https://latex.codecogs.com/svg.latex?n"> time series,or channel vectors, in <img src="https://latex.codecogs.com/svg.latex?T">-dimensional space; or as a collection ofspatiotemporal data segments (each e.g. an <img src="https://latex.codecogs.com/svg.latex?n\times L"> matrix) in<img src="https://latex.codecogs.com/svg.latex?(nL)">-dimensional space. As we are concerned here withinstantaneous ICA, we'll primarily think of the data as a set of
<img src="https://latex.codecogs.com/svg.latex?T"> vectors in <img src="https://latex.codecogs.com/svg.latex?n">-dimensional space, disregarding thetemporal order of the vectors.

ICA is a type of linear representation of data in terms of a set of
"basis" vectors. Since we're working here in <img src="https://latex.codecogs.com/svg.latex?n"> channel space, thevectors we're interested in will be in <img src="https://latex.codecogs.com/svg.latex?\mathbb{R}^n">. Toillustrate in the following we'll use a three dimensional example, say
recorded using three channels. The data then is given to us in three
dimensional vector space.


![700px](R3_2.png)


Each of these data points is a vector in three dimensional space.


<img src="https://latex.codecogs.com/svg.latex? \mathbf{x}_1,\mathbf{x}_2,\ldots,\mathbf{x}_T \in\mathbb{R}^3 ">

In general, any point in <img src="https://latex.codecogs.com/svg.latex?n">-dimensional space can be representedas a linear combination of any <img src="https://latex.codecogs.com/svg.latex?n"> vectors that are linearlyindependent. For example let's take the vectors,


<img src="https://latex.codecogs.com/svg.latex? \[\mathbf{b}_1 \mathbf{b}_2 \cdots \mathbf{b}_n\] \triangleq\mathbf{B} ">

Linear independence means that no vector in the set can be formed as a
linear combination of the others, i.e. each vector branches out into a
new dimension, and they do not all lie in a zero volume subspace of
<img src="https://latex.codecogs.com/svg.latex?\mathbb{R}^n">. Equivalently, there is no vector<img src="https://latex.codecogs.com/svg.latex?\mathbf{v}"> that can mulitply <img src="https://latex.codecogs.com/svg.latex?\mathbf{B}"> to produce thezero vector:


<img src="https://latex.codecogs.com/svg.latex? \nexists \; \mathbf{v} \; \text{such that}\; \mathbf{B}\mathbf{v} = 0 ">

Mathematically, this is true if and only if:


<img src="https://latex.codecogs.com/svg.latex? \det \mathbf{B} \neq 0 ">

So for example any data vector, <img src="https://latex.codecogs.com/svg.latex?\mathbf{x} \in \mathbb{R}^3">,can be represented in terms of three linearly independent basis vectors,
<img src="https://latex.codecogs.com/svg.latex?\mathbf{b}_1, \mathbf{b}_2, \mathbf{b}_3 \in\mathbb{R}^3">(unique) coefficient vector, <img src="https://latex.codecogs.com/svg.latex?\mathbf{c} \in \mathbb{R}^3">:

<img src="https://latex.codecogs.com/svg.latex? \mathbf{x} = \sum_{i=1}^3 c_i \mathbf{b}_i =\mathbf{B}\mathbf{c} ">

A linear representation of the data is a fixed basis set,
<img src="https://latex.codecogs.com/svg.latex?\mathbf{B}">, that is used to represent each data point:

<img src="https://latex.codecogs.com/svg.latex? \mathbf{x}_t = \sum_{i=1}^n c_{it} \mathbf{b}_i =\mathbf{B}\mathbf{c}_t ">

<img src="https://latex.codecogs.com/svg.latex?\mathbf{X} \triangleq\[\mathbf{x}_1\cdots \mathbf{x}_T\]">\\triangleq \[\\mathbf{c}_1\\cdots \\mathbf{c}_T\]</m>, the we can
write,


<img src="https://latex.codecogs.com/svg.latex? \mathbf{X} = \mathbf{B}\mathbf{C} ">

where <img src="https://latex.codecogs.com/svg.latex?\mathbf{X}"> is the <img src="https://latex.codecogs.com/svg.latex? n \times T\;"> data matrix, <img src="https://latex.codecogs.com/svg.latex?\mathbf{B}"> is the <img src="https://latex.codecogs.com/svg.latex? n \times n,\;"> matrix of basis vectors,and <img src="https://latex.codecogs.com/svg.latex?\mathbf{C}"> is the <img src="https://latex.codecogs.com/svg.latex? n \times T"> coefficient (orloading, or weight) matrix, with <img src="https://latex.codecogs.com/svg.latex?\mathbf{c}_t"> giving the"coordinates" of the point <img src="https://latex.codecogs.com/svg.latex?\mathbf{x}_t"> in the coordinate spacerepresented by the basis <img src="https://latex.codecogs.com/svg.latex?\mathbf{B}">.
We have assumed thus far that the data itself is "full rank", i.e. that
there exists a set of <img src="https://latex.codecogs.com/svg.latex?n"> data vectors that are linearlyindependent. It may happen, however, that the data do not lie in the
"full volume" of <img src="https://latex.codecogs.com/svg.latex?\mathbb{R}^n">, but rather occupy a subspace ofsmaller dimension.

In three dimensions, for example, all of the data might exist in a
two-dimensional subspace.


!![400px](R3_3.png)!![400px](R3_4.png)


The data is still represented as points or vectors in three dimensional
space, with three coordinates, but in fact only two coordinates are
required (once a "center" point has been fixed in the subspace).

Even if the data does not lie *exactly* in a subspace, it may be the
case that one of dimensions (directions) is just numerical noise.
Eliminating such extraneous dimensions can lead to more efficient and
stable subsequent processing of the data.

To understand how the data occupies the space volumetrically, and in the
case of data that is not full rank, how to determine which subspace the
data lies in, we will use Principle Component Analysis, described in the
next section.

</font>

**Principle Component Analysis (PCA)**
--------------------------------------

<font size=3> Let the data be represented by an <img src="https://latex.codecogs.com/svg.latex? n \times T"><img src="https://latex.codecogs.com/svg.latex?\mathbf{X} = \[\mathbf{x}_1\cdots \mathbf{x}_T\]"><img src="https://latex.codecogs.com/svg.latex?T"> vectors contained in the columns. Let us also assume that thedata is "zero mean", i.e. that the mean of each channel (row of
<img src="https://latex.codecogs.com/svg.latex?\mathbf{X}">) has been removed (subtracted from the row), so that:

<img src="https://latex.codecogs.com/svg.latex? \frac{1}{T} \sum_{t=1}^T \big\[\mathbf{X}\big\]_{it} =\, 0,\quad i = 1,\ldots, n ">

Now, one way to determine the rank of the data is to examine the
covariance matrix, or matrix of channel correlations, which is defined
by,


<img src="https://latex.codecogs.com/svg.latex? \mathbf{\Sigma} \;\triangleq\; \frac{1}{T} \sum_{t=1}^{T}\mathbf{x}_t \mathbf{x}_t^T \;=\; \mathbf{X}\mathbf{X}^T /\, T
">

The matrix <img src="https://latex.codecogs.com/svg.latex?\mathbf{\Sigma}"> has the same rank, or intrinsicdimensionality, as the matrix <img src="https://latex.codecogs.com/svg.latex?\mathbf{X}">. If we perform aneigen-decomposition of <img src="https://latex.codecogs.com/svg.latex?\mathbf{\Sigma}">, we get,

<img src="https://latex.codecogs.com/svg.latex? \mathbf{\Sigma} \;=\; \sum_{i=1}^{n} \lambda_i \mathbf{q}_i\mathbf{q_i}^T \;\triangleq\; \mathbf{Q}\mathbf{\Lambda}
\mathbf{Q}^T ">

where <img src="https://latex.codecogs.com/svg.latex?\lambda_i"> and <img src="https://latex.codecogs.com/svg.latex?\mathbf{q}_i,\, i = 1,\ldots,n,">are the eigenvalues and eigenvectors respectively.

Since <img src="https://latex.codecogs.com/svg.latex?\mathbf{\Sigma}"> is symmetric and "positive semidefinite",all the eigenvalues are real and non-negative. <img src="https://latex.codecogs.com/svg.latex?\mathbf{\Sigma}">(and thus <img src="https://latex.codecogs.com/svg.latex?\mathbf{X}">) is full rank if and only if all<img src="https://latex.codecogs.com/svg.latex? \lambda_i \> 0, \quad i =1,\ldots, n ">
If some of the eigenvalues are zero, then the data is not full rank, and
the rank is equal to the number of nonzero eigenvalues. In this case,
the data lies entirely in the <img src="https://latex.codecogs.com/svg.latex?r">-dimensional subspace spanned bythe eigenvectors corresponding to the nonzero eigenvalues.


<img src="https://latex.codecogs.com/svg.latex? \mathbf{x}_t = \sum_{i=1}^r c_{it} \mathbf{q}_i =\mathbf{B}\mathbf{c}_t ">

and,


<img src="https://latex.codecogs.com/svg.latex? \mathbf{X} = \mathbf{B}\mathbf{C} ">

where <img src="https://latex.codecogs.com/svg.latex?\mathbf{X}"> is the <img src="https://latex.codecogs.com/svg.latex? n \times T\;"> data matrix, <img src="https://latex.codecogs.com/svg.latex?\mathbf{B} = \[\mathbf{q}_1 \cdots \mathbf{q}_r\]"> is the <img src="https://latex.codecogs.com/svg.latex? n
\times r">matrix of basis vectors, and <img src="https://latex.codecogs.com/svg.latex?\mathbf{C}"> is the<img src="https://latex.codecogs.com/svg.latex? r \times T"> coefficient matrix, with <img src="https://latex.codecogs.com/svg.latex?\mathbf{c}_t">giving the "coordinates" of the point <img src="https://latex.codecogs.com/svg.latex?\mathbf{x}_t"> in the<img src="https://latex.codecogs.com/svg.latex?r">-dimensional space of the nonzero eigenvectors.
The data <img src="https://latex.codecogs.com/svg.latex?\mathbf{X}"> is reduced in dimension from <img src="https://latex.codecogs.com/svg.latex?n\times T"> to <img src="https://latex.codecogs.com/svg.latex?r\times T"> by "projecting" onto the <img src="https://latex.codecogs.com/svg.latex?r">-dimensionalspace,

<img src="https://latex.codecogs.com/svg.latex? \mathbf{C} = \mathbf{B}^T\mathbf{X} ">

Analysis may be conducted on the reduced data <img src="https://latex.codecogs.com/svg.latex?\mathbf{C}">, e.g.ICA may be performed, giving results in <img src="https://latex.codecogs.com/svg.latex?r"> dimensional space. Thecoordinates in the original <img src="https://latex.codecogs.com/svg.latex?n"> dimensional data space are thengiven by simply multiplying the <img src="https://latex.codecogs.com/svg.latex?r"> dimensional vectors by<img src="https://latex.codecogs.com/svg.latex?\mathbf{B}">. The <img src="https://latex.codecogs.com/svg.latex?n\times n">, rank <img src="https://latex.codecogs.com/svg.latex?r">, matrix<img src="https://latex.codecogs.com/svg.latex?\mathbf{P}">,

<img src="https://latex.codecogs.com/svg.latex? \mathbf{P} = \mathbf{B}\mathbf{B}^T ">

in this case is called a "projection matrix", projecting the data in the
full space onto the subspace spanned by the first <img src="https://latex.codecogs.com/svg.latex?r"> eigenvectors.
</font>

**Singular Value Decomposition (SVD)**
--------------------------------------

<font size = 3>

A related decomposition, called the Singular Value Decomposition (SVD),
can be performed directly on the data matrix itself to produce a linear
representation (of possibly reduced rank). The SVD decomposes the data
matrix into,


<img src="https://latex.codecogs.com/svg.latex? \mathbf{X} = \mathbf{U}\mathbf{S}\mathbf{V}^T ">

where <img src="https://latex.codecogs.com/svg.latex?\mathbf{X}"> is the <img src="https://latex.codecogs.com/svg.latex? n \times T\;"> data matrix, <img src="https://latex.codecogs.com/svg.latex?\\mathbf{U} = \[\mathbf{u}_1 \cdots \mathbf{u}_r\]"> is the <img src="https://latex.codecogs.com/svg.latex?n
\times r"> matrix of ortho-normal (orthogonal and unit norm) "left
eigenvectors", <img src="https://latex.codecogs.com/svg.latex?\mathbf{S}"> is the <img src="https://latex.codecogs.com/svg.latex? r \times r\;"> diagonalmatrix of strictly positive "singular values", and <img src="https://latex.codecogs.com/svg.latex?\mathbf{V}"> isthe <img src="https://latex.codecogs.com/svg.latex? T \times r"> matrix of orthonormal "right eigenvectors".
From the SVD, we see that,

<img src="https://latex.codecogs.com/svg.latex? \mathbf{\Sigma} \;\triangleq\; \mathbf{X}\mathbf{X}^T /\, T\;=\; \mathbf{U}\mathbf{S}\mathbf{V}^T
\mathbf{V}\mathbf{S}\mathbf{U}^T /\, T \;=\;
\mathbf{U}\mathbf{S}^2\mathbf{U}^T /\, T ">

so that <img src="https://latex.codecogs.com/svg.latex?\mathbf{U} = \mathbf{Q},"> and <img src="https://latex.codecogs.com/svg.latex?\mathbf{S}^2 /\, T =\mathbf{\Lambda}">. The SVD directly gives the linear
representation:


<img src="https://latex.codecogs.com/svg.latex? \mathbf{X} \;=\; \mathbf{U}\mathbf{C}\;=\;\mathbf{U}\big(\mathbf{U}^T\mathbf{X}\big) ">

<img src="https://latex.codecogs.com/svg.latex?\mathbf{C} = \mathbf{U}^T\mathbf{X} =\mathbf{S}\mathbf{V}^T">. The vectors in <img src="https://latex.codecogs.com/svg.latex?\mathbf{U}">orthonormal (orthogonal and unit norm), and the rows of
<img src="https://latex.codecogs.com/svg.latex?\mathbf{C}"> are orthogonal (since <img src="https://latex.codecogs.com/svg.latex?\mathbf{S}"> is diagonal,and <img src="https://latex.codecogs.com/svg.latex?\mathbf{V}"> is orthonormal.)
The SVD gives the unique linear representation (assuming singular values
are distinct) of the data matrix
<img src="https://latex.codecogs.com/svg.latex?\mathbf{X}=\mathbf{B}\mathbf{C}"> such that the columns of<img src="https://latex.codecogs.com/svg.latex?\mathbf{B}"> are orthonormal, and the rows of <img src="https://latex.codecogs.com/svg.latex?\mathbf{C}"><img src="https://latex.codecogs.com/svg.latex?\mathbf{C}\mathbf{C}^T =\mathbf{S}^2">values are all distinct; a subspace determined by equal singular values
does not have a unique orthonormal basis in this subspace, allowing for
arbitrary cancelling rotations of the left and right eigenvectors in
this subspace.)

Having the rows of <img src="https://latex.codecogs.com/svg.latex?\mathbf{C}"> be orthogonal, i.e. uncorrelated,is a desirable feature of the representation, but having the basis
vectors be orthonormal is overly restrictive in many cases of interest,
like EEG. However, if we only require the rows of <img src="https://latex.codecogs.com/svg.latex?\mathbf{C}"> tobe orthogonal, then we lose the uniqueness of the representation, since
for any orthonormal matrix <img src="https://latex.codecogs.com/svg.latex?\mathbf{R}">, and any full rankdiagonal matrix <img src="https://latex.codecogs.com/svg.latex?\mathbf{D}">, we have,

<img src="https://latex.codecogs.com/svg.latex? \mathbf{X} \;=\;(\mathbf{U}\mathbf{S}\mathbf{R}^T\mathbf{D}^{-1})(\mathbf{D}\mathbf{R}\mathbf{V}^{T})
">

where the rows of the new coefficient matrix
<img src="https://latex.codecogs.com/svg.latex?\mathbf{D}\mathbf{R}\mathbf{S}^{-1}\mathbf{C}"> are stillorthogonal, but the new matrix of basis vectors in the columns of,
<img src="https://latex.codecogs.com/svg.latex?\mathbf{U}\mathbf{S}\mathbf{R}^T\mathbf{D}^{-1}">, are nolonger orthogonal.

A linear representation of the data,


<img src="https://latex.codecogs.com/svg.latex? \mathbf{X} \;=\; \mathbf{B}\mathbf{C} ">

implies that the coefficients can be recovered from the data using the
inverse of <img src="https://latex.codecogs.com/svg.latex?\mathbf{B}"> (or in the case of rank deficient<img src="https://latex.codecogs.com/svg.latex?\mathbf{B}">, any left inverse, like the pseudoinverse):

<img src="https://latex.codecogs.com/svg.latex? \mathbf{C} \;=\; \mathbf{B}^{-1}\mathbf{X} ">

</font>

**PCA and Sphering**
--------------------

<font size=3> We have seen that the SVD representation is one linear
representation of the data matrix. The SVD puts,


<img src="https://latex.codecogs.com/svg.latex? \mathbf{R} = \mathbf{D} = \mathbf{I} ">

where <img src="https://latex.codecogs.com/svg.latex?\mathbf{I}"> is the identity matrix.
Another representation, which we call "sphering", puts,


<img src="https://latex.codecogs.com/svg.latex? \mathbf{R} = \mathbf{U}, \quad \mathbf{D} = \mathbf{I} ">

This latter representation has certain advantages. We can show, e.g.,
that the sphering transformation leaves the data changed as little as
possible among all "whitening" transformations, i.e. those that leave
the resulting rows of the coefficient matrix uncorrelated with unit
average power.


<img src="https://latex.codecogs.com/svg.latex? \frac{1}{T} \sum_{t=1}^T \big\[\mathbf{C}\big\]_{it}^2\,=\, 1, \quad i = 1,\ldots, n ">

This is equivalent to taking <img src="https://latex.codecogs.com/svg.latex?\mathbf{D} = \mathbf{I}">. Let thegeneral form of a "whitening" decorrelating transformation, then, be:


<img src="https://latex.codecogs.com/svg.latex? \mathbf{B}^{-1} \;=\; \mathbf{R}\mathbf{S}^{-1}\mathbf{U}^T">

for arbitrary orthonormal matrix <img src="https://latex.codecogs.com/svg.latex?\mathbf{R}">. We measure thedistance of the transformed data from the original data by the sum of
the squared errors:

<img src="https://latex.codecogs.com/svg.latex? E (\mathbf{B}^{-1}) = \frac{1}{T} \sum_{t=1}^{T}{\\|\mathbf{x}_t-\mathbf{B}^{-1}\mathbf{x}_t\\|^2} = \text{trace}((\mathbf{I}-\mathbf{B}^{-1})\mathbf{\Sigma}(\mathbf{I}-\mathbf{B}^{-1})^T) = \text{trace}(\mathbf{\Sigma}+\mathbf{B}^{-1}\mathbf{\Sigma}\mathbf{B}^{-T})-2 \,\text{trace}(\mathbf{B}^{-1}\mathbf{\Sigma}) ">

Writing <img src="https://latex.codecogs.com/svg.latex?\mathbf{B}^{-1}"> in the general form of the decorrelatingtransformation, we get,


<img src="https://latex.codecogs.com/svg.latex? E (\mathbf{R}) = \text{trace}(\mathbf{\Sigma}+\mathbf{I}) - 2\,\text{trace}(\mathbf{R}\mathbf{S}\mathbf{U}^T) =
\sum_{i=1}^n\; \sigma_{ii}^2 + 1 - 2\,\sigma_{ii}
\mathbf{u}_i^T \mathbf{r}_i \ge \sum_{i=1}^n\; (\sigma_{ii} -
1)^2 ">

Equality is achieved in the last inequality if and only if
<img src="https://latex.codecogs.com/svg.latex?\mathbf{R} = \mathbf{U}">. The resulting minimal squared error isthe same squared error that would be result from simply normalizing the
variance of each channel, which is equivalent to the transformation
<img src="https://latex.codecogs.com/svg.latex?\mathbf{S}^{-1}">.
We shall refer to this particular whitening transformation,
<img src="https://latex.codecogs.com/svg.latex?\mathbf{B}^{-1} \;=\; \mathbf{U}\mathbf{S}^{-1}\mathbf{U}^T">as the inverse of the "square root" of the covariance matrix
<img src="https://latex.codecogs.com/svg.latex?\mathbf{\Sigma}">. It is the unique symmetric matrix<img src="https://latex.codecogs.com/svg.latex?\mathbf{B}^{-1} \triangleq \mathbf{W}=\mathbf{W}^T"><img src="https://latex.codecogs.com/svg.latex?\mathbf{\Sigma} = \mathbf{W}\mathbf{W}^T =\mathbf{W}^2">
</font>

Remarks:

We can view this result as saying that the whitening matrix
<img src="https://latex.codecogs.com/svg.latex?\mathbf{B}^{-1} \;=\; \mathbf{U}\mathbf{S}^{-1}\mathbf{U}^T">either as a collection of channel vectors, or as a collection of channel
<img src="https://latex.codecogs.com/svg.latex?\mathbf{R} =\mathbf{U}"><img src="https://latex.codecogs.com/svg.latex?\mathbf{U}^T">.
We have found in practice, performing ICA on EEG data, that using the
(symmetric) sphering matrix as an initialization of for ICA generally
yields the best results and the quickest convergence, especially in
<img src="https://latex.codecogs.com/svg.latex?\mathbf{B}^{-1} \;=\;\mathbf{S}^{-1}\mathbf{U}^T ">whitening transformation produces more independent components than the
latter. This is confirmed empirically in our mutual information
computations.

Why should the sphering matrix
<img src="https://latex.codecogs.com/svg.latex?\mathbf{U}\mathbf{S}^{-1}\mathbf{U}^T "> produce moreindependent time series and a better starting point for ICA than the
whitening matrix <img src="https://latex.codecogs.com/svg.latex?\mathbf{S}^{-1}\mathbf{U}^T ">? In the case ofEEG, this is likely due to the fact that the EEG sensor electrodes are
spread out at distances of the same order as the distance between the
EEG sources. Thus the sources tend to have a much larger effect on a
relatively small number of sensors, rather than a moderate effect on all
of the sensors.

The whitening matrix <img src="https://latex.codecogs.com/svg.latex?\mathbf{S}^{-1}\mathbf{U}^T ">, inprojecting the data onto the eigenvectors of the covariance matrix,
produces time series that are each mixtures of all of the channels, and
in this sense more mixed than the original data, in which the sources
distribute over a relatively small number of channels.

The sphering matrix <img src="https://latex.codecogs.com/svg.latex?\mathbf{U}\mathbf{S}^{-1}\mathbf{U}^T "> onthe other hand, rotates the transformed data back into its original
coordinates, and produces time series that are closest to the original
data, which was relatively independent at the start.

By leaving the data in the eigenvector coordinate system, the whitening
matrix <img src="https://latex.codecogs.com/svg.latex?\mathbf{S}^{-1}\mathbf{U}^T "> forces the ICA algorithm to“undo” a great deal of mixing in the time series, and as a starting
point for iterative algorithms, makes it more difficult (in terms of
potential local optima) and more time consuming (since the starting
point is farther from the ICA optimum).

**EEG Data Reference and Re-referencing**
-----------------------------------------

<font size=3> EEG data is recorded as a potential difference between the
electrode location and the reference. Biosemi active recordings use a
reference that is separate from the scalp electrodes. If data is
recorded with a specific electrode reference, then the data essentially
includes a "zero" channel corresponding to the signal at the reference
location relative to itself.

A commonly used reference is the "average reference", which consists
essentially of subtracting the mean scalp potential at each time point
from the recorded channel potential. Let the vector of all ones be
denoted, <img src="https://latex.codecogs.com/svg.latex?\mathbf{e} \triangleq \[1 \cdots 1\]^T">. If the datais denoted <img src="https://latex.codecogs.com/svg.latex?\mathbf{X}">, then average referenced data isequivalent to,


<img src="https://latex.codecogs.com/svg.latex? (\mathbf{I} - \mathbf{e}\mathbf{e}^T\! / n) \mathbf{X}">

The average reference reduces the rank of the data because the
referencing matrix is rank <img src="https://latex.codecogs.com/svg.latex?n-1"> (note that if you include theoriginal reference when computing average reference, average reference
does not reduce the rank of the data). In particular, the vector
<img src="https://latex.codecogs.com/svg.latex?\mathbf{e}"> is in the "null space" of the referencing matrix:

<img src="https://latex.codecogs.com/svg.latex? (\mathbf{I} - \mathbf{e}\mathbf{e}^T\! / n) \mathbf{e} =\mathbf{0}">

The left-hand side is transformed as


<img src="https://latex.codecogs.com/svg.latex? (\mathbf{I} - \mathbf{e}\mathbf{e}^T\! / n) \mathbf{e}">

<img src="https://latex.codecogs.com/svg.latex? = \mathbf{e} - \mathbf{e}\*(\mathbf{e}^T\! \* \mathbf{e}) /n">

Here, the (1/**n**) is key since
(**e**<sup>*T*</sup>  \* **e**)/**n** = 1. Therefore,


<img src="https://latex.codecogs.com/svg.latex? = \mathbf{e} - \mathbf{e}">

<img src="https://latex.codecogs.com/svg.latex? = 0">

Re-referencing to a specific channel or channels can be represented
similarly. Let the vector with one in the *j*th position be denoted


<img src="https://latex.codecogs.com/svg.latex?\mathbf{e}_j \triangleq \[0 \cdots 0\,\overbrace{1}^{j\mathrm{th} }\, 0 \cdots 0\]^T">

Suppose e.g. that the mastoid electrode numbers are <img src="https://latex.codecogs.com/svg.latex?j"> and<img src="https://latex.codecogs.com/svg.latex?k">. Then the linked mastoid re-reference is equivalent to:

<img src="https://latex.codecogs.com/svg.latex? \big(\mathbf{I} -\mathbf{e}(\mathbf{e}_j+\mathbf{e}_k)^T\!/2\big) \mathbf{X}">

Again, however, <img src="https://latex.codecogs.com/svg.latex?\mathbf{e}"> is in the null space of thisreferencing matrix, showing that the rank is <img src="https://latex.codecogs.com/svg.latex?n-1">. Any referencingmatrix will be rank deficient, and will thus leave the data rank
deficient by one dimension.

In addition to referencing, EEG pre-processing usually includes
high-pass filtering (to reduce non-stationarity caused by slow drifts).
Linear filtering (such as high, low, band-pass, FIR, IIR, etc.) can be
represented as a matrix multiplication of the data on the right by a
large matrix <img src="https://latex.codecogs.com/svg.latex?\mathbf{F}"> whose columns are time shifted versionsof each other. The combined referencing and filtering operations can be
represented as:


<img src="https://latex.codecogs.com/svg.latex? \big(\mathbf{I} -\mathbf{e}(\mathbf{e}_j+\mathbf{e}_k)^T\!/2\big) \mathbf{X}
\mathbf{F}">

The resulting referenced and filtered matrix should remain rank
deficient by one. However when referencing is done first, reducing the
rank by one, and then filtering is performed, it may happen that the
rank of the data increases so that it becomes essentially full rank
again. This is apparently due to numerical effects of multiplying (in
effect) by a <img src="https://latex.codecogs.com/svg.latex?T \times T"> matrix <img src="https://latex.codecogs.com/svg.latex?\mathbf{F}">.
To summarize, re-referencing should reduce the rank of the data,
relegating it to an <img src="https://latex.codecogs.com/svg.latex?n-1"> dimensional subspace of the<img src="https://latex.codecogs.com/svg.latex?n">-dimensional channel space. However, subsequent filtering of therank-reduced referenced data *may* increase the rank of the data again
(so that the minimum singular value is significantly larger than zero.)
In this case, numerical noise in the vector (direction)
<img src="https://latex.codecogs.com/svg.latex?\mathbf{e}"> is essentially added back into the data as anindependent component.

</font>