from gmail.client import GmailClient
from gmail.service import GmailService
from gmail.decode import DecodeEmail
import logging


class Gmail:

    def __init__(self, token: str, credentials: str, scopes: list, query_email: str, mark_read: bool = False):
        self.token = token
        self.credentials = credentials
        self.scopes = scopes
        self.query_email = query_email
        self.mark_read = mark_read
        self.service = GmailService.get_service(token=self.token, credentials=self.credentials, scopes=self.scopes)

    def get_list_mails(self) -> list:
        result = GmailClient.get_email_id(service=self.service, query_email=self.query_email)
        messages = result['messages']
        list_mails = []

        for message in messages:
            email = GmailClient.get_email(message['id'], self.service)['message']
            decode = DecodeEmail.decode(email)
            list_mails.append(decode)
            if self.mark_read:
                GmailClient.post_modify_mark_read(message['id'], self.service)

        return list_mails

    def mark_read(self, mail_id) -> None:
        try:
            GmailClient.post_modify_mark_read(mail_id, self.service)
        except Exception as error:
            logging.error(error)
