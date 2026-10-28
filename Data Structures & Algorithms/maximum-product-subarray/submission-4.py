import sys
sys.setrecursionlimit(50000)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)

        res = 0

        def dfs(i):
            if i >= len(nums):
                return (1,1)
            if cache[i] != -1:
                return cache[i]

            next_min, next_max = dfs(i+1)

            a,b,c = nums[i], nums[i] * next_min, nums[i] * next_max

            one = min(a,b,c)
            two = max(a,b,c)

            cache[i] = (one, two)

            return cache[i]

        test = dfs(0)[1]
        


        return max(pair[1] for pair in cache)