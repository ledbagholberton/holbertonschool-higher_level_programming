#!/usr/bin/python3
class Square:
    __area = 0
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__area = self.__size * self.__size

    def area(self):
        return self.__area
