class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def mirrorBinaryTree(root):
    if root == None:
        return None
    mirrorBinaryTree(root.left)
    mirrorBinaryTree(root.right)
    root.left, root.right = root.right, root.left
    print(root.data,end = " ")
    return root

def takeInput():
    rootData = int(input())
    if rootData == -1:
        return

    root = BinaryTree(rootData)
    leftTree = takeInput()
    rightTree = takeInput()
    root.left = leftTree
    root.right = rightTree
    return root

root = takeInput()
mirrorBinaryTree(root)