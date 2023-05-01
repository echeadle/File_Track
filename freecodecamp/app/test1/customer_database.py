import sqlite3

class CustomerDatabase:
    def __init__(self, database_path):
        self.database_path = database_path

    def show_all(self):
        """Connect to the DB and return all records"""
        with sqlite3.connect(self.database_path) as conn:
            c = conn.cursor()

            # Query the Database - ORDER BY
            c.execute("SELECT rowid, *  FROM customers")
            items = c.fetchall()

            for item in items:
                print(item)

            #Commit command
            conn.commit()

    def add_one(self, first, last, email):
        """Add a new record to the Table"""
        with sqlite3.connect(self.database_path) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
            conn.commit()

    def add_many(self, list):
        """Add any number of new records to the Table
           The list must be passed in and put in Parenthesis
        """
        with sqlite3.connect(self.database_path) as conn:
            c = conn.cursor()
            c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
            conn.commit()

    def delete_one(self, id):
        """Delete a record from the Table
           id argument must be a string SQLite makes the change
        """
        with sqlite3.connect(self.database_path) as conn:
            c = conn.cursor()
            c.execute("DELETE FROM customers WHERE rowid = (?)", id)
            conn.commit()

    def email_lookup(self, email):
        """Lookup email from the Table"""
        with sqlite3.connect(self.database_path) as conn:
            c = conn.cursor()
            c.execute("SELECT rowid, *  FROM customers WHERE email = (?)", (email,))

            items = c.fetchall()
            for item in items:
                print(item)

            conn.commit()

if __name__ == '__main__':
    db = CustomerDatabase('customer.db')
    db.show_all()

    db.add_one('John', 'Doe', 'john@example.com')
    db.show_all()

    db.add_many([('Mary', 'Smith', 'mary@example.com'),
                 ('Jane', 'Doe', 'jane@example.com')])
    db.show_all()

    db.delete_one(1)
    db.show_all()

    db.email_lookup('john@example.com')

