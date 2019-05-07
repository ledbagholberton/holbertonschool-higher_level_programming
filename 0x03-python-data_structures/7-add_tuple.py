#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_b) is 0):
        tb0 = 0
        tb1 = 0
    if(len(tuple_b) is 1):
        tb1 = 0
    if (len(tuple_a) is 0):
        ta0 = 0
        ta1 = 0
    if(len(tuple_a) is 1):
        ta1 = 0


    elif(len(tuple_a) is 2):
        tc0 = tuple_a[0] + tuple_b[0]
        tc1 = tuple_a[1] + tuple_b[1]

    tuple_c = (tc0, tc1)
    return tuple_c
