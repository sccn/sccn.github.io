---
layout: default
title: amica
long_title: amica
parent: amica
grand_parent: Plugins
---
A multivariate pdf is generally a function of a vector space. If the individual variables, or components of the random vector, are independent, then the pdf factorizes into the product of univariate pdfs associated with the components.

# Mutual Information and Pairwise Mutual Information (PMI)
Mutual Information can be used as a measure of dependence. The MI between two random variables <img src="https://latex.codecogs.com/svg.latex?math=X">  and <img src="https://latex.codecogs.com/svg.latex?math=Y"> is always non-negative. Let <img src="https://latex.codecogs.com/svg.latex?math=X"> and <img src="https://latex.codecogs.com/svg.latex?math=Y"> have probability density functions <img src="https://latex.codecogs.com/svg.latex?math=p(x)"> and <img src="https://latex.codecogs.com/svg.latex?math=p(y)">. Then:

![](https://latex.codecogs.com/svg.latex?I(X;Y)%20=%20D\big(p(x,y)\,\big\|\,p(x)p(y)\big)%20=%20\iint%20p(x,y)%20\log%20\frac{p(x,y)}{p(x)p(y)}%20dx\hspace{1pt}%20dy%20\ge%200)

Furthermore, unlike correlation, the mutual information is equal to zero if and only if <img src="https://latex.codecogs.com/svg.latex?math=X"> and <img src="https://latex.codecogs.com/svg.latex?math=Y"> are independent.

In terms of entropy, the mutual information can be written,

![](https://latex.codecogs.com/svg.latex?I(X;Y)%20=%20H(X)%20+%20H(Y)%20-%20H(X,Y))

With a reasonable number of samples, we can estimate the bivariate entropy.
