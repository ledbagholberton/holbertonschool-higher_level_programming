#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""
    def __init__(self, width, height):
        """ __init__    """
        self.__width = width
        self.__height = height
        Rectangle.integer_validator(self, "width", width)
        Rectangle.integer_validator(self, "height", height)
        self.__area = self.__width * self.__height

    def area(self):
        """Area func"""
        return(self.__area)

    def __str__(self):
        """__str___"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
