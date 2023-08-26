# File for experimentation
import __meta
import smtplib
from email.message import EmailMessage
from PvtInfo.info import Google_Token, Email_Address

# Set up connection to SMTP server

class EmailSender():
    def __init__(self, receiver, subject, message) -> None:
        if not receiver.endswith('@gmail.com'):
            remove_index = receiver.index("@")
            receiver = receiver[:remove_index]
            print(receiver)
        self.receiver = receiver
        self.subject = subject
        self.message = message
    
    def set_connection(self):
        self.connection = smtplib.SMTP('smtp.gmail.com', 587)
        self.connection.starttls()
        self.connection.login(Email_Address, Google_Token)

    def compose_email(self):
        self.email = EmailMessage()
        self.email['Subject'] = self.subject
        self.email['From'] = Email_Address
        self.email['To'] = self.receiver
        self.email.set_content(self.message)
    
    def send_email(self):
        self.set_connection()
        self.compose_email()
        self.connection.send_message(self.email)
        self.close_connection()

    def close_connection(self):
        self.connection.quit()

emailsenderinstance = EmailSender('sarthakrawool09@gmail.com', 'soemthing', 'soemgsa')
emailsenderinstance.send_email()