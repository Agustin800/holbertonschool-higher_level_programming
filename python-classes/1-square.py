#!/usr/bin/python3
"""
Este módulo define la clase Square que representa un cuadrado con un tamaño dado.
"""


class  Square:
    """
    Clase que define un cuadrado con un atributo privado de tamaño.
    """
    def __init__(self, size):
        """
        Inicializa una nueva instancia de Square con un tamaño dado.

        Args:
            size: El tamaño del lado del cuadrado.
        """
        self.__size = size
