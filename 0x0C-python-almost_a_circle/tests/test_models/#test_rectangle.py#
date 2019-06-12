import unittest
from models.rectangle import Rectangle as RectangleClass

def setUpModule():
        print("I'm setup module")

def tearDownModule():
        print("I'm teardown module")

class TestRectangleClass(unittest.TestCase):
    """
    Pruebas
    """
    def setUp(self):
        "test setUp"
        self.r1 = RectangleClass(10, 2)
        self.r2 = RectangleClass(20, 4, 1, 1)
        self.r3 = RectangleClass(30, 6, 3, 5, 19)

    def tearDown(self):
        "test tearDown"
        pass

    def test_id_1(self):
        "test id"
        self.assertEqual(self.r1.id, 9)
        self.assertEqual(self.r2.id, 10)
        self.assertEqual(self.r3.id, 19)

    def test_h_1(self):
        "test heigth"
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 4)
        self.assertEqual(self.r3.height, 6)

    def test_w_1(self):
        "test width"
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 20)
        self.assertEqual(self.r3.width, 30)

    def test_x_1(self):
        "test x pos"
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 1)
        self.assertEqual(self.r3.x, 3)

    def test_y_1(self):
        "test y pos"
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 1)
        self.assertEqual(self.r3.y, 5)

    def test_area_1(self):
        "test area"
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 80)
        self.assertEqual(self.r3.area(), 180)

    def test_errors(self):
        with self.assertRaises(TypeError):
            self.r3.height = "A"
            self.r2.height = "A"
            self.r1.height = "A"

        with self.assertRaises(TypeError):
            self.r3.width = "B"
            self.r2.width = "B"
            self.r1.width = "B"

        with self.assertRaises(TypeError):
            self.r3.x = "C"
            self.r2.x = "C"
            self.r1.x = "C"

        with self.assertRaises(TypeError):
            self.r3.y = "Y"
            self.r2.y = "Y"
            self.r1.y = "Y"

        with self.assertRaises(ValueError):
            self.r3.height = -52
            self.r2.height = -52
            self.r1.height = -52

        with self.assertRaises(ValueError):
            self.r3.width = -26
            self.r2.width = -26
            self.r1.width = -26

        with self.assertRaises(ValueError):
            self.r3.x = -4
            self.r2.x = -5
            self.r1.x = -6

        with self.assertRaises(ValueError):
            self.r3.y = -7
            self.r2.y = -8
            self.r1.y = -9

    def test_update(self):
        self.r1.update(526)
        self.assertEqual(self.r1.id, 526)

        self.r1.update(526, 4)
        self.assertEqual(self.r1.width, 4)

        self.r1.update(526, 4, 6)
        self.assertEqual(self.r1.height, 6)

        self.r1.update(89, 4, 6, 15)
        self.assertEqual(self.r1.x, 15)

        self.r1.update(89, 4, 6, 15, 30)
        self.assertEqual(self.r1.y, 30)

    def test_update_2(self):
        self.r1.update(height=5)
        self.assertEqual(self.r1.height, 5)

        self.r1.update(width=15, x=25)
        self.assertEqual(self.r1.width, 15)
        self.assertEqual(self.r1.x, 25)

        self.r1.update(width=25, x=35, id=89)
        self.assertEqual(self.r1.width, 25)
        self.assertEqual(self.r1.x, 35)
        self.assertEqual(self.r1.id, 89)

        self.r1.update(x=15, height=25, y=35, width=45)
        self.assertEqual(self.r1.x, 15)
        self.assertEqual(self.r1.height, 25)
        self.assertEqual(self.r1.y, 35)
        self.assertEqual(self.r1.width, 45)

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
