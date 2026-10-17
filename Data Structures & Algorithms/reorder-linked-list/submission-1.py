# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow

        # reverse second part
        prev = None
        current = middle

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        original_list = head

        dummy = ListNode()
        tail = dummy

        flip = True
        while prev and head:
            if flip:
                tail.next = head
                tail = tail.next
                head = head.next
            else:
                tail.next = prev
                prev = prev.next
                tail = tail.next
            flip = not flip

        #return dummy.next