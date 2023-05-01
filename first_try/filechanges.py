import os
import sys
import sqlite3

def getbasefile():
    """Name of the SQLite DB file"""
    return os.path.splitext(os.path.basename(__file__))[0]


def connectdb():
    """Connect to the SQLite DB"""
    try:
        dbfile=f'{getbasefile()}.db'
        conn = sqlite.connect(dbfile, timeout=2)
    except BaseException as err:
        print(str(err))
    return conn

def corecursor(conn, query, args):
    """Opens a SQLite DB cursor"""
    result = False
    cursor = conn.cursor()
    try:
        cursor.execute(query, args)
        rows = cursor.fetchall()
        numrows = len(list(rows))
        if numrows > 0:
            result = True
    except sqlite3.OperationalError as err:
        print(str(err))
        if cursor != None:
            cursor.close()
    finally: if cursor != None:
        cursor.close()
    return result



 --------------------------------------------------
if __name__ == '__main__':
    print(getbasefile())


