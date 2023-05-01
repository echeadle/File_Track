# From FreeCodecamp
# https://www.youtube.com/watch?v=byHcYRpMgI4

import sqlite3



def show_all():
    """Connect to the DB and return all records"""

    # Connect to database
    conn = sqlite3.connect('customer.db')
    
    # Create a cursor
    c = conn.cursor()

    # Query the Database - ORDER BY
    c.execute("SELECT rowid, *  FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    #Commit command
    conn.commit()

    # C.lose Connection
    conn.close()


def add_one(first,last,email):
    """Add a new record to the Table"""
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
    conn.commit()
    conn.close()


def add_many(list):
    """Add any number of new records to the Table
       The list must be passed in and put in Parenthesis
    """
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    conn.commit()
    conn.close()

def delete_one(id):
    """Delete a record from the Table
       id argument must be a string SQLite makes the change
    """
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE rowid = (?)", id)
    conn.commit()
    conn.close()

def email_lookup(email):
    """Lookup email from the Table
    """
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, *  FROM customers WHERE email = (?)", (email,))

    items = c.fetchall()
    for item in items:
        print(item)

    conn.commit()
    conn.close()


