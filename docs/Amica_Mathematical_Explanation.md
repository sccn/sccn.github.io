---
layout: default
title: Amica Mathematical Explanation
permalink: /docs/Amica_Mathematical_Explanation
parent: Docs
---

This page is about the Amica algorithm itself. For installation and
application of Amica, refer to this [page](/AMICA "wikilink") instead.

This page provides a tutorial introduction to ICA using the Amica
algorithm and Matlab. <span style="color:#0000FF">For general tutorial
and information on Amica, including how to run Amica and how to analyze
Amica results, [visit this
page](https://sccn.ucsd.edu/wiki/AMICA).</span>

### **Introduction**

<font size=3> We will first illustrate the tools using generated example
data. For this purpose, we provide a matlab function to generate data
from the Generalized Gaussian distribution. A description, as well as
the notation we will use for the Generalized Gaussian density can be
found here:

[Generalized Gaussian Density](/Generalized_Gaussian "wikilink")

Further mathematical background and detail can be found at the following
pages:

[Linear Representations and Basis
Vectors](/Linear_Representations_and_Basis_Vectors "wikilink")

[Random Variables and Probability Density
Functions](/Random_Variables_and_Probability_Density_Functions "wikilink")

Let us consider first the case of two independent Generalized Gaussian
sources with shape parameter <m>\\rho = 3/2</m>.

<center>

<m> \\parstyle \\begin{eqnarray\*} S_1 \\sim
\\mathcal{GG}(s_1;0,1,3/2) \\\\ S_2 \\sim \\mathcal{GG}(s_2;0,3,3/2)
\\end{eqnarray\*} </m>

</center>

In Matlab, using the function gg6.m (available in the Matlab code
section of the above Generalized Gaussian link), we can generate
<m>N=2000</m> of these sources with the command:

`s = gg6(2,2000,[0 0],[1 3],[1.5 1.5]);`

Suppose our basis vectors and source vectors are given by:

<center>

<m> \\parstyle \\begin{eqnarray\*} \\mathbf{a}_1 =
\\left\[\\begin{matrix}1\\\\4\\end{matrix}\\right\], \\quad
\\mathbf{a}_2 = \\left\[\\begin{matrix}4\\\\1\\end{matrix}\\right\],
\\quad \\mathbf{A} = \[\\mathbf{a}_1\\, \\mathbf{a}_2\], \\quad
\\mathbf{s} = \\left\[\\begin{matrix}s_1\\\\s_2\\end{matrix}\\right\]
\\end{eqnarray\*} </m>

</center>

<center>

<m> \\parstyle \\begin{eqnarray\*} \\mathbf{x} = \\mathbf{A} \\mathbf{s}
\\end{eqnarray\*} </m>

</center>

In Matlab:

`A = [1 4 ; 4 1];`
`x = A*s;`

<center>

[900px](/Image:ica24.png "wikilink")

</center>

Matlab code used to generate this figure is here:
[LT_FIG.m](/ICA_FIG.m "wikilink")

## PCA

PCA can be used to determine the "principle axes" of a dataset, but it
does not uniquely determine the basis associated with the linear model
of the data,

<center>

<m> \\mathbf{x} = \\mathbf{A}\\mathbf{s}\\\\ </m>

</center>

PCA is only concerned with the second order (variance) characteristics
of the data, specifically the mean, <m>\\mathbf{\\mu}</m>, and
covariance,

<center>

<m> \\mathbf{\\Sigma} \\triangleq \\frac{1}{T} \\sum_{t=1}^T
(\\mathbf{x}_t-\\mathbf{\\mu})(\\mathbf{x}_t-\\mathbf{\\mu})^T\\\\
</m>

</center>

For independent sources combined linearly, the covariance matrix is just
(assuming zero mean),

<center>

<m> \\mathbf{\\Sigma} = \\frac{1}{T} \\sum_{t=1}^T \\mathbf{x}_t
\\mathbf{x}_t^T = \\frac{1}{T} \\sum_{t=1}^T \\mathbf{A}
\\mathbf{s}_t \\mathbf{s}_t^T \\mathbf{A}^T = \\mathbf{A} \\left(
\\frac{1}{T} \\sum_{t=1}^T \\mathbf{s}_t \\mathbf{s}_t^T\\right)
\\mathbf{A}^T = \\mathbf{A}\\mathbf{D}\\mathbf{A}^T </m>

</center>

where <m>\\mathbf{D}</m> is the diagonal matrix of source variances.
Thus any basis, <m>\\mathbf{A}</m>, satisfying,

<center>

<m> \\mathbf{\\Sigma} = \\mathbf{A}\\mathbf{D}\\mathbf{A}^T </m>

</center>

will lead to a covariance matrix of <m>\\mathbf{\\Sigma}</m>. And since
the decorrelating matrices are all determined solely based on the
covariance matrix, it is impossible to determine a unique linear basis
from the covariance alone. Matrices, unlike scalar real numbers,
gnerally have an infinite number of "square roots". See
[Linear_Representations_and_Basis_Vectors](/Linear_Representations_and_Basis_Vectors "wikilink")
for more information. As shown in that section, PCA can be used to
determine the subspace in which the data resides if it is not full rank.

To further illustrate the non-uniqueness of the PCA basis, consider the
following figure in which <m>\\mathcal{GG}(s;0,1,1)</m> (i.e. Laplacian)
sources are combined with the linear matrix,

`N = 2000;`
`A = [1 2 ; 4 0.1];`
`A(:,1)=A(:,1)/norm(A(:,1));`
`A(:,2)=A(:,2)/norm(A(:,2));`
`s = gg6(2,N,[0 0],[1 3],[1 1]);`
`x = A*s;`

We produce two sets of decorrelated sources, one that simply projects
onto the eigenvectors, and the other which uses the unique symmetric
square root "sphering" matrix (see [Linear Representations and Basis
Vectors](/Linear_Representations_and_Basis_Vectors "wikilink") for more
detail.)

`[V,D] = eig(x*x'/N);`
`Di = diag(sqrt(1./diag(D)));`
`u = Di * V' * x;`
`y = V * Di * V' * x;`

<center>

[1000px](/Image:pca_p1.png "wikilink")

</center>

Similarly for <m>\\mathcal{GG}(s;0,1,10)</m> sources,

`s = gg6(2,2000,[0 0],[1 3],[10 10]);`
`x = A*s;`

<center>

[1000px](/Image:pca_p10.png "wikilink")

</center>

Gaussian sources, unlike non-Gaussian sources, are completely determined
by second order statistics, i.e. mean and covariance. If Gaussian random
variables are uncorrelated, then they are independent as well.
Futhermore, linear combinations or Gaussians are Gaussian. So linearly
mixed Gaussian data is Gaussian with covariance matrix,

`s = gg6(2,2000,[0 0],[1 3],[2 2]);`
`x = A*s;`

<center>

<m> \\mathbf{\\Sigma} = \\mathbf{A}\\mathbf{D}\\mathbf{A}^T </m>

</center>

And any of the infinite number of root matrices <m>\\mathbf{A}</m>
satisfying this equation will yield Gaussian data with identical
statistics to the observed data.

<center>

[1000px](/Image:pca_p2.png "wikilink")

</center>

As seen in the bottom row, the joint source density is radially
symmetric, i.e. it "looks" exactly the same in all directions. There is
no additional structure in the data beyond the source variances and the
covariance. To fix a particular solution, constraints must be placed on
the variance of the sources, or the norm of the basis vectors. However,
this generally cannot be done since the ICA model assumes only
independence of the sources. The source or basis vector norm is usually
fixed, which determines the magnitude of the non-fixed variance or norm.

Fortunately, real sources are usually non-Gaussian, so if the ICA model
holds and the sources are independent, then there is a unique basis
representation of the data such that the sources are independent.

## Basic ICA

Let's take some two dimensional data following the ICA model.

`s = gg6(2,2000,[0 0],[1 3],[1 1]);`
`A = [1 2 ; 4 0.1];`
`x = A*s;`

The program amica_ex.m will be used to illustrate ICA using the Amica
algorithm. The output is shown below:

<center>

[800px](/Image:ica1.png "wikilink")

</center>

We can also experiment with multimodal sources using the function
ggrandmix0.m:

`s = ggrandmix0(2,20000,3); % random 2 x 20000 source matrix, with 3 mixtures in each source density`
`x = A*s;`

<center>

[800px](/Image:ica2.png "wikilink")

</center>

## Multiple Models

In the same way we created complex mixture source densities by combining
a number of Generalized Gaussian constituent densities, we can create a
complex data model by combining multiple ICA models in an ICA mixture
model. The likelihood of the data from a single time point, then is
given by,

<center>

<m> p(\\mathbf{x}_t) = \\sum_{h=1}^M \\gamma_h \\,
p_h(\\mathbf{x}_t;\\mathbf{A}_h,\\theta_h), \\quad \\sum_{h=1}^M
\\gamma_h = 1, \\quad \\gamma_h\\ge0, \\,\\,h = 1,\\ldots,M </m>

</center>

where <m>\\mathbf{A}_h</m> and <m>\\theta_h</m> are the mixing matrix
and density parameters associated with model <m>h</m>.

<center>

[500px](/Image:gg_clb.png "wikilink")

</center>

We can use the program ggmixdat.m to generate random ICA mixture model
data with random Generalized Gaussian sources:

`[x,As,cs] = ggmixdata(2,2000,3,[1 1; 1 1],ones(2,2),2);`

We use the program amica_ex.m to illustate:

`[A,c,LL,Lt,gm,alpha,mu,beta,rho] = amica_ex(x,3,1,200,1,1e-6,1,0,1,As,cs);`

<center>

[500px](/Image:ica_mix_dat.png "wikilink")

</center>

The output is shown below:

<center>

[1000px](/Image:ica_mix.png "wikilink")

</center>

Given a mixture model, we can use Bayes' Rule to determine the posterior
probability that model <m>h</m> generated the data at time point
<m>t</m>. Let <m>M_t</m> be the index of the model active at time point
<m>t</m>. Then for the probability of model <m>h</m> given
<m>\\mathbf{x}_t</m>, we have,

<center>

<m> P(M_t=h | \\mathbf{x}_t) \\; = \\; \\frac{p(\\mathbf{x}_t |
M_t=h) P(M_t=h)} {\\sum_{j=1}^M p(\\mathbf{x}_t | M_t=j) P(M_t=j)}
</m>

</center>

A plot of the posterior log likelihood given each model is shown below.

<center>

[1000px](/Image:LLggmix.png "wikilink")

</center>

</font>