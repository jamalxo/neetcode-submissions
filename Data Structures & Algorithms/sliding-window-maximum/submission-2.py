class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0

        h = []
        min_value = 2**31
        res = []

        while r < len(nums):
            negated = -nums[r]
            heapq.heappush(h, (negated, r))

            if r-l == k-1:
                res.append(h[0][0])
                l += 1
            
            while h and h[0][1] < l:
                heapq.heappop(h)

            r += 1

        return [-1 * i for i in res]


