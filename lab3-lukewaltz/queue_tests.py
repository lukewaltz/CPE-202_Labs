import unittest
from queue_array import Queue
# from queue_linked import Queue


class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_simple(self):
        queue = Queue(5)
        queue.enqueue(0)
        self.assertFalse(queue.is_empty())
        self.assertFalse(queue.is_full())
        self.assertEqual(queue.size(), 1)

    def test_size2(self):
        queue = Queue(5)
        queue.enqueue(0)
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())
        self.assertFalse(queue.is_full())
        self.assertEqual(queue.size(), 2)

    def test_stack_full(self):
        queue = Queue(2)
        queue.enqueue(0)
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())
        self.assertTrue(queue.is_full())
        self.assertEqual(queue.size(), 2)
        self.assertRaises(IndexError, queue.enqueue, 2)

    def test_stack_empty(self):
        queue = Queue(2)
        self.assertTrue(queue.is_empty())
        self.assertFalse(queue.is_full())
        self.assertEqual(queue.size(), 0)
        self.assertRaises(IndexError, queue.dequeue)

    def test_full_queue_enqueue(self):
        queue = Queue(5)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        self.assertTrue(queue.is_full())
        self.assertFalse(queue.is_empty())
        self.assertRaises(IndexError, queue.enqueue, 6)

    def test_full_queue_dequeue(self):
        queue = Queue(5)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        self.assertTrue(queue.is_full())
        self.assertEqual(queue.dequeue(), 1)

    def test_full_queue_2x_dequeue(self):
        queue = Queue(5)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        self.assertTrue(queue.is_full())
        queue.dequeue()
        self.assertFalse(queue.is_full())
        self.assertEqual(queue.dequeue(), 2)

    def test_empty_queue_dequeue(self):
        queue = Queue(5)
        self.assertTrue(queue.is_empty())
        self.assertRaises(IndexError, queue.dequeue)

    def test_queue_len_0(self):
        queue = Queue(0)
        self.assertTrue(queue.is_empty())
        self.assertTrue(queue.is_full())

    def test_full_enqueue(self):
        queue = Queue(3)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertTrue(queue.is_full())
        self.assertRaises(IndexError, queue.enqueue, 4)

    def test_circular_impl(self):
        q = Queue(5)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.dequeue()
        q.dequeue()
        self.assertEqual(q.num_items, 2)
        q.enqueue(5)
        q.enqueue(6)
        q.enqueue(7)
        self.assertTrue(q.is_full())

    def test_fill_and_empty(self):
        queue = Queue(3)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue('h')
        self.assertTrue(queue.is_full())
        queue.dequeue()
        queue.dequeue()
        self.assertEqual(queue.dequeue(), 'h')
        self.assertTrue(queue.is_empty())


if __name__ == '__main__':
    unittest.main()
