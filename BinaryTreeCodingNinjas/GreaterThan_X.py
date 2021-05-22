class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def greaterThan(root,x):
    count = 0
    if root == None:
        return 0
    count += greaterThan(root.left, x)
    count += greaterThan(root.right, x)
    if root.data > x:
        count += 1
    return count
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
print(greaterThan(root,x))