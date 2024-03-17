#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        charset="utf8",
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = db.cursor()
    query = """ SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY
        states.id ASC""".format(argv[4])
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
