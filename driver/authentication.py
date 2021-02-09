from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class AuthenticationGoogle:
    @classmethod
    def get_drive(cls):
        g_auth = GoogleAuth()
        g_auth.CommandLineAuth()
        drive = GoogleDrive(g_auth)
        return drive
