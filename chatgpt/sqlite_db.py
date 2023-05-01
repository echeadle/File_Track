import sqlite3
import os

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{k} {v}' for k, v in columns.items()])})"
        self.cursor.execute(query)
        self.conn.commit()

    def delete_table(self, table_name):
        query = f"DROP TABLE IF EXISTS {table_name}"
        self.cursor.execute(query)
        self.conn.commit()

    def add_record(self, table_name, record):
        query = f"INSERT INTO {table_name} ({', '.join(record.keys())}) VALUES ({', '.join(['?' for _ in record.values()])})"
        self.cursor.execute(query, list(record.values()))
        self.conn.commit()

    def delete_record(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        self.conn.commit()

    def show_all_records(self, table_name):
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def show_record(self, table_name, condition):
        query = f"SELECT * FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        return self.cursor.fetchone()

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
