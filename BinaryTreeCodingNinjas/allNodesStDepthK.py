class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printAllNodesDepth(root,k,d):
    if root == None:
        return None
    # 1st method
    # if k == 0:
    #     print(root.data,end=" ")
    #     return
    # printAllNodesDepth(root.left,k-1)
    # printAllNodesDepth(root.right,k-1)

    # 2nd Method
    if k == d:
        print(root.data,end=" ")
        return
    printAllNodesDepth(root.left,k,d+1)
    printAllNodesDepth(root.right, k, d + 1)

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
k = int(input("Enter k: "))
printAllNodesDepth(root,k,d=0)