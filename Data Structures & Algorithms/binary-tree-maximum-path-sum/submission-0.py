# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=float('-inf')
        def solve(node):
            nonlocal maxi
            if node is None:
                return 0
            leftsum=solve(node.left)
            if leftsum<0:
                leftsum=0
            rightsum=solve(node.right)
            if rightsum<0:
                rightsum=0
            maxi=max(maxi,leftsum+node.val+rightsum)
            return node.val+max(leftsum,rightsum)
        solve(root)
        return maxi

        