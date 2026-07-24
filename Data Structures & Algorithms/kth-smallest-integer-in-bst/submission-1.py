# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        def preorder(node):
            if node is None:
                return
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        res=sorted(res) #res.sort()
        return res[k-1]
            
        
            
            
            

        
        