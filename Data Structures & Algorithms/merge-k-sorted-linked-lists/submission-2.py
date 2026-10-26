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

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(h, (head.val, i, head))

        
        while h:
            val, i, node = heapq.heappop(h)
            tail.next = ListNode(val)
            tail = tail.next
            node = node.next
            if node:
                heapq.heappush(h, (node.val, i, node))

        return dummy.next