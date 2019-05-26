#!/usr/bin/python3
def add_integer(a, b=98):
    """ Function that summ two numbers integer or float.

        Args:
           a: First parameter (integer or float)
           b: Second paramenter (integer of float)

        Returns:
            Summ of a & b
    """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    elif type(a) is float:
        a = int(a)
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    elif type(b) is float:
        b = int(b)
    c = a + b
    return (c)
