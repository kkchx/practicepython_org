import unittest
from SolutionN import fibonacci

class MyTestCase(unittest.TestCase):
    def test_fibonacci(self):
        limit = 10
        self.assertEqual(fibonacci(limit), [0, 1, 1, 2, 3, 5, 8])

    def test_fibonacci2(self):
        limit = 0
        self.assertEqual(fibonacci(limit), [0, 1])

    def test_fibonacci3(self):
        limit = -1
        self.assertEqual(fibonacci(limit), [0, 1])

    def test_fibonacci4(self):
        limit = 3
        self.assertEqual(fibonacci(limit), [0, 1, 1, 2, 3])
if __name__ == '__main__':
    unittest.main()
