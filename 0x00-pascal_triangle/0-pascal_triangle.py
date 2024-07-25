#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Returns a list integers
    of the Pascal's Triangle up to level n
    Returns empty list if the n is less than 1
    """
    triangle = []
    if n <= 0:
        return triangle
    
    triangle.append([1])
    
    for level in range(1, n):
        row = [1]
        for idx in range(1, level):
            row.append(triangle[level - 1][idx - 1] + triangle[level - 1][idx])
        row.append(1)
        triangle.append(row)
    
    return triangle
