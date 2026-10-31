class ListNode:

    def __init__(self, key, value, next = None):
        self.key = key
        self.value = value
        self.next = next

    def update(self, value):
        self.value = value

class MyHashMap:

    def __init__(self):
        self.buckets = [ListNode(0, 0) for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        new = ListNode(key, value)
        hashed = key % 10**4
        prev = self.buckets[hashed]
        nxt = self.buckets[hashed].next
        while nxt:
            if nxt.key == key:
                nxt.update(value)
                return
            prev = prev.next
            nxt = nxt.next
        prev.next = new

    def get(self, key: int) -> int:
        hashed = key % 10**4
        nxt = self.buckets[hashed].next
        while nxt:
            if nxt.key == key:
                return nxt.value
            nxt = nxt.next
        return -1

    def remove(self, key: int) -> None:
        hashed = key % 10**4
        prev = self.buckets[hashed] 
        nxt = self.buckets[hashed].next
        while nxt:
            if nxt.key == key:
                prev.next = nxt.next
            prev = prev.next
            nxt = nxt.next
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)