#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    long = len(my_list) - 1
    for i in range(long, -1, -1):
        print("{}".format(my_list[i]))
