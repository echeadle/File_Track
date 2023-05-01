import hashlib
import os
import re

for folderName, subfolders, filenames in os.walk('/home/echeadle'):
    #print('The current folder is ' + folderName)
    subfolders[:] = [f for f in subfolders if not f in ['VirtualBox VMs','anaconda3','snap','venv','temp']]
    subfolders[:] = [f for f in subfolders if not f.startswith('.')]
    subfolders[:] = [f for f in subfolders if not f.startswith('__')]
    
    for subfolder in subfolders:
        #print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        pass
    filenames[:] = [f for f in filenames if  not f.startswith('.')]
    filenames[:] = [f for f in filenames if  not f.startswith('__')]
    #filenames[:] = [f for f in filenames if  re.findSall('test', f, flags=re.IGNORECASE)]
    for filename in filenames:
        #print('FILE INSIDE ' + folderName + ': '+ filename)
        full_file_path = os.path.join(folderName, f'"{filename}"')      
        the_hash = hashlib.sha256()   
        if os.path.isfile(full_file_path):
            with open(full_file_path, 'rb') as fn:
                for line in fn.readlines():
                    the_hash.update(line)
            fn.close()
            print(f'"{folderName}","{filename}","{the_hash.hexdigest()}"')

