#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        if matrix == []:
            return matrix
        else:
            n_matrix = []
            for i in matrix:
               n_matrix.append(i.copy())

          #  n_matrix = matrix.copy()
            for i in range(len(n_matrix)):
                for j in range(len(n_matrix[i])):
                    a = n_matrix[i][j] * n_matrix[i][j]
                    n_matrix[i][j] = a
            return(n_matrix)
