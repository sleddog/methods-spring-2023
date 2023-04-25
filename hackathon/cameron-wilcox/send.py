from __future__ import print_function
import base64
from email.mime.text import MIMEText
import os.path

from argparse import ArgumentParser

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://mail.google.com/']
CLIENT_CREDS = 'credentials.json'

parser : ArgumentParser = ArgumentParser(description="Gmail sending python script", prog="Gmail Sender")
parser.add_argument('-t','--to', metavar='RECIPIENT', help='Address to send email to', required=True)
parser.add_argument('-m', '--message', metavar='MESSAGE', help="Path to text file with message to be sent", required=True)
parser.add_argument('-s', '--subject', metavar='SUBJECT', help="Subject of message", default="")
args = parser.parse_args()

RECIPIENT   : str = args.to.strip()
MESSAGE     : str = args.message.strip()
SUBJECT     : str = args.subject.strip()

def main():
    body : str = ""
    with open(MESSAGE) as file:
        body = file.read()

    message = MIMEText(body)
    message['To'] = RECIPIENT
    message['Subject'] = SUBJECT
    create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_CREDS, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = (service.users().messages().send(userId="me", body=create_message).execute())
        print(F'sent message to {results} Message Id: {results["id"]}')
    except HttpError as error:
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()