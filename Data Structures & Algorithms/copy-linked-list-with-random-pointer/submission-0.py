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
        # create dictionary
        copies = {None: None}

        dummy_head = head

        while head:
            copies[head] = Node(head.val)
            head = head.next

        head = dummy_head

        while head:
            copies[head].next = copies[head.next]
            copies[head].random = copies[head.random]
            head = head.next
        
        return copies[dummy_head]