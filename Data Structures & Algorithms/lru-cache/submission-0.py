class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    # remove node from list
    def remove(self, node):
        previous = node.prev
        nxt = node.next
        previous.next = node.next
        nxt.prev = node.prev

    # insert at most recently used / right
    def insert(self, node):
        node.prev = self.right.prev
        node.next = self.right
        node.prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        new_node = Node(key, value)

        # maybe have to think about the case where a key is replaced instead of added here
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = new_node
        self.insert(new_node)

        if len(self.cache) > self.capacity:
            # remove least recent used
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]