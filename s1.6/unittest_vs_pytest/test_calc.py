import unittest

from calc import square, cube


class Test(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)

    def test_cube(self):
        self.assertEqual(cube(2), 8)