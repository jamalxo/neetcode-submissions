# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        h = []

        for root in lists:
            while root:
                heapq.heappush(h, root.val)
                root = root.next

        while h:
            lowest = heapq.heappop(h)
            tail.next = ListNode(lowest)
            tail = tail.next
        
        return dummy.next