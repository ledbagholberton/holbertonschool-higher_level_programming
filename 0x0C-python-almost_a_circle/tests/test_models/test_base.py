import unittest
from models.base import Base as BaseClass
import pep8


def setUpModule():
        print("I'm setup module")


def tearDownModule():
        print("I'm teardown module")


class TestCodeFormat(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        file1 = "models/base.py"
        file2 = "tests/test_models/test_base.py"
        result = pep8style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Style errors (and warnings).")


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
