import os
from functools import partial
  
root_directory = 'c:/__Canon Install'
  
list = ('01. Infos',
        '02. Install Files',
        '03. Backup/',
        '04. Tools/',
        '05. Customized Files')
  
concat_root_path = partial(os.path.join, root_directory)
make_directory = partial(os.makedirs, exist_ok=True)
  
for path_items in map(concat_root_path, list):
    make_directory(path_items)

outFileName="C:\\__Canon Install\README.txt"
outFile=open(outFileName, "w")
outFile.write("""Text""")
outFile.close()

