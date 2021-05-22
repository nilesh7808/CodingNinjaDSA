class GenericTree:
    def __init__(self, data):
        self.data = data
        self.children = list()

def maxOfNodes(root):
    if root == None:
        return

    max = root
    for child in root.children:
        if max.data < maxOfNodes(child).data:
            max = maxOfNodes(child)
    return max

def takeTreeInput():
    print("Enter Root Node:-")
    rootData = int(input())
    if rootData == -1:
        return  None
    root = GenericTree(rootData)
    print("Enter number of child for",rootData)
    numberChild = int(input())
    for i in range(numberChild):
        child = takeTreeInput()
        root.children.append(child)
    return root

root = takeTreeInput()
print(maxOfNodes(root).data)