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
    sep = " "
    if first_name == "":
        sep = ""
    print("My name is {:s}{:s}{:s}".format(first_name, sep, last_name))
