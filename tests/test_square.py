import unittest
import square

class SquareTestCase(unittest.TestCase):
    def test_zero_side_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_integer_side_area(self):
        res = square.area(15)
        self.assertEqual(res, 225)

    def test_float_side_area(self):
        res = square.area(12.4)
        self.assertAlmostEqual(res, 153.76)

    def test_negative_side_area(self):
        res = square.area(-4)
        self.assertEqual(res, 16)

    def test_zero_side_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_integer_side_perimeter(self):
        res = square.perimeter(15)
        self.assertEqual(res, 60)

    def test_float_side_perimeter(self):
        res = square.perimeter(12.4)
        self.assertAlmostEqual(res, 49.6)

    def test_negative_side_perimeter(self):
        res = square.perimeter(-4)
        self.assertEqual(res, 16)