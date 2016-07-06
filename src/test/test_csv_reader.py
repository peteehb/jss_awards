from unittest import TestCase
from csv_reader import CsvReader


class TestCsvReader(TestCase):
    def test_create_csv_reader(self):
        csv_reader = CsvReader('test')
        self.assertIsNotNone(csv_reader)
        self.assertEqual('test', csv_reader.filename)

    def test_read_data_from_csv_reader(self):
        csv_reader = CsvReader('test/test.csv')
        data = csv_reader.read()
        self.assertEqual(data, [{'key_1': 'value_1', 'key_2': 'value_2'}])
