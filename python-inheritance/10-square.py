#!/usr/bin/python3
'''Modulo'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Clase cuadrado'''
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2
