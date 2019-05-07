#!/usr/bin/python3
def no_c(my_string):
    table = {67: None, 99: None}
    return(my_string.translate({ord(i):None for i in "Cc"}))
