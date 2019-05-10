#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = a_dictionary.copy()
    for n, v in new_d.items():
        d1 = {n : v * 2}
        new_d.update(d1)
    return(new_d)
