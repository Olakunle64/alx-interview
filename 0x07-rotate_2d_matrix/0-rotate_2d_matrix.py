#!/usr/bin/python3
"""Rotate a 2D matrix clockwise"""


def sub(matrix, start, stop):
    if start >= stop:
        return
    temp = matrix[start]
    matrix[start] = matrix[stop - 1]
    matrix[stop - 1] = temp
    sub(matrix, start + 1, stop - 1)


def transpose_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            # Swap elements matrix[i][j] and matrix[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def rotate_2d_matrix(matrix):
    if not len(matrix):
        return None
    sub(matrix, 0, len(matrix))
    transpose_matrix(matrix)
