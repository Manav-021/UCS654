import os
import resend
import base64
from dotenv import load_dotenv
from config.settings import ZIP_FILE

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")
SENDER = os.getenv("SENDER_EMAIL")

def send_mail(receiver_email):

    with open(ZIP_FILE, "rb") as f:
        file_content = f.read()

    # Encode file to base64
    encoded_file = base64.b64encode(file_content).decode("utf-8")

    resend.Emails.send({
        "from": SENDER,
        "to": receiver_email,
        "subject": "Your Mashup File 🎵",
        "html": "<p>Your mashup file is attached.</p>",
        "attachments": [
            {
                "filename": "mashup.zip",
                "content": encoded_file
            }
        ]
    })
