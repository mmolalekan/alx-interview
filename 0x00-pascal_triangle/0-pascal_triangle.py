#!/usr/bin/python3
"""implementation of a pascal triangle"""


def factorial(n):
    if n <= 1:
        return 1
    else:
        result = n * factorial(n-1)
    return result


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    Returns an empty list if n <= 0
    """
    if n <= 0:
        return []
    result = []
    for i in range(n):
        temp = []
        for k in range(i + 1):
            res = (factorial(i)) / (factorial(k) * factorial(i - k))
            temp.append(round(res))
        result.append(temp)
    return result
