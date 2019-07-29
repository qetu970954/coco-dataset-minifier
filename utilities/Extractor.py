import random


class Extractor:
    def __init__(self, filename):
        self._content = dict()
        self.read_from(filename)

    def read_from(self, filename):
        self._content.clear()
        with open(filename, "r") as f:
            self._content = {index: line[:-1] for index, line in enumerate(f.readlines())}

    def extract(self, size):
        items = list(self._content.items())
        random.shuffle(items)
        return dict(items[:size]), dict(items[size:])
