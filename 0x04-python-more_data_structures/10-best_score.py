#!/usr/bin/python3
def best_score(a_dictionary):
    mayor = 0
    for a, b in a_dictionary.items():
        if b > mayor:
            mayor = b
            key_mayor = a
    if mayor == 0:
        key_mayor = "None"
    return key_mayor
