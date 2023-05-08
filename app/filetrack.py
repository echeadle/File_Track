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

import hash_module as hm
import sqlite_db as db
#import excel_rep as er

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

def setup_db(db_name, table, index, index_cols, columns):
    my_db = db.Database(db_name)
    my_db.create_table(table, columns)
    my_db.create_index(index, table, index_cols)
    return my_db


# --------------------------------------------------
def main():
    """File Track manin function"""

    
    args = get_args()
    str_arg = args.dir

    #print(f'str_arg = "{str_arg}"')
    folder = shlex.quote(str_arg)
    #print(is_file_or_dir(folder))

    # Move the following Variables to an ini file.
    db_name = 'my_db.db'
    table = 'file_hash'
    index = 'idx_hash'
    index_cols = 'file_hash'
    columns = columns = {'filename': 'TEXT', 'filepath': 'TEXT', 'filehash': 'TEXT'}
    mydb = setup_db(db_name, table, index, index_cols, columns)
          
    for root, subfolders, filenames in os.walk(folder):
        #print('The current folder is ' + folderName)
        subfolders[:] = [f for f in subfolders if not f in ['ansible_collections','node_modules','google-cloud-sdk', 'go', 'VirtualBox VMs','anaconda3','snap','env','venv','temp']]
        subfolders[:] = [f for f in subfolders if not f.startswith('.')]
        subfolders[:] = [f for f in subfolders if not f.startswith('__')]
        filenames[:] = [f for f in filenames if  not f.startswith('.') or not f.startswith('__')]
        #filenames[:] = [f for f in filenames if  not f.startswith('__')]

        #for subfolder in subfolders:
            #print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
            #filenames[:] = [f for f in filenames if  re.findSall('test', f, flags=re.IGNORECASE)]
            #pass
        for filename in filenames:
             #print('FILE INSIDE ' + folderName + ': '+ filename)
            full_file_path = shlex.quote(os.path.join(root, filename))
            #print(full_file_path)
            if os.path.isfile(full_file_path):
                filehash = hm.hash_file(full_file_path)
                record = {'filename':filename, 'filepath':full_file_path, 'filehash':filehash}
                check_record = mydb.show_duplicate_records(table, 'filehash', filehash)
                if len(check_record) == 0:
                        mydb.add_record(table, record)
                else:
                    for f_name, f_path, f_hash in check_record:
                        print(f"{f_name}\n{f_path}\n{f_hash}\n")
                
                #if  record_ck not in check_record:
                    #print(check_record)
            #print('-' * 70)
            #print(f'{full_file_path:70}\n{filename:25}\n{filehash:50}\n')
            
    #print('-' * 70)
            #print(folderName)
    all_records = mydb.show_all_records(table)
    for my_record in all_records:
        print(my_record[0], my_record[1], my_record[2])
        
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
