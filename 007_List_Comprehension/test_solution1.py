import unittest
from solution1 import list_sorter


class MyTestCase(unittest.TestCase):
    def test_list(self):
        list1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(list_sorter(list1), [8, 6, 4, 2])

    def test_list2(self):
        list2 = [1,3,5,7,9,11]
        self.assertEqual(list_sorter(list2), [])

    def test_list3(self):
        list3 = [8,11,13]
        self.assertEqual(list_sorter(list3), [8])

if __name__ == '__main__':
    unittest.main()
