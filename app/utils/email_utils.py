from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List


class EmailSchema(BaseModel):
    email: List[EmailStr]

conf = ConnectionConfig(
    MAIL_USERNAME = 'dce949c85db7d3',  
    MAIL_PASSWORD = 'cb2d2112b2a0f8',  
    MAIL_FROM = 'test@email.com',  
    MAIL_PORT = 2525,  
    MAIL_SERVER = 'sandbox.smtp.mailtrap.io',
    MAIL_FROM_NAME = 'Desired Name', 
    MAIL_STARTTLS = True,  
    MAIL_SSL_TLS = False,  
    USE_CREDENTIALS = True, 
    VALIDATE_CERTS = True 
)

app = FastAPI()


async def send_email_function(customer_email: EmailStr, response_message: str) -> JSONResponse:
    """
    Send an email with the given response message to the provided customer email.
    """
    # Construct the HTML content of the email
    html_content = f"""
    <p>Dear Customer,</p>
    <p>{response_message}</p>
    <p>Best regards,<br>
    Smart Email Assistant Team</p>
    """
    message = MessageSchema(
        subject="Automated Customer Support Response",
        recipients=[customer_email],  
        body=html_content,
        subtype=MessageType.html  
    )
    fm = FastMail(conf)
    await fm.send_message(message)
    # return JSONResponse({"message": "Email sent successfully"})
