import unittest
from driver.archive import ArchiveParameter
from driver.authentication import AuthenticationGoogle


class DriverTest(unittest.TestCase):
    def test_ArchiveParameter_not_query(self):
        ap = ArchiveParameter(directory_save='/home', title='title', mime_type='type')
        self.assertEqual(ap.query, "title contains 'title' and mimeType = 'type'")

    def test_ArchiveParameter_query(self):
        ap = ArchiveParameter(directory_save='/home', title='title', mime_type='type', query='test_query')
        self.assertEqual(ap.query, "test_query")

    def test_ArchiveParameter_only_query(self):
        ap = ArchiveParameter(directory_save='/home', query='test_query')
        self.assertEqual(ap.query, "test_query")

    def test_ArchiveParameter_exepition(self):
        with self.assertRaises(Exception) as context:
            ArchiveParameter(directory_save='/home')
        self.assertTrue('Invalid parameters!' in str(context.exception))

    def test_AuthenticationGoogle(self):
        # todo: testar
        self.assertTrue(AuthenticationGoogle.get_drive())
