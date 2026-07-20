# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def reverse_postorder(node, level):
            if node is None:
                return

            if level == len(ans):
                ans.append(node.val)

            reverse_postorder(node.right, level + 1)
            reverse_postorder(node.left, level + 1)

        reverse_postorder(root, 0)

        return ans
        