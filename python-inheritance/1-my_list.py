#!/usr/bin/python3
'''Clase MyList que hereda de list'''


class MyList(list):
    '''Subclase de list con un método para imprimir ordenado'''

    def print_sorted(self):
        '''Imprime la lista ordenada sin modificar la original'''
        print(sorted(self))
