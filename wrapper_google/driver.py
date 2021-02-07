from driver.archive import ArchiveParameter
from driver.authentication import AuthenticationGoogle


class Driver:
    def __init__(self):
        AuthenticationGoogle.get_drive()

    def get(self):
        ...

    def load(self):
        ...
