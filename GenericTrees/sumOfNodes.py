class GenericTree:
    def __init__(self, data):
        self.data = data
        self.children = list()

def sumNodes(root):
    if root == None:
        return
    sum = root.data
    for child in root.children:
        sum = sum + sumNodes(child)
    return sum

def takeTreeInput():
    print("Enter Root Node:-")
    rootData = int(input())

    if rootData == -1:
        return None

    root = GenericTree(rootData)
    print("Enter number of child for",rootData)
    numberNodes = int(input())
    for i in range(numberNodes):
        child = takeTreeInput()
        root.children.append(child)
    return root

root = takeTreeInput()
print(sumNodes(root))