import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    
    def __del__(self):
        self.conn.close()

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE {table_name} ({','.join([f'{col} {data_type}' for col, data_type in columns.items()])})"
        self.cursor.execute(query)
        self.conn.commit()

    def delete_table(self, table_name):
        query = f"DROP TABLE IF EXISTS {table_name}"
        self.cursor.execute(query)
        self.conn.commit()

    def add_record(self, table_name, values):
        query = f"INSERT INTO {table_name} ({','.join(values.keys())}) VALUES ({','.join(['?' for i in range(len(values))])})"
        self.cursor.execute(query, tuple(values.values()))
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

