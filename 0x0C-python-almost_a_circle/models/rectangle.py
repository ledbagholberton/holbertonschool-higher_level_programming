#!/usr/bin/python3
""" class rectangle """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        self.area = self.__width * self.__height
        return self.area

    def display(self):
        for i in range(self.__x):
            print()
        for i in range(self.__height):
            for h in range(self.__y):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y,
                       self.__width, self.__height))

    def update(self, *args, **kargs):
        if len(args) is 0:
            for key, value in kargs.items():
                if key == "id":
                    self.id = kargs.get(key)
                if key == "width":
                    self.__width = kargs.get(key)
                if key == "height":
                    self.__height = kargs.get(key)
                if key == "x":
                    self.__x = kargs.get(key)
                if key == "y":
                    self.__y = kargs.get(key)
        else:
            my_arg2 = []
            for arg in args:
                my_arg2.append(arg)
            leng = len(my_arg2)
            if leng == 0:
                pass
            if leng > 0:
                self.id = my_arg2[0]
            if leng > 1:
                self.__width = my_arg2[1]
            if leng > 2:
                self.__height = my_arg2[2]
            if leng > 3:
                self.__x = my_arg2[3]
            if leng > 4:
                self.__y = my_arg2[4]

    def to_dictionary(self):
        my_list = ["height", "width", "x", "y", "id"]
        sorted(self.__dict__)
        list_keys = self.__dict__.keys()
        list_values = self.__dict__.values()
        my_dict = {}
        for elem in list_keys:
            for elem2 in my_list:
                a = elem.find(elem2)
                if a != -1:
                    value = getattr(self, elem2)
                    my_dict.update({elem2: value})
        return my_dict
