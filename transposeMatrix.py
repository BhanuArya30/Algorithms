from typing import List


# def transposeMatrix(matrix: List) -> List:
#     rows = len(matrix)
#     cols = len(matrix[0])

#     transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

#     for row in range(rows):
#         for col in range(cols):
#             transposed_matrix[col][row] = matrix[row][col]
#     return transposed_matrix


def transposeMatrix(matrix: List) -> List:
    return list(zip(*matrix))

'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Unpacked Arguments with *:

    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]

Pairs because of zip.:

    (1, 4, 7)
    (2, 5, 8)
    (3, 6, 9)

The zip function returns an iterator of tuples containing the paired elements.

Iterator of Tuples:

    (1, 4, 7)
    (2, 5, 8)
    (3, 6, 9)
'''

matrix = [[11, 12], [21, 22], [31, 32]]

print(matrix)
print('-'*30)
print(transposeMatrix(matrix))
