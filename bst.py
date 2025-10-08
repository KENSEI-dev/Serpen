class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BT:
    def __init__(self,root_data):
        self.root=Node(root_data)
    def BinarySearchTree(self,root,val):
        while root is not None and root.data!=val:
            if val<root.data:
                root=root.left
            else:
                root=root.right
        return root
    def display(self,root,space=0,label="Root:",val=None):
        if root is not None:
            print(" " * space + label + " " + str(root.data))
            if root.data==val:
                print(" "*(space+4),"here it is")
            self.display(root.left,space+4,"L-->",val)
            self.display(root.right,space+4,"R-->",val)
    def countNodes(self,root):
        if root is None: 
            return 0
        lh=self.findheightLeft(root)
        rh=self.findheightRight(root)
        if lh==rh:
            return 2**lh-1
        
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
    def findheightLeft(self,root):
        height=0
        while root:
            height+=1
            root=root.left
        return height
    def findheightRight(self,root):
        height=0
        while root:
            height+=1
            root=root.right
        return height
    def findheight(self,root):
        if root is None:
            return 0
        lh=self.findheight(root.left)
        rh=self.findheight(root.right)
        return 1+ max(lh,rh)

if __name__=="__main__":
    tree = BT(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.left.left.left=Node(8)
    tree.root.left.left.right=Node(9)
    tree.root.left.right.left=Node(10)
    tree.root.left.right.right=Node(11)
    tree.root.right.left=Node(6)
    tree.root.right.right=Node(7)
    result=tree.BinarySearchTree(tree.root,20)
    print(tree.countNodes(tree.root))
    #print("found" if result is not None and result.data == 20 else "not found")
    #tree.display(tree.root,0,"Root:")
    print(tree.findheight(tree.root))