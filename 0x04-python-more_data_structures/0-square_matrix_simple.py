#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for i in range (0, len(new_matrix)):
        for j in range (0, len(new_matrix[i])):
            a = matrix[i][j]**2
            new_matrix[i][j] = a
    return(new_matrix)
