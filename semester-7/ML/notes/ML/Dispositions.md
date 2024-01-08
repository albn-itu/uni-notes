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
### General
- **Classification** is a method of predicting a discrete class
    - Fx predicting whether a picture is of a cat or a dog

### Linear classification and ”kernels”
- **Linear classification** is a method of classifying data into different classes using a linear function
    - We try to find a linear function that separates the data into different classes
    - Then we can test the data by seeing which side of the function it is on
    - Is probably the simplest and fastest form of classification
- **SVM** (Support Vector Machine)
    - Is a method of linear classification
    - It tries to find a hyperplane that separates the data into different classes
    - A hyperplane is a plane that has one less dimension than the ambient space
- **Kernels** are a method of transforming the data into a higher dimension to make it easier to classify
    - Fx classifying non linear data using linear classification

### Logistic regression
- **Logistic regression** is a method of classification
    - Uses a logistic function to model a binary dependent variable
    - Can have a better fit than linear classification
    - Instead of using a linear function to separate the data into different classes, we use a sigmoid function
    - A strength of logistic regression is that it can give a probability of the data being in a certain class

### Features/HOG Features and classification
- A **Feature** is a measurable property of the data
    - Fx the location and color of a pixel in an image
    - Fx Name,Age,Sex,Height,Weight of a person
    - Sometimes referred to as variables or attributes
- **HOG Features** (Histogram of Oriented Gradients) is a method of extracting features from an image
    - It's a feature descriptor that counts occurrences of gradient orientation in localized portions of an image
    - In other words it counts the number of times an edge with a certain orientation appears in a certain area of the image
    - Process:
        - **Preprocessing and smoothing**
          - This is done to reduce noise and make the image more uniform
        - **Calculating the gradient**
            - We do this by calculating the gradient magnitude and orientation of each pixel in the image
        - **Creating a histogram of gradient orientations**
            - Divide the image into cells and calculate the histogram of the gradient orientations in each cell
        - **Normalizing across blocks**
            - We do this to make the descriptor more robust to changes in lighting
            - We do this by dividing the cells into blocks and normalizing the histogram of each block
        - **Creating the feature vector**
            - We do this by concatenating the normalized histograms of each block
    - HOG Features are used in object detection and tracking
        - Fx. in the exercise we calculate the HOG Features of a Cat and a Human and compare the similarity
        - Can be used with a sliding window to detect objects in an image

## Q8: Week 9 - Evaluation
### Metrics/Evaluation of Classifiers
- **Accuracy** is the number of correct predictions divided by the total number of predictions
    - Accuracy is calculated as $\frac{TP+TN}{TP+TN+FP+FN}$
        - $TP$ is the number of true positives
        - $TN$ is the number of true negatives
        - $FP$ is the number of false positives
        - $FN$ is the number of false negatives
    - Accuracy is not a good metric when the data is imbalanced
        - Fx. if we have 1000 pictures of cats and 10 pictures of dogs, then a model that always predicts cat will have an accuracy of 99%
        - In this case we can use the F1 score instead
- **Precision** is the number of true positives divided by the number of true positives and false positives
    - Precision is calculated as $\frac{TP}{TP+FP}$
    - Precision is a good metric when we want to minimize false positives
        - Fx. if we want to minimize the number of healthy people that are diagnosed with cancer
- **Recall** is the number of true positives divided by the number of true positives and false negatives
    - Recall is calculated as $\frac{TP}{TP+FN}$
    - Recall is a good metric when we want to minimize false negatives
        - Fx. if we want to minimize the number of people with cancer that are diagnosed as healthy
- **F1 score** is the harmonic mean of precision and recall
    - F1 score is calculated as $2*\frac{precision*recall}{precision+recall}$
    - F1 score is a good metric when we want to minimize both false positives and false negatives
- **Specificity** is the number of true negatives divided by the number of true negatives and false positives
        - Fx. if we want to minimize the number of healthy people that are diagnosed with cancer and the number of people with cancer that are diagnosed as healthy
        - Basically the opoosite of recall
- **ROC Curve**
    - ROC (Receiver Operating Characteristic) Curve is a plot of the true positive rate against the false positive rate at each threshold setting
    - The closer the curve is to the top left corner the better the model
    - This curve is nice for visually comparing threshold values
