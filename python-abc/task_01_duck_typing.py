#!/usr/bin/python3
'''Modulo'''
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    '''clase rectangulo'''
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)

def shape_info(shape):
    print(f"Area: {shape.area():.1f}")
    print(f"Perimeter: {shape.perimeter():.1f}")
