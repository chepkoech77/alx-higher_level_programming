#!/usr/bin/python3

"""List cities"""

import MySQLdb
from sys import argv


def get_cities(username, password, database):
    """Function to get cities"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            db=database)
    cursor = db.cursor()
    query = """
    SELECT cities.id, cities.name, states.name FROM cities
    JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"""
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    get_cities(username, password, database)
