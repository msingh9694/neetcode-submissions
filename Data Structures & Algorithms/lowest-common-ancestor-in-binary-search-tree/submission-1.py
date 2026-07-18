# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, node, p, q):
        if node is None:
            return None

        if node == p or node == q:
            return node

        left = self.solve(node.left, p, q)
        right = self.solve(node.right, p, q)

        if left is None and right is None:
            return None
        elif left is None:
            return right
        elif right is None:
            return left

        return node

    def lowestCommonAncestor(self, root, p, q):
         while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        