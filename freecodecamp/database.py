# From FreeCodecamp
# https://www.youtube.com/watch?v=byHcYRpMgI4

import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db') 

# Create a cursor
c = conn.cursor()


def 

# Query the Database - ORDER BY
#c.execute("SELECT rowid, *  FROM customers ORDER BY rowid DESC")
c.execute("SELECT rowid, *  FROM customers ORDER BY last_name DESC")


items = c.fetchall()

for item in items:
    print(item)


#print("Command executed successfully...")
#Commit command
conn.commit()

# Close Connection
conn.close()
