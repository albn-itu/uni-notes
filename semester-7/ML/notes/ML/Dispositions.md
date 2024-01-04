---
tags:
  - meta
  - exam
---

# Dispositions
For each prepare a 5-6 minute presentation which covers
- Which exercise it is
- Important elements of the exercise
- The parts of the question
- Illustrate using the exercise

## Week 2 - Vectors
- A **vector** is a set of scalars to the $\hat{i}$, $\hat{j}$, $\hat{k}$ basis vectors.
  - These basis vectors have a length of 1 and are orthogonal to each other.
  - The basis vectors can be used to describe any vector in 3D space.
  - The scalar values can also be seen as a point where the vector "points to".
- If one where to scale a vector it would keep the same angle but change length.
- In Linear Combination we can also represent a vector as D other vectors multiplied by scalars and added together, for 2D
  - $v = a_1\overrightarrow(v) + a_2\overrightarrow{w}$
  - This will also create every possible vector
    - This requires the vectors to be linearly independent and for the vectors to not be the zero vector
  - This is a linear combination of the vectors $\overrightarrow{v}$ and $\overrightarrow{w}$
- The **span** of $\overrightarrow{v}$ and $\overrightarrow{w}$ is the set of all linear combinations of $\overrightarrow{v}$ and $\overrightarrow{w}$
- Vectors operations are
  - Addition
    - Is done element wise and results in a new vector
  - Subtraction
    - Is done element wise and results in a new vector
  - Scalar multiplication
    - Is done element wise and results in a new vector
  - Dot product / Inner product
    - Takes 2 vectors and returns a scalar
    - Is the sum of the products of the corresponding elements
    - $\overrightarrow{v} \cdot \overrightarrow{w} = \sum_{i=1}^n v_iw_i$
  - Cross product
    - Takes 2 vectors and returns another vector that is perpendicular to the 2 vectors
    - $\overrightarrow{v} \times \overrightarrow{w} = ||\overrightarrow{v}||||\overrightarrow{w}||\sin{(\theta)} n$
    - Where $\theta$ is the angle between the 2 vectors
    - $n$ is the unit vector perpendicular to the 2 vectors
- Distances
  - The length of a vector can be found using the Euclidean distance, this is also known as the L2 norm
    - *A norm* is a function that assigns a strictly positive length or size to each vector in a vector space
    - $||\overrightarrow{v}|| = \sqrt{\sum_{i=1}^n v_i^2}$
  - Distance between 2 vectors
    - The distance between 2 vectors describe how similar they are
    - $d(\overrightarrow{v}, \overrightarrow{w}) = ||\overrightarrow{v} - \overrightarrow{w}||$
- Relation to ML
  - Vectors can signify many things in Machine Learning.
  - Commonly used as a representation of data. Fx. by vectorizing input data
    - Vectorizing data is the process of converting data into numbers represented in a vector
  - Vectors can represent
    - Input data (features)(possibly after vectorization)
    - Weights
    - Biases
    - Output data (labels, predicted classes, etc.)

## Week 3 - Matrices
...

## Week 4 - Linear transformations
...

## Week 5 - Least squares
...

## Week 6 - Data, Data cleaning, Uncertainty
...

## Week 7 - Regularization, Filtering
...

## Week 8 - Classification
...

## Week 9 - Evaluation
...

## Week 10 - Principal component analysis
...

## Week 11 - Clustering and non-linear optimization
...

## Week 12 - Neural networks
...

## Week 13 / 14 - Architectures
...

