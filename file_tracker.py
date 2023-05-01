#!/usr/bin/env python3
"""
Author: ChatGPT
Date: 2023-04-30
Purpose: A program that tracks files and their SHA256 hash
"""

import argparse
import os
import hashlib
from datetime import datetime
from sqlite_db import Database

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='A program that tracks files and their SHA256 hash',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('path',
                        metavar='path',
                        help='File or directory path')

    parser.add_argument('-d',
                        '--db',
                        help='Database file',
                        metavar='FILE',
                        type=str,
                        default='file_tracker.db')

    return parser.parse_args()

# --------------------------------------------------
def create_database(database_file):
    """Create the database table"""
    db = Database(database_file)
    db.create_table('files', {
        'id': 'INTEGER PRIMARY KEY',
        'name': 'TEXT',
        'path': 'TEXT',
        'sha256': 'TEXT',
        'created_at': 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'})
    db.close_connection()

# --------------------------------------------------
def hash_file(file_path):
    """Calculate the SHA256 hash of the given file"""
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(8192)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

# --------------------------------------------------
def add_file_to_database(database_file, file_path):
    """Add the file to the database"""
    db = Database(database_file)
    sha256 = hash_file(file_path)
    file_name = os.path.basename(file_path)
    file_dir = os.path.dirname(os.path.abspath(file_path))
    db.add_record('files', {'name': file_name, 'path': file_dir, 'sha256': sha256})
    db.close_connection()

# --------------------------------------------------
def find_duplicate_files(database_file, file_path):
    """Find all files with the same SHA256 hash"""
    db = Database(database_file)
    sha256 = hash_file(file_path)
    results = db.show_all_records('files')
    duplicates = [result for result in results if result[3] == sha256]
    db.close_connection()
    return duplicates

# --------------------------------------------------
def main():
    """The main program"""
    args = get_args()
    database_file = args.db

    if not os.path.isfile(database_file):
        create_database(database_file)

    if os.path.isdir(args.path):
        # Search for all files in the directory and its subdirectories
        for root, dirs, files in os.walk(args.path):
            for file in files:
                file_path = os.path.join(root, file)
                add_file_to_database(database_file, file_path)
    elif os.path.isfile(args.path):
        add_file_to_database(database_file, args.path)

    duplicates = find_duplicate_files(database_file, args.path)
    if len(duplicates) > 1:
        print('Duplicate files:')
        for duplicate in duplicates:
            print(f'  {duplicate[1]} ({duplicate[2]})')
    else:
        print('No duplicate files found')

# --------------------------------------------------
if __name__ == '__main__':
    main()

