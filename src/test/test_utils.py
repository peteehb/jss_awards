from unittest import TestCase
import utils


class TestUtils(TestCase):
    def test_generate_timestamp(self):
        timestamp = utils.timestamp()
        self.assertIs(str, timestamp)

