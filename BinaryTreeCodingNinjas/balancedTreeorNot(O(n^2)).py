class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def getHeightandCheckBalanced(root):
    if root == None:
        return 0,True

    lh, isLeftBalanced = getHeightandCheckBalanced(root.left)
    rh, isRightBalanced = getHeightandCheckBalanced(root.right)

    h = 1 + max(lh, rh)

    if lh - rh > 1 and rh - lh > 1:
        return h, False

    if isLeftBalanced and isRightBalanced:
        return h, True
    else:
        return h, False

def isBalanced2(root):
    h, isrootBalancd = getHeightandCheckBalanced(root)
    return isrootBalancd

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
print(isBalanced2(root))