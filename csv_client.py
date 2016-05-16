from csv import DictReader
import ConfigParser
import os


def current_path(filename):
    return os.getcwd() + '/' + filename


def load_cfg(config_file):
    config = ConfigParser.ConfigParser()
    config.readfp(open(current_path(config_file)))
    return config


class CsvClient(object):
    def __init__(self, filename):
        self.csv_file = open(current_path(filename), 'rb')

    def read(self):
        self.reader = DictReader(self.csv_file)
        data = []
        for row in self.reader:
            data.append(row)
        return data
