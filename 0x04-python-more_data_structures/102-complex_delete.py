#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for x, y in a_dictionary.items():
            if y == value:
                a_dictionary.pop(x)
                break
    return a_dictionary
