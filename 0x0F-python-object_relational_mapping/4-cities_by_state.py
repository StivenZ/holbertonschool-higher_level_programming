#!/usr/bin/python3
"""REtrieves cities names from table
"""

if __name__ == "__main__":
    import MySQLdb as sql
    from sys import argv

    uname, password, d_base = argv[1], argv[2], argv[3]
    db = sql.connect(host="localhost", db=d_base, user=uname,
                     passwd=password, port=3306)

    cur = db.cursor()

    query = ("SELECT cities.id, cities.name, states.name \
FROM cities JOIN states ON cities.id ORDER BY cities.id;")
    cur.execute(query)
    the_cities = cur.fetchall()

    for name in the_cities:
        print(name)

    db.close
