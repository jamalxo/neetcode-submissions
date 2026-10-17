# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0

        dummy = head

        length = 0

        while head:
            head = head.next
            length += 1

        head = dummy

        while head:
            #print(length, n, i)
            if length - n - 1 == i:            
                head.next = head.next.next if head.next else None    
            elif length - n - 1 < 0:
                return head.next
            else:
                head = head.next
            i += 1
        
        return dummy