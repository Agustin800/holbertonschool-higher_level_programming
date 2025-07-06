#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
Results are sorted by cities.id in ascending order.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]

    # Conexión a la base de datos
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_pass,
        db=db_name
    )

    cursor = db.cursor()

    # Ejecutar la consulta con JOIN entre cities y states
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
