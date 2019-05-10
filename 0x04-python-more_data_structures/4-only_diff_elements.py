#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    set_u = set_1.union(set_2)
    set_i = set_1.intersection(set_2)
    set_r = set_u - set_i
    return set_r

