class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def printAllNodes(root):
    if root == None:
        return
    print(root.data, end=": ")
    if root.left != None:
        print("L:", root.left.data, end=" ")

    if root.right != None:
        print("R:", root.right.data)
    print()
    printAllNodes(root.left)
    printAllNodes(root.right)


def takeInput():
    rootData = int(input("Enter Data "))
    if rootData == -1:
        return
    root = BinaryTree(rootData)
    leftTree = takeInput()
    rightTree = takeInput()
    root.left = leftTree
    root.right = rightTree
    return root


root = takeInput()
printAllNodes(root)