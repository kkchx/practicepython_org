import unittest
from solution3 import check_number

class TestCheckNumber(unittest.TestCase):
    def test_multiple_of_4(self):
        self.assertEqual(check_number(12, 3), "12 is a multiple of 4\n12 divides evenly by 3")

    def test_even_number(self):
        self.assertEqual(check_number(6, 3), "6 is an even number\n6 divides evenly by 3")

    def test_odd_number(self):
        self.assertEqual(check_number(5, 3), "5 is an odd number\n5 does not divide evenly by 3")

    def test_divides_evenly(self):
        self.assertEqual(check_number(12, 3), "12 is a multiple of 4\n12 divides evenly by 3")

    def test_does_not_divide_evenly(self):
        self.assertEqual(check_number(13, 3), "13 is an odd number\n13 does not divide evenly by 3")

if __name__ == '__main__':
    unittest.main()