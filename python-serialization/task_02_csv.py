#!/usr/bin/python3
'''Modulo basico de serializacion de cvs a json'''
import csv  
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, newline="") as f:
            reader = csv.DictReader(f)
            data = list(reader)

        with open("data.json", "w") as json_file:
            json.dump(data, json_file)

        return True

    except Exception:
        return False
