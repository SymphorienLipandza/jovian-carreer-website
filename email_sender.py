#Importing library
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Email sender function
def send_email(to_email, subject, message):
    # Set up SMTP server and email credentials
    smtp_server = os.environ['smtp_server']
    smtp_port = os.environ['smtp_port']
    sender_email = os.environ['email']
    sender_password = os.environ['password']

    # Create a multipart message
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = to_email
    email_message['Subject'] = subject

    # Add the message body
    email_message.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.set_debuglevel(1)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(email_message)
