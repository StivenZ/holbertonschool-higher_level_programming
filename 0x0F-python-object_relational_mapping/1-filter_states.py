#!/usr/bin/python3
"""Perform classification within a query:
    selects only results starting with 'N'
"""

if __name__ == '__main__':
    import MySQLdb as sql
    from sys import argv

    username, password, database = argv[1], argv[2], argv[3]
    db = sql.connect(host="localhost", db=database, user=username,
                     passwd=password, port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states ORDER BY states.id"
    cur.execute(query)

    for data in cur.fetchall():
        if data[1][0] == 'N':
            print(data)

    db.close()
