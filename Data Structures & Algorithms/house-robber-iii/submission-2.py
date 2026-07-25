# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # return pair[withRoot,withoutRoot]
        def dfs(root):
            if not root:
                return [0,0]
            leftPair=dfs(root.left)
            rightPair=dfs(root.right)
            withRoot=root.val+leftPair[1]+rightPair[1]
            withoutRoot=max(leftPair)+max(rightPair)
            return [withRoot,withoutRoot]
        return max(dfs(root))
      #  Expression	Meaning
#root.val	Rob the current node.
#leftPair[1]	Since the current node is robbed, the left child cannot be robbed, so take the maximum amount when the left child is not robbed.
#rightPair[1]	Since the current node is robbed, the right child cannot be robbed, so take the maximum amount when the right child is not robbed.
#withRoot	Maximum money obtainable when the current node is robbed.

        