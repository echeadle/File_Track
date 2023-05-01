# Unit test file
import unittest
from sqlite_db import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(':memory:')
        self.db.create_table('users', {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT', 'email': 'TEXT'})
        self.db.add_record('users', {'name': 'Alice', 'email': 'alice@example.com'})
        self.db.add_record('users', {'name': 'Bob', 'email': 'bob@example.com'})

    def tearDown(self):
        self.db.delete_table('users')

    def test_create_table(self):
        self.db.create_table('test_table', {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT'})
        self.assertIn(('test_table',), self.db.show_all_tables())

    def test_delete_table(self):
        self.db.delete_table('users')
        tables = [table[0] for table in self.db.show_all_tables()]
        self.assertNotIn('users', tables)

    #def test_delete_table(self):
    #    self.db.delete_table('users')
    #    self.assertNotIn(('users',), self.db.show_all_tables())

    def test_add_record(self):
        self.db.add_record('users', {'name': 'Charlie', 'email': 'charlie@example.com'})
        self.assertEqual(self.db.show_record('users', "name='Charlie'"), (3, 'Charlie', 'charlie@example.com'))

    def test_delete_record(self):
        self.db.delete_record('users', "name='Bob'")
        self.assertIsNone(self.db.show_record('users', "name='Bob'"))

    def test_show_all_records(self):
        self.assertEqual(self.db.show_all_records('users'), [(1, 'Alice', 'alice@example.com'), (2, 'Bob', 'bob@example.com')])

    def test_show_record(self):
        self.assertEqual(self.db.show_record('users', "name='Bob'"), (2, 'Bob', 'bob@example.com'))

if __name__ == '__main__':
    unittest.main()

