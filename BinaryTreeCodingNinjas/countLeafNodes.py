class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def countLeafNodes(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    countLeftNode = countLeafNodes(root.left)
    countRightNode = countLeafNodes(root.right)
    return countLeftNode + countRightNode
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
print(countLeafNodes(root))