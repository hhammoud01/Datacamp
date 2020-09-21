#1 Create arrays for the features and the target variable from df. As a reminder, the target variable is 'party'.
#2 Instantiate a KNeighborsClassifier with 6 neighbors.
#3 Fit the classifier to the data.
#4 Predict the labels of the training data, X.
#5 Predict the label of the new data point X_new.

# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier

# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X, y)

# Predict the labels for the training data X
y_pred = knn.predict(X)

# Predict and print the label for the new data point X_new
new_prediction = knn.predict(X_new)
print("Prediction: {}".format(new_prediction))
