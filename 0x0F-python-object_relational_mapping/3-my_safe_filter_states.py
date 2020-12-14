#!/usr/bin/python3
"""Prevents from SQL injections.
"""

if __name__ == "__main__":
    import MySQLdb as sql
    from sys import argv

    uname, password, d_base, s_name = argv[1], argv[2], argv[3], argv[4]
    db = sql.connect(host="localhost", db=d_base, user=uname,
                     passwd=password, port=3306)

    cur = db.cursor()

    query = ("SELECT * FROM states WHERE states.name \
LIKE BINARY '{}';".format(s_name))
    cur.execute(query)
    the_states = cur.fetchall()

    for name in the_states:
        print(name)

    db.close
