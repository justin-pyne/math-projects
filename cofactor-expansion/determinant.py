def minor(matrix, row, col):
    return [row[:col] + row[col+1:] for row in (matrix[:row] + matrix[row+1:])]

def determinant(matrix):
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(len(matrix[0])):
        det += ((-1)**c) * matrix[0][c] * determinant(minor(matrix, 0, c))
    return det

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2], [3, 4]]
matrix3 = [[4]]
matrix4 = [[1, 2, 3], [0, 1, 4], [2, 3, 1]]
matrix5 = [[3, 8], [4, 6]]

print(determinant(matrix1))
print(determinant(matrix2))
print(determinant(matrix3))
print(determinant(matrix4))
print(determinant(matrix5))
