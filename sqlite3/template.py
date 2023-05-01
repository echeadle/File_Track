import sqlite3

# Create  a connection
conn = sqlite3.connect("check_file.db")
# Create Cursor
c = conn.cursor()

print("Command Executed")
# commit change will execute command
conn.commit()

# Close our connection
conn.close()
