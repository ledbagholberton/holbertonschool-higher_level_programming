#!/usr/bin/python3
import numpy as np
def matrix_mul(m_a, m_b):
    """ Function that multiplies two matrix

        Args:
           m_a: matrix a
           m_b: matrix b

        Returns:
           new matrix with the multiplication or Errors
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    m_a_files = len(m_a)
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
        m_a_rows = len(row)
        if m_a_rows == 0:
            raise TypeError("m_a can't be empty")
            for index, j in enumerate(row[:]):
                if type(j) is not int and type(j) is not float:
                    raise TypeError("m_a should contain only integers or floats")

    m_b_files = len(m_b)
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
        m_b_rows = len(row)
        if m_b_rows == 0:
            raise TypeError("m_b can't be empty")
            for index, j in enumerate(row[:]):
                if type(j) is not int and type(j) is not float:
                    raise TypeError("m_b should contain only integers or floats")

    if (m_a_files is not m_b_rows):
        raise ValueError("m_a and m_b can't be multiplied")
    return np.dot(m_a, m_b)
