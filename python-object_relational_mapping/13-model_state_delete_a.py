#!/usr/bin/python3
"""
a script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py <mysql username> "
              "<mysql password> <database name>")
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

    states_to_delete = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .all()
    )


    for state in states_to_delete:
        session.delete(state)

    session.commit()

    print(f"Deleted {len(states_to_delete)} state(s)")

    session.close()
