#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]
    search_term = sys.argv[4]


    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_pass,
        db=db_name
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE '{}'"
        "ORDER BY id ASC".format('Nevada')
        )

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
