#!/usr/bin/python3
"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]

    # Crear el motor de conexión
    engine = create_engine(f"mysql+mysqldb://{mysql_user}:{mysql_pass}@localhost:3306/{db_name}")

    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Consultar los estados ordenados por id ascendente
    states = session.query(State).order_by(State.id).all()

    # Mostrar resultados
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
