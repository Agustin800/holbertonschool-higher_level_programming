#!/usr/bin/python3
def uppercase(str):
    for letra in str:
        if 'a' <= letra <= 'z':
            mayus = chr(ord(letra) - 32)
        else:
            mayus = letra
