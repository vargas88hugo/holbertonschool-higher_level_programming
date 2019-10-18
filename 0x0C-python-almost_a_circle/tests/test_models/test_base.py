#!/usr/bin/python3
"""
Unittest for base module
"""
import unittest
from models.base import Base


class TestMaxInteger(unittest.TestCase):
    """ Tests for Base Class """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_base_type(self):
        b1 = Base()
        self.assertTrue(type(b1) is Base)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
