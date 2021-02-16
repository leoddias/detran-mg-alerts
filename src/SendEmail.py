import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class SendEmail:
    def __init__(self):
        self.from_email = os.environ.get('FROM_EMAIL')
        self.to_emails = os.environ.get('TO_EMAILS')

    def send_email(self, subject, content):
        message = Mail(
            from_email=self.from_email,
            to_emails=self.to_emails,
            subject=subject,
            html_content=content)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            sg.send(message)
        except Exception as e:
            print(e.message)