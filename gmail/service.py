import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path


class GmailService:

    @classmethod
    def get_service(cls, token: str, credentials: str, scopes: list):
        creds = None

        if os.path.exists(token):
            with open(token, 'rb') as token_open:
                creds = pickle.load(token_open)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials, scopes)
                creds = flow.run_local_server(port=0)

            with open(token, 'wb') as token_open:
                pickle.dump(creds, token_open)

        service = build('gmail', 'v1', credentials=creds)
        return service
