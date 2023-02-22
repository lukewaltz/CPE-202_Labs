import unittest

# Use the imports below to test either your array-based stack
from stack_array import Stack
# from stack_linked import Stack


class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)

    def test_size2(self):
        stack = Stack(5)
        stack.push(0)
        stack.push(1)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.peek(), 1)

    def test_stack_full(self):
        stack = Stack(2)
        stack.push(0)
        stack.push(1)
        self.assertFalse(stack.is_empty())
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.peek(), 1)
        self.assertRaises(IndexError, stack.push, 2)

    def test_stack_empty(self):
        stack = Stack(5)
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertRaises(IndexError, stack.pop)
        self.assertRaises(IndexError, stack.peek)

    def test_stack_pop(self):
        stack = Stack(5)
        stack.push(2)
        stack.push(1)
        stack.pop()
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 2)


if __name__ == '__main__':
    unittest.main()
