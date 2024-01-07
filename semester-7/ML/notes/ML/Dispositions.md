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

## Q1: Week 2 - Vectors
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
- In terms of the exercise
    - In the exercise we represent a pose as a list of vectors or points.
    - We then calculate the Euclidean distance (L2 Norm) of each pose compared to the other poses to find their similarity.
    - We can use those distances to find the most similar poses and most different poses.

## Q2: Week 3 - Matrices
### General
- A **matrix** is a 2D array of scalars arranged in rows and columns

### Focus on operations
- Matrix operations include
    - Addition
        - Is done element wise and results in a new matrix of the same size
    - Subtraction
        - Is done element wise and results in a new matrix of the same size
    - Scalar multiplication
        - Is done element wise and results in a new matrix of the same size.
        - Just multiply each element by the scalar
    - Transpose
        - Is done by flipping the matrix over its diagonal
        - AKA turning the rows into columns and the columns into rows
        - $A^T_{ij} = A_{ji}$
        - Example: $\begin{bmatrix}1 & 2 & 3 \\ 4 & 5 & 6\end{bmatrix}^T = \begin{bmatrix}1 & 4 \\ 2 & 5 \\ 3 & 6\end{bmatrix}$
    - Determinant
        - The determinant of a matrix is a scalar value that can be computed from the elements of a square matrix.
        - The linear set of equations given in the matrix has a unique solution if and only if the determinant is not zero.
        - It is the volume of a matrix, if the determinant is zero then the matrix is flat and has no volume.
        - Denoted $det(\mathbf{A})$ or $|\mathbf{A}|$
    - Multiplication
        - Multiplication is only possible if the columns of the left matrix is the same as the number of rows. AKA if $\mathbf{A}$ is $m$-by-$n$ and $\mathbf{B}$ is $n$-by-$p$.
            - Then the resulting matrix is the $m$-by-$p$ matrix $\mathbf{C}$.
            - Each entry is given by the dot product of the corresponding row of $\mathbf{A}$ and the corresponding column of $\mathbf{B}$
            - $C_{i,j} = \sum_{k=1}^n A_{i,k}B_{k,j}$
            - Example: ${\begin{aligned}{\begin{bmatrix}{\underline {2}}&{\underline {3}}&{\underline {4}}\\1&0&0\\\end{bmatrix}}{\begin{bmatrix}0&{\underline {1000}}\\1&{\underline {100}}\\0&{\underline {10}}\\\end{bmatrix}}&={\begin{bmatrix}3&{\underline {2340}}\\0&1000\\\end{bmatrix}}.\end{aligned}}$ 
    - Inversion
        - A $n$-by-$n$ matrix $\mathbf{A}$ is invertible if there exists an $n$-by-$n$ matrix $\mathbf{B}$ such that $\mathbf{AB} = \mathbf{BA} = \mathbf{I}$ where $\mathbf{I}$ is the identity matrix. $\mathbf{B}$ in this case would be the inverted $\mathbf{A}$ matrix. So rewritten it is $\mathbf{A}\mathbf{A}^{-1}=I$
        - Denoted $\mathbf{A}^{-1}$
        - A matrix is invertible if and only if its determinant is not zero
        - Its crucial in machine learning because of the formula $\mathbf{A}\cdot \overrightarrow{w} = \mathbf{b}$ where $\mathbf{A}$ is the input data, $\overrightarrow{w}$ is the weights and $\mathbf{b}$ is the output data. We can then find the weights by multiplying both sides by $\mathbf{A}^{-1}$ and get $\overrightarrow{w} = \mathbf{A}^{-1}\mathbf{b}$
    - Orthogonal
        - A matrix is orthogonal if its columns are orthogonal unit vectors. AKA each of the column vectors are right angles on each other
        - If a matrix is orthogonal then its inverse is equal to its transpose
            - $\mathbf{A}^{-1} = \mathbf{A}^T$
        - Its determinant is either 1 or -1
