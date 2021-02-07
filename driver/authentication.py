from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class AuthenticationGoogle:
    @classmethod
    def get_drive(cls):
        gauth = GoogleAuth()
        gauth.CommandLineAuth()
        drive = GoogleDrive(gauth)
        return drive
