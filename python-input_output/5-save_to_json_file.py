#!/usr/bin/python3
'''Modulo'''
import json


def save_to_json_file(my_obj, filename):
    '''Funcion para escribir un obj en un archivo en formato json'''
    with open(filename, "w") as f:
       return json.dumps(my_obj, f)
