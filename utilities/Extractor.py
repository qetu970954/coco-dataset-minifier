import random


class Extractor:
    """
    Extract some category and it's corresponding index

    :param filename: The file where the category names are stored.
    """
    def __init__(self, filename):
        self._content = dict()
        self.read_from(filename)

    def read_from(self, filename):
        self._content.clear()
        with open(filename, "r") as f:
            self._content = {index: line[:-1] for index, line in enumerate(f.readlines())}

    def extract(self, size: int):
        items = list(self._content.items())
        random.shuffle(items)

        # Return two sub dictionaries divided by the given size
        return dict(items[:size]), dict(items[size:])

    def extract_specific(self, specifics: list):
        # The dictionary, inverse_content, is the inverse version of self._content.
        # If the original dict is { 14: 'bird', 0: 'person'},
        # then the inverse version should be {'bird' : 14, 'person' : 0}
        inverse_content = {v: k for k, v in self._content.items()}
        all_possible_categories = self._content.values()

        extracted_result = {inverse_content[category]: category
                            for category in all_possible_categories if category in specifics}

        remain = {inverse_content[category]: category
                  for category in all_possible_categories if category not in specifics}

        return extracted_result, remain
