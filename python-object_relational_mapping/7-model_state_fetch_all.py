#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Leer argumentos: usuario, contraseña, base de datos
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]

    # Construir la URL de conexión a la base de datos
    db_url = (
        f"mysql+mysqldb://{mysql_user}:{mysql_pass}"
        f"@localhost:3306/{db_name}"
    )

    # Crear el motor de conexión con SQLAlchemy
    engine = create_engine(db_url)

    # Crear una sesión para interactuar con la base de datos
    Session = sessionmaker(bind=engine)
    session = Session()

    # Consultar todos los estados ordenados por id ascendente
    states = session.query(State).order_by(State.id).all()

    # Mostrar los resultados en el formato requerido
    for state in states:
        print(f"{state.id}: {state.name}")

    # Cerrar la sesión
    session.close()
