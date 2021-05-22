class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printDetailedTree(root):
    if root == None:
        return
    print(root.data,end= " : ")
    if root.left != None:
        print("L",root.left.data,end= ", ")
    if root.right != None:
        print("R",root.right.data,end = " ")
    print()
    printDetailedTree(root.left)
    printDetailedTree(root.right)

def takeTreeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    leftTree = takeTreeInput()
    rightTree = takeTreeInput()
    root.left = leftTree
    root.right = rightTree
    return root
root = takeTreeInput()
printDetailedTree(root)