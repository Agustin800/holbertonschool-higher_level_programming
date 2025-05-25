#!/usr/bin/python3
'''Clase de un rectangulo'''


class Rectangle:
    '''atributo publico enumera cracion y eliminacion de instancias'''
    number_of_instances = 0
    '''atributo publico'''
    print_symbol = "#"

    '''clase rectangulo'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

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
        lines = [
            str(self.print_symbol) * self.__width
            for _ in range(self.__height)
        ]
        return "\n".join(lines)

    def __repr__(self):
        '''Imprime la representacion en forma de srting'''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        '''Imprime Bye rectangle..., cuando se elimina una instancia'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
