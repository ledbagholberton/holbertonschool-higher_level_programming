#!/usr/bin/python3
import json
import csv


class Base:
    """ Class Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        a = json.dumps(list_dictionaries)
        return (a)

    @classmethod
    def save_to_file(cls, list_objs):
        json_list = []
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        my_file = open(filename, "w")
        for elem in list_objs:
            a = elem.to_dictionary()
            json_list.append(a)
        json_file = cls.to_json_string(json_list)
        my_file.write(json_file)
        my_file.close

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) is 0:
            return []
        else:
            return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        dummy_rc = cls(1, 1)
        dummy_rc.update(**dictionary)
        return dummy_rc

    @classmethod
    def load_from_file(cls):

        b = []
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                b = cls.from_json_string(file.read())
            for i, j in enumerate(b):
                b[i] = cls.create(**b[i])
            return b
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        csv_list = []
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')

    @classmethod
    def load_from_file_csv(cls):
        b = []
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
            return csv_reader
        except IOError:
            return []
