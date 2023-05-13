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
    columns = columns = {'filename': 'TEXT', 'filepath': 'TEXT', 'filehash': 'TEXT', 'timestamp': 'TEXT'}
    mydb = setup_db(db_name, table, index, index_cols, columns)
    # get hostname
    host_name = get_hostname()
    print(f'Host Name: {host_name}')
    for root, subfolders, filenames in os.walk(folder):
        #print('The current folder is ' + folderName)
        subfolders[:] = [f for f in subfolders if not f in ['ansible_collections','node_modules','google-cloud-sdk', 'go', 'VirtualBox VMs','anaconda3','snap','env','venv','temp']]
        subfolders[:] = [f for f in subfolders if not f.startswith('.')]
        subfolders[:] = [f for f in subfolders if not f.startswith('__')]
        filenames[:] = [f for f in filenames if  not f.startswith('.') or not f.startswith('__')]
        for filename in filenames:
            full_file_path = shlex.quote(os.path.join(root, filename))
            filehash = hm.hash_file(full_file_path)
            tstamp = getmoddate(full_file_path)
            record = {'filename':filename,
                      'filepath':full_file_path,
                      'filehash':filehash,
                      'timestamp':tstamp}
            dup_records = mydb.show_duplicate_records(table, 'filehash', filehash)
            if len(dup_records) == 0:
                mydb.add_record(table, record)
            else:
                cur_record = mydb.show_record(table,full_file_path)
                print(cur_record)
                


        #print(dup_records)
# --------------------------------------------------
if __name__ == '__main__':
    main()
