#!/usr/bin/python3
"""
This script lists all states that matches with the argument
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
    This method lists all the states of the database
    """
    cur, conn = connection()

    if ';' not in argv[4]:
        cur.execute("SELECT * FROM states WHERE name=%s\
        ORDER BY states.id ASC", (argv[4], ))  # avoids SQL injection's
        query = cur.fetchall()   # fetches all rows and returns a list of tuple
        for i in query:
            print(i)

    cur.close()
    conn.close()


if __name__ == "__main__":
    get_save_argument_state()
