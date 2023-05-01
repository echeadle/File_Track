import unittest
from db_class import DB

class TestDB(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.db = DB(':memory:')
        self.c = self.db.cursor()
        self.c.execute("""
            CREATE TABLE customers (
                first_name text,
                last_name text,
                email text
             )
         """)
        self.db.add_one('Jane', 'Doe', 'jane@example.com')
        self.db.add_many([
            ('John', 'Doe', 'john@example.com'),
            ('David', 'Smith', 'david@example.com'),
            ('Jane', 'Smith', 'jane@example.com')
        ])

    def test_show_all(self):
        expected_output = [
            (1, 'John', 'Doe', 'john@example.com'),
            (2, 'Jane', 'Doe', 'jane@example.com'),
            (3, 'Bob', 'Smith', 'bob@example.com')
        ]
        self.assertListEqual(self.db.show_all(), expected_output)

    def test_add_one(self):
        self.db.add_one('Joe', 'Bloggs', 'joe@example.com')
        expected_output = [
            (1, 'John', 'Doe', 'john@example.com'),
            (2, 'Jane', 'Doe', 'jane@example.com'),
            (3, 'Bob', 'Smith', 'bob@example.com'),
            (4, 'Joe', 'Bloggs', 'joe@example.com')
        ]
        self.assertListEqual(self.db.show_all(), expected_output)

    def test_add_many(self):
        self.db.add_many([('Tom', 'Jones', 'tom@example.com'),
                          ('Harry', 'Potter', 'harry@example.com')])
        expected_output = [
            (1, 'John', 'Doe', 'john@example.com'),
            (2, 'Jane', 'Doe', 'jane@example.com'),
            (3, 'Bob', 'Smith', 'bob@example.com'),
            (4, 'Joe', 'Bloggs', 'joe@example.com'),
            (5, 'Tom', 'Jones', 'tom@example.com'),
            (6, 'Harry', 'Potter', 'harry@example.com')
        ]
        self.assertListEqual(self.db.show_all(), expected_output)

    def test_delete_one(self):
        self.db.delete_one(2)
        expected_output = [
            (1, 'John', 'Doe', 'john@example.com'),
            (3, 'Bob', 'Smith', 'bob@example.com')
        ]
        self.assertListEqual(self.db.show_all(), expected_output)

    def test_email_lookup(self):
        self.assertEqual(self.db.email_lookup('jane@example.com'), [(2, 'Jane', 'Doe', 'jane@example.com')])

if __name__ == '__main__':
    unittest.main()

