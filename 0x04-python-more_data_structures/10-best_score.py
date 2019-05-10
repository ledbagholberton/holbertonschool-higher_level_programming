#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        if len(a_dictionary) is not 0:
            mayor = 0
            for a, b in a_dictionary.items():
                if b > mayor:
                    mayor = b
                    key_mayor = a
            return key_mayor
