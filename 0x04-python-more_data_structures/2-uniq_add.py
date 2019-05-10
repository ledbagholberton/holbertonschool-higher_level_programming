#!/usr/bin/python3
def uniq_add(my_list=[]):
    suma = 0
    for i in range(1, len(my_list)):
        if i in my_list:
            suma = suma + i
    return(suma)
