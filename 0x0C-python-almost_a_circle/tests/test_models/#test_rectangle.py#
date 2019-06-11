import unittest
from models.rectangle import Rectangle as RectangleClass

class Pruebas(unittest.TestCase):
    """
    def test_nb(self):
        __nb_objects = 55
        raise AttributeError()
    """
    def test_id_1(self):
        b1 = RectangleClass(10, 2)
        self.assertEqual(b1.id, 1)
        b2 = RectangleClass(2, 10)
        self.assertEqual(b2.id, 2)
        b3 = RectangleClass(10, 2, 0, 0, 26)
        self.assertEqual(b3.id, 26)
        with Assertion(TypeError):
            b4 = RectangleClass(10, "2")
            b5 = RectangleClass("10", 2)
            b6 = RectangleClass("10", 2)
            b7 = RectangleClass("10", 2)


        r = Rectangle(10, 2)
        r.width = -10
        raise [ValueError] width must be > 0
        r = Rectangle(10, 2)
        r.x = {}
        raise [ValueError] x must be an integer
        r = Rectangle(10, 2, 3, -1)
        raise [ValueError] y must be > 0
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area, 6)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area, 56)

"""
r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

    def test_id_2(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b1.id, 2)
"""
if __name__ == '__main__':
    unittest.main()
