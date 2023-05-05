import os
import sqlite3
import unittest
from unittest.mock import Mock, patch
from sqlite_db import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(':memory:')
        self.db.create_table('users', {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT', 'email': 'TEXT'})
        self.db.add_record('users', {'name': 'Alice', 'email': 'alice@example.com'})
        self.db.add_record('users', {'name': 'Bob', 'email': 'bob@example.com'})
        self.db.add_record('users', {'name': 'Charlie', 'email': 'charlie@example.com'})

    def tearDown(self):
        self.db.delete_table('users')
        self.db.close_connection()

    def test_create_table(self):
        self.assertTrue('users' in [row[0] for row in self.db.show_all_tables()])

    def test_add_record(self):
        self.db.add_record('users', {'name': 'David', 'email': 'david@example.com'})
        self.assertEqual(len(self.db.show_all_records('users')), 4)

    def test_delete_record(self):
        self.db.delete_record('users', "name='Bob'")
        self.assertEqual(len(self.db.show_all_records('users')), 2)

    def test_show_record(self):
        record = self.db.show_record('users', "name='Alice'")
        self.assertEqual(record[1], 'Alice')
        self.assertEqual(record[2], 'alice@example.com')

    def test_show_all_records(self):
        records = self.db.show_all_records('users')
        self.assertEqual(len(records), 3)
        self.assertTrue((1, 'Alice', 'alice@example.com') in records)
        self.assertTrue((2, 'Bob', 'bob@example.com') in records)
        self.assertTrue((3, 'Charlie', 'charlie@example.com') in records)

    def test_delete_table(self):
        self.db.delete_table('users')
        self.assertEqual(len(self.db.show_all_tables()), 0)

    def test_create_index(self):
        mock_cursor = Mock()
        mock_conn = Mock()
        mock_conn.cursor.return_value = mock_cursor

        with patch.object(sqlite3, 'connect', return_value=mock_conn):
            db = Database('test.db')
            db.create_index('users', 'name')
            mock_cursor.execute.assert_called_with("CREATE INDEX idx_hash ON table_name (hash_name)")

if __name__ == '__main__':
    unittest.main()

