---
layout: default
parent: AMICA
grand_parent: Plugins
render_with_liquid: false

title: Random-Variables-and-Probability-Density-Functions
long_title: Random-Variables-and-Probability-Density-Functions
---
<font size = 3> This page reviews the concepts of random variables
(rv's) and probability density functions (pdfs). It describes
Kullback-Leibler (KL) Divergence and Maximum Likelihood (ML) estimation,
as well as multivariate probability densities and the effect of linear
transformations on multivariate probability density functions. </font>

**RVs and PDFs**
----------------

<font size = 3> A random variable <img src="https://latex.codecogs.com/svg.latex?X"> can be thought of as anordinary variable <img src="https://latex.codecogs.com/svg.latex?x">, together with a rule for assigning to everyset <img src="https://latex.codecogs.com/svg.latex?\mathcal{D}"> a probability that the variable takes a value inthat set, <img src="https://latex.codecogs.com/svg.latex?P(X \in \mathcal{D})">, which in our case will bedefined in terms of the probability density function:


<img src="https://latex.codecogs.com/svg.latex? P(X \in \mathcal{D}) = \int_{\mathcal{D} } p_{X}(x)\,dx ">

That is, the probability that <img src="https://latex.codecogs.com/svg.latex?X \in \mathcal{D}"> is given by theintegral of the probability density function over <img src="https://latex.codecogs.com/svg.latex?\mathcal{D}">.So a (continuous) random variable can be thought of as a variable and a
pdf. When the values taken by a random variable are discrete, e.g. 0 or
1, then the distribution associated with the random variable is referred
to as a probability *mass* function, or pmf. Here we will be concerned
primarily with signals taking values in a continuous range.

Continuous random variables are often taken to be Gaussian, in which
case the associated probability density function is the Gaussian, or
Normal, distribution,


<img src="https://latex.codecogs.com/svg.latex? p_{X}(x) \;=\; \mathcal{N}(x; \mu, \sigma^2) \;\triangleq\;(2\pi)^{-1/2}\sigma^{-1}
\exp(\mbox{$-\frac{1}{2}$}\hspace{1pt}\sigma^{-2} (x-\mu)^2 ) ">

![500px](Npdf.png)


The Gaussian density is defined by two parameters: the location, or
mean, <img src="https://latex.codecogs.com/svg.latex?\mu">, and the scale, or variance, <img src="https://latex.codecogs.com/svg.latex?\sigma^2">.
</font>

### Confidence intervals and *p* values

<font size = 3> An example of using the density function to calculate
probabilities is the computation of confidence intervals and <img src="https://latex.codecogs.com/svg.latex?p"><img src="https://latex.codecogs.com/svg.latex?\mathcal{D} \triangleq\[\mu-R,\mu+R\]">that,


<img src="https://latex.codecogs.com/svg.latex? P(\mu-R\le X \le \mu+R) = \int_{\mu-R}^{\mu+R} p_X(x)\,dx\; = \; 0.95 ">

Similarly, a (one-sided) <img src="https://latex.codecogs.com/svg.latex?p"> value or score for an observation<img src="https://latex.codecogs.com/svg.latex?x_0 > 0">, given a probability density function <img src="https://latex.codecogs.com/svg.latex?p_0(x)"> isgiven by,


<img src="https://latex.codecogs.com/svg.latex? P(X \ge x_0) = \int_{x_0}^{\infty} p_0(x)\,dx \; = \; p ">

This gives the probability that the random variable takes a value in the
tail region, defined (after the observation) as the set of values with
positive magnitude at least as great as the observed value, given that
the probability density is <img src="https://latex.codecogs.com/svg.latex?p_0(x)">. (A two-sided <img src="https://latex.codecogs.com/svg.latex?p"> valueconcerning the magnitude would include the integral from <img src="https://latex.codecogs.com/svg.latex?-x_0"> to<img src="https://latex.codecogs.com/svg.latex?-\infty"> as well.) A low <img src="https://latex.codecogs.com/svg.latex?p"> value can be used as evidencethat the probability density function <img src="https://latex.codecogs.com/svg.latex?p_0(x)"> is not the trueprobability density function <img src="https://latex.codecogs.com/svg.latex?p_X(x)">, i.e. to reject the nullhypothesis that <img src="https://latex.codecogs.com/svg.latex?p_0(x)"> is the probability density function, ormodel, associated with <img src="https://latex.codecogs.com/svg.latex?X">, on the grounds that if it were thecorrect model, then an event of very low probability would have
occurred.

Note that the value of a pdf at any point is not a probability value.
Probabilities for continuous random variables are only associated with
*regions*, and are only determined by integrating the pdf.

</font>

### Model Comparison and Posterior Likelihood Evaluation

<font size = 3> Related to the idea of <img src="https://latex.codecogs.com/svg.latex?p"> values is testing the"goodness of fit" of a model. The model is defined in terms of a
probability distribution, and the fit of the model is defined in terms
of the fit of the model probability distribution to the actual
probability distribution.

Bayes' Rule is often used to calculate the probability that a certain
model, say <img src="https://latex.codecogs.com/svg.latex?M_{i}"> from a set of <img src="https://latex.codecogs.com/svg.latex?n"> models,<img src="https://latex.codecogs.com/svg.latex?M_1,\ldots,M_n">, generated an observation <img src="https://latex.codecogs.com/svg.latex?x_0">:

<img src="https://latex.codecogs.com/svg.latex? P(M_i \| x_0) \; = \; \frac{p(x_0 \| M_i) P(M_i)} {\sum_{j=1}^np(x_0 \| M_j) P(M_j)} ">

</font>

**Model Fitting -- KL Divergence and ML Estimation**
----------------------------------------------------

<font size = 3> A probability density with a set of parameters can be
thought of as a class or set of probability density functions, for example the set of all Gaussian densities with <img src="https://latex.codecogs.com/svg.latex?-\infty%20%3C%20\mu%20%3C%20\infty,%20\sigma^2%20%3E%200">.

Fitting a model to an observed data set can be thought of as looking for
the particular density in the class of densities defined by the model,
that "best fits" the distribution of the data. One way of defining the
distance between two densities, as a measure of fit, is the
Kullback-Leibler Divergence:

<img src="https://latex.codecogs.com/svg.latex? D\big(p(x) \|\, p_0(x)\big)\; \triangleq \; \int p(x) \log\frac{p(x)}{p_0(x)} \, dx ">

where <img src="https://latex.codecogs.com/svg.latex?p_0(x)"> is a model density, and <img src="https://latex.codecogs.com/svg.latex?p(x)"> is the truedensity. The KL divergence is non-negative and zero if and only if
densities are the same. However note that it is non-symmetric in the
densities. If we write out the KL divergence as stated, we get,

<img src="https://latex.codecogs.com/svg.latex? D\big(p(x) \|\, p_0(x)\big)\; \triangleq \; \int -p(x)\log p_0(x) \, dx - h(X) \; \ge \; 0 ">

where <img src="https://latex.codecogs.com/svg.latex?h(X)"> is the entropy of <img src="https://latex.codecogs.com/svg.latex?X">. This shows that we the KLdivergence can be viewed as the excess entropy, or minimal coding rate,
imposed by assuming that the distribution of <img src="https://latex.codecogs.com/svg.latex?X"> is <img src="https://latex.codecogs.com/svg.latex?p_0">.
Writing the KL divergence in this way also shows its relationship to
Maximum Likelihood (ML) estimation with independent samples. In this
case, the ML problem, assuming a model <img src="https://latex.codecogs.com/svg.latex?M_0"> with parameters <img src="https://latex.codecogs.com/svg.latex?\theta">, for the random variable <img src="https://latex.codecogs.com/svg.latex?X">, is to maximize:

<img src="https://latex.codecogs.com/svg.latex?%20L(\{x_1,\ldots,x_T\}%20|%20%20M_0)%20=\sum_{t=1}^T%20\log%20p_0(x_t)">

But by the law of large numbers, we have,

<img src="https://latex.codecogs.com/svg.latex?%20\frac{1}{T}\sum_{t=1}^T\log%20p_0(x_t)\to_{T\to\infty}%20\int%20p(x)\log%20p_0(x)dx">

So in fact,

<img src="https://latex.codecogs.com/svg.latex? \arg \max_{\theta} \frac{1}{T}\sum_{t=1}^T \log p_0(x_t\,\, \\; \theta) \; \to \; \arg \max_{\theta}
-D\big(p(x) \\|\, p_0(x \,\\; \theta)\big)-h(X) \; = \; \arg
\min_{\theta} D\big(p(x)\\|\,p_0(x\,\, \\; \theta)\big) ">

and we see that as <img src="https://latex.codecogs.com/svg.latex?T \to \infty">, ML estimation is equivalent todetermining the density in the class of densities defined by the
variation of the parameter <img src="https://latex.codecogs.com/svg.latex?\theta">.
</font>

**Multivariate Probability Densities and Independence**
-------------------------------------------------------

<font size = 3> As in the univariate case, multivariate RVs are defined
by rules for assigning probabilities to the events that the multivariate
random random variable (i.e. random vector) takes a value in some
multidimensional set.


<img src="https://latex.codecogs.com/svg.latex? P\big(\[X_1,\ldots,X_n\]^T \in \mathcal{D}\big) =\int_{\mathcal{D} } p_{X_1,\ldots,X_n}(\mathbf{x})\,d\mathbf{x}
">

A set of random variables is defined to be independent if it's joint
probability density function factorizes into the product of the
"marginal" densities:


<img src="https://latex.codecogs.com/svg.latex? p_{X_1,\ldots,X_n}(x_1,\ldots,x_n) \; = \; \prod_{i=1}^n\,p_{X_i}(x_i) ">

In the case of a random vector with independent components, the
probability that the vector takes a value in a hypercubic set is simply
the product of the probabilities that the individual components lie in
the region defining the respective side of the hypercube:


<img src="https://latex.codecogs.com/svg.latex? P\big(\[X_1,\ldots,X_n\]^T \in \mathcal{D}_1 \times \cdots\times \mathcal{D}_n \big) = \prod_{i=1}^n\,P(X_i \in
\mathcal{D}_i) ">

