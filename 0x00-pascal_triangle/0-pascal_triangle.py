#!/usr/bin/python3
"""This module contains a function that construct a pascal triangle
"""


def pascal_triangle(n):
    """Construct the pascal triangle of size (n)
        Args:
            n: an integer

        Return: returns a list of lists of integers representing
                the Pascal’s triangle of n

                Returns an empty list if n <= 0
    """
    big_pascal = []
    if n <= 0:
        return big_pascal
    if n >= 1:
        big_pascal.append([1])
        n -= 1
    while n > 0:
        last_pascal = big_pascal[-1]
        i = 0
        new_pascal = [1]
        while i < len(last_pascal):
            if i + 1 == len(last_pascal):
                new_pascal.append(1)
                break
            new_pascal.append(last_pascal[i] + last_pascal[i + 1])
            i += 1
        big_pascal.append(new_pascal)
        n -= 1
    return big_pascal
