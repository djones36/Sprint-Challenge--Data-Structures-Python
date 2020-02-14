class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value == self.value:
            return "already in the Binary tree"
        elif value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Base case
        if self.value == target:
            return True
        elif target < self.value:
            if self.left != None:
                return self.left.contains(target)
        else:
            if self.right != None:
                return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        maximum = self.value
        if self.right != None:
            return self.right.get_max()
        else:
            return maximum

    # Call the function `cb` on the value of each node
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