- **AUC** (Area Under the Curve)
    - AUC is the area under the ROC curve
    - The closer the AUC is to 1 the better the model, with 1 signifying a perfect model
    - AUC is a good metric when we want to compare different models
- **Precision-recall curve**
    - Precision-recall curve is a plot of precision against recall at each threshold setting
    - The closer the curve is to the top right corner the better the model
    - This curve is nice for visually comparing threshold values

### Metrics/Evaluation of Regression models
- **Mean Absolute Error** is the average absolute difference between the predicted value and the actual value
    - Mean Absolute Error is calculated as $\frac{1}{n}\sum_i|y_i-\hat{y_i}|$
        - $y_i$ is the actual value
        - $\hat{y_i}$ is the predicted value
        - $n$ is the number of data points
    - Mean Absolute Error is a good metric when we want to penalize small errors
- **Mean Squared Error** is the average squared difference between the predicted value and the actual value
    - Mean Squared Error is calculated as $\frac{1}{n}\sum_i(y_i-\hat{y_i})^2$
        - $y_i$ is the actual value
        - $\hat{y_i}$ is the predicted value
        - $n$ is the number of data points
    - Mean Squared Error is a good metric when we want to penalize large errors
- **Root Mean Squared Error** is the square root of the average squared difference between the predicted value and the actual value
    - Root Mean Squared Error is calculated as $\sqrt{\frac{1}{n}\sum_i(y_i-\hat{y_i})^2}$
        - $y_i$ is the actual value
        - $\hat{y_i}$ is the predicted value
        - $n$ is the number of data points
    - Root Mean Squared Error is a good metric when we want to penalize large errors, Specifically outliers.
        - In some cases MAE or $R^2$ is better
- **Root Mean Squared Logarithmic Error** is the square root of the average squared logarithmic difference between the predicted value and the actual value
    - Root Mean Squared Logarithmic Error is calculated as $\sqrt{\frac{1}{n}\sum_i(\log(y_i+1)-\log(\hat{y_i}+1))^2}$
        - $y_i$ is the actual value
        - $\hat{y_i}$ is the predicted value
        - $n$ is the number of data points
    - Root Mean Squared Logarithmic Error is a good metric when the errors exhibit exponential growth or decay
        - Fx. when the error increases as the predicted value increases
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

### Features/HOG Features and classification.
- A **Feature** is a measurable property of the data
    - Fx the location and color of a pixel in an image
    - Fx Name,Age,Sex,Height,Weight of a person
    - Sometimes referred to as variables or attributes
- **HOG Features** (Histogram of Oriented Gradients) is a method of extracting features from an image
    - It's a feature descriptor that counts occurrences of gradient orientation in localized portions of an image
    - In other words it counts the number of times an edge with a certain orientation appears in a certain area of the image
    - Process:
        - **Preprocessing and smoothing**
          - This is done to reduce noise and make the image more uniform
        - **Calculating the gradient**
            - We do this by calculating the gradient magnitude and orientation of each pixel in the image
        - **Creating a histogram of gradient orientations**
            - Divide the image into cells and calculate the histogram of the gradient orientations in each cell
        - **Normalizing across blocks**
            - We do this to make the descriptor more robust to changes in lighting
            - We do this by dividing the cells into blocks and normalizing the histogram of each block
        - **Creating the feature vector**
            - We do this by concatenating the normalized histograms of each block
    - HOG Features are used in object detection and tracking
        - Fx. in the exercise we calculate the HOG Features of a Cat and a Human and compare the similarity
        - Can be used with a sliding window to detect objects in an image

### Imbalanced data for classification and regression
- Imbalanced data can really mess up the model
- If the data is imbalanced the model will be biased towards the majority class, there are both ways to detect and fix this.
- Detection:
    - **Confusion matrix**
        - A confusion matrix is a table that is used to describe the performance of a classification model
        - It shows the number of correct and incorrect predictions made by the classification model compared to the actual outcomes
    - We can also use a mix of the metrics we have already learned
        - Fx. Accuracy, Precision, Recall, F1 score, Specificity
    - **Matthews correlation coefficient**
        - The Matthews correlation coefficient is used in machine learning as a measure of the quality of binary (two-class) classifications
        - It takes into account true and false positives and negatives and is generally regarded as a balanced measure which can be used even if the classes are of very different sizes
