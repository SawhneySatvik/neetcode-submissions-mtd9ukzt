class Node:
    def __init__(self, key:int, val: int):
        self.key = key
        self.val = val
        self.prev = self.nxt = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.nxt, self.right.prev = self.right, self.left

    def remove(self, node) -> None:
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def insert(self, node) -> None:
        prev_node = self.right.prev
        self.right.prev, prev_node.nxt = node, node
        node.nxt, node.prev = self.right, prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]