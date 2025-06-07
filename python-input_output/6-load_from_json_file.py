#!/usr/bin/python3
'''Modulo'''
import json


def load_from_json_file(filename):
    with open(filename, "a") as o:
        return json.dumps(o)
