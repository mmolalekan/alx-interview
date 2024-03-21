#!/bin/python3
"""module documentation"""


def minOperations(n):
    """Function definition"""
    if n < 1 or not isinstance(n, int):
        return 0

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)
    return n