</font>

**Probability Densities of Linear Transformations of RVs**
----------------------------------------------------------

<font size = 3>

If <img src="https://latex.codecogs.com/svg.latex?a \ne 0"> is a fixed real number, and <img src="https://latex.codecogs.com/svg.latex?S"> is a randomvariable <img src="https://latex.codecogs.com/svg.latex?X"> with pdf <img src="https://latex.codecogs.com/svg.latex?p_s(s)">, then a random variable definedby


<img src="https://latex.codecogs.com/svg.latex? X = a S ">

has pdf,


<img src="https://latex.codecogs.com/svg.latex? p_{x}(x) = \frac{1}{\|a\|}\, p_s\!\left(\frac{x}{a}\right) =\|a\|^{-1} p_{s}(a^{-1}x) ">

If <img src="https://latex.codecogs.com/svg.latex?A"> is an invertible <img src="https://latex.codecogs.com/svg.latex?n \times n"> matrix, and<img src="https://latex.codecogs.com/svg.latex?\mathbf{s}"> is a random vector with pdf <m>p_{\mathbf{s}}(\\mathbf{s})</m>, then the probability density of the random vector
<img src="https://latex.codecogs.com/svg.latex?\mathbf{x}">, produced by the linear transformation,

<img src="https://latex.codecogs.com/svg.latex? \mathbf{x} = \mathbf{A} \mathbf{s} ">

