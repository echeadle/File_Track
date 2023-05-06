import sqlite_db as db

mypc_db = db.Database("mypc_db.db")

table_name = 'file_hash'
index_name = 'idx_hash'
columns = {'filename': 'TEXT', 'filepath': 'TEXT', 'filehash': 'TEXT'}
f_hash = '0eacfadc0b4254f1ba51710dbd83220b087c112b24f8c679388f11574961edab'
mypc_db.create_table(table_name, columns)

record = {
            'filename': 'test2_sqlite_db.py',
            'filepath': '/home/echeadle/Workspace/AI_Prog/File_Track/app/test2_sqlite_db.py',
            'filehash': '0eacfadc0b4254f1ba51710dbd83220b087c112b24f8c679388f11574961edab'
        }
mypc_db.add_record(table_name, record)
record = {
            'filename': 'test_sqlite_db.py',
            'filepath': '/home/echeadle/Workspace/AI_Prog/File_Track/app/test_sqlite_db.py',
            'filehash': '0eacfadc0b4254f1ba51710dbd83220b087c112b24f8c679388f11574961edab'
        }
mypc_db.add_record(table_name, record)
record = {
            'filename': 'sqlite_db.py',
            'filepath': '/home/echeadle/Workspace/AI_Prog/File_Track/app/sqlite_db.py',
            'filehash': 'a8dde4f88d4a4c6e8387ecbc3709842fd619db22b3d6ab17d77b2670749d9e4e'
        }
mypc_db.add_record(table_name, record)
print(mypc_db.show_all_tables())
#mypc_db.create_index(index_name, table_name, ('filepath', 'filehash'))
print('-----------------------------------------------------------------------------------')
#print(mypc_db.show_all_records('file_hash'))

all_records = mypc_db.show_all_records('file_hash')
#print(all_records)
for filename, filepath, filehash in all_records:
    print(f'{filename} :\n{filepath} :\n{filehash}\n')
    print('---------------------------------------------------------------------------------')
print(mypc_db.run_query(f"SELECT filename, filepath FROM {table_name} WHERE filehash = '{f_hash}'"))
print(mypc_db.run_query(f"SELECT type, name,tbl_name, sql FROM sqlite_master WHERE type='index'"))

#print(mypc_db.show_duplicate_records(table_name, index_name, f_hash))

#db.delete_record('users', "name='Bob'")
 #print(db.show_all_records('users'))
 #db.delete_table('users')
mypc_db.close_connection()
 #os.remove('test.db')

"""
/home/echeadle/Workspace/AI_Prog/File_Track/app
c2d184b2c31e0782e18111f39d2470fb2d928488f74c1f5fd20b06278f4f2212  test2_sqlite_db.py
0eacfadc0b4254f1ba51710dbd83220b087c112b24f8c679388f11574961edab  test_sqlite_db.py
a8dde4f88d4a4c6e8387ecbc3709842fd619db22b3d6ab17d77b2670749d9e4e  sqlite_db.py

"""
