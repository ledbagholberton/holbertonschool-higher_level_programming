#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ Function that divides a matrix by a div

        Args:
           matrix: List of lists (integers or float)
           div: Div (integer of float)

        Returns:
           matrix same size of original matrix
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    new_matrix = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if len(row) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append(row[:])
    for i, row in enumerate(new_matrix[:]):
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        for index, j in enumerate(row[:]):
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
            new_matrix[i][index] = round(j / div, 2)
    return (new_matrix)
