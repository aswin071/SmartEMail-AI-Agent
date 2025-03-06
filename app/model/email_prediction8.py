"""
Once the model if trained try to predict the intent or category
"""
from app.model.prepare_data1 import *
from app.model.text_preprocessing2 import *
from app.model.feature_extraction3 import *
from app.model.text_classification4 import *
from app.model.labeling5 import *
from app.model.final_feature_set6 import *
from app.model.train_model7 import *

def predict_category(text):
    """
    Predict the category of a given text using the trained classifier.
    """
    processed_text = preprocess_text(text)
    text_vec = vectorizer.transform([processed_text]).toarray()  # Convert to dense array
    prediction = clf.predict(text_vec)

    # Ensure 'intent' is of the 'category' dtype
    if data['intent'].dtype != 'category':
        data['intent'] = data['intent'].astype('category')

    return data['intent'].cat.categories[prediction[0]]

# Example usage
sample_text = "can you help me to solve issues with payment?"
predicted_category = predict_category(sample_text)

# Responses for different categories
responses = {
    'cancel_order': "To cancel your order, please follow the instructions on our website or contact our customer service.",
    'change_order': "To change your order, please visit our order change portal or reach out to support.",
    "get_invoice" : "To get your invoice please visit our order change portal."
}

# Generate a response based on the predicted category
def generate_response(text):
    predicted_category = predict_category(text)
    return responses.get(predicted_category, "Sorry, I couldn't understand your request.")

# Example usage
response = generate_response(sample_text)

