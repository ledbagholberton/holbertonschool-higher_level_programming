#!/usr/bin/python3
def no_c(my_string):
    long = len(my_string)
    for i in range (0, long):
        if my_string[i] is not "c" or my_string[i] is not "C":
            print("{:s}".format(my_string[i]), end="")
    print()