- In Machine learning we use a series of these operations to transform and manipulate data
    - For transformations we use
        - Scaling
            - Scaling is done by multiplying each element by a scalar
        - Translation
            - Translation is done by adding a vector to each element
        - Rotation
            - Rotation is done by multiplying the matrix by a rotation matrix
            - A rotation matrix is a matrix that rotates a vector by a given angle
            - Example: $\begin{bmatrix}\cos{\theta} & -\sin{\theta} \\ \sin{\theta} & \cos{\theta}\end{bmatrix}$
        - For many transformations we can use the formula $\mathbf{A}\cdot \overrightarrow{v} = \overrightarrow{b}$ where $\mathbf{A}$ is the transformation matrix, $\overrightarrow{v}$ is the vector to be transformed and $\overrightarrow{b}$ is the transformed vector.
    - A basis is a set of vectors that generates all elements of the vector space and the vectors in the set are linearly independent.
        - We regularly use these to transform between different coordinate systems

### Focus on linear equations
- In machine learning we regularly represent linear equations as matrices like so:
    - Consider the linear equations $5x_1 + 2x_2 = 900$ and $3x_1 + 4x_2 = 960$ then we can represent these as matrices and vectors:
    - $\begin{bmatrix}5 & 2 \\ 3 & 4\end{bmatrix}\begin{bmatrix}x_1 \\ x_2\end{bmatrix} = \begin{bmatrix}900 \\ 960\end{bmatrix}$
    - If we were to graph these equations we would see that they intersect at a point, this point is the solution to the equations.
    - The solution to the equations can be optained by optaining the vector $\overrightarrow{x}$ by multiplying both sides by the inverse of the matrix $\mathbf{A}$. 
        - AKA: $\overrightarrow{x} = \mathbf{A}^{-1}\mathbf{b}$
    - We can generalise this to
        - $ax_1 + bx_2 = c$
        - $dx_1 + ex_2 = f$
        - $\begin{bmatrix}a & b \\ d & e\end{bmatrix}\begin{bmatrix}x_1 \\ x_2\end{bmatrix} = \begin{bmatrix}c \\ f\end{bmatrix}$


## Q3: Week 4 - Linear transformations
### General
- Transformations
    - A **transformation** is a function that map elements from a set A to a set B
        - Also written as $y = f(x)$ where $x \in A$ and $y \in B$
        - $A$ is the domain and $B$ is the codomain
        - If $T(x)=y$ then $x$ is the preimage of $y$ and $y$ is the image of $x$ under $T$
- A **linear transformation** is a function that maps a vector space to another vector space and preserves the vector space operations of addition and scalar multiplication.
- A linear transformation always maps the origin of $\mathbf{V}$ to the origin of $\mathbf{W}$
- Rules:
    - $T(\overrightarrow{u} + \overrightarrow{v}) = T(\overrightarrow{u}) + T(\overrightarrow{v})$
    - $T(c\overrightarrow{u}) = cT(\overrightarrow{u})$
- For it to be linear it must satisfy both of these rules and which also ensure that straight lines stay straight.

### Focus on 2D and 3D, relate to higher dimensions
- In 2D we can represent a linear transformation as a matrix
    - $\begin{bmatrix}a & b \\ c & d\end{bmatrix}$
    - Where $a$ and $d$ are the scaling of the x and y axis respectively
    - $b$ and $c$ are the shearing of the x and y axis respectively
- In 2D there are the transformations:
    - Stretching is not really done with matrices as it's just multiplying the vector by a scalar
    - Scaling
        - Scaling is done by multiplying each element by a scalar
        - $\begin{bmatrix}a & 0 \\ 0 & d\end{bmatrix}$
    - Translation
        - Translation is done by adding a vector to each element
        - $\begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix} + \begin{bmatrix}x \\ y\end{bmatrix}$
    - Rotation
        - Rotation is done by multiplying the matrix by a rotation matrix
        - A rotation matrix is a matrix that rotates a vector by a given angle
        - $\begin{bmatrix}\cos{\theta} & -\sin{\theta} \\ \sin{\theta} & \cos{\theta}\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}x\cos \theta -y\sin \theta \\x\sin \theta +y\cos \theta \end{bmatrix}$
    - Shearing
        - Shearing is done by multiplying the matrix with the shear matrix:
        - For shearing parallel to the x-axis: $\begin{bmatrix}1 & b \\ 0 & 1\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}$
        - For shearing parallel to the y-axis: $\begin{bmatrix}1 & 0 \\ b & 1\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}$
    - Reflection
        - Reflection mirrors the vector over a line $l$
        - The tranformation vector looks like:
        - $\mathbf {A} ={\frac {1}{\lVert \mathbf {l} \rVert ^{2}}}{\begin{bmatrix}l_{x}^{2}-l_{y}^{2}&2l_{x}l_{y}\\2l_{x}l_{y}&l_{y}^{2}-l_{x}^{2}\end{bmatrix}}$
