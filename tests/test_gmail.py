from gmail.client import GmailClient
from gmail.service import GmailService
#from table.parser import TableParser
#from usage.parser import UsageParser
from gmail.decode import DecodeEmail

# (from:(alvesmoreiraigor@gmail.com) subject:(Relatório de uso diário) after:2021/5/17) OR ( from:(alvesmoreiraigor@gmail.com) subject:(Relatório de uso diário) is:unread )

class ExtractUsage:
    @classmethod
    def extract(cls, mark_read=True) -> list:
        service = GmailService.get_service(token='token.pickle', credentials='credentials_gmail.json',
                                           scopes=['https://www.googleapis.com/auth/gmail.readonly',
                                                   'https://www.googleapis.com/auth/gmail.modify'])
        result = GmailClient.get_email_id(service=service,
                                          query_email='(from:(alvesmoreiraigor@gmail.com) subject:(Relatório de uso diário) after:2021/5/17) '
                                                      'OR ( from:(alvesmoreiraigor@gmail.com) subject:(Relatório de uso diário) is:unread )')
        messages = result['messages']
        usage_list = []
        count = 0
        for message in messages:
            email = GmailClient.get_email(message['id'], service)['message']
            decode = DecodeEmail.decode(email)
            #table = TableParser.parser(decode)
            #usage = UsageParser.parser(table)
            #usage_list.append(usage)
            count+=1
            if mark_read:
                GmailClient.post_modify_mark_read(message['id'], service)

        return count


print(ExtractUsage.extract())

