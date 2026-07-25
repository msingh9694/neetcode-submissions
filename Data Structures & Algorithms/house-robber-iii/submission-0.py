class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return (0, 0)   # (rob, notRob)

            left = dfs(node.left)
            right = dfs(node.right)

            rob = node.val + left[1] + right[1]

            notRob = max(left) + max(right)

            return (rob, notRob)

        return max(dfs(root))