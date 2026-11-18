# https://github.com/devparikh1512/lab11-DP-VN
# Partner 1: Dev Parikh
# Partner 2: Vishal Naveen
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-4, 5), -20)
        self.assertEqual(mul(0, 9), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertAlmostEqual(div(3, 1), 1 / 3)
        self.assertEqual(div(4, -8), -2)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(5, 1), 0.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 8)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, -1)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), 1.41421356, places=6)
        with self.assertRaises(ValueError):
            square_root(-1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()