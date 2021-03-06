#!/usr/bin/python3
""" Rectangle

"""


class Rectangle:
    """
    Class Rectangle: create a rectangle
    Arguments:
    Width : width of rectangle
    Height: height of rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialization of object attributes w __init__ method"
        Arguments:
        Width : width of rectangle
        Height: height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Instance attribute area"""
        area = 0
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """ Instance attribute perimeter"""
        perimeter = 0
        perimeter = 2 * self.__width + 2 * self.__height
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        return perimeter

    def __str__(self):
        """ Method __str__"""
        list_rect = []
        if (self.__height * self.__width == 0):
            list_rect.append("")
        else:
            for i in range(self.__height):
                for i in range(self.__width):
                    list_rect.append("{}".format(self.print_symbol))
                list_rect.append("\n")
        return("".join(list_rect))

    def __repr__(self):
        """ Method __repr__"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ Method __del__"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
