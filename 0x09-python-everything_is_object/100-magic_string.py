#!/usr/bin/python3
def magic_string(cont=[0]):
    cont[0] += 1
    return("".join(list("Holberton" * cont[0])))
