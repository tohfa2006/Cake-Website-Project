"""
Email module made by Kevin Caplescu
Used to allows interaction from company automated email in regards to certain events.
"""
import smtplib
import ssl
import os
import dotenv

from dotenv import load_dotenv

load_dotenv()

class EmailManager:
    def __log_in_server__(self):
        cntx = ssl.create_default_context()
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=cntx)
        return(server)
    
    def __init__(self):
        self.email_address = os.getenv("EMAIL_USER")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.server = self.__log_in_server__()
    
    
    def send_email(self, recipient, subject, message):
        self.server.login(self.email_address, self.email_password)
        self.server.sendmail(self.email_address, recipient, f"Subject: {subject}\n\n{message}")