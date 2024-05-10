import unittest
from solution3 import main

class MyTestCase(unittest.TestCase):
    def test_name(self):
        user_entry = ["a", 10, 2024]
        self.assertEqual(main(user_entry), 2114)

    def test_name2(self):
        user_entry2 = [1, 10, 2024]
        self.assertEqual(main(user_entry2), 2114)

    def test_age(self):
        user_entry3 = ["a", 10, 2024]
        self.assertEqual(main(user_entry3), 2114)

    def test_age2(self):
        user_entry4 = ["a", 9, 2024]
        self.assertEqual(main(user_entry4), 2115)

    def test_year(self):
        user_entry5 = ["a", 10, 2024]
        self.assertEqual(main(user_entry5), 2114)

    def test_year2(self):
        user_entry6 = [6, 10, 2024]
        self.assertEqual(main(user_entry6), 2114)

if __name__ == '__main__':
    unittest.main()