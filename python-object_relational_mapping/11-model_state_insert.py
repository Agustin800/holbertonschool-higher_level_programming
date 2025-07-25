#!/usr/bin/python3
"""
a script that adds the State object “Louisiana” to
the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print(
            "Usage: ./script.py <mysql username> "
            "<mysql password> <database name>"
        )
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}'
        f'@localhost/{database_name}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")

    session.add(new_state)
    session.commit()

    print(f"{new_state.id}")

    session.close()
