class ListNode:
    def __init__(self,key,val):
        self.key,self.val=key,val
        self.prev,self.next=None,None

class LRUCache:
    

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.left,self.right=ListNode(0,0),ListNode(0,0)
        self.left.next,self.right.prev=self.right,self.left

    def remove(self,node):
        prev,nxt=node.prev,node.next
        prev.next=nxt
        nxt.prev=prev
    def insert(self,node):
        prev,nxt=self.right.prev,self.right
        prev.next=node
        node.prev=prev
        node.next=nxt
        nxt.prev=node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node=ListNode(key,value)
        self.cache[key]=node
        self.insert(node)
        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
