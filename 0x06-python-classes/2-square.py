#!/usr/bin/python3
class Square:
    def __init__(self, size):
        try:
            if size < 0:
                    print("size must be >= 0")
            else:
                self.__size = size
        except (TypeError, ValueError):
            print("size must be an integer")
