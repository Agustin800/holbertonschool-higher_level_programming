#!/usr/bin/python3
'''Modulo'''


def read_file(filename=""):
    '''Abre, lee y cierra el archivo'''
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
