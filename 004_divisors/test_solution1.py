import unittest

class MyTestCase(unittest.TestCase):
    def test_num(self):
        num = 2
        list_range = list(range(1, num + 1))
        divisor_list = []
        for number in list_range:
            if num % number == 0:
                divisor_list.append(number)
        self.assertEqual(divisor_list, [1, 2])

    def test_num1(self):
        num2 = 3
        list_range = list(range(1, num2 + 1))
        divisor_list = []
        for number in list_range:
            if num2 % number == 0:
                divisor_list.append(number)
        self.assertEqual(divisor_list, [1, 3])

    def test_num2(self):
        num3 = "a"
        list_range = list(range(1, num3 + 1))
        divisor_list = []
        for number in list_range:
            if num3 % number == 0:
                divisor_list.append(number)
        self.assertEqual(divisor_list, "a")

if __name__ == '__main__':
    unittest.main()