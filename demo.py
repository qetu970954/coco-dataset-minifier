import fnmatch
import os
from shutil import copyfile

import utilities.Extractor as extractor
import utilities.LineRemover as remover

extractor = extractor.Extractor()
extractor.read_from("coco.names")
extracted_item, remains = extractor.extract(70)

with open("mini_coco.names", 'w') as f:
    for name in remains.values():
        print(name, file=f)

new_dict = {idx: value for idx, value in enumerate(remains.values())}


remover = remover.LineRemover("img/")
remover.remove_lines_start_with(extracted_item.keys())

TEXT_FILE_NAMES = [filename for filename in os.listdir("img/rm") if fnmatch.fnmatch(filename, '*.txt')]
for name in TEXT_FILE_NAMES:
    IMG_NAME = name[:-3] + "jpg"
    copyfile(f"img/{IMG_NAME}", f"img/rm/{IMG_NAME}")