- In 3D we can do the same transformations with larger matrices
- The transformation has to be $k$-by-$k$ where $k$ is the dimension. So in 2D it has to be 2-by-2 and in 3D it has to be 3-by-3
    - Thats because each column describes where the basis vectors ($\begin{bmatrix}1\\0\end{bmatrix}$ and $\begin{bmatrix}0\\1\end{bmatrix}$) ends up
- For higher dimensions it all works the same, there are just $k$ basis vectors instead of 2 or 3, each basis vector has a 1 placed in some position.
- Non-linear transformations are transformations that are not linear, they can be anything else. Fx. a circle or a sine wave. They can bend the existing lines and completely ignore the origin.
- Fx. tranformations between color spaces or temperature scales are non-linear.

### Focus on affine transformations, homogenous coordinates and composition of functions
- An **affine transformation** is a linear transformation where the origin does not have to be preserved. We can represent them as a transformation and a translation.
    - Formally, take the invertible transformation matrix $\mathbf{A}$ and the translation vector $\overrightarrow{b}$ then the affine transformation is $y = \mathbf{Ax} + \overrightarrow{b}$
    - In matrix form it looks like $\begin{bmatrix}a_1 & a_2 \\ a_3 & a_4\end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix} + \begin{bmatrix}b_1\\b_2\end{bmatrix}$
- Homogenous coordinates are cartesian coordinates that are scaled by a factor $Z$. This is done by adding an extra dimension to the vector and setting it to $Z$.
    - We can then represent the vector as $\begin{bmatrix}x\\y\\Z\end{bmatrix}$
    - This allows for $(xZ, yZ, Z)$ to be represented as $(x, y, Z)$
    - For a coordinate $(x, y)$ we can represent it as $(x, y, 1)$
    - To convert back to cartesian coordinates we can divide each element by $Z$
        - $(x, y, Z) \rightarrow (\frac{x}{Z}, \frac{y}{Z})$
- Homogenous coordinates are great for affine transformations because they allow us to represent translations as a matrix multiplication.
    - $y=\left[{\begin{array}{ccc|c}&A&&\overrightarrow{b} \\0&\cdots &0&1\end{array}}\right]{\begin{bmatrix}\mathbf {x} \\1\end{bmatrix}}$
    - $y = \begin{bmatrix}a_1 & a_2 & b_1 \\ a_3 & a_4 & b_2 \\ 0 & 0 & 1\end{bmatrix}\begin{bmatrix}x_1\\x_2\\1\end{bmatrix}$
- Composition of linear transformations are relatively simple as the assosiativity of matrix multiplication allows us to just multiply the matrices together.
    - Take the matrices $\mathbf{A}$, $\mathbf{B}$ and $\mathbf{C}$ then the composition of the linear transformations is $C(B(Ax))$
    - But we can simplify to $Dx$ where $D=CBA$

## Q4: Week 5 - Least squares
### General
- Least squares is a method for finding the best fit of a set of data points.
- This involves finding the line of best fit for a set of data points, this is done by minimizing the sum of the squares of the differences between the observed values and the predicted values.
- Least squares are great when having a lot of data points and you want to find a line of best fit, there are usually more points than the output and model parameters
- Mathematically we setup a system of linear equations and solve it using linear algebra
    - We can represent the system of linear equations as $\mathbf{A}\overrightarrow{x} = \overrightarrow{b}$
    - But in this case $\overrightarrow{b}$ will likely be outside of the column space of $\mathbf{A}$ so we can't solve it directly
        - Column space is the set of all possible linear combinations of the columns of $\mathbf{A}$
    - Instead we should find values for $\overrightarrow{x}$ that minimizes the difference between $\overrightarrow{b*}$ and $\overrightarrow{b}$. Where $\overrightarrow{b*}$ is any result of $A\overrightarrow{x}$.
        - This would minimize the loss
    - The best candidate is $\overrightarrow{b_{\text{proj}}}$ which is the projection of $\overrightarrow{b}$ onto the column space of $\mathbf{A}$
    - Therefore:
