#!/usr/bin/python3
'''Modulo'''


def pascal_triangle(n):
    '''funcion que devuelve el triangulo de pascal'''
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev_row = triangle[-1]
            new_row = [1]

            for j in range(len(prev_row) - 1):
                new_row.append(prev_row[j] + prev_row[j + 1])

            new_row.append(1)
            triangle.append(new_row)

    return triangle
