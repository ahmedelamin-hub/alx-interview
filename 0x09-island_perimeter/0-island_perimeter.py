#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A 2D grid representing the map where
                                     1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:  # Land found
                # Check each direction (up, down, left, right)
                if i == 0 or grid[i - 1][j] == 0:  # Up
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:  # Down
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Left
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:  # Right
                    perimeter += 1

    return perimeter
