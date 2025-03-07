from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from app.model.text_preprocessing2 import preprocess_text  
from app.model.feature_extraction3 import *  
from app.model.text_classification4 import *  
from app.model.prepare_data1 import *
from app.model.labeling5 import *
from app.model.final_feature_set6 import *
from app.model.train_model7 import *
from app.utils.email_utils import *

app = FastAPI() 

# Pydantic model for the request body
class TextRequest(BaseModel):
    text: str
    email : str

# Function to predict the category
def predict_category(sample_text):
    """
    Predict the category of a given text using the trained classifier.
    """
    processed_text = preprocess_text(sample_text) 
    text_vec = vectorizer.transform([processed_text]).toarray()  
    
    prediction = clf.predict(text_vec)
    
    if data['intent'].dtype != 'category':
        data['intent'] = data['intent'].astype('category')
    
    predicted_category = data['intent'].cat.categories[prediction[0]]
    return predicted_category

@app.post("/predict")
async def predict_category_endpoint(request: TextRequest):
    """
    Endpoint for predicting the category of a given text.
    """
    sample_text = request.text 
    predicted_category = predict_category(sample_text)  
    return {"predicted_category": predicted_category}

@app.post("/generate_response")
async def generate_response(request: TextRequest):
    """
    Generate a response based on the predicted category.
    """
    sample_text = request.text  
    customer_email = request.email

    
    # Responses for different categories
    responses = {
        'cancel_order': "To cancel your order, please follow the instructions on our website or contact our customer service for further assistance. We're here to help!",
        'change_order': "If you would like to change your order, please visit our order change portal or reach out to our support team for assistance.",
        'get_invoice' : "To obtain your invoice, please visit our order change portal. You will be able to view and download your invoice there.",
        'change_shipping_address': "To change your shipping address, please log in to your account and update your address under the 'My Profile' section. For help, feel free to contact support.",
        'check_cancellation_fee': "To check if there are any cancellation fees for your order, please refer to our cancellation policy on our website. If you have further questions, our customer service team is happy to assist you.",
        'check_invoice': "You can check the details of your invoice by logging into your account. If you have any trouble accessing it, please let us know, and we’ll assist you.",
        'check_payment_methods': "We accept a variety of payment methods, including credit/debit cards, PayPal, and bank transfers. Please visit our payment methods page for more details.",
        'check_refund_policy': "For information on our refund policy, please visit our Refunds and Returns page. If you have any specific questions, feel free to reach out to our support team.",
        'complaint': "We apologize for any inconvenience. Please share the details of your complaint, and our team will work to resolve the issue as quickly as possible.",
        'contact_customer_service': "If you need to get in touch with our customer service team, please use the contact form on our website or call us at our support number. We’re here to help!",
        'contact_human_agent': "If you prefer to speak to a human agent, please visit our support page to initiate a live chat or call us directly.",
        'create_account': "To create a new account, please visit our sign-up page and follow the instructions. If you need any assistance, feel free to reach out.",
        'delete_account': "To delete your account, please visit your account settings and follow the instructions. If you need help, we are here to assist you.",
        'delivery_options': "We offer multiple delivery options for your convenience. Please check our delivery options page to choose the one that suits you best.",
        'delivery_period': "The estimated delivery period for your order can be found in your order confirmation email. If you need more detailed information, our customer service can assist you.",
        'edit_account': "To edit your account details, log in to your account and go to the 'My Profile' section where you can update your information.",
        'get_refund': "To request a refund, please follow our refund process outlined in our Refund Policy. If you have any issues, don’t hesitate to reach out.",
        'newsletter_subscription': "To subscribe or unsubscribe from our newsletter, please visit our newsletter preferences page. We send periodic updates and offers.",
        'payment_issue': "If you’re facing issues with payment, please double-check your payment details and ensure your account is active. For help, our support team is available.",
        'place_order': "To place an order, please visit our website, browse through the available products, and follow the checkout steps. If you face any difficulty, our team is here to guide you.",
        'recover_password': "To recover your password, please visit the 'Forgot Password' page on our website. You will receive instructions to reset your password via email.",
        'registration_problems': "If you're facing problems with registration, please ensure that all required fields are filled correctly. If issues persist, contact our support team for further assistance.",
        'review': "We appreciate your feedback! Please visit our review page to leave a review or share your experience. We value your opinion and look forward to your thoughts.",
        'set_up_shipping_address': "To set up or update your shipping address, log into your account and go to the 'My Profile' section. If you need assistance, feel free to contact us.",
        'switch_account': "To switch accounts, please log out of the current account and sign in with your other account credentials. For further assistance, our support team is available.",
        'track_order': "To track your order, please visit our order tracking page and enter your order number. You’ll be able to see the real-time status of your shipment.",
        'track_refund': "To track the status of your refund, please visit our refund tracking page and enter your refund number. If you need assistance, our support team is happy to help."
    }

    
    # Predict category and generate response
    predicted_category = predict_category(sample_text)
    response_message = responses.get(predicted_category, "Sorry, I couldn't understand your request.")
    await send_email_function(customer_email, response_message)
    return JSONResponse(status_code=200, content={"message": "Email has been sent successfully!"})
