#!/usr/bin/python3
'''Modulo'''
from abc import ABC, abstractmethod


class Animal(ABC):
    '''Clase Animal'''
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
