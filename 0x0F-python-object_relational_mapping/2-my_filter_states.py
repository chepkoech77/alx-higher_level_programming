#!/usr/bin/python3

"""Matches parameter provided"""
import MySQLdb
from sys import argv


def search_state(username, password, database, state):
    """searches the state"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)
    cursor = db.cursor()

    query = """
    SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    query = query.format(state)

    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    db.close()


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state = argv[4]

    search_state(username, password, database, state)
