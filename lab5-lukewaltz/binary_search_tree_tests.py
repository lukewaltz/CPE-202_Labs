import unittest
from binary_search_tree import *


class TestLab5(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_insert_five(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(30, 'root')
        bst.insert(15, 'left eldest')
        bst.insert(45, 'right eldest')
        bst.insert(20, 'left right')
        bst.insert(40, 'right left')
        self.assertFalse(bst.is_empty())
        self.assertEqual(bst.find_max(), (45, 'right eldest'))
        self.assertEqual(bst.inorder_list(), [15, 20, 30, 40, 45])
        self.assertEqual(bst.preorder_list(), [30, 15, 20, 45, 40])
        self.assertEqual(bst.level_order_list(), [30, 15, 45, 20, 40])
        self.assertEqual(bst.tree_height(), 2)

    def test_search_empty(self):
        bst = BinarySearchTree()
        self.assertIsNone(bst.tree_height())
        self.assertIsNone(bst.level_order_list())
        self.assertTrue(bst.is_empty())
        self.assertIsNone(bst.find_max())
        self.assertIsNone(bst.find_min())
        self.assertFalse(bst.search(10))

    def test_4(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(30, 'root')
        bst.insert(15, 'left eldest')
        bst.insert(45, 'right eldest')
        bst.insert(20, 'left right')
        bst.insert(40, 'right left')
        self.assertTrue(bst.search(40))
        self.assertTrue(bst.search(15))
        self.assertEqual(bst.find_min(), (15, 'left eldest'))


if __name__ == '__main__':
    unittest.main()
