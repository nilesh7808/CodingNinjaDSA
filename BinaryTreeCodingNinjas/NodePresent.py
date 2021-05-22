class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def isNodePresent(root,x):
    if root == None:
        return False
    if root.data == x:
        return True
    leftPresent = isNodePresent(root.left,x)
    rightPresent = isNodePresent(root.right, x)
    if leftPresent :
        return True
    elif rightPresent :
        return True
    else:
        return False

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
x = int(input("X = "))
if isNodePresent(root,x):
    print("true")
else:
    print("false")