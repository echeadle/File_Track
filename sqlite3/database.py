import sqlite3

# In memory database
# conn = sqlite3.connect(':memory:')

# Create  a connection
conn = sqlite3.connect("check_file.db")


# Create Cursor
c = conn.cursor()

# create a db table
# DataTypes:  Null Integer Real Text Blob
c.execute(
    """CREATE TABLE file_checks (
            hash_tag  TEXT,
            file_name text,
            file_path text
        )
    """
)

# commit change will execute command
conn.commit()

# Close our connection
conn.close()
