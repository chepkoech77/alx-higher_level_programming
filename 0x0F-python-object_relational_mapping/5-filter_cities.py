#!/usr/bin/python3
"""This list cities"""

import MySQLdb
from sys import argv


def get_cities_states(username, password, database, state):
    """This is a function"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)
    cursor = db.cursor()
    query = """SELECT cities.id, cities.name
    FROM cities JOIN states ON cities.state_id = states.id
    WHERE states.name = %s ORDER BY cities.id ASC"""

    cursor.execute(query, (state,))
    results = cursor.fetchall()

    for row in results:
        print(row)

    db.close()


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state = argv[4]

    get_cities_states(username, password, database, state)
