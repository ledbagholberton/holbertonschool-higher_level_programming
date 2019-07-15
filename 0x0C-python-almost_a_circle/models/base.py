#!/usr/bin/python3
""" class base """
import json
import csv
import turtle


class Base:
    """ Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init method"""
        self.id = id
        if self.id is not None:
            pass
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ static method to_json_string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            a = json.dumps(list_dictionaries)
            return (a)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save to file """
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
        """ Static method """
        if (json_string is None) or (len(json_string) == 0):
            return([])
        else:
            return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ Create """
        if cls.__name__ == "Rectangle":
            dummy_rc = cls(1, 1)
        else:
            dummy_rc = cls(1)
        dummy_rc.update(**dictionary)
        return dummy_rc

    @classmethod
    def load_from_file(cls):
        """ load_from_file """
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
        """ save_to_file_csv """
        names_rec = ["id", "width", "height", "x", "y"]
        names_squ = ["id", "size", "x", "y"]
        filename = cls.__name__ + ".csv"
        if cls.__name__ is "Rectangle":
            names = names_rec
        else:
            names = names_squ
        with open(filename, mode='w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=names)
            if list_objs is None:
                csv_writer.writerow([[]])
            else:
                csv_writer.writeheader()
                for a in list_objs:
                    csv_writer.writerow(a.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ load from file """
        filename = cls.__name__ + ".csv"
        my_list = []
        try:
            with open(filename, newline='') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    for keys, values in row.items():
                        row[keys] = int(values)
                    my_list.append(row)
                return [cls.create(**a) for a in my_list]
        except IOError:
            return []
"""
    @staticmethod
    def draw(list_rectangles, list_squares):
        "draw with turtle"
        for elem in list_rectangles:
            turtle.penup()
            turtle.home()
            turtle.color("green")
            turtle.setpos(elem.x, elem.y)
            turtle.pendown()
            turtle.forward(elem.width)
            turtle.left(90)
            turtle.forward(elem.height)
            turtle.left(90)
            turtle.forward(elem.width)
            turtle.left(90)
            turtle.forward(elem.height)
        for elem in list_squares:
            turtle.penup()
            turtle.home()
            turtle.color("red")
            turtle.setpos(elem.x, elem.y)
            turtle.pendown()
            turtle.forward(elem.size)
            turtle.left(90)
            turtle.forward(elem.size)
            turtle.left(90)
            turtle.forward(elem.size)
            turtle.left(90)
            turtle.forward(elem.size)
        turtle.exitonclick()
"""
    @staticmethod
    def draw(list_rectangles, list_squares):
    """
    class to create a rectangle object
    """
        ventana = turtle.Screen()
        lapiz = turtle.Turtle()
    
        lapiz.pensize(2)
    
        for info in list_rectangles:
            R = random.random()
            B = random.random()
            G = random.random()
            lapiz.color(R, G, B)
            print(info.x)
            lapiz.up()
            lapiz.setx(info.x)
            lapiz.sety(info.y)
            lapiz.down()
            lapiz.begin_fill()
            for i in range(2):
                lapiz.forward(info.width)
                lapiz.right(90)
                lapiz.forward(info.height)
                lapiz.right(90)
            lapiz.end_fill()

        for info in list_squares:
            R = random.random()
            B = random.random()
            G = random.random()
            lapiz.color(R, G, B)
            print(info.x)
            lapiz.up()
            lapiz.setx(info.x)
            lapiz.sety(info.y)
            lapiz.down()
            lapiz.begin_fill()
            for i in range(2):
                lapiz.forward(info.width)
                lapiz.right(90)
                lapiz.forward(info.height)
                lapiz.right(90)
            lapiz.end_fill()
        ventana.exitonclick()
        """
        t = turtle.Turtle()
        t.forward(100)
        turtle.done()
        """
