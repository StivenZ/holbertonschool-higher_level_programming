#!/usr/bin/python3
"""Module on mysqldb"""
if __name__ == "__main__":
    """List results from 2 tables"""
    import MySQLdb
    import sys

    uname, psswd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=uname,
                         passwd=psswd, db=db, port=3306)
    cur = db.cursor()

    cur.execute("""SELECT c.id, c.name, s.name FROM states AS s
                 JOIN cities AS c WHERE c.state_id = s.id""")
    city = cur.fetchall()
    for cities in city:
        print(cities)
    cur.close()
    db.close()
