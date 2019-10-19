#!/usr/bin/python3
"""
Unittest for base module
"""
import io
import unittest
import unittest.mock
from models.base import Base
from models.rectangle import Rectangle


class TestMaxInteger(unittest.TestCase):
    """ Tests for Rectangle Class """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle_get_values(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

    def test_rectangle_set_values(self):
        r1 = Rectangle(1, 1)
        r1.width = 5
        r1.height = 6
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 6)

    def test_rectangle_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_rectangle_type(self):
        r1 = Rectangle(10, 2)
        self.assertTrue(type(r1) is Rectangle)
        self.assertIsInstance(r1, Base)

    def test_rectangle_error_width_01(self):
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle("1", 2)
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle([1, 2, 3], 2)
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(None, 2)
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1.5, 2)
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle((1, 2), 2)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_rectangle_error_width_02(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(-10, 2)
        self.assertEqual(str(e.exception), "width must be > 0")
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(-99999999999999, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_rectangle_error_height_01(self):
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(2, "1")
        self.assertEqual(str(e.exception), "height must be an integer")
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(2, [1, 2, 3])
        self.assertEqual(str(e.exception), "height must be an integer")
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(2, None)
        self.assertEqual(str(e.exception), "height must be an integer")
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(2, 1.5)
        self.assertEqual(str(e.exception), "height must be an integer")
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(2, (1, 2))
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_rectangle_error_height_02(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(2, 0)
        self.assertEqual(str(e.exception), "height must be > 0")
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(2, -10)
        self.assertEqual(str(e.exception), "height must be > 0")
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(2, -99999999999999)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_rectangle_error_x_01(self):
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, "0", 0)
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, [1, 2, 3], 0)
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, None, 2)
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, 1.5, 2)
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, (1, 2), 2)
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_rectangle_error_x_02(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(1, 2, -10, 2)
        self.assertEqual(str(e.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(1, 2, -99999999999999, 2)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_rectangle_error_y_01(self):
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, 0, "0")
        self.assertEqual(str(e.exception), "y must be an integer")
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, 0, [1, 2, 3])
        self.assertEqual(str(e.exception), "y must be an integer")
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, 2, None)
        self.assertEqual(str(e.exception), "y must be an integer")
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, 2, 1.5)
        self.assertEqual(str(e.exception), "y must be an integer")
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, 2, (1, 2))
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_rectangle_error_y_02(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(1, 2, 1, -10)
        self.assertEqual(str(e.exception), "y must be >= 0")
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(1, 2, 1, -99999999999999)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_rectangle_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_rectangle_display(self, mock_stdout):
        r1 = Rectangle(4, 6)
        r1.display()
        print("---")
        r2 = Rectangle(2, 2)
        r2.display()
        print("---")
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        print("---")
        r2 = Rectangle(3, 2, 1, 0)
        r2.display()
        print("---")
        r2 = Rectangle(1, 1, 0, 0)
        r2.display()
        self.assertEqual(mock_stdout.getvalue(), """####
####
####
####
####
####
---
##
##
---


  ##
  ##
  ##
---
 ###
 ###
---
#
""")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_rectangle_str(self, mock_stdout):
        r1 = Rectangle(4, 6, 2, 1, 12)
        print(r1)
        r2 = Rectangle(5, 5, 1)
        print(r2)
        self.assertEqual(mock_stdout.getvalue(), """[Rectangle] (12) 2/1 - 4/6
[Rectangle] (1) 1/0 - 5/5
""")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_rectangle_str(self, mock_stdout):
        r1 = Rectangle(10, 10, 10, 10)
        print(r1)
        r1.update(89)
        print(r1)
        r1.update(89, 2)
        print(r1)
        r1.update(89, 2, 3)
        print(r1)
        r1.update(89, 2, 3, 4)
        print(r1)
        r1.update(89, 2, 3, 4, 5)
        print(r1)
        self.assertEqual(mock_stdout.getvalue(),
                         """[Rectangle] (1) 10/10 - 10/10
[Rectangle] (89) 10/10 - 10/10
[Rectangle] (89) 10/10 - 2/10
[Rectangle] (89) 10/10 - 2/3
[Rectangle] (89) 4/10 - 2/3
[Rectangle] (89) 4/5 - 2/3
""")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()