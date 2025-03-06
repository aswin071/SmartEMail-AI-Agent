"""
need to transform the text into numerical features. 
TF-IDF (Term Frequency-Inverse Document Frequency), which is a commonly used method for text classification tasks.
The TF-IDF Vectorizer converts the text data into numerical vectors, which the machine learning model can use to identify patterns.

-definition :TF-IDF (Term Frequency-Inverse Document Frequency) is a method that highlights important words based 
on how frequently they appear in a document versus across all documents, improving the model’s ability to identify relevant features.
"""
from app.model.prepare_data1 import *
from app.model.feature_extraction3 import *
from app.model.text_classification4 import *
#import text_classification  module
from sklearn.feature_extraction.text import TfidfVectorizer


vectorizer = TfidfVectorizer(stop_words='english')
# Transform the processed_utterance column into a matrix of TF-IDF features
X = vectorizer.fit_transform(data['processed_utterance'])
# print('==',X)
# Convert the sparse matrix to a DataFrame for easier readability
tfidf_df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
# print(tfidf_df.head())
