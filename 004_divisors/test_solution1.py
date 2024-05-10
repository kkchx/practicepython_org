import unittest
from solution1 import find_divisors
class MyTestCase(unittest.TestCase):
    def test_find_divisors(self):
        self.assertEqual(find_divisors(3), [1, 3])

    def test_find_divisors2(self):
        self.assertEqual(find_divisors(0), [])

    def test_find_divisors3(self):
        self.assertEqual(find_divisors(-2), [])

    def test_find_divisor4(self):
        self.assertEqual(find_divisors(1), [1])

if __name__ == '__main__':
    unittest.main()