#!/usr/bin/python3
class Square:
    __area = 0

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__area

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for a in range(self.position[1]):
                print()
            for i in range(self.size):
                for a in range(self.position[0]):
                    print("_", end="")
                for j in range(self.size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(position) > 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(position[0]) is not int or type(position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__area = self.__size * self.__size
