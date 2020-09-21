"""
Import the following modules:
Imputer from sklearn.preprocessing and Pipeline from sklearn.pipeline.
SVC from sklearn.svm.
Create the pipeline using Pipeline() and steps.
Create training and test sets. Use 30% of the data for testing and a random state of 42.
Fit the pipeline to the training set and predict the labels of the test set.
Compute the classification report.
"""

# Import necessary modules
from sklearn.preprocessing import Imputer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

# Setup the pipeline steps: steps
steps = [('imputation', Imputer(missing_values='NaN', strategy='most_frequent', axis=0)),
        ('SVM', SVC())]

# Create the pipeline: pipeline
pipeline = Pipeline(steps)

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit the pipeline to the train set
pipeline.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = pipeline.predict(X_test)

# Compute metrics
print(classification_report(y_test, y_pred))
