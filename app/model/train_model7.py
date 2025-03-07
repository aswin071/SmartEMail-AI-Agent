"""
Train a machine learning model like SVM, RandomForest
"""

from app.model.prepare_data1 import *
from app.model.text_preprocessing2 import *
from app.model.feature_extraction3 import *
from app.model.text_classification4 import *
from app.model.labeling5 import *
from app.model.final_feature_set6 import *

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(tfidf_df, data['label'], test_size=0.3, random_state=42)

# Initialize and train the classifier
clf = SVC(kernel='linear')
clf.fit(X_train, y_train)

# Predict on the test set
y_pred = clf.predict(X_test)

# Evaluate the performance
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.4f}')
