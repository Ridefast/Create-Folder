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
outFile.write("""Script that creates a Folder on the C Drive
called ___Canon Install inside that Folder five other Folders will be created.

1.Infos
Informations about the Customer for Example A Docutool Export File.

2.Install Files
Any Files that have been installed on the Customer Environment like
MEAPS, UF Update Files etc.

3. Any kind of Backup Files like Workflows, SQL Backups or DCM Files etc.

4.Tools - Tools like RSOK or UFTools etc.

5.Customized Files - Files that are specially edited for the Customer.""")
outFile.close()

