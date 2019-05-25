#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

  def t_max(self):
    my_l = [1, 2, 3, 4, 7]
    self.assertEqual(7, max_integer(my_l))

  def t_neg(self):
    my_l = [-1, -4, -5, 0]
    self.assertEqual(0, max_integer(my_l))

  def t_empty(self):
    my_l = []
    self.assertEqual(None, max_integer(my_l))

  def t_none(self):
    my_l = None
    self.assertEqual(None, max_integer(my_l))

  def t_empty(self):
    my_l = []
    self.assertEqual(None, max_integer(my_l))

  def t_None(self):
    my_l = None
    with self.assertRaises(TypeError):
      max_integer(my_l)

if __name__ == '__main__':
    unittest.main()
