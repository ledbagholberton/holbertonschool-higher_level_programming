#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        long = len(matrix)
        for i in range(0, long):
            long2 = len(matrix[i])
            for j in range(0, long2):
                print("{:d}".format(matrix[i][j]), end=" "
                      if j < long2 - 1 else "")
            print("")
