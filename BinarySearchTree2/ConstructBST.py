class BinarySearchtree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.numNodes = 0

    def printTreeHelper(self, root):

        if root == None:
            return None

        print(root.data, end=": ")
        if root.left != None:
            print("L:", root.left.data,end="," )

        if root.right != None:
            print("R:", root.right.data, end=" ")
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)

    def printTree(self):
        self.printTreeHelper(self.root)

    def isPresentHelper(self, root, data):
        if root == None:
            return False

        if root.data == data:
            return True

        if root.data > data:
            return self.isPresentHelper(root.left, data)

        if root.data < data:
            return self.isPresentHelper(root.right, data)

    def isPresent(self, data):
        return self.isPresentHelper(self.root, data)

    def insertHelper(self, root, data):
        if root == None:
            node = BinarySearchtree(data)
            return node

        if root.data > data:
            root.left = self.insertHelper(root.left, data)
            return root

        else:
            root.right = self.insertHelper(root.right, data)
            return root

    def insert(self, data):
        self.numNodes += 1
        self.root = self.insertHelper(self.root, data)

    def min(self, root):
        if root == None:
            return 1000

        if root.left == None:
            return root.data
        return self.min(root.left)

    def DeleteHelper(self, root, data):
        if root == None:
            return False, None

        if root.data > data:
            deleted, newLeftNode = self.DeleteHelper(root.left, data)
            root.left = newLeftNode
            return deleted, root

        if root.data < data:
            deleted, newRightNode = self.DeleteHelper(root.right, data)
            root.right = newRightNode
            return deleted, root

        # if root is leaf

        if root.left == None and root.right == None:
            return True, None

        # if root has only one child

        if root.left == None:
            return True, root.right

        if root.right == None:
            return True, root.left

        # if root has two children
        replacement = self.min(root.right)
        root.data = replacement
        deleted, newRightNode = self.DeleteHelper(root.right, replacement)
        root.right = newRightNode
        return True, root

    def delete(self, data):
        deleted, newRoot = self.DeleteHelper(self.root, data)
        if deleted:
            self.numNodes -= 1
        self.root = newRoot
        return deleted

    def count(self):
        return self.numNodes

b = BST()
b.insert(10)
b.insert(5)
b.insert(12)
b.insert(10)
b.insert(7)
b.insert(4)
b.insert(11)
b.insert(15)
b.insert(12)
b.printTree()

print(b.isPresent(10))
print(b.isPresent(7))
print(b.delete(4))
print(b.delete(10))
print(b.count())
b.printTree()