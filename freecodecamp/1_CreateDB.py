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

# Create a table

c.execute("""CREATE TABLE customers(
    first_name TEXT,
    last_name  TEXT,
    email      TEXT
)""")

#Commit command
conn.commit()

# Close Connection
conn.close()
