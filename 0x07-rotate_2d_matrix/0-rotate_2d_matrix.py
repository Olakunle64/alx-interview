#!/usr/bin/python3
"""Rotate a 2D matrix clockwise"""


def sub(matrix, start, stop):
    if start >= stop:
        return
    temp = matrix[start]
    matrix[start] = matrix[stop - 1]
    matrix[stop - 1] = temp
    sub(matrix, start + 1, stop - 1)


# def transpose_matrix(matrix):
#     n = len(matrix)
#     for i in range(n):
#         for j in range(i + 1, n):
#             # Swap elements matrix[i][j] and matrix[j][i]
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def transpose_matrix(matrix):
    """"get the transpose of a matrix"""
    col = 0
    n = len(matrix)
    i = 0
    while i < n:
        j = i
        row = i
        while j < n:
            temp = matrix[row][col]
            matrix[row][col] = matrix[i][j]
            matrix[i][j] = temp
            j += 1
            row += 1
        col += 1
        i += 1


def rotate_2d_matrix(matrix):
    if not len(matrix):
        return None
    sub(matrix, 0, len(matrix))
    transpose_matrix(matrix)
