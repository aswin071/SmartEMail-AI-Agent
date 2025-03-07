"""
Since customer queries are often messy (with punctuation, stopwords, etc.), we will clean and preprocess the text data
Text preprocessing is crucial in NLP tasks to clean the raw data. This involves:

    Converting all text to lowercase so the model does not differentiate between 'Hello' and 'hello'.
    Removing non-alphabet characters and stop words.
    Tokenizing (splitting) text into words. This ensures that the model gets cleaner, more consistent input.
"""
from app.model.prepare_data1 import *

import re
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')  # For word tokenization
nltk.download('punkt_tab') 


# Preprocessing function to clean text
def preprocess_text(text):
    # Lowercase and remove non-alphabet characters
    text = text.lower() #conver text to lowercase 
    text = re.sub(r'[^a-z\s]', '', text) #remove non-alphabet characters
    tokens = word_tokenize(text) #split text into words
    return ' '.join(tokens)
data = prepare_data(file_path)
# Apply preprocessing to the 'utterance' column
data['processed_utterance'] = data['utterance'].apply(preprocess_text)
# print('==',data)
