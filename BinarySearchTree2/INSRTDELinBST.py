class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST2:
    def __init__(self):
        self.root = None
        self.numNodes = 0

    def printTree(self):
        return False
    #
    # def searchHelper(self, root, data):
    #     pass

    def search(self, data):
        return self.searchHelper(self.root, data)

    def insertHelper(self, root, data):
        if root == None:
            node = BinaryTreeNode(data)
            return node

        if root.data > data:
            root.left = self.insertHelper(root.left, data)
            return root

        else:
            root.right = self.insertHelper(root.right, data)
            return root

    def insert(self, data):
        self.numNodes += 1
        return self.insertHelper(self.root, data)

    def deleteHelper(self, root, data):
        if root == None:

    def delete(self, data):
        self.numNodes -= 1
        return self.deleteHelper(self.root, data)

    def count(self):
        return 0

b2 = BST2()
b2.insert(4)
b2.insert(2)
b2.insert(11)
print(b2.delete(5))
print(b2.count())