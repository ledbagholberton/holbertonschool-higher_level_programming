#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    a = 0
    with open(filename, 'r', encoding = 'utf-8') as f:
        a = f.read()
        a_l = a.count("\n")
        lineas = 1
        if nb_lines <= 0 or nb_lines >= a_l:
            print (a)
            return
    with open(filename, 'r', encoding = 'utf-8') as f:
        while lineas <= nb_lines:
            a = f.readline()
            print ("{:s}".format(a, end=""))
            lineas += 1
