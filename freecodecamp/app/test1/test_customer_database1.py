import os
import sqlite3
import unittest
from customer_database import CustomerDatabase

class TestCustomerDatabase(unittest.TestCase):
    """Tests for the CustomerDatabase class"""

    def setUp(self):
        self.database_path = 'test_customer.db'
        self.db = CustomerDatabase(self.database_path)
        self.db.add_many([('John', 'Doe', 'john@example.com'),
                          ('Mary', 'Smith', 'mary@example.com')])

    def tearDown(self):
        os.remove(self.database_path)

    def test_show_all(self):
        """Test show_all() method"""
        expected_output = [(1, 'John', 'Doe', 'john@example.com'),
                           (2, 'Mary', 'Smith', 'mary@example.com')]

        with self.assertRaises(SystemExit) as cm:
            self.db.show_all()

        output = cm.exception.code
        self.assertEqual(output, None)

        with sqlite3.connect(self.database_path) as conn:
            c = conn.cursor()
            c.execute("SELECT rowid, *  FROM customers")
            items = c.fetchall()
            self.assertEqual(items, expected_output)

    def test_add_one(self):
        """Test add_one() method"""
        self.db.add_one('Jane', 'Doe', 'jane@example.com')
        expected_output = [(1, 'John', 'Doe', 'john@example.com'),
                           (2, 'Mary', 'Smith', 'mary@example.com'),
                           (3, 'Jane', 'Doe', 'jane@example.com')]

        with sqlite3.connect(self.database_path) as conn:
            c = conn.cursor()
            c.execute("SELECT rowid, *  FROM customers")
            items = c.fetchall()
            self.assertEqual(items, expected_output)

    def test_add_many(self):
        """Test add_many() method"""
        self.db.add_many([('Bob', 'Johnson', 'bob@example.com'),
                          ('Alice', 'Williams', 'alice@example.com')])
        expected_output = [(1, 'John', 'Doe', 'john@example.com'),
                           (2, 'Mary', 'Smith', 'mary@example.com'),
                           (3, 'Bob', 'Johnson', 'bob@example.com'),
                           (4, 'Alice', 'Williams', 'alice@example.com')]

        with sqlite3.connect(self.database_path) as conn:
            c = conn.cursor()
            c.execute("SELECT rowid, *  FROM customers")
            items = c.fetchall()
            self.assertEqual(items, expected_output)

    def test_delete_one(self):
        """Test delete_one() method"""
        self.db.delete_one(1)
        expected_output = [(2, 'Mary', 'Smith', 'mary@example.com')]

        with sqlite3.connect(self.database_path) as conn:
            c = conn.cursor()
            c.execute("SELECT rowid, *  FROM customers")
            items = c.fetchall()
            self.assertEqual(items, expected_output)

    def test_email_lookup(self):
        """Test email_lookup() method"""
        expected_output = [(1, 'John', 'Doe', 'john@example.com')]

        with self.assertRaises(SystemExit) as cm:
            self.db.email_lookup('john@example.com')

        output = cm.exception.code
        self.assertEqual(output, None)

        with sqlite3.connect(self.database_path) as conn:
            c = conn.cursor()
            c.execute("SELECT rowid, *  FROM customers WHERE email = (?)", ('john@example.com',))
            items = c.fetchall()
            self.assertEqual(items, expected_output)


if __name__ == '__main__':
    unittest.main()

