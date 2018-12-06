# K-Nearest-Neighbors (KNN)

**Reference:** https://kevinzakka.github.io/2016/07/13/k-nearest-neighbor/

# Introduction

KNN is a robust and versatile classifier that is often used as a benchmark for more complex classifiers such as ANN and SVM.
Despite its simplicity, KNN can outperform more powerful classifiers and is used in a variety of applicatiosn such as **economic forecasting**,
**data compression** and **genetics**. For example, KNN was leveraged in 2006 as a study of functional genomics for the assignment of genes based
on their expression profiles.

## What is KNN?

**x** denotes a feature and **y** denotes the target we are trying to predict.

KNN is a **supervised learning** algorithm. We are given a labelled dataset contains (**x**, **y**) and would like to capture the relationship
between **x** and **y**. Our goal is to learn a function **h**: **X** -> **Y** so that given another **x**, **h(x)** can confidently
predict the corresponding output **y**.

KNN is a **non-parametric** and **instance-based** learning algorithm


* **Non-parametric:**
```
It makes no explicit assumptions about the functional form of **h**, avoiding the dangers of mismodeling the
underlying distribution of the data.
For example, suppose our data is highly non-Gaussian but the learning model we choose assumes a Gaussian form. 
In that case, our algorithmwould make extremely poor predictions.
```

* **Instance-based**

```
Our algorithm doesn't explictly learn a model. Instead, it chooses to memorize the training instances which are 
subsequently used as ''Knowledge'' for the prediction phase. Concretely, this means that only when a query ot 
our database is made (i.e. when we ask it to predict a label given an input), will the algorithm use the traing
instances to spit out and answer.
```

## Minimal training but expensive testing.

It is worth noticing that the minimal training phase of KNN comes both at a **memory cost**, since we must store a potential
huge dataset, as well as a **computational cost** during test time since classifying a given observation (**x**) requires a 
run down of the whole dataset. Practically speaking, this is undesirable since we usually want fast responses.


# How does KNN work?

A popular choice is the **Euclidean distance**:

<a href="https://www.codecogs.com/eqnedit.php?latex=d(x,&space;x{}')=\sqrt{(x_{1}&space;-&space;x_{1}{}')&space;&plus;&space;
(x_{2}&space;-&space;x_{2}{}')&space;&plus;&space;...&space;&plus;&space;(x_{n}&space;-&space;x_{n}{}')}" target="_blank">
<img src="https://latex.codecogs.com/gif.latex?d(x,&space;x{}')=\sqrt{(x_{1}&space;-&space;x_{1}{}')&space;&plus;&space;(x_{2}&space;-&space;x_{2}{}')&space;&plus;&space;...&space;&plus;&space;(x_{n}&space;-&space;x_{n}{}')}" title="d(x, x{}')=\sqrt{(x_{1} - x_{1}{}')+ (x_{2} - x_{2}{}') + ... + (x_{n} - x_{n}{}')}" /></a>

However, there are also other measures can be more suitable for a given setting and include the **Manhattan**, **Chebyshev** and 
**Hamming** distance.

Concretely, given a positive integer K, and unseen observation **x** and a similarity metric **d**, KNN performs the following steps:

* It runs through the whole dataset computing **d** between **x** and each training observation. We'll call the K points in the
training data that are closest to **x** the set **A**. Note k is usually odd to prevent tie situations

* It then estimates the conditional probability for each class, that is, the fraction of points in **A** will that given class label.
(Note **I(x)** is the indicator function which evaluates to **1** when the argument **x** is true and **0** otherwise.

<a href="https://www.codecogs.com/eqnedit.php?latex=P(y=j|X=x)=\frac{1}{K}\sum_{i&space;\in&space;A}I(y^{(i)}=j)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(y=j|X=x)=\frac{1}{K}\sum_{i&space;\in&space;A}I(y^{(i)}=j)" title="P(y=j|X=x)=\frac{1}{K}\sum_{i \in A}I(y^{(i)}=j)" /></a>

Finally, our input **x** gets assigned to the class with the  largest probability.

# K 

In KNN, K is a hyperparameter that you must pick in order to get the best possible fit for the dataset.
You can think of K as controlling the shape of the decision boundary we talked about earlier.

When K is small: Low bias but high variance.

![image](https://github.com/AnEscapist/MachineLearning-DeepLearning/blob/master/Chapter%203%20-%20Classification/KNN/img/k%3D1.PNG)

On the other hand, a higher K averages more voters in each prediction and hence is more resilient to outliers. K=20:

![image](https://github.com/AnEscapist/MachineLearning-DeepLearning/blob/master/Chapter%203%20-%20Classification/KNN/img/k%3D20.PNG)

# KNN with Python

The dataset we'll be using is the **Iris Flower Datast**.

![image](https://github.com/AnEscapist/MachineLearning-DeepLearning/blob/master/Chapter%203%20-%20Classification/KNN/img/iris%20flower.PNG)














