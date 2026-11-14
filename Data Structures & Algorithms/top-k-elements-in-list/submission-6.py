class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []

        freq = k


        c = Counter(nums)

        for k,v in c.items():
            heapq.heappush(h, (-v, k))

        res = []
        for i in range(freq):
            res.append(heapq.heappop(h)[1])
        
        return res