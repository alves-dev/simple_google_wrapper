from typing import Union, List
from driver.archive import ArchiveParameter
from driver.authentication import AuthenticationGoogle
import logging


class Driver:
    def __init__(self, archive_parameter: ArchiveParameter):
        self.archive_parameter = archive_parameter
        self.drive_authenticated = AuthenticationGoogle.get_drive()

    def get_archive_download(self, directory_save: str, list_files_download: List[dict], extension: str = None) -> \
            Union[bool, List[str]]:
        """
        It will download the files from the past list and save them, in the given directory.

        :param directory_save:
        :param list_files_download:
        :param extension: for archives
        :return: list archives downloaded
        """
        list_downloaded = []
        mimetype = None
        for file in list_files_download:
            file = dict(file)
            try:
                file_d = self.drive_authenticated.CreateFile({'id': file['id']})
                if extension is None:
                    if file['mimeType'] == 'application/vnd.google-apps.spreadsheet':
                        extension = 'csv'
                        mimetype = 'text/csv'
                if extension is None:
                    raise ValueError('Invalid extension!')

                directory = directory_save + str(file['title']) + '.' + extension
                file_d.GetContentFile(directory, mimetype)
                list_downloaded.append(directory)
                logging.info(f'{str(file["title"])} downloaded!')
            except Exception as error:
                logging.error(error)
        return list_downloaded

    def get_archives_list(self) -> list:
        try:
            return self.drive_authenticated.ListFile({'q': self.archive_parameter.query, 'orderBy': 'title'}).GetList()
        except Exception as error:
            logging.error(error)
            return []

    def load(self):
        ...
