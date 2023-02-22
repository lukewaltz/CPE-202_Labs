from queue_array import Queue


class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right


def search_helper(key, cur):
    if key == cur.key:
        return True
    elif key < cur.key and cur.left is not None:
        return search_helper(key, cur.left)
    elif key > cur.key and cur.right is not None:
        return search_helper(key, cur.right)


def min_helper(cur):
    if cur.left is None:
        return cur.key, cur.data
    return min_helper(cur.left)


def max_helper(cur):
    if cur.right is None:
        return cur.key, cur.data
    return max_helper(cur.right)


def insert_helper(key, cur, data):
    if key < cur.key:
        if cur.left is None:
            cur.left = TreeNode(key, data)
        else:
            insert_helper(key, cur.left, data)
    elif key > cur.key:
        if cur.right is None:
            cur.right = TreeNode(key, data)
        else:
            insert_helper(key, cur.right, data)
    else:
        cur.data = data
    return cur


def height_helper(cur):
    if cur is None:
        return 0
    return 1 + max(height_helper(cur.left), height_helper(cur.right))


def inorder_helper(cur, inlist):
    if cur is not None:
        inorder_helper(cur.left, inlist)
        inlist.append(cur.key)
        inorder_helper(cur.right, inlist)
    return inlist


def preorder_helper(cur, prelist):
    if cur is not None:
        prelist.append(cur.key)
        preorder_helper(cur.left, prelist)
        preorder_helper(cur.right, prelist)
    return prelist


class BinarySearchTree:

    def __init__(self):
        # Returns empty BST
        self.root = None

    def is_empty(self):
        # returns True if tree is empty, else False
        if self.root is None:
            return True
        else:
            return False

    def search(self, key):
        # returns True if key is in a node of the tree, else False
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.root is not None:
            return search_helper(key, self.root)
        else:
            return False

    def insert(self, key, data=None):
        # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.root is None:
            self.root = TreeNode(key, data)
        else:
            self.root = insert_helper(key, self.root, data)

    def find_min(self):
        # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return None
        cur = self.root
        return min_helper(cur)

    def find_max(self):
        # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return None
        cur = self.root
        return max_helper(cur)

    def tree_height(self):  # return the height of the tree
        # returns None if tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return None
        return height_helper(self.root) - 1

    def inorder_list(self):
        # return Python list of BST keys representing in-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        cur = self.root
        inlist = []
        return inorder_helper(cur, inlist)

    def preorder_list(self):
        # return Python list of BST keys representing pre-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        cur = self.root
        prelist = []
        return preorder_helper(cur, prelist)

    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        # DON'T attempt to use recursion
        q = Queue(25000)  # Don't change this!
        lvlst = []
        cur = self.root
        if cur is None:
            return None
        q.enqueue(cur)
        while not q.is_empty():
            root = q.dequeue()
            lvlst.append(root.key)
            if root.left is not None:
                q.enqueue(root.left)
            if root.right is not None:
                q.enqueue(root.right)
        return lvlst
