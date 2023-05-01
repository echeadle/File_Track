from sqlite_db import Database

db = Database(':memory:')
db.create_table('users', {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT', 'email': 'TEXT'})
db.add_record('users', {'name': 'Alice', 'email': 'alice@example.com'})
db.add_record('users', {'name': 'Bob', 'email': 'bob@example.com'})
db.delete_record('users', "name='Bob'")
rows = db.show_all_records('users')
for row in rows:
    print(row)


