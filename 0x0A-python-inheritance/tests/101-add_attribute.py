#!/usr/bin/python3
def add_attribute(clase, atrib, nombre):
    if (clase.__dict___) or (clase.__slot___):
        raise ("can't add new attribute")
    else:
        setattr(atrib, nombre)
