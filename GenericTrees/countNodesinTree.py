class GenericTree:
    def __init__(self, data):
        self.data = data
        self.children = list()

def printTree(root):
    if root == None:
        return
    print(root.data,":",end=" ")

    for child in root.children:
        print(child.data,",",end=" ")
    print()
    for child in root.children:
        printTree(child)

def takeTreeInput():
    print("Enter the root node:-")
    rootData = int(input())

    if rootData == -1:
        return None
    root = GenericTree(rootData)
    print("Enter number of children of", rootData)
    childrencount = int(input())
    for i in range(childrencount):
        child = takeTreeInput()
        root.children.append(child)
    return root


root = takeTreeInput()
printTree(root)