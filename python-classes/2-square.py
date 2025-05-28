#!/usr/bin/python3
"""
Este módulo define una clase Square que representa un cuadrado.
"""


class Square:
    """
    Clase que define un cuadrado con un atributo privado de tamaño.
    """
    def __init__(self, size=0):
        """
        Inicializa una nueva instancia de Square.

        Args:
            size (int): El tamaño del lado del cuadrado (por defecto 0).

        Raises:
            TypeError: Si size no es un entero.
            ValueError: Si size es menor que 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
