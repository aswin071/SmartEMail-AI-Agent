"""
Let "category" or "intent" as the target variable, you can map them to numerical values for classification.
"""
from app.model.prepare_data1 import *
from app.model.text_preprocessing2 import *
from app.model.feature_extraction3 import *
from app.model.text_classification4 import *

# Ensure 'intent' column is categorical before encoding
data['intent'] = data['intent'].astype('category')  
# Convert categorical intent values into numerical labels
data['label'] = data['intent'].cat.codes  

print(data[['category', 'label']].head())
