import argparse
import database
import hash_module

# File Checker v2.0

def main():
    parser = argparse.ArgumentParser(description='File check and database insertion')
    parser.add_argument('filename', nargs='?', help='file to check')
    parser.add_argument('--db-type', dest='db_type', default='sqlite3', help='database type')
    parser.add_argument('--db-name', dest='db_name', default='filecheck.db', help='database name')
    parser.add_argument('--table-name', dest='table_name', default='file_hashes', help='table name')
    parser.add_argument('--hash-type', dest='hash_type', default='sha256', help='hash type')
    parser.add_argument('--list', dest='list_files', action='store_true', help='list all files in database')
    args = parser.parse_args()

    db = database.SQLiteDB(args.db_name)
    db.create_table(args.table_name, 'id INTEGER PRIMARY KEY, filename TEXT, hash TEXT, hash_type TEXT')

    if args.list_files:
        rows = db.select_all(args.table_name)
        if not rows:
            print(f"No files found in database {args.db_name}, table {args.table_name}")
        else:
            print("List of all files in database:")
            for row in rows:
                print(row[1])
    else:
        if not args.filename:
            print("Please specify a file to check or use --list to list all files in database.")
            return

        file_hash = hash_module.hash_file(args.filename, args.hash_type)
        db.insert_data(args.table_name, ['filename', 'hash', 'hash_type'], [args.filename, file_hash, args.hash_type])
        print(f'File {args.filename} added to database {args.db_name}, table {args.table_name}')

if __name__ == "__main__":
    main()

