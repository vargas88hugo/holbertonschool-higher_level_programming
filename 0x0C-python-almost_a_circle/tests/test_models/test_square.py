#!/usr/bin/python3
"""
Unittest for square module
"""
import io
import unittest
import unittest.mock
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Square(unittest.TestCase):
    """ Tests for Square Class """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_get_values(self):
        s1 = Square(10)
        self.assertEqual(s1.size, 10)

    def test_square_set_values(self):
        s1 = Square(1)
        s1.size = 5
        self.assertEqual(s1.size, 5)

    def test_square_id(self):
        s1 = Square(10)
        self.assertEqual(s1.id, 1)
        s2 = Square(2)
        self.assertEqual(s2.id, 2)
        s3 = Square(10, 0, 0, 12)
        self.assertEqual(s3.id, 12)

    def test_square_type(self):
        s1 = Square(10, 2)
        self.assertTrue(type(s1) is Square)
        self.assertIsInstance(s1, Base)
        self.assertIsInstance(s1, Rectangle)

    def test_square_error_width_01(self):
        with self.assertRaises(TypeError) as e:
            s1 = Square("1")
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            s1 = Square([1, 2, 3])
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            s1 = Square(None)
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            s1 = Square(1.5)
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            s1 = Square((1, 2))
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_square_error_width_02(self):
        with self.assertRaises(ValueError) as e:
            s1 = Square(0)
        self.assertEqual(str(e.exception), "width must be > 0")
        with self.assertRaises(ValueError) as e:
            s1 = Square(-10)
        self.assertEqual(str(e.exception), "width must be > 0")
        with self.assertRaises(ValueError) as e:
            s1 = Square(-99999999999999)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_square_error_x_01(self):
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, "0", 0)
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, [1, 2, 3], 0)
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, None, 2)
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 1.5, 2)
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, (1, 2), 2)
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_square_error_x_02(self):
        with self.assertRaises(ValueError) as e:
            s1 = Square(1, -10, 2)
        self.assertEqual(str(e.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as e:
            s1 = Square(1, -99999999999999, 2)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_square_error_y_01(self):
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 0, "0")
        self.assertEqual(str(e.exception), "y must be an integer")
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 0, [1, 2, 3])
        self.assertEqual(str(e.exception), "y must be an integer")
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 2, None)
        self.assertEqual(str(e.exception), "y must be an integer")
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 2, 1.5)
        self.assertEqual(str(e.exception), "y must be an integer")
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 2, (1, 2))
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_square_error_y_02(self):
        with self.assertRaises(ValueError) as e:
            s1 = Square(1, 1, -10)
        self.assertEqual(str(e.exception), "y must be >= 0")
        with self.assertRaises(ValueError) as e:
            s1 = Square(1, 1, -99999999999999)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_square_area(self):
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)
        s2 = Square(2)
        self.assertEqual(s2.area(), 4)
        s3 = Square(8, 0, 0, 12)
        self.assertEqual(s3.area(), 64)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_square_display(self, mock_stdout):
        s1 = Square(4)
        s1.display()
        print("---")
        s2 = Square(2, 2)
        s2.display()
        print("---")
        s1 = Square(2, 3, 2)
        s1.display()
        print("---")
        s2 = Square(3, 2, 1)
        s2.display()
        print("---")
        s1 = Square(1, 1, 0)
        s1.display()
        self.assertEqual(mock_stdout.getvalue(), """####
####
####
####
---
  ##
  ##
---


   ##
   ##
---

  ###
  ###
  ###
---
 #
""")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_square_str(self, mock_stdout):
        s1 = Square(4, 2, 1, 12)
        print(s1)
        s2 = Square(5, 5, 1)
        print(s2)
        self.assertEqual(mock_stdout.getvalue(), """[Square] (12) 2/1 - 4
[Square] (1) 5/1 - 5
""")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_square_update_kwargs(self, mock_stdout):
        s1 = Square(5)
        print(s1)
        s1.update(10)
        print(s1)
        s1.update(1, 2)
        print(s1)
        s1.update(1, 2, 3)
        print(s1)
        s1.update(1, 2, 3, 4)
        print(s1)
        s1.update(x=12)
        print(s1)
        s1.update(size=7, y=1)
        print(s1)
        s1.update(size=7, id=89, y=1)
        print(s1)
        self.assertEqual(mock_stdout.getvalue(),
                         """[Square] (1) 0/0 - 5
[Square] (10) 0/0 - 5
[Square] (1) 0/0 - 2
[Square] (1) 3/0 - 2
[Square] (1) 3/4 - 2
[Square] (1) 12/4 - 2
[Square] (1) 12/1 - 7
[Square] (89) 12/1 - 7
""")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_square_dictionary(self, mock_stdout):
        s1 = Square(10, 2, 1)
        s1_d = s1.to_dictionary()
        self.assertDictEqual(s1_d, {'x': 2, 'y': 1, 'id': 1, 'size': 10})
        s2 = Square(1, 1, 1, 1)
        s2_d = s2.to_dictionary()
        self.assertDictEqual(s2_d, {'x': 1, 'y': 1, 'id': 1, 'size': 1})
        s3 = Square(9, 9, 9, 9)
        s3.update(**s2_d)
        s3_d = s3.to_dictionary()
        self.assertDictEqual(s1_d, {'x': 2, 'y': 1, 'id': 1, 'size': 10})
        print(s1)
        print(s2)
        print(s3)
        self.assertEqual(mock_stdout.getvalue(),
                         """[Square] (1) 2/1 - 10
[Square] (1) 1/1 - 1
[Square] (1) 1/1 - 1
""")

    def tearDown(self):
        pass
