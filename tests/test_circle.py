import unittest
import circle

class CircleTestCase(unittest.TestCase):
    def test_zero_radius_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_integer_radius_area(self):
        res = circle.area(15)
        self.assertAlmostEqual(res, 706.8583471)

    def test_float_radius_area(self):
        res = circle.area(12.4)
        self.assertAlmostEqual(res, 483.0512864)

    def test_negative_radius_area(self):
        res = circle.area(-4)
        self.assertAlmostEqual(res, 50.2654825)

    def test_zero_radius_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_integer_radius_perimeter(self):
        res = circle.perimeter(15)
        self.assertAlmostEqual(res, 94.2477796)

    def test_float_radius_perimeter(self):
        res = circle.perimeter(12.4)
        self.assertAlmostEqual(res, 77.9114978)

    def test_negative_radius_perimeter(self):
        res = circle.perimeter(-4)
        self.assertAlmostEqual(res, 25.1327412)

    def test_invalid_type_perimeter(self):
        with self.assertRaises(TypeError):
            circle.perimeter("test")

    def test_invalid_type_perimeter(self):
        with self.assertRaises(TypeError):
            circle.perimeter("asdf")