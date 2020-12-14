#!/usr/bin/python3

if __name__ == '__main__':
    import MySQLdb as sql
    from sys import argv

    username, password, database = argv[1], argv[2], argv[3]
    db = sql.connect(host="localhost", db=database, user=username,
                     passwd=password, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    for data in cur.fetchall():
        print(data)
    db.close()
