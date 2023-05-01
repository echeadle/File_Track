import sqlite3

# Create  a connection
conn = sqlite3.connect("check_file.db")
# Create Cursor
c = conn.cursor()

many_files = [
                ('HSJD', 'afile.py', '/home/echeadle/files2'),
                ('JSJD', 'twofile.py', '/home/echeadle'),
                ('HSJD', 'afile.py', '/home/echeadle/files3')
              ]

c.executemany("INSERT INTO file_checks VALUES (?, ?, ?)", many_files)

print("Command Executed")
# commit change will execute command
conn.commit()

# Close our connection
conn.close()
