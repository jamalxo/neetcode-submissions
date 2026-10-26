# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self,head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
    def length(self,head):
        i = 0
        while head:
            i+=1
            head = head.next
        return i

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        groups = []
        i = 0
        start = None
        while head:
            if i % k == 0:
                start = head
            temp = head.next
            if i % k == k-1:
                groups.append(start)
                head.next = None
            head = temp
            i+=1
        if i % k != 0:          # after the loop, i == number of nodes
            groups.append(start)

        
        connect = None
        rev = []
        for root in groups:
            new = None
            if self.length(root) == k:
                new = (self.reverse(root), root)
            else:
                temp = root
                while root.next:
                    root = root.next
                new = (temp, root)
            rev.append(new)
        
        tail = None
        result = rev[0][0]
        for tup in rev:
            if not tail:
                tail = tup[1]
            else:
                tail.next = tup[0]
                tail = tup[1]
        
        return result
















        