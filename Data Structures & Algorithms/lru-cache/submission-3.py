class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    # map + doubly linkedlist   
    def __init__(self, capacity: int):
        self.nodes = {}
        self.capacity = capacity
        self.least = Node(0,0)
        self.most = Node(0,0)
        self.least.next = self.most
        self.most.prev = self.least
        
    # insert at right
    def insert(self, node):
        temp = self.most.prev
        self.most.prev = node
        node.next = self.most
        node.prev = temp
        temp.next = node

    def remove(self, node):
        nxt, prev = node.next, node.prev
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.nodes:
            self.remove(self.nodes[key])
            self.insert(self.nodes[key])
            return self.nodes[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        new_node = Node(key, value)
        
        # think of already exists
        if key in self.nodes:
            self.remove(self.nodes[key])
        self.nodes[key] = new_node
        self.insert(new_node)

        if len(self.nodes) > self.capacity:
            lru = self.least.next
            self.remove(lru)
            del self.nodes[lru.key]
        
        

        
