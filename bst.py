class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Solution:
    def __init__(self,root_data):
        self.root=Node(root_data)
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None and root.val != val:
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return root