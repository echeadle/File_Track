import unittest
import sqlite3
import os
from sqlite_db import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(':memory:')
        self.db.create_table('users', {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT', 'email': 'TEXT'})

    def tearDown(self):
        self.db.delete_table('users')
        self.db.close_connection()

    def test_add_record(self):
        self.db.add_record('users', {'name': 'Alice', 'email': 'alice@example.com'})
        record = self.db.show_record('users', "name='Alice'")
        self.assertEqual(('Alice', 'alice@example.com'), record[1:])

    def test_show_all_records(self):
        self.db.add_record('users', {'name': 'Alice', 'email': 'alice@example.com'})
        self.db.add_record('users', {'name': 'Bob', 'email': 'bob@example.com'})
        self.db.add_record('users', {'name': 'Charlie', 'email': 'charlie@example.com'})
        records = self.db.show_all_records('users')
        print(records)  # Debugging line
        self.assertTrue((1, 'Alice', 'alice@example.com') in records)
        self.assertTrue((2, 'Bob', 'bob@example.com') in records)

if __name__ == '__main__':
    unittest.main()

