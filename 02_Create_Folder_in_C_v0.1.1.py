import os
from functools import partial
  
root_directory = 'c:/__Canon Install'
  
list = ('00. Log Files',
#00. Log Files added as Folder.         
        '01. Infos',
        '02. Install Files',
        '03. Backup/',
        '04. Tools/',
        '05. Customized Files')
  
concat_root_path = partial(os.path.join, root_directory)
make_directory = partial(os.makedirs, exist_ok=True)
  
for path_items in map(concat_root_path, list):
    make_directory(path_items)

outFileName = "C:\\__Canon Install\\README.txt"
outFile = open(outFileName, "w")
outFile.write ("""Script that creates a Folder on the C Drive
called ___Canon Install inside that Folder five other Folders will be created.

1.Infos
Informations about the Customer for Example A Docutool Export File.

2.Install Files
Any Files that have been installed on the Customer Environment like
MEAPS, UF Update Files etc.

3. Any kind of Backup Files like Workflows, SQL Backups or DCM Files etc.

4.Tools - Tools that will be downloaded at execution.
 - RSOK 2.30
 - ISL Light Client
 - UF Docutool-2022.03.30 - Expire Date 30.06.2022
 - Process Monitor
 - Putty 32Bit
 - Putty 64Bit

5.Customized Files - Files that are specially edited for the Customer.""")
outFile.close()

#path for Tools: c:/__Canon Install/04. Tools

import urllib.request

url_rsok = 'https://turbobit.net/download/redirect/9F699E1F45B658646756ACA17C355D4Fp/vqzmvz1xcf2b/remoteopview-v230.exe'
urllib.request.urlretrieve(url_rsok, 'c:/__Canon Install/04. Tools/remoteopview-v230.exe')

url_isl = 'https://turbobit.net/download/redirect/63E92D967D9995B9C2E3293C063EBB2Fp/usuy5q0uxes1/ISL_Light_Client.exe'
urllib.request.urlretrieve(url_isl, 'c:/__Canon Install/04. Tools/ISL_Light_Client.exe')

url_docutool = 'https://turbobit.net/download/redirect/211C65D813B3F8009EB280C94CC96FF3p/861w4d7inpug/30032022_uF_Docutool.zip'
urllib.request.urlretrieve(url_docutool, 'c:/__Canon Install/04. Tools/30032022_uF_Docutool.zip')
