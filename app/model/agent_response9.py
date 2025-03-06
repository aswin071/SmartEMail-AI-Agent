"""
To generate automated responses based on the predicted intent,store predefined responses for each category/intent
"""


from app.model.prepare_data1 import *
from app.model.text_preprocessing2 import *
from app.model.feature_extraction3 import *
from app.model.text_classification4 import *
from app.model.labeling5 import *
from app.model.final_feature_set6 import *
from app.model.train_model7 import *
from app.model.email_prediction8 import *
# Define responses for each category
responses = {
    'cancel_order': "To cancel your order, please follow the instructions on our website or contact our customer service.",
    'change_order': "To change your order, please visit our order change portal or reach out to support."
    'invoice_data' "dhsntfjkersdhgfhdrfjksfdhghsdfjguhsdhfghsfdhig"
}

# Generate a response based on the predicted category
def generate_response(text):
    predicted_category = predict_category(text)
    return responses.get(predicted_category, "Sorry, I couldn't understand your request.")

# Example usage
response = generate_response(sample_text)

