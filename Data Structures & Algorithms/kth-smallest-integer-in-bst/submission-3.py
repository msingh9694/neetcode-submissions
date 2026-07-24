# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        curr = root

        while curr:

            # No left subtree
            if curr.left is None:
                count += 1
                if count == k:
                    return curr.val
                curr = curr.right

            else:
                # Find inorder predecessor
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                # Create thread
                if pred.right is None:
                    pred.right = curr
                    curr = curr.left

                # Thread already exists
                else:
                    pred.right = None
                    count += 1
                    if count == k:
                        return curr.val
                    curr = curr.right

