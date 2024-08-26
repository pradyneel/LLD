class EmailClient:
    def send_email(self, recipient, subject, body):
        raise NotImplementedError

class GmailClient(EmailClient):
    def send_email(self, recipient, subject, body):
        # Logic to send email using GMail API
        pass

class OutlookClient(EmailClient):
    def send_email(self, recipient, subject, body):
        # Logic to send email using Outlook API
        pass

class EmailService:
    def __init__(self, email_client):
        self.email_client = email_client
    
    def send_email(self, recipient, subject, body):
        self.email_client.send_email(recipient, subject, body)

gmail_client = GmailClient()
email_service = EmailService(gmail_client)
email_service.send_email("recipient@example.com", "Subject", "Email body")