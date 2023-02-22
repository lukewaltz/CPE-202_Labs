class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        pass


class Queue:
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.front = None
        self.end = None
        self.num_items = 0
        pass

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        if self.front is None:
            return True
        return False

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == self.capacity:
            return True
        return False

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full():
            raise IndexError
        node = Node(item)
        if self.num_items == 0:
            self.front = node
            self.end = node
            self.num_items += 1
        else:
            self.end.next = node  # inserts the new node
            self.end = node
            self.num_items += 1  # increases num_items for the queue

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.num_items > 0:
            if self.num_items == 1:
                dequeued = self.front.item
                self.front = None
                self.end = None
                self.num_items = 0
                return dequeued
            dequeued = self.front.item
            self.front = self.front.next
            self.num_items -= 1
            return dequeued
        raise IndexError

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items
