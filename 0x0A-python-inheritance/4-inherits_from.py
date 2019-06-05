#!/usr/bin/python3
""" Inherits_from  """


def inherits_from(obj, a_class):
    """ Return if a_classs is a parents of an object
        Parameters:
        obj - Object
        a_class - class
        Return:
        True or False

    """
    if type(obj) is a_class:
        return False
    else:
        return(isinstance(obj, a_class))
