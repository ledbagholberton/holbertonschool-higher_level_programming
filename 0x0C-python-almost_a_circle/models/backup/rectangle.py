#!/usr/bin/python3
from models.base import Base
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, width):
            self.__width = width

        @width.getter
        def get_width(self):
            return self.__width

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, height):
            self.__height = height

        @height.getter
        def get_height(self):
            return self.__height

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, x):
            self.__x = x

        @x.getter
        def get_x(self):
            return self.__x

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, y):
            self.__y = y

        @y.getter
        def get_y(self):
            return self.__y
