#!/usr/bin/python3
""" Student module
"""


class Student:
    """ class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            my_dict = {}
            cla = self.__dict__.keys()
            val = self.__dict__.keys()
            for elem in attrs:
                if elem in cla:
                    value = getattr(self, elem)
                    my_dict.update({elem: value})
            return my_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        dic = json
        for key, value in zip(dic.keys(), dic.values()):
            setattr(self, key, value)
