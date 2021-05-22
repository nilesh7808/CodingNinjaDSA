class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preOrder(root):
    if root == None:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)
def takeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTree(rootData)
    leftTree = takeInput()
    rightTree = takeInput()
    root.left = leftTree
    root.right = rightTree
    return root

root = takeInput()
preOrder(root)