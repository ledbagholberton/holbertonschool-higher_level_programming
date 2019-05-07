def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
    else:
        long = len(matrix[0])
        for i in range(0, long):
            print("{}".format(matrix[i]))
