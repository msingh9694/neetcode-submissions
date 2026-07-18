# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res=[]
        p=[]
        def preorder(node):
            if node is  None:
                res.append(None)
                return 
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        def preorder1(node):
            if node is None:
                p.append(None)
                return
            p.append(node.val)
            preorder1(node.left)
            preorder1(node.right)
        preorder1(subRoot)
        k = len(p)
        for i in range(len(res) - k + 1):
            if res[i:i+k] == p:
                return True
        return False
            
        