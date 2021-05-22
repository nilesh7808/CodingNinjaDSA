class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def constructBST(lst):
    if len(lst) == 0:
        return None
    x = (len(lst)-1 )// 2
    rootData = lst[x]
    root = BinaryTreeNode(rootData)
    leftNodes = constructBST(lst[0:x])
    rightNodes = constructBST(lst[x+1:])
    root.left = leftNodes
    root.right = rightNodes
    return root
def preOrder(root):
    if root == None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)
n = int(input())
lst = [int(i) for i in input().strip().split()]
root = constructBST(lst)
preOrder(root)
