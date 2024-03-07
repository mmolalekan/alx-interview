#!/usr/bin/python3
'''Implementing Pascal's triangle.
'''


def pascal_triangle(n):
    '''returns a Pascal's triangle of a given integer.
    '''
    if type(n) is not int or n <= 0:
        return []
    res = [[1]]
    for i in range(n - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res
