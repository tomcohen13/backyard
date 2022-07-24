# 
from app import app, mail

# Import data models
from app.models import Institution, User

# Flask Mail
from flask import request, session
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
import os


s = URLSafeTimedSerializer(app.config["MAIL_KEY"])


def send_confirmation(user : User):
    token = s.dumps(user.id, salt = os.environ["MAIL_SALT"])
    link = "https://www.bkyrd.com/mail/confirm?token=" + token
    msg = Message(subject="[The Backyard] Complete Your Registation!",
                    sender="tom@bkyrd.com",
                    recipients = [user.email],
                    body = f"Hey {user.name.split()[0]}! Complete your registration here: {link}")

    # change message ID
    msg.msgId = msg.msgId.split('@')[0] + '@bkyrd'  # for instance your domain name

    # send email
    mail.send(msg)


    