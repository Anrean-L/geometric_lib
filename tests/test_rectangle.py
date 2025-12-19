import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):
    def test_two_zero_sides_area(self):
        res = rectangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_zero_height_area(self):
        res = rectangle.area(0, 1530)
        self.assertEqual(res, 0)

    def test_zero_width_area(self):
        res = rectangle.area(1043, 0)
        self.assertEqual(res, 0)

    def test_integer_sides_area(self):
        res = rectangle.area(15, 32)
        self.assertEqual(res, 480)

    def test_float_sides_area(self):
        res = rectangle.area(12.44, 62.39)
        self.assertAlmostEqual(res, 776.1316)

    def test_square_area(self):
        res = rectangle.area(4, 4)
        self.assertEqual(res, 16)

    def test_negative_area(self):
        res = rectangle.area(-10, 13)
        self.assertEqual(res, 130)

    def test_two_zero_sides_perimeter(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_zero_height_perimeter(self):
        res = rectangle.perimeter(0, 15)
        self.assertEqual(res, 30)

    def test_zero_width_perimeter(self):
        res = rectangle.perimeter(124, 0)
        self.assertEqual(res, 248)

    def test_float_perimeter(self):
        res = rectangle.perimeter(13.7, 23.69)
        self.assertAlmostEqual(res, 74.78)

    def test_square_perimeter(self):
        res = rectangle.perimeter(12, 12)
        self.assertEqual(res, 48)

    def test_negative_perimeter(self):
        res = rectangle.perimeter(12, -34.5)
        self.assertAlmostEqual(res, 93)

    def test_invalid_type_area(self):
        with self.assertRaises(TypeError):
            rectangle.area("930", 29)

    def test_invalid_type_perimeter(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(None)