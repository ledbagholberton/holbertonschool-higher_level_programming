#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    list_c = [0, 0]
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    if (len(list_b) is 0):
        list_b = [0, 0]
    if(len(list_b) is 1):
        list_b.append(0)
    if (len(list_a) is 0):
        list_a = [0, 0]
    if(len(list_a) is 1):
        list_a.append(0)
    list_c[0] = list_a[0] + list_b[0]
    list_c[1] = list_a[1] + list_b[1]
    tuple_c = (list_c[0], list_c[1])
    return tuple_c
