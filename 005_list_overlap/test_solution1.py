import unittest
import random
from solution1 import common_elements
class MyTestCase(unittest.TestCase):
    def test_common_ele(self):
        # Test case 1: Lists with common elements
        list1 = [1, 2, 3, 4, 5]
        list2 = [4, 5, 6, 7, 8]
        self.assertEqual(common_elements(list1, list2), [4, 5])
    def test_common_ele2(self):
        # Test case 2: Lists with no common elements
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        self.assertEqual(common_elements(list1, list2), [])

    def test_common_ele3(self):
        # Test case 3: Lists with all common elements
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        self.assertEqual(common_elements(list1, list2), [1, 2, 3])

    def test_common_ele4(self):
        # Test case 4: Lists with duplicate common elements
        list1 = [1, 1, 2, 2, 3, 3]
        list2 = []
        self.assertEqual(common_elements(list1, list2), [])

    def test_common_ele5(self):
        # Test case 5: Random lists
        list1 = random.sample(range(1, 20), 7)
        list2 = random.sample(range(1, 20), 10)
        expected_result = list(set(list1) & set(list2))
        self.assertEqual(common_elements(list1, list2), expected_result)

if __name__ == '__main__':
    unittest.main()