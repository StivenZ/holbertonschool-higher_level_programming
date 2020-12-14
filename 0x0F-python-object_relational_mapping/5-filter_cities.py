#!/usr/bin/python3
"""Retrieves cities from given state
"""

if __name__ == "__main__":
    import MySQLdb as sql
    from sys import argv

    uname, password, d_base, state_name = argv[1], argv[2], argv[3], argv[4]
    db = sql.connect(host="localhost", db=d_base, user=uname,
                     passwd=password, port=3306)

    cur = db.cursor()

    query = ("SELECT name FROM cities WHERE state_id\
    = (SELECT id FROM states WHERE states.name LIKE BINARY '{}'\
    ORDER BY cities.id ASC);".format(state_name))
    cur.execute(query)
    the_cities = cur.fetchall()

    for name in the_cities:
        if the_cities[-1] == name:
            print(name[0])
        else:
            print(name[0], end=', ')

    db.close
