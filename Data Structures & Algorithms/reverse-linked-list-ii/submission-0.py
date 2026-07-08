# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        pre=dummy
        for i in range(left-1):
            pre=pre.next
        currNode=pre.next
        preNode=None
        for i in range(right-left+1):
            nextNode=currNode.next
            currNode.next=preNode
            preNode=currNode
            currNode=nextNode
        pre.next.next=currNode
        pre.next=preNode
        return dummy.next

