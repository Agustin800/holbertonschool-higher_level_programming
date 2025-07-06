#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa
where name matches the argument. But this time, write one that
is safe from MySQL injections!
"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_pass,
        db=db_name
    )

    cursor = de.cursor

    query = (
        "SELECT * FROM states WHERE BINARYNAME = '{}' "
        "ORDER BY id ASC"
    ).format(state_name)

    cursor.execute(query)

    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()

    if __name__ == "__main__":
        main()
