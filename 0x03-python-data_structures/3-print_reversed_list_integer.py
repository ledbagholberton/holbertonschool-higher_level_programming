#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    long = len(my_list) - 1
    if (long + 1) >= 0:
        for i in range(long, -1, -1):
            print("{:d}".format(my_list[i]))
