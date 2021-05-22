# import queue
class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def print_Detailed_Tree(root):
    if root == None:
        return
    print(root.data,end=": ")
    if root.left != None:
        print("L:",root.left.data,end=", ")
    if root.right != None:
        print("R:",root.right.data,end="")
    print()
    print_Detailed_Tree(root.left)
    print_Detailed_Tree(root.right)
    return root
def build_tree_from_pre_and_in(preOrder,inOrder):
    if len(preOrder) == 0:
        return None
    rootData = preOrder[0]
    root = BinaryTree(rootData)
    rootIndex_in_Inorder = -1
    for i in range(0,len(inOrder)):
        if inOrder[i] == rootData:
            rootIndex_in_Inorder = i
            break

    leftInOrder = inOrder[0:rootIndex_in_Inorder]
    rightInOrder = inOrder[rootIndex_in_Inorder + 1 :]

    lenleftSubtree = len(leftInOrder)

    leftPreOrder = preOrder[1:lenleftSubtree+1]
    rightPreOrder = preOrder[lenleftSubtree+1:]

    leftChild = build_tree_from_pre_and_in(leftPreOrder, leftInOrder)
    rightChild = build_tree_from_pre_and_in(rightPreOrder, rightInOrder)

    root.left = leftChild
    root.right = rightChild
    return root
    pass

# def input_levelwise_tree():
#     q = queue.Queue()
#     print("Enter Root")
#     rootData = int(input())
#     if rootData == -1:
#         return None
#     root = BinaryTree
#     q.put(root)
#     while (not(q.empty())):
#         Current_Node = q.get()
#         print("Enter Left Nodes of",Current_Node)
#         leftChildData = int(input())
#         if leftChildData != -1:
#             leftChild = BinaryTree(leftChildData)
#             Current_Node.left = leftChild
#             q.put(leftChild)
#
#         print("Enter right Child of",Current_Node)
#         rightChildData = int(input())
#         if rightChildData != -1:
#             rightChild = BinaryTree(rightChildData)
#             Current_Node.right = rightChild
#             q.put(rightChild)
#     return root
preOrder = [int (i) for i in input().strip().split()]
inOrder = list(int (i) for i in input().strip().split())
#
# root = input_levelwise_tree()
root = build_tree_from_pre_and_in(preOrder,inOrder)
print_Detailed_Tree(root)