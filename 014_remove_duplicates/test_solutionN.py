import unittest
from SolutionN import remove_duplicates, remove_duplicates_check

class MyTestCase(unittest.TestCase):
    def test_remove_duplicates_with_duplicates(self):
        input_list = [1, 2, 2, 3, 4, 4, 5]
        self.assertEqual(remove_duplicates(input_list), [1, 2, 3, 4, 5])


    def test_remove_duplicates_no_duplicates(self):
        input_list = [1, 2, 3, 4, 5]
        self.assertEqual(remove_duplicates(input_list), [1, 2, 3, 4, 5])


    def test_remove_duplicates_empty_list(self):
        input_list = []
        self.assertEqual(remove_duplicates(input_list), [])


    def test_remove_duplicates_check_with_duplicates(self):
        input_list = [1, 2, 2, 3, 4, 4, 5]
        self.assertEqual(remove_duplicates_check(input_list), [1, 3, 5])


    def test_remove_duplicates_check_no_duplicates(self):
        input_list = [1, 2, 3, 4, 5]
        self.assertEqual(remove_duplicates_check(input_list), [1, 2, 3, 4, 5])


    def test_remove_duplicates_check_empty_list(self):
        input_list = []
        self.assertEqual(remove_duplicates_check(input_list), [])


    def test_remove_duplicates_check_all_duplicates(self):
        input_list = [1, 1, 1, 1, 1]
        self.assertEqual(remove_duplicates_check(input_list), [])


    def test_remove_duplicates_check_mixed_types(self):
        input_list = [1, 'a', 'a', 2, 3, 3, 'b', 'b', 'c']
        self.assertEqual(remove_duplicates_check(input_list), [1, 2, 'c'])

if __name__ == "__main__":
    unittest.main()