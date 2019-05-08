#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        long = len(matrix[0])
        for i in range(0, long):
            long2 = len(matrix[i])
            for j in range(0, long2 - 1):
                print("{} ".format(matrix[i][j]), end=" ")
            print("{} ".format(matrix[i][j + 1]))
        else:
            print()

