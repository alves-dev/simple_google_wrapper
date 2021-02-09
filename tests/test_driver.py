import unittest
from pydrive.drive import GoogleDrive
from driver.archive import ArchiveParameter
from driver.authentication import AuthenticationGoogle
from wrapper_google.driver import Driver


class DriverTest(unittest.TestCase):
    global list_archives, driver
    ap = ArchiveParameter(
        query="title contains 'Historico_tempo_' ")
    driver = Driver(ap)
    list_archives = driver.get_archives_list()

    def test_ArchiveParameter_not_query(self):
        ap = ArchiveParameter(title='title', mime_type='type')
        self.assertEqual(ap.query, "title contains 'title' and mimeType = 'type'")

    def test_ArchiveParameter_query(self):
        ap = ArchiveParameter(title='title', mime_type='type', query='test_query')
        self.assertEqual(ap.query, "test_query")

    def test_ArchiveParameter_only_query(self):
        ap = ArchiveParameter(query='test_query')
        self.assertEqual(ap.query, "test_query")

    def test_ArchiveParameter_exception(self):
        with self.assertRaises(Exception) as context:
            ArchiveParameter()
        self.assertTrue('Invalid parameters!' in str(context.exception))

    def test_AuthenticationGoogle(self):
        # TODO: Verificar a possibilidade de testar
        # self.assertIsInstance(GoogleDrive, (AuthenticationGoogle.get_drive()))
        pass

    def test_Driver_archives_list(self):
        global list_archives
        self.assertTrue(len(list_archives) > 0)

    def test_Driver_archive_download(self):
        global list_archives, driver
        archive = driver.get_archive_download('.', [dict(list_archives[1])])
        self.assertTrue(isinstance(archive, list))

    def test_Driver_archive_download_invalid_extension(self):
        global list_archives, driver
        archive = driver.get_archive_download('.', [dict(list_archives[0])])
        self.assertFalse(archive)
