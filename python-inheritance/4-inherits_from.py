#!/usr/bin/python3
'''Modulo'''


def inherits_from(obj, a_class):
    '''Verifica si es una instancia heredada directa o indirectamente'''

    if issubclass(type(obj), a_class):
        return True
    else:
        return False