- Fixing:
    - **Oversampling**
        - Oversampling is the process of randomly duplicating observations from the minority class in order to reinforce its signal.
        - Carries an inherent risk of overfitting towards the minority class.
            - Some newer methods use generative models to generate synthetic data points
    - **Undersampling**
        - Undersampling is the process of randomly removing observations from the majority class to prevent its signal from dominating the learning algorithm.
        - Carries an inherent risk of information loss in the majority class

## Q9: Week 10 - Principal component analysis
### General
- **Eigenvalues** and **eigenvectors**
    - An **Eigenvector** is a vector that doesn't change its direction when a linear transformation is applied to it
    - An **Eigenvalue** is the scalar that is used to transform the Eigenvector
    - Thus an eigenvector $\mathbf{v}$ of a linear transformation $T$ is a nonzero vector that, when $T$ is applied to it, does not change direction
        - $T(\mathbf{v})=\lambda\mathbf{v}$
            - $\lambda$ is the eigenvalue

### Dimensionality reduction and PCA. Focus on mandatory 2
- **Dimensionality reduction** is the process of reducing the number of features in a dataset while retaining as much information as possible.
    - This is done to reduce the computational cost of the model
    - The transformation is done by projecting the data into a $k$-dimensional subspace (where $k$ is less than the original number of features)
- Principal Component Analysis (PCA) is a dimensionality reduction technique that identifies the features withing the dataset that maximises the variance.
    - The features with the highest variance are the ones that contain the most information, that is valuable to the model
    - High-variance features often capture significant features
    - Steps for PCA:
        - Center the data
            - Compute the $D$-dimensional mean vector ($D$ is the number of features)
                - $\mathbf{m}=\frac{1}{N}\sum_{i=1}^N\mathbf{x_i}$
                    - $N$ is the number of data points
                    - $\mathbf{x_i}$ is the $i$th data point
            - Subtract the mean from each data point
        - Calculate the covariance matrix ($C$)
            - The covariance matrix is a matrix that summarizes the covariance between several variables
            - The covariance matrix is a square matrix with the same number of rows and columns as the number of variables in the dataset
            - $C=\frac{1}{N}X^TX$
                - $X$ is the centered data
                - $N$ is the number of data points
        - Calculate the eigenvectors $v_i$ and eigenvalues $\lambda_i$ of the covariance matrix
            - Uphold $C=V\Lambda V^T$
                - $V$ is the matrix of eigenvectors
                    - $V=\begin{bmatrix}
                        v_1 & v_2 & \cdots & v_n\end{bmatrix}$
                - $\Lambda$ is the diagonal matrix of eigenvalues
                    - $\Lambda=\begin{bmatrix}
                        \lambda_1 & 0 & \cdots & 0 \\
                        0 & \lambda_2 & \cdots & 0 \\
                        \vdots & \vdots & \ddots & \vdots \\
                        0 & 0 & \cdots & \lambda_n\end{bmatrix}$
        - Sort the eigenvectors by decreasing eigenvalues
            - The eigenvector with the largest eigenvalue corresponds to the direction of maximum variance
        - Select a subspace of size $Dxk$ where $k$ is the number of eigenvectors selected
        - Use the $Dxk$ matrix $\phi$ to transform the data into the new subspace spanned by the eigenvectors
            - $y=\phi^Tx$
                - $x$ is a $Dx1$ vector representing a sample
                - $y$ is the transformed $kx1$ sample
            - $Y=\phi^TX^T$
                - $X$ is the centered data
                - $Y$ is the transformed $kxN$ matrix

### Generative models and PCA
- **Generative models** are a class of models that are used to generate new data points from a given dataset
- PCA can be used to reduce the size of the original dataset, but one has to be careful.
    - If the dataset is reduced too much, the model will not be able to generate new data points that are similar to the original dataset
    - If the dataset is reduced too little, the model will not be able to generate new data points that are different from the original dataset
    - When reducing the dataset we have to ensure that the latent space that we eventually map to is representative and doesn't deviate too much from the original space.
        - AKA we have to know that numbers generated in latent space have meaning in original space.
    - Say we have datapoints $x_i$ that maps to the vectors $a_i$ in latent space. Then we can constrain the variance by the eigenvalues. Since they represent the variance in the direction given by the eigenvectors (which are the ones we are mapping with).
    - So if we were to constrain by some percentage in each direction, we can setup the following:
        - $-s\sqrt{\lambda_i}\leq a_i\leq s\sqrt{\lambda_i}$
            - $s$ is a factor determining the level of allowed deviation
            - $\lambda_i$ is the $i$th eigenvalue
    - This establishes a boundary in latent space where the generated data points can be mapped to, thereby ensuring the original space remains representative.
