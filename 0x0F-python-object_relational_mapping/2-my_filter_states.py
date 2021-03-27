#!/usr/bin/python3
if __name__ == "__main__":
    import MySQLdb
    import sys
    import re

    uname, psswd = sys.argv[1], sys.argv[2]
    db, state_name = sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(host='localhost', user=uname,
                         passwd=psswd, db=db, port=3306)
    cur = db.cursor()

    cur.execute("""SELECT * FROM states WHERE name = (%s)
                ORDER BY id""", (state_name,))
    state = cur.fetchall()
    for states in state:
        print(states)
    cur.close()
    db.close()
