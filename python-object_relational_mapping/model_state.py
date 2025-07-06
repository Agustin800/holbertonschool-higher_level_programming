#!/usr/bin/python3
"""
a python file that contains the class definition of a State and
an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Instancia de la base para las clases declarativas
Base = declarative_base()


class State(Base):
    """Clase que representa la tabla 'states' en la base de datos"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
