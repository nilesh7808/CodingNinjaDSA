class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getDiameter(root):
    h, giveDiameter = Diameter(root)
    return giveDiameter


def Diameter(root):

    if root == None:
        return 0, 0

    h, ld = Diameter(root.left)
    h, rd = Diameter(root.right)
    lh = Diameter(root.left)
    rh = Diameter(root.right)

    return h, max(lh + rh, ld, rd)

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
print(getDiameter(root))