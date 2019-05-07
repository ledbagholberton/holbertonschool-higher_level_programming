#!/usr/bin/python3
def element_at(my_list, idx):
    long = len(my_list)
    if idx < 0 or idx > long or long == 0:
        return None
    else:
        return (my_list[idx])
