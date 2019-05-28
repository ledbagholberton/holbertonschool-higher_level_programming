#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        area = 0
        area = self.__width * self.__height
        return area

    def perimeter(self):
        perimeter = 0
        perimeter = 2 * self.__width + 2 * self.__height
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        return perimeter

    def __str__(self):
        list_rect = []
        if (self.__height * self.__width == 0):
            list_rect.append("")
        else:
            for i in range (self.__height):
                for i in  range (self.__width):
                    list_rect.append("{}".format(self.print_symbol))
                list_rect.append("\n")
        return("".join(list_rect))

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances  -= 1
        print("Bye rectangle...")
