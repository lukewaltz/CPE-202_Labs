import unittest
from ordered_list import *


class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_add_to_middle(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        t_list.add(40)
        t_list.add(50)
        self.assertEqual(t_list.size(), 4)
        self.assertFalse(t_list.is_empty())
        self.assertTrue(t_list.search(10))
        self.assertEqual(t_list.index(40), 2)
        t_list.add(30)
        self.assertEqual(t_list.index(30), 2)
        t_list.remove(10)
        self.assertEqual(t_list.index(30), 1)
        self.assertFalse(t_list.search(10))
        self.assertFalse(t_list.add(40))

    def test_add_letter_to_middle(self):
        t_list = OrderedList()
        t_list.add('a')
        t_list.add('b')
        t_list.add('d')
        t_list.add('e')
        self.assertEqual(t_list.size(), 4)
        self.assertFalse(t_list.is_empty())
        self.assertTrue(t_list.search('a'))
        t_list.add('c')
        self.assertEqual(t_list.index('c'), 2)
        t_list.remove('a')
        self.assertEqual(t_list.index('c'), 1)
        self.assertFalse(t_list.search('a'))

    def test_is_empty(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        self.assertFalse(t_list.remove(10))
        self.assertIsNone(t_list.index(10))
        self.assertRaises(IndexError, t_list.pop, 0)
        self.assertEqual(t_list.size(), 0)

    def test_item_not_in_list(self):
        t_list = OrderedList()
        t_list.add('a')
        t_list.add('b')
        t_list.add('d')
        t_list.add('e')
        self.assertFalse(t_list.remove(10))
        self.assertRaises(IndexError, t_list.pop, -2)
        self.assertRaises(IndexError, t_list.pop, 6)
        self.assertEqual(t_list.pop(2), 'd')
        t_list.add('d')
        self.assertFalse(t_list.search('f'))
        self.assertFalse(t_list.search('c'))
        self.assertEqual(t_list.python_list(), ['a', 'b', 'd', 'e'])
        self.assertEqual(t_list.python_list_reversed(), ['e', 'd', 'b', 'a'])

    def test_lower_upper_case_items(self):
        t_list = OrderedList()
        t_list.add('a')
        t_list.add('b')
        t_list.add('d')
        t_list.add('e')
        self.assertEqual(t_list.python_list(), ['a', 'b', 'd', 'e'])
        t_list.add('A')
        t_list.add('B')
        t_list.add('D')
        t_list.add('E')
        self.assertEqual(t_list.python_list(), ['A', 'B', 'D', 'E', 'a', 'b', 'd', 'e'])

    def test_reverse_and_index_none_tolerance(self):
        t_list = OrderedList()
        self.assertEqual(t_list.python_list_reversed(), [])
        self.assertEqual(t_list.index(5), None)


if __name__ == '__main__':
    unittest.main()
