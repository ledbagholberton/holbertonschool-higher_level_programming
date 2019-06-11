import unittest
from models.base import Base as BaseClass

"""
class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)
"""
class Pruebas(unittest.TestCase):

    def test_nb(self):
        __nb_objects = 55
        with self.assertRaises(AttributeError)x


    def test_id_1(self):
        b1 = BaseClass()
        self.assertEqual(b1.id, 1)
        b2 = BaseClass()
        self.assertEqual(b2.id, 2)
        b3 = BaseClass(26)
        self.assertEqual(b3.id, 26)
"""
    def test_id_2(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b1.id, 2)
"""
if __name__ == '__main__':
    unittest.main()
