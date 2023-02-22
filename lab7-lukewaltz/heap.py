class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be
        created. '''
        self.capacity = capacity
        self.heap = [None] * (capacity + 1)
        self.num_items = 0

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator'''
        # Should call perc_up
        if self.is_full():
            return False
        self.num_items += 1
        self.heap[self.num_items] = item
        self.perc_up(self.num_items)
        return True

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.is_empty():
            return None
        return self.heap[1]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        if self.is_empty():
            return None
        max_item = self.heap[1]
        # replace root with bottom right
        self.heap[1], self.heap[self.num_items] = self.heap[self.num_items], self.heap[1]
        # move max to end of array
        self.num_items -= 1
        # remove old max from array completely
        self.heap.pop()
        # restore heap property
        self.perc_down(1)  # perc down max
        return max_item

    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        if self.is_empty():
            return None
        content = self.heap[1: self.num_items + 1]
        return content

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from 
        the items in alist using the bottom-up construction method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate 
        exactly the number of items in alist'''
        # Bottom-Up construction.  Do NOT call enqueue
        # capacity of the heap will be increased to accommodate exactly the number of items in alist
        self.num_items = 0
        for i in range(len(alist)):
            if i < len(self.heap) - 1:
                self.heap[i + 1] = alist[i]  # iterate through and assign alist vals to heap
                self.num_items += 1
            else:
                self.heap.append(alist[i])  # append so array grows beyond capacity
                self.num_items += 1
        # perc down starting at bottom
        for i in range(self.num_items, 0, -1):
            self.perc_down(i)

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        if self.num_items == 0:
            return True
        return False

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        if self.num_items == self.get_capacity():
            return True
        return False

    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return len(self.heap) - 1

    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.num_items

    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        complete = False
        while not complete and 2 * i <= self.num_items:  # there is a child
            # child indices
            child1 = 2 * i
            child2 = (2 * i) + 1
            # checks if children are actually in the heap
            if self.num_items >= child2 and self.heap[child2] > self.heap[child1]:
                if self.heap[i] < self.heap[child2]:
                    # swap
                    self.heap[i], self.heap[child2] = self.heap[child2], self.heap[i]
                    i = child2
                else:
                    complete = True
            else:
                if self.heap[child1] > self.heap[i]:
                    # swap
                    self.heap[i], self.heap[child1] = self.heap[child1], self.heap[i]
                    i = child1
                else:
                    complete = True

    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while i // 2 >= 1:
            parent = (i // 2)
            if self.heap[i] > self.heap[parent]:
                # swap
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        self.build_heap(alist)
        while self.num_items > 0:
            max_item = self.dequeue()
            alist[self.num_items] = max_item
