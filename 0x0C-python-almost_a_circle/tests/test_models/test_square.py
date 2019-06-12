import unittest
from models.square import Square as SquareClass


def setUpModule():
        print("I'm setup module from Square")


def tearDownModule():
        print("I'm teardown module from Square")


class TestSquareClass(unittest.TestCase):
    """
    Pruebas
    """
    def setUp(self):
        "test setUp"
        self.s1 = SquareClass(10)
        self.s2 = SquareClass(20, 1, 1)
        self.s3 = SquareClass(30, 3, 5, 19)

    def tearDown(self):
        "test tearDown"
        pass

    def test_id_1(self):
        "test id"
        self.assertEqual(self.s1.id, 25)
        self.assertEqual(self.s2.id, 26)
        self.assertEqual(self.s3.id, 19)

    def test_s_1(self):
        "test size"
        self.assertEqual(self.s1.size, 10)
        self.assertEqual(self.s2.size, 20)
        self.assertEqual(self.s3.size, 30)

    def test_x_1(self):
        "test x pos"
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 1)
        self.assertEqual(self.s3.x, 3)

    def test_y_1(self):
        "test y pos"
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 1)
        self.assertEqual(self.s3.y, 5)

    def test_area_1(self):
        "test area"
        self.assertEqual(self.s1.area(), 100)
        self.assertEqual(self.s2.area(), 400)
        self.assertEqual(self.s3.area(), 900)

    def test_update(self):
        self.s1.update(526)
        self.assertEqual(self.s1.id, 526)

        self.s1.update(526, 4)
        self.assertEqual(self.s1.size, 4)

        self.s1.update(526, 4, 6)
        self.assertEqual(self.s1.x, 6)

        self.s1.update(89, 4, 6, 15)
        self.assertEqual(self.s1.y, 15)

    def test_update_2(self):
        self.s1.update(size=5)
        self.assertEqual(self.s1.size, 5)

        self.s1.update(size=15, x=25)
        self.assertEqual(self.s1.size, 15)
        self.assertEqual(self.s1.x, 25)

        self.s1.update(size=25, x=35, id=89)
        self.assertEqual(self.s1.size, 25)
        self.assertEqual(self.s1.x, 35)
        self.assertEqual(self.s1.id, 89)

    def test_errors(self):
        with self.assertRaises(TypeError):
            self.s3.size = "A"
            self.s2.size = "A"
            self.s1.size = "A"

        with self.assertRaises(TypeError):
            self.s3.x = "C"
            self.s2.x = "C"
            self.s1.x = "C"

        with self.assertRaises(TypeError):
            self.s3.y = "Y"
            self.s2.y = "Y"
            self.s1.y = "Y"

        with self.assertRaises(ValueError):
            self.s3.size = -52
            self.s2.size = -52
            self.s1.size = -52

        with self.assertRaises(ValueError):
            self.s3.x = -4
            self.s2.x = -5
            self.s1.x = -6

        with self.assertRaises(ValueError):
            self.s3.y = -7
            self.s2.y = -8
            self.s1.y = -9

    @classmethod
    def setUpClass(cls):
        "test Setup cclass"
        print("I'm a setUpClass from Square")

    @classmethod
    def tearDownClass(cls):
        "test tearDown class"
        print("I'm a tearDownClass from Square")

if __name__ == '__main__':
    unittest.main()
