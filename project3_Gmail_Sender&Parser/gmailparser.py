# import os
# import base64
# from google.auth.transport.requests import Request
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from google.oauth2.credentials import Credentials

# # ----- Gmail API Scope -----
# SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# # ----- Authentication Function -----
# def authenticate():
#     creds = None  # Holds your credentials

#     # Use previously saved login (if available)
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)

#     # If credentials are missing or invalid
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())  # Refresh using saved token
#         else:
#             # First-time login using credentials.json file
#             flow = InstalledAppFlow.from_client_secrets_file(r'C:\Users\METVT\Desktop\SummerPythonProjects\project3_gmailParser\credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)  # Opens browser to log in

#         # Save the new credentials to token.json
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())

#     return creds

# # ----- Function to List Recent Emails and Check Body -----
# def list_recent_emails():
#     creds = authenticate()
#     service = build('gmail', 'v1', credentials=creds)

#     # Get the 5 most recent messages
#     results = service.users().messages().list(userId='me', maxResults=5).execute() #me can be replaced with my actual email 
#     messages = results.get('messages', [])

#     for msg in messages:
#         msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()

#         headers = msg_data.get('payload', {}).get('headers', [])
#         subject = next((header['value'] for header in headers if header['name'] == 'Subject'), '(No Subject)')
#         print(f"Subject: {subject}")

#         # --- Body extraction ---
#         payload = msg_data.get('payload', {})
#         body = None

#         # Case 1: Simple message, no 'parts' aka plain text 
#         if 'data' in payload.get('body', {}):
#             body_data = payload['body']['data']
#             body = base64.urlsafe_b64decode(body_data).decode('utf-8', errors='replace')

#         # Case 2: Multipart message aka plain text and html, look for text/plain part
#         elif 'parts' in payload:
#             for part in payload['parts']:
#                 if part.get('mimeType') == 'text/plain' and 'data' in part.get('body', {}):
#                     body_data = part['body']['data']
#                     body = base64.urlsafe_b64decode(body_data).decode('utf-8', errors='replace')
#                     break  # Stop after first plain-text part

#         if body:
#             print("Body Preview:")
#             print(body[:300])  # Just show first 300 characters
#             print()

#             # Check if the email body contains your phrase
#             if "You sent" in body and "to" in body:
#                 print("Match found: This email looks like a sent funds alert.\n")
#         else:
#             print("No body found.\n")

# # ----- Run the Parser -----
# if __name__ == '__main__':
#     list_recent_emails()


import os
import base64
from datetime import datetime
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# ----- Gmail API Scope -----
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# ----- Authenticate the User -----
def authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                r'C:\Users\METVT\Desktop\SummerPythonProjects\project3_gmailParser\credentials.json',
                SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

# ----- Fetch Only Today's Emails from Specific Sender -----
def fetch_recent_emails(service, max_results=50):
    today = datetime.now().strftime('%Y/%m/%d')
    query = f'from:kye.test.parser@gmail.com after:{today}'

    results = service.users().messages().list(userId='me', maxResults=max_results, q=query).execute()
    messages = results.get('messages', [])
    message_data = []

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        message_data.append(msg_data)

    return message_data

# ----- Extract Subject and Body from Message -----
def extract_email_details(msg_data):
    headers = msg_data.get('payload', {}).get('headers', [])
    subject = next((header['value'] for header in headers if header['name'] == 'Subject'), '(No Subject)')

    payload = msg_data.get('payload', {})
    body = None

    if 'data' in payload.get('body', {}):
        body_data = payload['body']['data']
        body = base64.urlsafe_b64decode(body_data).decode('utf-8', errors='replace')
    elif 'parts' in payload:
        for part in payload['parts']:
            if part.get('mimeType') == 'text/plain' and 'data' in part.get('body', {}):
                body_data = part['body']['data']
                body = base64.urlsafe_b64decode(body_data).decode('utf-8', errors='replace')
                break

    return {'subject': subject, 'body': body}

# ----- Categorize Email Based on Body Text -----
def classify_email(body):
    if body is None:
        return 'uncategorized'
    if "You have received" in body and "from" in body:
        return 'received'
    elif "was charged" in body:
        return 'spent'
    elif "You sent" in body and "to" in body:
        return 'sent'
    else:
        return 'uncategorized'

# ----- Group Emails into Categories -----
def categorize_emails(email_list):
    categories = {
        'received': [],
        'spent': [],
        'sent': [],
        'uncategorized': []
    }

    for email in email_list:
        category = classify_email(email['body'])
        categories[category].append(email)

    return categories

# ----- Show Emails for a Given Category -----
def display_emails_for_category(categories, category):
    emails = categories.get(category, [])
    if not emails:
        print(f"No emails found in category: {category}")
        return

    for i, email in enumerate(emails, start=1):
        print(f"\n--- Email {i} ---")
        print(f"Subject: {email['subject']}")
        print(f"Body (first 300 chars):\n{email['body'][:300] if email['body'] else 'No body found'}")
        print("------------------------")

# ----- Main Runner -----
def main():
    creds = authenticate()
    service = build('gmail', 'v1', credentials=creds)

    print("Fetching today's emails...")
    raw_messages = fetch_recent_emails(service)

    if not raw_messages:
        print("No transactions were made today.")
        return

    processed_emails = [extract_email_details(msg) for msg in raw_messages]
    categorized = categorize_emails(processed_emails)

    print("\nAvailable Categories:")
    for cat in categorized.keys():
        print(f" - {cat} ({len(categorized[cat])} emails)")

    choice = input("\nEnter the category you want to view (e.g. 'spent', 'received', 'sent'): ").strip().lower()
    display_emails_for_category(categorized, choice)

# ----- Run the Script -----
if __name__ == '__main__':
    main()
