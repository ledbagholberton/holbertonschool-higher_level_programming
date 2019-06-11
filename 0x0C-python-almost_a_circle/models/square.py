#!/usr/bin/python3
"""class Square"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Init """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter size """
        return super().width

    @size.setter
    def size(self, size):
        """ setter size """
        super(Square, self.__class__).width.fset(self, size)

    def __str__(self):
        """ __str___ """
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".
                format(self.id, super().x, super().y, self.size))

    def update(self, *args, **kargs):
        """ Update """
        if len(args) is 0:
            for key, value in kargs.items():
                if key == "id":
                    self.id = kargs.get(key)
                if key == "size":
                    self.size = kargs.get(key)
                if key == "x":
                    self.x = kargs.get(key)
                if key == "y":
                    self.y = kargs.get(key)
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
                self.size = my_arg2[1]
            if leng > 2:
                self.x = my_arg2[2]
            if leng > 3:
                self.y = my_arg2[3]

    def to_dictionary(self):
        """ to dictionary"""
        return (super().__dict__)

    def to_dictionary(self):
        my_list = ["height", "width", "x", "y", "id"]
        sorted(super().__dict__)
        list_keys = super().__dict__.keys()
        list_values = super().__dict__.values()
        my_dict = {}
        for elem in list_keys:
            for elem2 in my_list:
                a = elem.find(elem2)
                if a != -1:
                    value = getattr(self, elem2)
                    if elem2 is "width":
                        my_dict.update({"size": value})
                    elif elem2 is "height":
                        pass
                    else:
                        my_dict.update({elem2: value})
        return my_dict
