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
    cursor.execute("""
        SELECT cities.name FROM cities
        LEFT JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
        """, (argv[4],))
    cities = cursor.fetchall()
    print(', '.join(city[0] for city in cities))
    cursor.close()
    db.close()
