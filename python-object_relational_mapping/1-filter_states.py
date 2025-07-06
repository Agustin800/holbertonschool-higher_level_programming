#!/usr/bin/python3
"""
a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_pass,
        db=db_name
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
        )

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
