import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # create heap tuple (diff, index) k-heap

        comp = []

        for i in range(len(arr)):
            comp.append((abs(arr[i]-x), i))

        heapq.heapify(comp)

        res = []

        while k > 0:
            popped = heapq.heappop(comp)
            res.append(arr[popped[1]])
            k -=1

        print(res[::1])
        
        return sorted(res)