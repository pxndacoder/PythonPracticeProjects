from __future__ import print_function
import base64
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os.path


SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate():
    """Logs in and returns Gmail API service."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
    'C:/Users/METVT/Desktop/SummerPythonProjects/project3_gmailParser/credentials.json', SCOPES)

            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def create_message(to, subject, body):
    """Creates a MIMEText email and encodes it for Gmail API."""
    message = MIMEText(body)
    message['to'] = to
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}

def send_email(service, user_id, message):
    """Sends the message using Gmail API."""
    sent = service.users().messages().send(userId=user_id, body=message).execute()
    print(f"✅ Email sent! Message ID: {sent['id']}")

def main():
    service = authenticate()
    to = "kye.test.parser@gmail.com"

    # 4 sample test emails
    test_emails = [
    (
        "You sent money",
        """Dear John Brown,

You sent $250.00 BBD to John Smith at 9:28 PM (GMT). Your transaction has been completed successfully.

If you did not perform this transaction please contact us immediately at 1 866 743 2257.

Sincerely,
CIBC Notification Service."""
    ),
    (
        "Card purchase",
        """Dear John Brown,

Your card ending in 1234 was charged $78.50 BBD at CARIBBEAN ELECTRONICS LTD.

If you did not make this purchase please contact us immediately at 1 866 743 2257.

Sincerely,
CIBC Notification Service."""
    ),
    (
        "You sent money",
        """Dear John Brown,

You sent $250.00 BBD to John Smith at 9:28 PM (GMT). Your transaction has been completed successfully.

If you did not perform this transaction please contact us immediately at 1 866 743 2257.

Sincerely,
CIBC Notification Service."""
    ),
    (
        "Attempted send",
        """Dear John Brown,

You attempted to send $9.00 BBD to sharkisha Brown at 11:33 PM (GMT). Your transaction has been completed successfully.

If you did not perform this transaction please contact us immediately at 1 866 743 2257.

Sincerely,
CIBC Notification Service."""
    ),
]


    for subject, body in test_emails:
        msg = create_message(to, subject, body)
        send_email(service, 'me', msg)

if __name__ == '__main__':
    main()
