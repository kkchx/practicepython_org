import unittest
from solution1 import first_last
class MyTestCase(unittest.TestCase):
    def test_list(self):
        test_list = [0, 1, 2]
        self.assertEqual(first_last(test_list),[0, 2])

    def test_list1(self):
        test_list1 = []
        self.assertEqual(first_last(test_list1),None)

    def test_list2(self):
        test_list2 = [3]
        self.assertEqual(first_last(test_list2),[3, 3])

    def test_list3(self):
        test_list3 = [0, 1, 2, 3]
        self.assertEqual(first_last(test_list3),[0, 3])

if __name__ == '__main__':
    unittest.main()