- In the assignment we do this ensuring a 95% variance in the latent space.

### Eigenvalues, covariance matrix and basis
- **Covariance matrix**
    - The covariance matrix is a matrix that summarizes the covariance between several variables
        - As in how much do the variables change together
    - The covariance matrix is a square matrix with the same number of rows and columns as the number of variables in the dataset
    - $C=\frac{1}{N}X^TX$
        - $X$ is the centered data
        - $N$ is the number of data points
- Eigenvalues of a covariance matrix
    - Calculating the eigenvectors and values of a covariance matrix is a way to find the directions of maximum variance in the dataset. Therefore the largest eigenvalues of the correlation matrix must be the features with the most variance
- A basis is a set of vectors that generates all elements of the vector space and the vectors in the set are linearly independent.
    - We regularly use these to transform between different coordinate systems
    - Basis vectors for 2D: ($\begin{bmatrix}1\\0\end{bmatrix}$ and $\begin{bmatrix}0\\1\end{bmatrix}$)
- For higher dimensions it all works the same, there are just $k$ basis vectors instead of 2 or 3, each basis vector has a 1 placed in some position.

## Q10: Week 11 - Clustering and non-linear optimization
- **K-means** is a clustering algorithm that tries to partition a set of points into $k$ clusters, where each point belongs to the cluster with the nearest mean (also known as cluster centers).
    - The algorithm works as follows:
        - Select $k$ points as the initial centroids
        - Assign each point to the closest centroid
        - Recompute the centroids
        - Repeat steps 2 and 3 until the SSD is minimized
            - This is known as **WCSS** (Within cluster sum of squares)
            - SSD is sum of squared distances between each point and its centroid
                - $\sum_{c_i\in C}\sum_{x_i\in c_i}||x_i-c_i||^2$
                - In this case the metric is the L2 Norm (Euclidean distance), but it can be any metric

### K-means and Mean shift
- **Mean shift** is a clustering algorithm that tries to find so-called modes in the dataset
    - The algorithm works as follows:
        - Create a sliding window for each data point
        - Calculate the mean of the data points in the window (Some radius around the data point, known as the kernel)
        - Shift the data point towards the mean
        - Repeat steps 2 and 3 until the data points converge
        - Each cluster is the set of data points that converge to the same point, these are the returned centroids
        - The number of clusters is determined by the algorithm
    - The hard part about Mean shift is selecting the bandwith (size of sliding window)
        - If the bandwith is too small then there will be too many clusters
            - An extreme case is that each point will be its own cluster
        - If the bandwith is too large then there will be too few clusters
            - An extreme case is that all points will be in the same cluster

|          | **K-means** | **Mean shift** |
| -------- | ----------- | -------------- |
| **Pros** | Simple and fast to compute<br>Converges to local minimum of WCSE | Does not assume cluster shape<br>Only one parameter choice (bandwith)<br>Can find many modes, you don't need to decide the cluster amount<br>Robust to outliers |
| **Cons** | Selecting $k$ is hard, even with the ELBOW method<br>Can be sensitive to the initial centers<br>Sensitive to outliers<br>Clusters are spherical| Selecting the window size is hard<br>Does not scale well with more dimensions<br>Extremely bad runtime, nearest-neighbor runs in $O(n^2)$ |

### K-means and Algomerative clustering
- **Algomerative** or **Agglomerative** clustering is a clustering method which starts with each data point as its own cluster and then merges the closest clusters until there is only one cluster left
    - The algorithm works as follows:
        - Start with each data point as its own cluster
        - Merge the 2 closest clusters
        - Repeat step 2 until there is only one cluster left or until a threshold for number of clusters/distance is reached
    - The hard part about Algomerative clustering is selecting the threshold value
    - Pros
        - Free choice of distance metric
        - Easy to implement
        - Any cluster size
        - Clusters have very adaptive shapes
    - Cons
        - Extreme runtime, nearest-neighbor runs in $O(n^2)$
        - Imbalanced: Outliers will be their own cluster
        - Still have to choose the number of clusters

