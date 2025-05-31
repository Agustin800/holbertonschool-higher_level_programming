#!/usr/bin/python3
'''Modulo'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Clase hija de BaseGeometry'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Devuelve el area del rectangulo'''
        return self.__width * self.__height

    def __str__(self):
        '''Imprime el rectangulo'''
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    '''Clase cuadrado'''
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
