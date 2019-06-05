#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        Rectangle.__init__(self, size, size)
        Rectangle.integer_validator(self, "size", size)
        self.__area = self.__size * self.__size

    def area(self):
        return(self.__area)
