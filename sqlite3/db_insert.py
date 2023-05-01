import sqlite3

# Create  a connection
conn = sqlite3.connect("check_file.db")
# Create Cursor
c = conn.cursor()

c.execute("INSERT INTO file_checks VALUES ('08HEN&UKENXHX', 'scratch_file.py', 'home/echeadle')")

print("Command Executed")
# commit change will execute command
conn.commit()

# Close our connection
conn.close()
