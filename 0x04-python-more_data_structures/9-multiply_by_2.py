#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = a_dictionary.copy()
    for n, v in sorted(new_d.items()):
        item_dict = {n: v * 2}
        new_d.update(item_dict)
    return(new_d)