### K-means and ELBOW
- The **ELBOW** method is a method of finding the optimal number of clusters in a dataset
    - The method works by plotting the number of clusters against the within cluster sum of squares (WCSS)
    - The optimal number of clusters ($k$) is the point where the WCSS starts to flatten out
    - The point where the WCSS starts to flatten out is called the elbow

### Nonlinear functions, graphs, gradients and gradient descent with relation to model training and non-linear models
- **Gradient descent** is a method for finding the minimum of a non-linear function
    - This is extremely useful in machine learning as we can use it to find the minimum of a non-linear loss function
    - Fx take the non-linear loss function $L=\sum_{i=1}^n(F_w(x_i)-y_i)^2$
        - $F_w$ is a non-linear transformation
        - $x_i$ is the $i$th data point
        - $y_i$ is the $i$th label
        - $w$ is the weights of the model
    - In such a situation we must use iterative methods to find the minimum.
    - In gradient descent we consider 4 possible points
        - The global maximum
        - The global minimum
        - The local maximum (There can be many of these)
        - The local minimum (There can be many of these)
    - Our goal is to find the global minimum
    - The algorithm works as follows:
        - Start at a point $x_0$
        - Calculate the next estimate using $x_{n+1}=x_n-\alpha\nabla f(x_n)$
            - $\alpha$ is the learning rate
            - $\nabla f(x_n)$ is the gradient of the function at $x_n$
                - The gradient is the vector of partial derivatives of the function
        - Repeat step 2 until we reach a gradient of 0 or a predefined number of iterations
    - If you have multiple dimensions then you take the derivative of both directions in the point you are currently in, and go in the direction of the steepest slope.
    - This can be optimized using momentum
        - Sometimes we will only find the local minima, when a global minima exists
        - Momentum takes the last steps into account to take larger steps when we are far from the minima and smaller steps when we are close to the minima
            - Compare to a ball
            - A ball will gain speed when rolling down a hill
            - A small bump or plateau in the hill will not stop the ball, but will slow it down
            - This is what momentum does

## Q11: Week 12 - Neural networks
- A **Neural network** is a series of functions.
    - Each **Layer** is a function much like the ones we've been discussing up to this point. 
    - Each layer/function has it's own parameters $w$.
    - The output of one function is passed on to the next until it's eventually outputted
    - Each layer contains an activation function
        - The activation function is a non-linear function that is applied to the output of the layer
        - The activation function is what makes the neural network non-linear
        - The activation function is usually the same for all layers
    - Each layer has the inherent risk of overfitting and underfitting that has been discussed many times, and one must therefore be very careful when training.
        - Each layer can have a regularization function that helps with this
    - Most of the time we don't really care about the parameters of each layer, we just want to find the parameters that minimize the loss function
        - Especially because the parameters are really hard to reverse engineer
    - Bigger networks can represent more an more complex functions
        - But they are also more prone to overfitting

### Neural networks prediction (regression vs classification)
- Regression is the process of predicting a continuous value
    - Fx predicting the price of a house
- Classification is the process of predicting a discre class or label
    - Fx predicting whether a picture is of a cat or a dog
- For both of these there exists normal linear models, but these are limited by the fact that they can only model linear relationships.
    - So in more complex relationships they will not be able to model the data well.
- Neural networks are able to model non-linear relationships, which makes them more powerful than linear models.
- In classification neural networks are really nice because they can find multiple different classes instead of just the 2 of linear classification

### Neural networks training (Gradients, the chain rule and back/forward propagation)
- **Forward propagation** is the process of calculating the output of the neural network
    - This is done by passing the input through each layer of the network
    - The output of one layer is the input of the next layer
    - The output of the last layer is the output of the network
- **Backwards propagation** is the process of calculating the gradients of the loss function with respect to the parameters of the network
    - This is done by using the chain rule to calculate the gradients of each layer, working backwards from the last layer (hence the name)
    - The gradients of each layer is then used to update the parameters of the network
    - Essentially we are just doing gradient descent but for each layer
- **The chain rule** is a method of calculating the derivative of a function that is composed of other functions
    - Take the function $h(x)=f(g(x))$
        - Then the chain rule states that $h'(x)=f'(g(x))g'(x)$
            - This allows us to efficiently calculate the derivative of functions when starting from the bottom as you don't have to recompute the derivatives for each layer
        - In Leibniz notation if the variable $z$ depends on the variable $y$ which depends on $x$ then:
            - $\frac{dz}{dx}=\frac{dz}{dy}\frac{dy}{dx}$
