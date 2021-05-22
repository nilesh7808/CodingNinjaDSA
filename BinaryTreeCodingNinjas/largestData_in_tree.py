class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def largestData(root):
    if root == None:
        return -1
    leftLargest = largestData(root.left)
    rightLargest = largestData(root.right)
    return max(leftLargest,rightLargest,root.data)
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
print(largestData(root))