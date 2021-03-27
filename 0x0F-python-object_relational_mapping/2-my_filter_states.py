#!/usr/bin/python3
"""Module on MySQLdb
"""
if __name__ == "__main__":
    """Filter state on user input
    """
    import MySQLdb
    import sys

    uname, psswd = sys.argv[1], sys.argv[2]
    db, state_name = sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(host='localhost', user=uname,
                         passwd=psswd, db=db, port=3306)
    cur = db.cursor()

    cur.execute("""SELECT * FROM states WHERE name = '{}'
                ORDER BY id""".format(state_name))
    state = cur.fetchall()
    print(state[0])
    cur.close()
    db.close()
