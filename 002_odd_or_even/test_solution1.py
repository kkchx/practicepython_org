import unittest

class MyTestCase(unittest.TestCase):
    def test_num1(self):
        num = 1
        mod = num % 2
        self.assertEqual(mod, 1)

    def test_num2(self):
        num = 2
        mod = num % 2
        self.assertEqual(mod, 0)

    def test_num3(self):
        num = "a"
        mod = num % 2
        self.assertEqual(mod, "a")

if __name__ == '__main__':
    unittest.main()