- **Gradient descent** is a method for finding the minimum of a non-linear function
    - This is extremely useful in machine learning as we can use it to find the minimum of a non-linear loss function
    - Fx take the non-linear loss function $L=\sum_{i=1}^n(F_w(x_i)-y_i)^2$
        - $F_w$ is a non-linear transformation
        - $x_i$ is the $i$th data point
        - $y_i$ is the $i$th label
        - $w$ is the weights of the model
    - In such a situation we must use iterative methods to find the minimum.
    - In gradient descent we consider 4 possible points
        - The global maximum
        - The global minimum
        - The local maximum (There can be many of these)
        - The local minimum (There can be many of these)
    - Our goal is to find the global minimum
    - The algorithm works as follows:
        - Start at a point $x_0$
        - Calculate the next estimate using $x_{n+1}=x_n-\alpha\nabla f(x_n)$
            - $\alpha$ is the learning rate
            - $\nabla f(x_n)$ is the gradient of the function at $x_n$
                - The gradient is the vector of partial derivatives of the function
        - Repeat step 2 until we reach a gradient of 0 or a predefined number of iterations
    - If you have multiple dimensions then you take the derivative of both directions in the point you are currently in, and go in the direction of the steepest slope.
    - This can be optimized using momentum
        - Sometimes we will only find the local minima, when a global minima exists
        - Momentum takes the last steps into account to take larger steps when we are far from the minima and smaller steps when we are close to the minima
            - Compare to a ball
            - A ball will gain speed when rolling down a hill
            - A small bump or plateau in the hill will not stop the ball, but will slow it down
            - This is what momentum does

### Training and Evaluation
- **Supervised learning** is a method of training a model using labeled data
    - Fx. training a model to predict whether a picture is of a cat or a dog
- **Unsupervised learning** is a method of training a model using unlabeled data
    - These models are trained to find patterns in the data, patterns we don't know of
    - Fx. training a model to cluster data points into different groups
- We learn by minimizing the loss function using forwards and backwards propagation, see previous
- We evaluate based on metrics
    - Classification has,
        - **Accuracy** is the number of correct predictions divided by the total number of predictions
        - **Precision** is the number of true positives divided by the number of true positives and false positives
        - **Recall** is the number of true positives divided by the number of true positives and false negatives
        - **F1 score** is the harmonic mean of precision and recall
        - **Specificity** is the number of true negatives divided by the number of true negatives and false positives
    - Regression has,
        - **Mean Absolute Error** is the average absolute difference between the predicted value and the actual value
            - Mean Absolute Error is a good metric when we want to penalize small errors
        - **Mean Squared Error** is the average squared difference between the predicted value and the actual value
            - Mean Squared Error is a good metric when we want to penalize large errors
        - **Root Mean Squared Error** is the square root of the average squared difference between the predicted value and the actual value
            - Root Mean Squared Error is a good metric when we want to penalize large errors, Specifically outliers.
        - **Root Mean Squared Logarithmic Error** is the square root of the average squared logarithmic difference between the predicted value and the actual value
            - Root Mean Squared Logarithmic Error is a good metric when the errors exhibit exponential growth or decay
        - $\mathbf{R^2}$ is the proportion of the variance in the dependent variable that is predictable from the independent variable(s)

## Q12: Week 13 / 14 - Architectures
### Model architectures: Difference between fully connected/multi layer perceptron (MLP) and CNN
- A **Perceptron** is a linear classifier. It's a single layer neural network that can only classify linearly separable data
    - It's a binary classifier, meaning it can only classify data into 2 classes
    - It's a single layer neural network, meaning it only has one layer of neurons
    - It can only classify linearly separable data, meaning it can only classify data that can be separated by a line
-  **Fully connected** or **Multi layer perceptron** (MLP) is a neural network architecture where each neuron in a layer is connected to all neurons in the next layer
    - It consists of an input layer, one or more hidden layers and an output layer
    - The hidden layers are fully connected, meaning each neuron in a layer is connected to all neurons in the next layer
    - The hidden layers are all perceptrons, meaning they are all linear classifiers, possibly using sigmoid functions to use the probability that something is in a class
    - Due to these factors an MLP can classify non-linearly separable data, instead of just linearly like the perceptron. This is basically the classification version of a regression neural network
