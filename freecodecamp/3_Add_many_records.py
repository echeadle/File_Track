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
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)


print("Command executed successfully...")
#Commit command
conn.commit()

# Close Connection
conn.close()
