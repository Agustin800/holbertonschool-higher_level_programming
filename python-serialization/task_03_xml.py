#!/usr/bin/python3
'''Modulo basico de serializacion de xml a objeto de python'''
import xml.etree.ElementTree as ET
import json


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
