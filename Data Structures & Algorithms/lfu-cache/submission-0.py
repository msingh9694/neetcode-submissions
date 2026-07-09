from collections import defaultdict


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

        self.size = 0

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

        self.size += 1

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

        self.size -= 1

    def removeLeft(self):
        if self.size == 0:
            return None

        node = self.left.next
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 0

        self.cache = {}
        self.freqMap = defaultdict(DLL)

    def update(self, node):
        freq = node.freq

        self.freqMap[freq].remove(node)

        if freq == self.minFreq and self.freqMap[freq].size == 0:
            self.minFreq += 1

        node.freq += 1
        self.freqMap[node.freq].insert(node)

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.update(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.update(node)
            return

        if len(self.cache) == self.capacity:
            lru = self.freqMap[self.minFreq].removeLeft()
            del self.cache[lru.key]

        node = Node(key, value)

        self.cache[key] = node
        self.freqMap[1].insert(node)

        self.minFreq = 1