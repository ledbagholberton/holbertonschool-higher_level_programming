#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dictionary = dict(a_dictionary)
    try:
        del new_dictionary[key]
        return new_dictionary
    except KeyError as ex:
        return(a_dictionary)
