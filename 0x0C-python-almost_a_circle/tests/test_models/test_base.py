#!/usr/bin/python3
"""
Unittest for base module
"""
import io
import unittest
import unittest.mock
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_base_json_string(self, mock_stdout):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        self.assertDictEqual(dictionary, {'x': 2, 'y': 8, 'id': 1, 'height': 7,
                                          'width': 10})
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(str([dictionary]).replace("'", '"'), json_dictionary)
        json_empty = Base.to_json_string([])
        self.assertEqual(str([]), json_empty)
        json_none = Base.to_json_string(None)
        self.assertEqual(str([]), json_none)
        print(type(dictionary))
        print(type(json_dictionary))
        self.assertEqual(mock_stdout.getvalue(),
                         """<class 'dict'>
<class 'str'>
""")

    def test_base_save_json(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            data = json.load(f)
        a = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertEqual(a, data)

    def test_base_string_json(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_base_create(self, mock_stdout):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        print(r1)
        print(r2)
        print(r1 is r2)
        print(r1 == r2)
        s1 = Square(3)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        print(s1)
        print(s2)
        print(s1 is s2)
        print(s1 == s2)
        self.assertEqual(mock_stdout.getvalue(),
                         """[Rectangle] (1) 1/0 - 3/5
[Rectangle] (1) 1/0 - 3/5
False
False
[Square] (3) 0/0 - 3
[Square] (3) 0/0 - 3
False
False
""")

    def test_base_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertNotEqual(list_rectangles_input, list_rectangles_output)
        d1 = [i.to_dictionary() for i in list_rectangles_input]
        d2 = [i.to_dictionary() for i in list_rectangles_output]
        self.assertEqual(d1, d2)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
