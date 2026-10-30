class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        hashed = key % 10**4
        init_node = self.set[hashed].next
        prev = self.set[hashed]
        while init_node:
            if init_node.key == key:
                return
            prev = init_node
            init_node = init_node.next
        prev.next = ListNode(key)

    def remove(self, key: int) -> None:
        hashed = key % 10**4
        init_node = self.set[hashed].next
        prev = self.set[hashed]
        while init_node:
            if init_node.key == key:
                prev.next = init_node.next
                return
            prev = init_node
            init_node = init_node.next
        

    def contains(self, key: int) -> bool:
        hashed = key % 10**4
        init_node = self.set[hashed].next
        while init_node:
            if init_node.key == key:
                return True
            init_node = init_node.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)