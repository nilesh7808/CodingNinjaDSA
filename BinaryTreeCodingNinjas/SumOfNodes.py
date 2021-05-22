class BinaryTrees:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def treeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTrees(rootData)
    leftRoot = treeInput()
    rightRoot = treeInput()
    root.left = leftRoot
    root.right = rightRoot
    return root

def nodeSum(root):
    if root == None:
        return 0
    leftSum = nodeSum(root.left)
    rightSum = nodeSum(root.right)
    return (root.data + leftSum + rightSum)

root = treeInput()
print(nodeSum(root))
