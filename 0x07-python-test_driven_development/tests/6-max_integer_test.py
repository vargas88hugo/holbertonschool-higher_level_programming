"""
Unittest for 6-max_integer function
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Test for integers """
    def test_integers(self):
        self.assertEqual(max_integer(
            []
        ), None)
        self.assertEqual(max_integer(
            [1, 2, 3, 4, 5]
        ), 5)
        self.assertEqual(max_integer(
           [0, -2, -3, -4, -5]
        ), 0)
        self.assertEqual(max_integer(
            [-9999999999999999999, 1, 2]
        ), 2)
        self.assertEqual(max_integer(
            [2, 2, 2]
        ), 2)
        self.assertEqual(max_integer(
            [2]
        ), 2)

    """ Test for floats """
    def test_floats(self):
        self.assertEqual(max_integer(
            [0.5, 0.6, 0.7, 0.8]
        ), 0.8)
        self.assertEqual(max_integer(
            [0.5, 0.06, 0.07, 0.08]
        ), 0.5)
        self.assertEqual(max_integer(
            [-0.5, 0.06, 0.07, 0.08]
        ), 0.08)
        self.assertEqual(max_integer(
            [-999999999.5, 999999999.06, 99999.07, 99999999999999999.08]
        ), 99999999999999999.08)
        self.assertEqual(max_integer(
            [2.2, 2.2, 2.2]
        ), 2.2)

    """ Test for Strings """
    def test_strings(self):
        self.assertEqual(max_integer(
            ["1", "2", "3"]
        ), "3")
        self.assertEqual(max_integer(
            "Hello World"
        ), "r")

    """ Test for Errors """
    def test_errors(self):
        with self.assertRaises(TypeError):
            max_integer(
                [None, None, 1]
            )
        with self.assertRaises(TypeError):
            max_integer(
                12345
            )
        with self.assertRaises(TypeError):
            max_integer(
                1234.1234
            )


if __name__ == '__main__':
    unittest.main()
