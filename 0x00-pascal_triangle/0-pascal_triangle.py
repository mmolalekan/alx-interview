#!/bin/python3
"""Module documentation"""


def pascal_triangle(n):
    """function documentation"""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)  # Create a list of length i+1 filled with 1s
        for j in range(1, i):
            # Calculate the value at position (i, j)
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    return triangle
