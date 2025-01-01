#!/usr/bin/python3

"""Filter states"""
import MySQLdb
from sys import argv


def filter_states(username, password, database):
    """function to filter states"""
    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    results = cursor.fetchall()

    for row in results:
        if row[1].startswith("N"):
            print(row)

    db.close()


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]

    filter_states(username, password, database)
