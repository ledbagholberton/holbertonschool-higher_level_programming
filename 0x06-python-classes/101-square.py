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

    def __str__(self):
        list_print = []
        if self.size == 0:
            list_print.append("\n")
        else:
            for a in range(self.position[1]):
                list_print.append("\n")
            for i in range(self.size):
                for a in range(self.position[0]):
                    list_print.append("_")
                for j in range(self.size):
                    list_print.append("#")
                list_print.append("\n")
        return("".join(list_print))

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) > 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int or type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
            self.__area = self.__size * self.__size
