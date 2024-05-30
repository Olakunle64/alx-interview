def transpose_matrix(matrix):
    """"ddd"""
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

def transpose_matrix2(matrix):
    """"ddd"""
    n = len(matrix)
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            temp = matrix[j][i]
            matrix[j][i] = matrix[i][j]
            matrix[i][j] = temp
            j += 1
        i += 1

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
print(matrix)
transpose_matrix(matrix)
print(matrix)