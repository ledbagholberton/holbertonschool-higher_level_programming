#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is []:
        return 0
    else:
        a, b = 0, 0
        for (x, y) in my_list:
            a = (x * y) + a
            b = y + b
        r = a / b
    return (r)
