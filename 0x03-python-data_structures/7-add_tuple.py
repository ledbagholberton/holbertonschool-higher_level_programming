#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_b) is 0):
        tc0 = tuple_a[0]
        tc1 = tuple_a[1]
    elif(len(tuple_b) is 1):
        tc0 = tuple_a[0] + tuple_b[0]
        tc1 = tuple_a[1]
    else:
        tc0 = tuple_a[0] + tuple_b[0]
        tc1 = tuple_a[1] + tuple_b[1]
    tuple_c = (tc0, tc1)
    return tuple_c
