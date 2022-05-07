import os
from functools import partial
  
root_directory = 'c:/__Canon Install'
  
list = ('01. Infos/sub_file_1',
        '02. Install Files/sub_file_2',
        '03. Backup/sub_file_3',
        '04. Tools/sub_file_4'
        '05. Customized Files/sub_file5')
  
concat_root_path = partial(os.path.join, root_directory)
make_directory = partial(os.makedirs, exist_ok=True)
  
for path_items in map(concat_root_path, list):
    make_directory(path_items)
    