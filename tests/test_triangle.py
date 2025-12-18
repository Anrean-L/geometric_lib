import unittest
import triangle

class TriangleTestCase(unittest.TestCase):
    def test_zero_side_area(self):
        res = triangle.area(0, 7)
        self.assertEqual(res, 0)

    def test_zero_height_area(self):
        res = triangle.area(3, 0)
        self.assertEqual(res, 0)

    def test_integer_args_area(self):
        res = triangle.area(15, 12)
        self.assertEqual(res, 90)

    def test_odd_args_area(self):
        res = triangle.area(15, 11)
        self.assertEqual(res, 82.5)

    def test_float_args_area(self):
        res = triangle.area(4.83, 5.87)
        self.assertAlmostEqual(res, 14.17605)

    def test_negative_area(self):
        res = triangle.area(-4, 4)
        self.assertEqual(res, 8)

    def test_zero_sides_perimeter(self):
        res = triangle.perimeter(0, 2, 7)
        self.assertEqual(res, 9)

    def test_integer_side_perimeter(self):
        res = triangle.perimeter(15, 4, 9)
        self.assertEqual(res, 28)

    def test_float_side_perimeter(self):
        res = triangle.perimeter(12.4, 15.8, 10.5)
        self.assertAlmostEqual(res, 38.7)

    def test_negative_side_perimeter(self):
        res = triangle.perimeter(-4, -5, 3)
        self.assertEqual(res, 12)