#!/usr/bin/python3
"""Module to connect to database"""

if __name__ == "__main__":
    """Executes query to database from user input
    """
    import MySQLdb
    import sys

    uname, psswd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=uname,
                         passwd=psswd, db=db, port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    state = cur.fetchall()
    for states in state:
        print(states)
    cur.close()
    db.close()
