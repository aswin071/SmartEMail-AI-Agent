""""
Combine the engineered features (like text_length, contains_keyword columns, and TF-IDF features) into a ,
single dataset to use for training your machine learning model.
"""

from app.model.prepare_data1 import *
from app.model.text_preprocessing2 import *
from app.model.feature_extraction3 import *
from app.model.text_classification4 import *
from app.model.labeling5 import *

# Combine TF-IDF features with the additional engineered features
final_df = pd.concat([tfidf_df, data[['text_length'] + [f'contains_{keyword}' for keyword in keywords]]], axis=1)

# Target variable
y = data['label']

# Final feature set
X = final_df

# print(X.head())