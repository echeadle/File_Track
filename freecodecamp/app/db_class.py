import sqlite3

class DB:
    def __init__(self, db_name, db_path=''):  # add db_path argument with default value
        self.db_name = db_name
        self.db_path = db_path

    def create_table(self):
        """Create a table in the Database"""
        conn = sqlite3.connect(self.db_path + self.db_name)
        c = conn.cursor()
        c.execute("""CREATE TABLE customers (
                    first text,
                    last text,
                    email text
                    )""")
        conn.commit()
        conn.close()

    def add_one(self, first, last, email):
        """Add a new record to the Table"""
        conn = sqlite3.connect(self.db_path + self.db_name)
        c = conn.cursor()
        c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
        conn.commit()
        conn.close()

    def add_many(self, lst):
        """Add any number of new records to the Table
           The list must be passed in and put in Parenthesis
        """
        conn = sqlite3.connect(self.db_path + self.db_name)
        c = conn.cursor()
        c.executemany("INSERT INTO customers VALUES (?,?,?)", lst)
        conn.commit()
        conn.close()

    def delete_one(self, id):
        """Delete a record from the Table
           id argument must be a string SQLite makes the change
        """
        conn = sqlite3.connect(self.db_path + self.db_name)
        c = conn.cursor()
        c.execute("DELETE FROM customers WHERE rowid = (?)", id)
        conn.commit()
        conn.close()

    def email_lookup(self, email):
        """Lookup email from the Table
        """
        conn = sqlite3.connect(self.db_path + self.db_name)
        c = conn.cursor()
        c.execute("SELECT rowid, *  FROM customers WHERE email = (?)", (email,))

        items = c.fetchall()
        for item in items:
            print(item)

        conn.commit()
        conn.close()

