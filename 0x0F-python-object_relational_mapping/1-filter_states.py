#!/usr/bin/python3
"""MySQLdb Query module
"""
if __name__ == "__main__":
    """Filter query by starting character
    """
    import MySQLdb
    import sys
    import re

    uname, psswd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=uname,
                         passwd=psswd, db=db, port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")
    state = cur.fetchall()
    for states in state:
        match = re.match('^N', states[1])
        if match is not None:
            print(states)
    cur.close()
    db.close()
