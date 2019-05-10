#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    try:
        del a_dictionary[key]
        return a_dictionary
    except KeyError as ex:
        return(a_dictionary)
