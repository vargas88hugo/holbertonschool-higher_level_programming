#!/usr/bin/python3
"""
This script lists all cities that matches with the argument
"""

import MySQLdb
from sys import argv


def connection():
    """
    This method establishes the connection to database
    """
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])
    cur = conn.cursor()   # gives us the ability to have multiple enviroments

    return cur, conn


def get_save_argument_state():
    """
    This method lists all the cities of the database
    """
    cur, conn = connection()

    cur.execute("""SELECT
    cities.id,
    cities.name,
    states.name
FROM
    cities
LEFT JOIN
    states
ON
    cities.state_id = states.id
ORDER BY
    cities.id ASC""")
    query = cur.fetchall()   # fetches all rows and returns a list of tuple
    for i in query:
        print(i)

    cur.close()
    conn.close()


if __name__ == "__main__":
    get_save_argument_state()
