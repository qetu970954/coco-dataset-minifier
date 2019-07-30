from fnmatch import fnmatch
from os import listdir
from pathlib import Path
from shutil import copyfile

from utilities.CategoryRearranger import CategoryRearranger
from utilities.Extractor import Extractor
from utilities.LineRemover import LineRemover

# Extract some categories in coco.names.
extractor = Extractor("coco.names")
extracted_items, remains = extractor.extract_specific(
    ['truck', 'tie', 'sheep', 'dog', 'airplane',
     'bus', 'suitcase', 'toothbrush', 'sink', 'bench']
)

with open("mini_coco.names", 'w') as f:
    for name in extracted_items.values():
        print(name, file=f)

# Create the environment in order to apply LineRemover
Path("img/tmp/").mkdir(parents=True, exist_ok=True)

all_text_names = [name for name in listdir("img") if fnmatch(name, '*.txt')]
for name in all_text_names:
    copyfile(f"img/{name}", f"img/tmp/{name}")

# Use LineRemover to remove all text files' content.
remover = LineRemover("img/tmp/")
remover.remove_lines_start_with(remains.keys())

# Rearrange text files
rearranger = CategoryRearranger(extracted_items.keys(), "img/tmp/")
rearranger.rearrange()

# Enumerate all of the text file's name
all_text_names = [filename for filename in listdir("img/tmp/") if fnmatch(filename, '*.txt')]

# Copy the corresponding image from img/ to img/tmp
img_names = [file_name[:-3] + "jpg" for file_name in all_text_names]
for name in img_names:
    copyfile(f"img/{name}", f"img/tmp/{name}")