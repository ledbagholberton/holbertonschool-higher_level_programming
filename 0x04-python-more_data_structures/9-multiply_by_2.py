#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mayor = 0
    new_d = a_dictionary.copy()
    for a, b in a_dictionary.items():
        if b > mayor:
            mayor = b
            new_d = dic(a=b)
    return new_d
