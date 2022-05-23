# Machine learning notes
## Algorithms
### Linear Algorithms
Calculates a score from a linear combination of the input data and the weights. Works best for classifications. Cheap to train, but the data needs to be normalized first as one bad value can mess with the entire dataset
- Averaged perceptron = Best for text classification
- Stochastic dual coordinated ascent = Good performance
- L-BFGS = Good for large numbers
- Symbolic stochastic gradient descent = Fastest birnary classification
- Online gradient descent = Has loss functions

### Decision tree algorithms
A model that has a series of decisions, essentially a flow chart through the data. Can take alot of different values, no need for normalization. Known to be very accurate, these are hard to explain though and can grow very large.
- Light gradient boosted machine = Fast binary classification
- Fast tree = Good with unbalanced data
- Fast forest = Works well with noisy data
- Generalized additive model = Very explainable

## Tasks
### Binary classification
Figure out which of 2 categories a data point belongs to.

Example: Does a picture contain a dog or not?

### Multiclass classification
Used to predict the category of input data, the training data is a bunch of labeled examples.

Example: Categorizing music into different genres.

### Regression
Used to predict the value of a label from related data.

Example: Predict house prices based on attributes. Such as number of bedrooms, location, size etc.

### Clustering
Group instances of data into clusters that contain similar data. Can be used to identify non obvious relation ships.

Example: Identifying segments hotel guest habits based on habits and choices

### Anomaly detection
Detect rare events.

Example: Detect intrusions into networks

### Ranking
Scores groups of data

### Recommendation
Recommend new data based on old data

Example: Using book ratings to recommend other books

### Forecasting
Make predictions about future behaviour.

Example: Predict the weather

### Image classification
Predict the category of an image, kind of like multi classification.

Example: Determining the race of cat on the picture.

### Object detection
Image classification, but it can contain multiple objects and the algorithm creates a boundary box around the object it detects.

Example: Determining the races of cats on a picture.

