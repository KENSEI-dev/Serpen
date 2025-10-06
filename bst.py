class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)
    def searchBST(self, root, val):
        while root is not None and root.data != val:
            if val < root.data:
                root = root.left
            else:
                root = root.right
        return root
    def display_tree(self, root, space=0, label="Root:", val=None):
        if root is not None:
            print(" " * space + label + " " + str(root.data))
            if val is not None and root.data == val:
                print(" " * (space + 4) + "here it is.")
            self.display_tree(root.left, space + 4, "L-->", val)
            self.display_tree(root.right, space + 4, "R-->", val)
if __name__ == "__main__":
    
    tree = BinaryTree(10)
    tree.root.left = Node(5)
    tree.root.right = Node(20)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(7)
    tree.display_tree(tree.root, 0, "Root:", )
    result = tree.searchBST(tree.root, 5)
    '''if result is not None and result.data == 5:
        print("Finding value 5 in BST : True")
    else:
        print("Finding value 5 in BST : False")
'''