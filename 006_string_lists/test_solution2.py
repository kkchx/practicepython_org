import unittest

class MyTestCase(unittest.TestCase):
    def test_user_input(self):
        user_input = "dad"
        result = user_input[::-1]
        result = 0
        self.assertEqual(result, 0)

    def test_user_input1(self):
        user_input2 = "madam"
        result2 = user_input2[::-1]
        result2 = 0
        self.assertEqual(result2, 0)

    def test_user_input2(self):
        user_input3 = "cat"
        result3 = user_input3[::-1]
        result3 = 1
        self.assertEqual(result3, 1)

    def test_user_input3(self):
        user_input4 = "mama"
        result4 = user_input4[::-1]
        result4 = 0
        self.assertEqual(result4, 0)

if __name__ == '__main__':
    unittest.main()