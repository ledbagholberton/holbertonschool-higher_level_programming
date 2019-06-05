#!/usr/bin/python3
""" Is  same class"""


def is_same_class(obj, a_class):
    """ Return if obj is same class
        Parameters:
        obj - Object
        a_class - class to compare
        Return:
        True or false

    """
    return(type(obj) == a_class)