is given by the formula,


<img src="https://latex.codecogs.com/svg.latex? p_{\mathbf{x} }(\mathbf{x}) = \|\det \mathbf{A}\|^{-1}p_{\mathbf{s} }(\mathbf{A}^{-1}\mathbf{x}) ">

If <img src="https://latex.codecogs.com/svg.latex?\mathbf{A}"> is not square, but rather is "undercomplete", then PCA analysis can readily identifyan orthonormal basis for the <img src="https://latex.codecogs.com/svg.latex?r">-dimensional subspace in which thedata resides, and subsequent processing, e.g. ICA, can generally be
carried out in the reduced <img src="https://latex.codecogs.com/svg.latex?r">-dimensional space and a square <m>r\\times r</m> linear transformation.

If there is additional non-negligible noise in the undercomplete or
complete (square) case,


<img src="https://latex.codecogs.com/svg.latex? \mathbf{x} = \mathbf{A} \mathbf{s} + \mathbf{\nu} ">

with <img src="https://latex.codecogs.com/svg.latex?\mathbf{\Sigma} = E\{\mathbf{\nu}\mathbf{\nu}^T\}">,then the problem essentially becomes an "overcomplete" one with
<img src="https://latex.codecogs.com/svg.latex?\tilde{\mathbf{A} } \triangleq\big\[\mathbf{A}\,\mathbf{\Sigma}^{1/2}\big\]">
If the matrix <img src="https://latex.codecogs.com/svg.latex?\mathbf{A}"> is "overcomplete" with <img src="https://latex.codecogs.com/svg.latex?n\>m">,then the pdf of <img src="https://latex.codecogs.com/svg.latex?\mathbf{x}"> cannot generally be determined inclosed form unless <img src="https://latex.codecogs.com/svg.latex?\mathbf{s}"> is Gaussian. We will consider theovercomplete in another section.

</font>