from fnmatch import fnmatch
from os import listdir, path


class CategoryRearranger:
    """
    Update all outdated category inside a directory.

    :param old_ids: Old category ids going to update.
    :param where: The location to apply the update.
    """

    def __init__(self, old_ids: list, where: str):
        self.foundation = {i: j for i, j in zip(old_ids, range(len(old_ids)))}
        self.rearrange_location = where

    def rearrange(self):
        total_updated_lines = 0
        for filename in listdir(self.rearrange_location):
            if fnmatch(filename, '*.txt'):
                with open(path.join(self.rearrange_location, f"{filename}"), 'r') as src:
                    new_contents, num_updated_lines = self._perform_rearrangement(src)

                with open(path.join(self.rearrange_location, f"{filename}"), 'w') as dest:
                    for line in new_contents:
                        print(line, file=dest)

                total_updated_lines += num_updated_lines

        return total_updated_lines

    def _perform_rearrangement(self, src):
        result = list()
        num_update_lines = 0

        for line in src.readlines():
            split_line = line.split()

            if int(split_line[0]) in self.foundation.keys():
                num_update_lines += 1
                split_line[0] = str(self.foundation[int(split_line[0])])

            result.append(' '.join(split_line))
        return result, num_update_lines
