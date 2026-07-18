# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = []
        new = []

        def preorder(node):
            if node is None:
                res.append(None)      # Add null marker
                return
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(p)

        def preorder1(node):
            if node is None:
                new.append(None)        # Add null marker
                return
            new.append(node.val)
            preorder1(node.left)
            preorder1(node.right)

        preorder1(q)

        for i in range(len(res)):
            if res == new:
                return True

        return False
        