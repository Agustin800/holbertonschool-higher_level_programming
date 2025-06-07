#!/usr/bin/python3
'''Modulo'''
import json


def load_from_json_file(filename):
    '''Crear un obj json en un archivo'''
    with open(filename, "r") as o:
        return json.load(o)
