class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i, prev):
            #print(cache)
            if i >= len(nums):
                return 0
            
            if (i, prev) in cache:
                return cache[(i, prev)]

            can_take = True
            if prev is not None and nums[i] <= prev:
                can_take = False
            
            maxi = 0
            taking = 0
            #take
            if can_take:
                taking = 1 + dfs(i+1, nums[i])
            #skipping
            skipping = dfs(i+1, prev)

            maxi = max(taking, skipping)
            cache[(i, prev)] = maxi
            return maxi
        
        return dfs(0,None)

