import sqlite3

# Create  a connection
conn = sqlite3.connect("check_file.db")
# Create Cursor
c = conn.cursor()

c.execute("SELECT * FROM file_checks")
#c.fetchone()
#c.fetchmany(3)
print(c.fetchall())

c.execute("SELECT * FROM file_checks WHERE file_name LIKE '%afile.py'")
items = c.fetchall()
for item in items:
    print(item)

#print("Command Executed")
# commit change will execute command
conn.commit()

# Close our connection
conn.close()
