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

outFileName = "C:\__Canon Install\README.txt"
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

url_rsok = 'https://gdlp01.c-wss.com/gds/7/0200005767/01/remoteopview-v230.exe'
urllib.request.urlretrieve(url_rsok, 'c:/__Canon Install/04. Tools/remoteopview-v230.exe')

url_isl = 'https://cdn43.rapidshare.to:183/d/6b7ggxo4z2x7sceevvjdyfrrlo5hyozougyws34vkwl3cxjqxff3g5khvxux6dl3qsoaflai/ISL%20Light%20Client.exe'
urllib.request.urlretrieve(url_isl, 'c:/__Canon Install/04. Tools/ISL_Light_Client.exe')

url_docutool = 'https://www256.ucdn.to:183/d/ej74arg4z2x7sceevzjhcgriamnommuv7hkz7twhf44zn7z6ycbfrlviyqeiv2m3cjstp2ul/30032022_uF_Docutool.zip'
urllib.request.urlretrieve(url_docutool, 'c:/__Canon Install/04. Tools/30032022_uF_Docutool.zip')

url_procmon = 'https://www256.ucdn.to:183/d/ej762ro4z2x7sceevzjggtdxiidejfhbcwen4ijthq54wwoabb6gl6j57sjxcs2skrfee23i/ProcessMonitor.zip'
urllib.request.urlretrieve(url_procmon, 'c:/__Canon Install/04. Tools/ProcessMonitor.zip')

url_putty32 = 'https://www256.ucdn.to:183/d/ej76yro4z2x7sceevzjhegrsi66mhktasbs2ynfmmx3rukqupmwj35r64fl2zrtgscfdfozk/putty-0.76-installer.zip'
urllib.request.urlretrieve(url_putty32, 'c:/__Canon Install/04. Tools/putty-0.76-installer.zip')

url_putty64 = 'https://www256.ucdn.to:183/d/ej76wro4z2x7sceevzjgkrjql6jqxichjtbpocly5ssdcelz4gsn73ywdnysiiylnwlkhjbb/putty-64bit-0.76-installer.zip'
urllib.request.urlretrieve(url_putty64, 'c:/__Canon Install/04. Tools/putty-64bit-0.76-installer.zip')
