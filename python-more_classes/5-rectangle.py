#!/usr/bin/python3
'''Clase de un rectangulo'''


class Rectangle:
    '''clase rectangulo'''
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter: devuelve el valor de __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter: valida y asigna __width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter: devuelve el valor de __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter: valida y asigna __height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Devuelve el área del rectangulo actual."""
        return self.__width * self.__height

    def perimeter(self):
        '''Devuelve el perimetro del rectangulo'''
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        '''Imprime el rectangulo'''
        if self.__height == 0 or self.__width == 0:
            return ""
        lines = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        '''Imprime la representacion en forma de srting'''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        '''Imprime Bye rectangle..., cuando se elimina una instancia'''
        print("Bye rectangle...")