$$
\begin{aligned}
\mathbf{A}\overrightarrow{x} &= \overrightarrow{b_{\text{proj}}} \\
\mathbf{A}\overrightarrow{x}-\overrightarrow{b} &= \overrightarrow{b_{\text{proj}}}-\overrightarrow{b}
\end{aligned}
$$
    
- Since $\overrightarrow{b_{\text{proj}}}-\overrightarrow{b}$ is orthogonal to the column space of $\mathbf{A}$ we can solve for it

$$
\begin{aligned}
  A\overrightarrow{x} - \overrightarrow{b} &\in N(A^\top) \\
        A^\top(A\overrightarrow{x} - \overrightarrow{b}) &= 0 \\
        A^\top A\overrightarrow{x} - A^\top\overrightarrow{b} &= 0 \\
        A^\top A\overrightarrow{x} &= A^\top\overrightarrow{b} \\
        (A^\top A)^{-1} A^\top A\overrightarrow{x} &= (A^\top A)^{-1} A^\top\overrightarrow{b} \\
        \overrightarrow{x} &= (A^\top A)^{-1} A^\top\overrightarrow{b} 
\end{aligned}
$$

### Focus on the relation between least squares and projections
- A **projection** on a vector space $V$ is a linear transformation $P:V \rightarrow V$ such that $P^2 = P$
- A square matrix $P$ is a projection matrix if and only if $P^2 = P$
- A square matrix $P$ is a orthogonal projection matrix if and only if $P^2 = P = P^\top$
- Orthogonal projection matrices are the ones we use in least squares
- Least squares utilizes projections to find the best fit for a set of data points.
- The projection of $\overrightarrow{b}$ onto the column space of $\mathbf{A}$ is the best fit for $\overrightarrow{b}$ in the column space of $\mathbf{A}$.

### Focus solving linear least squares problems for model fitting (including design matrix)
- We can use the formula $\overrightarrow{x} = (A^\top A)^{-1} A^\top\overrightarrow{b}$ to solve for the weights in a linear regression problem.
- This can be done for any polynomial, where there are $n$ data points and $m$ parameters. $m$ will be $d+1$ where $d$ is the degree of the polynomial, so a 2nd degree polynomial has 3 parameters as the formula:
    - $y = ax^2 + bx + c$
- This can be generalised to
    - $p_n(x) = w_0 + w_1x + w_2x^2 + \cdots + w_nx^n$
    - or $p_n(x) = \sum_{i=0}^n w_ix^i$
    - or as inner product $p_n(x) = \begin{bmatrix}w_0 & w_1 & w_2 & \cdots & w_n\end{bmatrix}\begin{bmatrix}1 \\ x \\ x^2 \\ \vdots \\ x^n\end{bmatrix}$
    - aka $p_n(x) = \overrightarrow{w}^\top\overrightarrow{x}$
- If we were to calculate this:
$$
\begin{bmatrix}
    1 & x_1^2 & x_1^3 \cdots x_1^n\\
    1 & x_2^2 & x_2^3 \cdots x_2^n\\
    \vdots  & \vdots & \vdots \cdots \vdots\\
    1 & x_m^2 & x_m^3 \cdots x_m^n
\end{bmatrix}
\begin{bmatrix}w_0 \\ w_1 \\ w_2 \\ \vdots \\ w_n\end{bmatrix}
= \begin{bmatrix}y_1 \\ y_2 \\ y_3 \\ \vdots \\ y_m\end{bmatrix}
$$
- Where $m$ is the number of data points and $n$ is the degree of the polynomial
- We can then solve for $\overrightarrow{w}$ using the formula $\overrightarrow{w} = (A^\top A)^{-1} A^\top\overrightarrow{b}$

