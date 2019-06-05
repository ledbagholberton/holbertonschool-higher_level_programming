#!/usr/bin/python3
def add_attribute(my_ob, atrib, nombre):
    if '__dict__' not in dir(my_ob) or '__slots__' in dir(my_ob):
        raise TypeError("can't add new attribute")
    else:
        setattr(my_ob, atrib, nombre)
