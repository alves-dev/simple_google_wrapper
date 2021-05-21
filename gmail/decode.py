import base64


class DecodeEmail:

    @classmethod
    def decode(cls, data):
        contents = base64.urlsafe_b64decode(data.encode('ASCII'))
        return contents
