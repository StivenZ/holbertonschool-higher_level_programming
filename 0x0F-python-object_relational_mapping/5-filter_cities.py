#!/usr/bin/python3
if __name__ == "__main__":
    import MySQLdb
    import sys

    uname, psswd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost', user=uname,
                         passwd=psswd, db=db, port=3306)
    cur = db.cursor()

    cur.execute("""SELECT * FROM cities WHERE state_id =
                (SELECT id FROM states WHERE name = (%s))
                 ORDER BY cities.id""", (state_name,))
    cities = cur.fetchall()
    for city in cities:
        if city != cities[-1]:
            print(city[2], end=', ')
        else:
            print(city[2])
    cur.close()
    db.close()
