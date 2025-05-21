#!/usr/bin/python3
"""
Cuadra2 ** 2 + 1
"""


class Square:
    """
    Clase que define un cuadrado con un atributo privado de tamaño.
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Getter: devuelve el valor de __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: valida y asigna __size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Devuelve el área del cuadrado actual.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Imprime el cuadrado en stdout usando el carácter #.
        Si size es 0, imprime una línea vacía.
        """
        if self.__size == 0:
            print()
            return
        for _ in range (self.__size):
            print ("#" * self.__size)
