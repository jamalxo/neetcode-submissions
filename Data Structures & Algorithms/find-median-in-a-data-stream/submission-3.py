class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

        if self.min_heap and self.min_heap[0] < -self.max_heap[0]:
            popped = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -popped)
        
        # even if max heap is + 1
        if len(self.max_heap) < len(self.min_heap):
            popped = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -popped)
        
        if len(self.max_heap) > len(self.min_heap)+1:
            popped = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -popped)

    def findMedian(self) -> float:
        #print(self.max_heap, self.min_heap)
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] + -self.max_heap[0])/2
        else:
            return -self.max_heap[0]
        