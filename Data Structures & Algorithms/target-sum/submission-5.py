class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i, total):
            if i >= len(nums) and total != target:
                return 0
        
            if total == target and i == len(nums):
                return 1

            if (i, total) in cache:
                return cache[(i, total)]

            positive = dfs(i+1, total + nums[i])

            negative = dfs(i+1, total - nums[i])

            new = positive + negative

            cache[(i, total)] = new
            return cache[(i, total)]
                
        return dfs(0, 0)