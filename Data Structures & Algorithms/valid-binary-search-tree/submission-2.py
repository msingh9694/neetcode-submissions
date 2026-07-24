# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []
        self.helper(root, inorder)

        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i - 1]:
                return False

        return True

    def helper(self, root, inorder):
        if not root:
            return

        self.helper(root.left, inorder)
        inorder.append(root.val)
        self.helper(root.right, inorder)
        