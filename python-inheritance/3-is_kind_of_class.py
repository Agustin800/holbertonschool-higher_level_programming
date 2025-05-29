#!/usr/bin/python3
'''Modulo'''


def is_kind_of_class(obj, a_class):
    '''Revisa si es una instancia o uuna que heredo de otra clase'''
    if isinstance(obj, a_class):
        return True
    else:
        return False
