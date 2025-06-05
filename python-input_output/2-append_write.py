#!/usr/bin/python3
'''Modulo'''


def append_write(filename="", text=""):
    '''Funcion'''
    with open(filename, "a", encoding="utf-8") as f:
        count = f.write(text)
    return count
