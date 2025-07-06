#!/usr/bin/python3
"""
a script that lists all State objects that contain the
letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State) \
    .filter(State.name.like('%a%')) \
    .order_by(State.id) \
    .all()


    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    session.close()
