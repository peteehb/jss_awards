import os
from unittest import TestCase
import utils


class TestUtils(TestCase):
    def test_generate_timestamp(self):
        timestamp = utils.timestamp()
        self.assertIsInstance(str, timestamp)

    def test_load_cfg(self):
        config = utils.load_cfg('test/conf.cfg')
        self.assertIsNotNone(config)

    def test_create_folder(self):
        folder_path = utils.create_folder('test/test_folder')
        expected_folder_path = str(os.getcwd()) + '/test/test_folder'
        self.assertEquals(folder_path, expected_folder_path)

    def test_zip_output(self):
        pass

    def test_clean_up(self):
        pass
