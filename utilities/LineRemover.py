import fnmatch
import os
import pathlib


class LineRemover:
    def __init__(self, remove_path):
        self.result = list()
        self.path = remove_path

    def remove_lines_start_with(self, start_with: list):
        """
        Remove lines in the text files start with ${start_with}.

        e.g.
        Suppose the file, A.txt, has contents:
             1 3 34 2 1
             3 42 2 5 45
             4 1 3 4 2
             >>EOF

        After invoking this command with [1,4], there will be two separated text files, A.txt and rm/A.txt.
        A.txt remains the same, but rm/A.txt is:
             3 42 2 5 45
             >>EOF

        Note: This function creates rm/ directory and store the results into it.
        :return Number of lines being removed.
        """
        pathlib.Path(self.path + r"/rm").mkdir(parents=True, exist_ok=True)

        num_removed_lines = 0

        for filename in os.listdir(self.path):
            if fnmatch.fnmatch(filename, '*.txt'):
                with open(os.path.join(self.path, filename), 'r') as src:
                    destination_content = str()
                    for line in src.readlines():
                        if int(line.split()[0]) in start_with:
                            num_removed_lines += 1
                            continue
                        destination_content += line
                if destination_content:
                    with open(os.path.join(self.path + r"\rm", f"{filename}"), 'w') as dest:
                        dest.write(destination_content)

        return num_removed_lines