### Focus on mandatory 1
- Mandatory 1 is about finding the best function to map a set of points from one space to another. Specifically from a pupil position to a screen coordinate.
- We map both a linear and a quadratic function to the points and then calculate the error of each function.

## Q5: Week 6 - Data, Data cleaning, Uncertainty
### General
- The exercise attempts to handle missing data using
    - Mean Imputation
    - Interpolating
- It also uses different methods of evaluation
- **Noise** is unwanted data that is not part of the underlying pattern
    - Types
        - Can be instrument errors
        - Can be enviromental effects, such as the constant radiation from the sun
        - Observational errors
    - Can be random or systematic
        - Random noise is unpredictable and can be reduced by averaging
        - Systematic noise is predictable and can be reduced by calibration
    - Reasons
        - Limits in measurement accuracy
        - Interference from other sources
    - Handled by
        - Excluding noisy attributes
        - Filtering
        - Include a model of the noise
    - In images
        - Salt-and-pepper noise: Randomly distributed white and black pixels
        - Gaussian noise: Randomly distributed pixels with a Gaussian distribution
        - Impulse noise: Random white pixels
- **Outliers**
    - An outlier is a data point that is significantly different from the rest of the data
        - Reasons
            - Measurement errors
            - Data corruption
            - True outliers
        - Handled by
            - Excluding outliers
            - Include a model of the outliers
- **Missing data** is data that is missing from the dataset
    - Reasons
        - Data was not collected
        - Data was lost
        - Data was not available
    - Handled by
        - Imputing the data
- **Duplicate data** is data that is duplicated in the dataset
    - Reasons
        - Data was collected multiple times
        - Data was copied
    - Handled by
        - Excluding the data
        - Imputing the data

### Uncertainty / descriptive statistics. Relate this to model learning and data evaluation.
- Both the data and the model have uncertainty
    - The data uncertainty is the noise and outliers
    - The model uncertainty is the error of the model
    - Data uncertainty can affect the model uncertainty
- **Descriptive statistics** is a set of methods for summarizing and describing data
    - **Mean** is the average of the data points
        - $\overline{x} = \frac{1}{n}\sum_{i=1}^n x_i$
    - **Median** is the middle value of the data points
    - **Variance** is the average of the squared differences from the mean
        - $\sigma^2 = \frac{1}{n}\sum_{i=1}^n (x_i - \overline{x})^2$
    - **Mid-range** is the average of the minimum and maximum values
    - **Mode** is the most common value
    - **Sample mean** is the mean of a sample of the data
        - $\overline{x_i} = \frac{\sum_{i=1}^n x_i^t}{n}$
    - **Covariance** is the measure of how much 2 random variables change together
        - $\sigma_{x,y} = \frac{\sum_i^n(x_i - \overline{x}) * (y_i - \overline{y})}{n}$
    - **Correlation** is the measure of how much 2 random variables change together, but it is normalized
        - $\rho_{x,y} = \frac{\sigma_{xy}}{var(x)var(y)}$

### Data, uncertainty and over/underfitting.
- See above
- Over and under fitting
    - Overfitting is when the model fits the training data too well and therefore does not generalize well
    - Underfitting is when the model does not fit the training data well enough and therefore does not generalize well

### Focus on uncertainty, data cleaning in relation to regression, classification, clustering or dimensionality reduction.
- Data cleaning is important in all of these
    - Can consist of transforming the data, resizing / normalizing images, removing noise, reming unwanted observations or outliers and handling missing data 
    - Normalization
        - Normalization is the process of scaling individual samples to have unit norm
        - $x_{i}' = \frac{x_i-x_{min}}{x_{max}-x_{min}}$
    - Standardization
        - Standardization is the process of scaling individual samples to have mean 0 and variance 1
        - $x_{i}' = \frac{x_i-\overline{x}}{\sigma}$
    - These 2 reduce bias and improve consistency
