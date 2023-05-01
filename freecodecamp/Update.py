# From FreeCodecamp
# https://www.youtube.com/watch?v=byHcYRpMgI4

import sqlite3


#conn = sqlite.connect(':memory:')  Puts database in memory. 
# Sqlite3 has 5 datatypes

# NULL
# INTEGER
# REAL
# TEXT
# BLOB

conn = sqlite3.connect('customer.db') 

# Create a cursor
c = conn.cursor()

many_customers = [
                    ('Wes', 'Brown', 'wes@brown.com'),
                    ('Steph', 'Kuewa', 'steph@kuewa.com'),
                    ('Dan', 'Pas', 'dan@pas.com'),
                 ]

# Execute one
# c.execute("INSERT INTO  customers VALUES ('Mary', 'Brown', 'mary@codemy.com')")
# Execute many
#c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
# Query the Database
#c.execute("SELECT rowid, * FROM customers")
#c.execute("SELECT  * FROM customers WHERE last_name = 'Elder'")
#c.execute("SELECT  * FROM customers WHERE last_name LIKE 'Br%'")
c.execute("""UPDATE customers SET first_name = 'John'
            WHERE rowid = 1
        """)
conn.commit()
c.execute("SELECT  * FROM customers")
#print(f'Fetch one:\n {c.fetchone()[0]}')
#print(f'Fetch many:\n {c.fetchmany(3)}')
items = c.fetchall()

for item in items:
    print(item)

for fname, lname, email in items:
    print(f'{lname:10} {fname:10} {email:10}')

# Format


print("Command executed successfully...")
#Commit command
conn.commit()

# Close Connection
conn.close()