- **Convolutional Neural Network** (CNN) is a neural network architecture that is used for image classification
    - It consists of an input layer, output layer and some number of hidden layers
    - We usually say there are a few types of layers in a convulational network
        - Convolutional layers
            - Convolutional layers are used to extract features from the image
            - This could be edges, corners, etc.
            - This is done by applying a filter to the image using a kernel. Much like HOG
            - Some convulational layers also minimize the size of the image, fx. gray scaling it
        - Pooling layers
            - Pooling layers are used to reduce the size of the image, to save on computational complexity.
            - This is usually done by extracting the dominant features.
            - Pooling is usually either
                - **Max pooling** which takes the maximum value in a sliding window
                    - This also discards noise and minor features, usually performing better than average pooling
                - **Average pooling** which takes the average value in a sliding window
            - Again much like HOG which uses a sliding window and blocks to reduce the size of the feature space.
        - Fully connected layers
            - These are the same as in a MLP
            - They take the output from the previous steps to classify the image, or parts of the image
    - Not all CNNs have all of these layers, but they all have at least one convolutional layer and one fully connected layer

### Regularization, data augmentation, model complexity and norms
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
- Data augmentation is a method of increasing the size of the dataset by adding slightly modified copies of the data points
    - This is done to reduce overfitting
    - Fx. if we have a dataset of pictures of cats, we can augment the dataset by flipping the pictures horizontally
    - This is done because the model will not be able to tell the difference between a cat that is flipped horizontally and a cat that is not flipped horizontally
    - We can also add noise to the data points to make the model more robust
- Batch normalization is a method of normalizing the input data
    - This both improves speed and Accuracy
    - The reasons are contested, but for something like images, ensuring everything is centered can make the processing easier
    - You basically just standardize the input data
- Model complexity is the complexity of the model
    - This is usually measured by the number of parameters in the model
    - The more complex the model is, the more prone it is to overfitting
    - This is something to be very careful with in neural networks, and can be helped with regularization
- Norms are used to measure the size of a vector
    - The L2 norm is the Euclidean distance, or the length of the vector
        - $||\mathbf{x}||_2=\sqrt{\sum_{i=1}^nx_i^2}$
    - These can be used to measure the error of a model
        - Fx. the L2 norm of the difference between the predicted value and the actual value
    - This seems weird to have here ngl

### Model tuning, dropout, early stopping, complexity
- **Model tuning** is the process of finding the optimal parameters for a model
    - We do this to improve performance
    - Done by tuning things like
        - Learning rate and momentum
        - Probability of dropout
        - Regularization
        - Node count
        - Batch size
- **Dropout** is a method of reducing overfitting by randomly dropping neuron outputs during training.
    - This ensures that the model doesn't overly rely on any one neuron
    - The next layer just sees the previous layer as having less neurons
- **Early stopping** is a method of reducing overfitting by stopping the training when the validation loss starts to increase or flatten out
    - Limits overfitting, is a type of regularization
    - More specifically take the minimum loss of the last $p$ epochs and take the best model if the loss $>~=$ minimum loss
    - This can take a patience parameter to set how many times the loss can increase or do nothing before stopping

### Convolutional Neural Networks (CNN) (Convolutional layers, max pooling)
- **Convolutional Neural Network** (CNN) is a neural network architecture that is used for image classification
    - It consists of an input layer, output layer and some number of hidden layers
    - We usually say there are a few types of layers in a convulational network
        - Convolutional layers
            - Convolutional layers are used to extract features from the image
            - This could be edges, corners, etc.
            - This is done by applying a filter to the image using a kernel. Much like HOG
            - Some convulational layers also minimize the size of the image, fx. gray scaling it
        - Pooling layers
            - Pooling layers are used to reduce the size of the image, to save on computational complexity.
            - This is usually done by extracting the dominant features.
            - Pooling is usually either
                - **Max pooling** which takes the maximum value in a sliding window
                    - This also discards noise and minor features, usually performing better than average pooling
                - **Average pooling** which takes the average value in a sliding window
            - Again much like HOG which uses a sliding window and blocks to reduce the size of the feature space.
        - Fully connected layers
            - These are the same as in a MLP
            - They take the output from the previous steps to classify the image, or parts of the image
    - Not all CNNs have all of these layers, but they all have at least one convolutional layer and one fully connected layer
