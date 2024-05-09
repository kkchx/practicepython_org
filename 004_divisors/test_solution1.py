import unittest
from solution2 import find_divisors

class MyTestCase(unittest.TestCase):
    def test_num(self):
        self.assertEqual(find_divisors(3), [1, 3])

    def test_num1(self):
        self.assertEqual(find_divisors(16), [1, 2, 4, 8, 16])

    def test_num2(self):
        self.assertEqual(find_divisors(0), [])

if __name__ == '__main__':
    unittest.main()