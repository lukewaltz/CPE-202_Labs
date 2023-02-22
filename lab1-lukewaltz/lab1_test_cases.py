import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter_1(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_2(self):
        tlist = [1, 2, 5, 4, 3, 1]
        self.assertEqual(max_list_iter(tlist), 5)  # regular list

    def test_max_list_iter_3(self):
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)  # empty list return none

    def test_max_list_iter_4(self):
        tlist = [-10, -7, -6, -4]
        self.assertEqual(max_list_iter(tlist), -4)  # negatives

    def test_reverse_rec_1(self):
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])

    def test_reverse_rec_2(self):  # list is None
        int_list = None
        with self.assertRaises(ValueError):
            reverse_rec(int_list)

    def test_reverse_rec_3(self):  # list length 1
        int_list = [1]
        self.assertEqual(reverse_rec(int_list), [1])

    def test_bin_search_1(self):  # target, low, high, int_list - Target is middle
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        target = 4
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(target, low, high, list_val), 4)

    def test_bin_search_2(self):  # empty list
        list_val = []
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), None)

    def test_bin_search_3(self):  # list is None
        list_val = None
        low = 0
        high = 2
        target = 1
        with self.assertRaises(ValueError):
            bin_search(target, low, high, list_val)

    def test_bin_search_4(self):  # target is outside of high and low
        list_val = [1, 2, 3, 4, 5, 6, 7, 8]
        low = 0
        high = 4
        target = 7
        self.assertEqual(bin_search(target, low, high, list_val), None)

    def test_bin_search_5(self):  # target is in upper half
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        target = 8
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(target, low, high, list_val), 6)

    def test_bin_search_6(self):  # target is in lower half
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        target = 2
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(target, low, high, list_val), 2)

    def test_bin_search_7(self):  # low > high
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        target = 4
        low = 5
        high = 2
        self.assertEqual(bin_search(target, low, high, list_val), None)

    def test_bin_search_8(self):  # repeated numbers part 1
        list_val = [0, 2, 2, 3, 4, 6, 9, 9, 10]
        target = 2
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(target, low, high, list_val), 1)

    def test_bin_search_9(self):  # repeated numbers part 2
        list_val = [0, 2, 2, 3, 4, 7, 9, 9, 10]
        target = 9
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(target, low, high, list_val), 6)

    def test_bin_search_10(self):  # Negative int
        list_val = [-3, -2, -1, 0, 2]
        target = -1
        low = -3
        high = len(list_val) - 1
        self.assertEqual(bin_search(target, low, high, list_val), 2)

    def test_reverse_list_mutate_1(self):
        int_list = [1, 2, 3, 4, 5]
        reverse_list_mutate(int_list)
        self.assertListEqual(int_list, [5, 4, 3, 2, 1])
        self.assertEqual(reverse_list_mutate(int_list), None)

    def test_reverse_mutate_2(self):
        int_list = []
        reverse_list_mutate(int_list)
        self.assertEqual(int_list, [])
        self.assertEqual(reverse_list_mutate(int_list), None)  # empty list

    def test_reverse_mutate_3(self):
        int_list = None
        with self.assertRaises(ValueError):  # list is None
            reverse_list_mutate(int_list)

    def test_reverse_mutate_4(self):
        int_list = [1]
        reverse_list_mutate(int_list)
        self.assertEqual(int_list, [1])
        self.assertEqual(reverse_list_mutate(int_list), None)  # list len 1


if __name__ == "__main__":
    unittest.main()
