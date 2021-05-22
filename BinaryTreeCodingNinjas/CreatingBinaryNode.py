#pre -order
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# # def printTree(root):
# #     if root == None:
# #         return
# #     print(root.data)
# #     printDetailedOfTree(root.left)
# #     printDetailedOfTree(root.right)
def printDetailedOfTree(root):
    if root == None:
        return
    #pre-order
    print(root.data,end=" : ")
    if root.left != None:
        print("L", root.left.data,end=", ")
    if root.right != None:
        print("R" , root.right.data,end= " ")
    print()
    # post-order
    # if root.left != None:
    #     print("L", root.left.data, end=", ")
    # if root.right != None:
    #     print("R", root.right.data, end=" ")
    # print(root.data,end=" : ")
    # print()

    #in-order
    # if root.left != None:
    #     print("L", root.left.data, end=", ")
    # print(root.data,end=" : ")
    # if root.right != None:
    #     print("R", root.right.data, end=" ")

    # print()
    printDetailedOfTree(root.left)
    printDetailedOfTree(root.right)
btn1 = BinaryTreeNode(1)
btn2 = BinaryTreeNode(4)
btn3 = BinaryTreeNode(5)

btn1.left = btn2
btn1.right = btn3
printDetailedOfTree(btn1)