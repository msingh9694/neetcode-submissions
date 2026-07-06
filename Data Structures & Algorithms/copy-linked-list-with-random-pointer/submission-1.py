"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # original node -> copied node
        mp = {}

        # Step 1: Create a copy of every node
        cur = head
        while cur:
            mp[cur] = Node(cur.val)
            cur = cur.next

        # Step 2: Connect next and random pointers
        cur = head
        while cur:
            mp[cur].next = mp.get(cur.next)
            mp[cur].random = mp.get(cur.random)
            cur = cur.next

        # Return copied head
        return mp[head]
        