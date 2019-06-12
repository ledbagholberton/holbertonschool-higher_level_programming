import unittest
from models.base import Base as BaseClass

def setUpModule():
        print("I'm setup module")

def tearDownModule():
        print("I'm teardown module")

class TestBaseClass(unittest.TestCase):
    """
    Setup , teardown
    """
    def setUp(self):
        "test set_up"
        self.b1 = BaseClass()
        self.b2 = BaseClass()
        self.b3 = BaseClass(10)
        self.b4 = BaseClass(56)

    def tearDown(self):
        "test tearDown"
        pass

    def test_id(self):
        "test test_id"
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 10)
        self.assertEqual(self.b4.id, 56)


    @classmethod
    def setUpClass(cls):
        "test Setup cclass"
        print("I'm a setUpClass")

    @classmethod
    def tearDownClass(cls):
        "test tearDown class"
        print("I'm a tearDownClass")

if __name__ == '__main__':
    unittest.main()