- Regression
    - Uncertainty can be used to evaluate the confidence and variability of the prediction
    - Data cleaning is extremely critical as the model as bad data can significantly affect the fit of the resulting model.... See exercise
- Classification
    - Uncertainty estimation determines the confindence of the assignment of a particular class of labels
    - Misclassification can be seen as a form of uncertainty that has to be handled in the data cleaning
- Clustering
    - Uncertainty can be used to determine the reliability of the assignment of clusters. Sometimes the algorithm can output the uncertainty of the assignment of a point to a cluster
    - Data cleaning ensures that outliers or noisy instances do not affect the clustering, as they could form their own clusters or affect the boundaries of others
- Dimensionality reduction
    - There can be uncertainty when evaluation lower dimensional representations of the data. Understanding uncertainty can help understand closeness and distance of points in the reduced space.
    - Data cleanin is crucial to remove irrelevant or redundant features as it can affect the effectiveness of the lower dimensions

### Missing data, duplicate data, outlier detection, and data imputation
- Missing data can be handled by
    - Using the K nearest neighbours to impute the data, such as the mean and median
    - Interpolating between points
    - Using recommendation systems or other models that can predict the missing data
- Outlier removal can be done using the z-score
    - $z = \frac{x-\overline{x}}{\sigma}$
    - If $z$ is greater than 3 or less than -3 then the data point is an outlier

## Q6: Week 7 - Regularization, Filtering
### General

### Focus on filtering (convolution and correlation, noise, image gradients) 
- Filtering can be used to reduce noise.
- One such method is doing convolution which is just inner products of a kernel calculated in a sliding window.
    - The kernel is flipped on the x and y axis, or just flipped if the kernel is 1 dimensional
- We call the kernel $\mathbf{h} = [h_1, h_2, h_3, \cdots, h_M]$ of length $M$
    - The product of each value is calculated as $y_n = \sum_{k=0}^M h_kx_{n-k}$
- For noise reduction we can fx use the average filter which is just a kernel of length $M$ where each value is $\frac{1}{M}$, that would make each value the average of the neighbours.
- Correlation is the same as convolution but without flipping the kernel.
- An **Image gradient** is a change in intensity or color.
    - We can use the gradient to detect sharp changes in intensity or color, which can be used to detect edges.
- In the exercise for this week we use filters to blur and sharpen images.
- We also use correlation to make a kernel that is a template and then try and then for each pixel calculate how the template, over that image, correlates.

### Focus on matching and metrics.
- Matching is the process of finding the best match of a template in a dateset.
- Fx in image data we can take a template image and compute for each pixel in a different image the one that correlates the most with that template, thereby creating a detection algorithm for that image.
- When we match we can use a few different metrics to determine how well the template matches the image.
    - Correlation
        - $H(m,n)=\sum_k\sum_l g(k,l)f(m+k,n+l)$
    - True detections
        $H(m,n)=\sum_k\sum_l(g(k,l)-\overline{g})f(m+k,n+l)$
    - SSD (Sum of Squared Differences)
        - $H(m,n)=\sum_k\sum_l(g(k,l)-f(m+k,n+l))^2$
    - Normalized cross correlation
        - Works by subtracting the mean
        - And then dividing by the standard deviation
        - $H(m,n)=\frac{\sum_k\sum_l(g(k,l)-\overline{g})(f(m+k,n+l)-\overline{f})}{\sqrt{\sum_k\sum_l(g(k,l)-\overline{g})^2\sum_k\sum_l(f(k,l)-\overline{f})^2}}$

### Focus on Cross validation
- Also known as $k$-fold cross validation
- Cross validation is a method of evaluating a model by training it on a subset of the data and then testing it on the rest of the data.
- Helps to see how well the model generalizes. Aka how well it works on unseen data
- The data is split into $k$ parts (folds) which are used for $k$ experiments. For each experiment a new set of data is used as validation data, such as the $i$th dataset, and the remaining $k-1$ datasets are used to train on. We then evaluate the model on how well it predicts the validation data.
- The average of all the iterations is the final score of the model.
- While this method is designed to prevent over/under fitting the issue comes when deciding $k$
    - If $k$ is too small then the model will have few, but large datasets. This can lead to underfitting as the model has had less data to train with, but can lead to more consistent performance.
    - If $k$ is too large then the model has had more data to train with, but less data to validate on. Which can lead to overfitting and therefore also not generalise well.
    - It can help to also look at the variance over each experiment as the variance over the experiments can detect whether the model is sensitive to certain subsets of data. This variance would usually be hidden by the average if $k$ is large.
