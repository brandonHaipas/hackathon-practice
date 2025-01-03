from fastapi import FastAPI, Form
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

@app.post("/webhook")
async def whatsapp_webhook(From: str = Form(...), Body: str = Form(...)):
    """
    Handles incoming WhatsApp messages.
    Args:
        From (str): The sender's phone number.
        Body (str): The content of the message.
    """
    print(f"Message received from {From}: {Body}")
    
    # Create a response
    response = MessagingResponse()
    response.message("Hi! This is your bot responding.")
    
    return str(response)
