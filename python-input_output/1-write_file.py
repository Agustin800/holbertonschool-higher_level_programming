#!/usr/bin/python3
'''Modulo'''


def write_file(filename="", text=""):
    '''Funcion'''
    with open(filename, "w", encoding="utf-81")as f:
        return f.write(text)
