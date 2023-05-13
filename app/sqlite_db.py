import sqlite3
import os
import shlex
class Database():

    def __init__(self, db_file):
        """Connect to the SQLite DB"""
        try:
            self.conn = sqlite3.connect(db_file)
            self.cursor = self.conn.cursor()
        except BaseException as err:
            #print(str(err))
            self.conn = None
            self.cursor = None

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{k} {v}' for k, v in columns.items()])})"
        self.cursor.execute(query)
        self.conn.commit()

    def create_index(self, index_name, table_name, column_list):
        #query = f"CREATE INDEX IF NOT EXISTS {index_name} ON {table_name} ({column_list})"
        query = f"CREATE INDEX IF NOT EXISTS idx_hash ON file_hash(filepath, filehash)"
        self.cursor.execute(query)
        self.conn.commit()

    def delete_table(self, table_name):
        query = f"DROP TABLE IF EXISTS {table_name}"
        self.cursor.execute(query)
        self.conn.commit()

    def add_record(self, table_name, record):
        query = f"INSERT INTO {table_name} ({', '.join(record.keys())}) VALUES ({', '.join(['?' for _ in record.values()])})"
        #print(query)
        self.cursor.execute(query, list(record.values()))
        self.conn.commit()

    def delete_record(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        self.conn.commit()

    def run_query(self, query):
        #print(query)
        self.cursor.execute(query, args)
        return self.cursor.fetchall()
    
    def show_all_records(self, table_name):
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def show_record(self, table_name, filepath):
        file_path = (filepath)
        #query = f"SELECT * FROM {table_name} WHERE {condition}"
        #print(f"SELECT filename,filepath, filehash, timestamp  FROM {table_name}  WHERE filepath = '{file_path}'")
        query = f'SELECT filename,filepath, filehash, timestamp  FROM {table_name}  WHERE filepath = "{file_path}"'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_record(self, table, filepath, filehash): 
        """Update the SQLite File Table"""
        file_path = filepath
        #print(f"file path: {file_path}")
        query = f"UPDATE {table}  SET filehash = '{filehash}' WHERE filepath = '{file_path}'"
        self.cursor.execute(query)
        return self.cursor.fetchall()


    def is_rec_modifed(filepath,filehash,timestamp):
        """Check record for any changes
           Returning false until function is completed"""
        return False

            
    def show_duplicate_records(self, table_name, index_name, value):
        query = f"SELECT filename, filepath, filehash FROM {table_name} WHERE {index_name} = '{value}'"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def show_all_tables(self):
        query = "SELECT name FROM sqlite_master WHERE type='table'"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()

if __name__ == '__main__':
    db = Database('test.db')
    db.create_table('users', {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT', 'email': 'TEXT'})
    db.add_record('users', {'name': 'Alice', 'email': 'alice@example.com'})
    db.add_record('users', {'name': 'Bob', 'email': 'bob@example.com'})
    db.add_record('users', {'name': 'Charlie', 'email': 'charlie@example.com'})
    print(db.show_all_records('users'))
    print(db.show_record('users', "name='Alice'"))
    db.delete_record('users', "name='Bob'")
    print(db.show_all_records('users'))
    db.delete_table('users')
    db.close_connection()
    os.remove('test.db')
