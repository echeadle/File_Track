#!/usr/bin/env python3
"""
Author : echeadle <echeadle@localhost>
Date   : 2023-05-01
Purpose: File Tracker
"""

import argparse
import os
import re
import shlex

import hash_module

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='File Tracker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('-d',
                        '--dir',
                        help='Directory/folder to scan',
                        metavar='str',
                        type=str,
                        default='/home/echeadle/Ansible')


    return parser.parse_args()

def is_file_or_dir(path):
    if os.path.isfile(path):
        return 'file'
    elif os.path.isdir(path):
        return 'directory'
    else:
        return False

# --------------------------------------------------
def main():
    """File Track manin function"""

    args = get_args()
    str_arg = args.dir

    print(f'str_arg = "{str_arg}"')
    folder = shlex.quote(str_arg)
    print(is_file_or_dir(folder))

    for folderName, subfolders, filenames in os.walk(folder):
        #print('The current folder is ' + folderName)
        subfolders[:] = [f for f in subfolders if not f in ['ansible_collections','node_modules','google-cloud-sdk', 'go', 'VirtualBox VMs','anaconda3','snap','env','venv','temp']]
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
            full_file_path = os.path.join(shlex.quote(folderName), shlex.quote(filename))
            if os.path.isfile(full_file_path):
                filehash = hash_module.hash_file(full_file_path)
                print(f'"{folderName}"  ,  "{filename}"  ,  "{filehash}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
