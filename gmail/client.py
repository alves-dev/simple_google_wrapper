from gmail.service import GmailService


class GmailClient:

    @classmethod
    def get_email_id(cls, service: GmailService, query_email: str) -> dict:
        results = service.users().messages().list(userId='me', q=query_email).execute()
        messages = results.get('messages', [])
        if len(messages) > 0:
            return {'results': True, 'messages': messages}
        else:
            return {'results': False, 'messages': messages}

    @classmethod
    def get_email(cls, email_id, service: GmailService) -> dict:
        email = service.users().messages().get(userId='me', id=email_id).execute()
        message = email['payload']['body']['data']
        if len(message) > 0:
            return {'results': True, 'message': message}
        else:
            return {'results': False, 'message': 'Bad requests or invalid mail_id'}

    @classmethod
    def post_modify_mark_read(cls, email_id, service: GmailService):
        service.users().messages().modify(userId='me', id=email_id, body={'removeLabelIds': ['UNREAD']}).execute()
        return True
