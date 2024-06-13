#!/usr/bin/python3
"""This module has a function named island_perimeter"""


def island_perimeter(grid):
    """This function returns the perimeter
        of the island described in grid
    """
    if not grid or not grid[0]:
        return 0
    perimeter = 0
    row = 0
    while row < len(grid):
        col = 0
        while col < len(grid[row]):
            if grid[row][col] == 1:
                tempPerimeter = 4

                # check right
                if col + 1 < len(grid[row]):
                    if grid[row][col + 1] == 1:
                        tempPerimeter -= 1

                # check left
                if col - 1 >= 0:
                    if grid[row][col - 1] == 1:
                        tempPerimeter -= 1

                # check up
                if row - 1 >= 0:
                    if grid[row - 1][col] == 1:
                        tempPerimeter -= 1

                # check down
                if row + 1 < len(grid):
                    if grid[row + 1][col] == 1:
                        tempPerimeter -= 1
                perimeter += tempPerimeter

            col += 1
        row += 1
    return perimeter
