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
        self.data = []

    def read(self):
        self.reader = DictReader(self.csv_file)
        for row in self.reader:
            if not all(v is '' for k,v in row.iteritems()):
                self.data.append(row)
        return self.data

