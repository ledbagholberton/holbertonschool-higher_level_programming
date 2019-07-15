#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """ Function that print the full name

        Args:
           first_name: String with first name
           last_name: String with last name

        Returns:
           Nothing - just print full name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
