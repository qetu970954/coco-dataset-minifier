import fnmatch
import os

class LineRemover:
    def __init__(self, remove_path):
        self.result = list()
        self.remove_path = remove_path

    def remove_lines_start_with(self, start_with: list):
        """
        Remove lines in the text files start with ${start_with}.

        e.g.
        Suppose the file, A.txt, has contents:
             1 3 34 2 1
             3 42 2 5 45
             4 1 3 4 2
             >>EOF

        After invoke this function :
        >>> self.remove_lines_start_with([1,4])
        A.txt becomes:
             3 42 2 5 45
             >>EOF
        Line 1 and Line 3 are removed.

        Note: If there is no remaining content in the file, this file will be removed.

        :return Number of lines being removed.
        """
        num_removed_lines = 0

        for filename in os.listdir(self.remove_path):
            if fnmatch.fnmatch(filename, '*.txt'):
                with open(os.path.join(self.remove_path, filename), 'r') as src:
                    destination_content = str()
                    for line in src.readlines():
                        if int(line.split()[0]) in start_with:
                            num_removed_lines += 1
                            continue
                        destination_content += line

                if destination_content:
                    with open(os.path.join(self.remove_path, filename), 'w') as dest:
                        dest.write(destination_content)
                else:
                    os.remove(os.path.join(self.remove_path, filename))

        return num_removed_lines
