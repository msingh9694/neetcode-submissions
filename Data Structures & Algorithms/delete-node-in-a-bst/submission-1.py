class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)

        if key in res:
            res.remove(key)

        # Build a balanced BST from the sorted inorder list
        def buildBST(nums):
            if not nums:
                return None

            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left = buildBST(nums[:mid])
            node.right = buildBST(nums[mid + 1:])
            return node

        return buildBST(res)