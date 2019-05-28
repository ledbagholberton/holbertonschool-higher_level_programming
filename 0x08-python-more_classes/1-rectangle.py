#!/usr/bin/python3
""" Rectangle

"""


class Rectangle:
    """
    Class Rectangle: creates a rectangle
    Arguments:
          Width : width of rectangle
          Heigth: height of rectangle
    """
    def __init__(self, width=0, height=0):
        """ Initialization of object attributes w __init__ method
        Arguments:
        Width : width of rectangle
        Heigth: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ property"""
        return self.__width

    @property
    def height(self):
        """ property"""
        return self.__height

    @width.setter
    def width(self, value):
        """ Setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ Setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
