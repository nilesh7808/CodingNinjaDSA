class BinaryTreeCount:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def takeTreeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeCount(rootData)
    rootLeft = takeTreeInput()
    rootRight = takeTreeInput()
    root.left = rootLeft
    root.right = rootRight
    return root
def countNumNodes(root):
    if root == None:
        return 0
    leftcount = countNumNodes(root.left)
    rightCount = countNumNodes(root.right)
    return 1 + leftcount + rightCount

root = takeTreeInput()
print(countNumNodes(root))