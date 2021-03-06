#!/usr/bin/python3
from models.base import Base
class Rectangle(Base):
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
                raise TypeError("width must be integer")
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
                raise TypeError("height must be integer")
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
                raise TypeError("x must be integer")
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
                raise TypeError("y must be integer")
            elif y < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = y
