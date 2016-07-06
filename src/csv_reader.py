from csv import DictReader
import utils


class CsvReader(object):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        data = []
        with open(utils.current_path(self.filename), 'rb') as f:
            reader = DictReader(f)
            for row in reader:
                if not all(v is '' for k, v in row.iteritems()):
                    data.append(row)
        return data