- RMSE (Root Mean Squared Error) is a metric that can be used to evaluate the model
    - $RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^n (y_i - \hat{y_i})^2}$
    - Where $y_i$ is the actual value and $\hat{y_i}$ is the predicted value
    - If RMSE is high for small and large values of $k$ then the model is probably bad as it's underfitting
    - If RMSE is low for small values of $k$, but high for large values of $k$ then the model is probably overfitting
    - If the model has a low RMSE for both small and large values of $k$ then the model is probably good

### Focus on Regularization
- Regularization is a method of reducing overfitting, thereby improving the generalization of the model.
- It does this by adding a penalty to the loss function, which is the function that the model tries to minimize.
    - Take the loss function $J(\mathbf{w})$, Mean-squared error $E_D(\mathbf{w})$ and a penalty term $\lambda E_w(\mathbf{w})$ to it, then the new loss function is $J(\mathbf{w})=E_D(\mathbf{w})+\lambda E_w(\mathbf{w})$
    - $\lambda$ is the regularization parameter
    - $E_w(\mathbf{w})$ is the regularization term. In this case the L2 norm of the weights
    - We can change $\lambda$ to change the amount of regularization
    - This is also known as weight decay
    - Adding this penalty term to the loss function makes the model prefer smaller weights, thereby reducing overfitting
    - This is all called L2 regularization or Ridge regression
    - We can insert more bias via the regularization parameter ($\lambda$) to reduce the variance of the model

### Focus on Bias /Variance, $\mathbf{R^2}$
- Bias is errors from the model due to incorrect assumptions in the model.
    - High bias can lead to underfitting as it misses the relevant relations between features and target outputs.
- Variance is errors from the model due to sensitivity to small fluctuations in the training set.
    - High variance can lead to overfitting as it learns the noise in the training data.
- We want to find a balance between bias and variance. Usually minimizing the 2 as much as possible, but there usually is a tradeoff.
    - When creating models we can usually decrease the bias by adding more model parameters thereby becoming more flexible, but this decrease in bias increases the variance.
- When we do ridge regression we introduce bias into the model to reduce the variance.
- $\mathbf{R^2}$ is a metric that can be used to evaluate the model
    - $\mathbf{R^2}$ is the proportion of the variance in the dependent variable that is predictable from the independent variable(s)
    - The "dependent variable" is the predicted data
    - The "independent variable" is the input data
    - Essentially it's a measure of how well the model fits the data
        - Or just how close the data is to the fitted regression line
    - $\mathbf{R^2}$ is, usually, between 0 and 1
    - $\mathbf{R^2}$ is 0 when the model is as good as the mean of the data
    - $\mathbf{R^2}$ is 1 when the model is perfect
    - $\mathbf{R^2}$ is negative when the model is worse than the mean of the data
    - $\mathbf{R^2}$ is calculated as $1-\frac{SS_{res}}{SS_{tot}}$
        - $SS_{res}$ is the sum of squares of the residual (the difference between the predicted value and the actual value)
            - $SS_{res}=\sum_i(y_i-\hat{y_i})^2$
                - $\hat{y_i}$ is the predicted value
        - $SS_{tot}$ is the total sum of squares (the difference between the actual value and the mean of the data)
            - $SS_{tot}=\sum_i(y_i-\overline{y})^2$
                - $\overline{y}$ is the mean of the data
        - $y_i$ is the actual value

## Q7: Week 8 - Classification
...

## Q8: Week 9 - Evaluation
...

## Q9: Week 10 - Principal component analysis
...

## Q10: Week 11 - Clustering and non-linear optimization
...

## Q11: Week 12 - Neural networks
...

## Q12: Week 13 / 14 - Architectures
...

