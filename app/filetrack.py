#!/usr/bin/env python3
"""
Author : echeadle <echeadle@localhost>
Date   : 2023-05-08
Purpose: File Tracker
"""

import argparse
import os
import re
import shlex
import datetime
import socket

import hash_module as hm
import sqlite_db as db

from openpyxl import Workbook
from openpyxl.styles import Font

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
                        default='/home/echeadle/TESTFILECHECK')
        
    parser.add_argument('-u',
                        '--update',
                        help='A boolean flag',
                        action='store_true')

    parser.add_argument('-p',
                        '--dup',
                        help='A boolean flag',
                        action='store_false')


    return parser.parse_args()

def get_hostname():
    return socket.gethostname()

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

def getmoddate(fname):
    """Get file modified date"""
    try:
        m_time = os.path.getmtime(fname)
    except OSError as emsg:
        print(str(emsg))
        m_time = 0
    return datetime.datetime.fromtimestamp(m_time)

def print_all_records(db, table):
    all_records = db.show_all_records(table)
    for my_record in all_records:
        print(my_record[:])

def file_walk(folder):
    for root, subfolders, filenames in os.walk(folder):
        #print('The current folder is ' + folderName) 
        subfolders[:] = [f for f in subfolders if not f in ['ansible_collections','node_modules','google-cloud-sdk', 'go', 'VirtualBox VMs','anaconda3','snap','env','venv','temp']]
        subfolders[:] = [f for f in subfolders if not f.startswith('.')]
        subfolders[:] = [f for f in subfolders if not f.startswith('__')] 
        filenames[:] = [f for f in filenames if not f.startswith('.')]
        filenames[:] = [f for f in filenames if not f.startswith('__')]

        for filename in filenames:
            yield root, filename

def create_record(filepath, filename):
    full_file_path = os.path.join(filepath, filename)
#    print(full_file_path)
    filehash = hm.hash_file(full_file_path)
    tstamp = getmoddate(full_file_path)
    record = {'filename':filename,
              'filepath':full_file_path,
              'filehash':filehash,
              'timestamp':tstamp}
    return record

# --------------------------------------------------
def main():
    """File Track manin function"""

    
    args = get_args()
    str_arg = args.dir

    #print(f'str_arg = "{str_arg}"')
    folder = shlex.quote(str_arg)
    #print(is_file_or_dir(folder))

    # Move the following Variables to an ini file.
    update_files = True
    find_duplicates = True
    db_name = 'my_db.db'
    table = 'file_hash'
    index = 'idx_hash'
    index_cols = 'file_hash'
    columns = columns = {'filename': 'TEXT', 'filepath': 'TEXT', 'filehash': 'TEXT', 'timestamp': 'TEXT'}
    mydb = setup_db(db_name, table, index, index_cols, columns)
    # get hostname
    host_name = get_hostname()
    
    used_hash = []
    for root, filename in file_walk(folder):
        record = create_record(root, filename)
        db_record = mydb.show_record(table,record['filepath'])
        #print(f"Before: Record {record['filehash']} DB {db_record[0][2]}")
        if len(db_record) == 0:
            mydb.add_record(table, record)
        else:
            if update_files:
                update_file = record['filepath']
                new_hash = record['filehash']
                cur_hash = db_record[0][2]
                if new_hash != cur_hash:
                    #print(update_file)
                    #print(f"Before: Record {record['filehash']} DB {db_record[0][2]}") 
                    mydb.update_record(table, update_file, new_hash)
                    #print(f"After: Record {record['filehash'] } DB {db_record[0][2]}")

            if find_duplicates:
                cur_hash = record['filehash']
                dup_records = mydb.show_duplicate_records(table, 'filehash', 
                                                      cur_hash)
                
                if len(dup_records) > 1 and cur_hash not in used_hash :
                    used_hash.append(cur_hash)
                    #print(f"Used Hash: {used_hash}\nCurrent hash:{cur_hash}\n")
                #org_filepath = record['filepath']
                #print( '-' * 50)
                    for filename, filepath, filehash in dup_records:
                        print(filename, filepath, filehash)
                #print('-' * 50)
    all_records = mydb.show_all_records(table)
    for filename, filepath, filehash, tstamp in all_records:
        print( '-' * 50)
        print(f"{filename}\n{filepath}\n{filehash}\n{tstamp}\n")
        print( '-' * 50)
# --------------------------------------------------
if __name__ == '__main__':
    main()
