#!/usr/bin/python3
'''Modulo'''


def is_same_class(obj, a_class):
    '''Revisa con type() que obj sea igual a la instancia en a_class'''

    if type(obj) == a_class:
        return True
    else:
        return False
