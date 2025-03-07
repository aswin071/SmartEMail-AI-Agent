"""
Creating features that can help in classifying text to the model.
Feature engineering allows you to add new useful data features for the model to learn from.
    Text length gives a rough idea of how long or complex the query is.
    Keyword presence (e.g., 'cancel', 'change') can help the model identify intent based on the words in the query. For example, 
    if 'cancel' is present, it might suggest that the user wants to cancel an order.
"""
from app.model.prepare_data1 import *
from app.model.text_preprocessing2 import *
data['text_length'] = data['processed_utterance'].apply(lambda x: len(x.split()))

# Create features for keywords presence (e.g., 'cancel', 'change')
keywords = ['cancel', ' ', 'help', 'change']
for keyword in keywords:
    data[f'contains_{keyword}'] = data['processed_utterance'].apply(lambda x: 1 if keyword in x else 0)
# print('==', data)