#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        if matrix ==  []:
            return matrix
        else:
            new_matrix = matrix.copy()
            for i in range(0, len(matrix)):
                for j in range(0, len(matrix[i])):
                    a = new_matrix[i][j]**2
                    new_matrix[i][j] = a
            return(new_matrix)
