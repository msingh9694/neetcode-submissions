from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        queue = deque([(p, q)])

        while queue:
            node1, node2 = queue.popleft()

            # Both nodes are None
            if node1 is None and node2 is None:
                continue

            # One node is None
            if node1 is None or node2 is None:
                return False

            # Values are different
            if node1.val != node2.val:
                return False

            # Compare left children
            queue.append((node1.left, node2.left))

            # Compare right children
            queue.append((node1.right, node2.right))

        return True