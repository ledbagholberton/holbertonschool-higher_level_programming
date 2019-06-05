#!/usr/bin/python3
""" Lookup                """


def lookup(obj):
    """ Return the valid attributes of an object
        Parameters:
        obj - Object
        Return:
        List with attributes of object

    """
    return(dir(obj))
