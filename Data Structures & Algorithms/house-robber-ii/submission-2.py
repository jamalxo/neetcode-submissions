class Solution:

    def dp(self, nums):
        cache = [-1] * len(nums)


        def dfs(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return cache[i]
        
        return dfs(0)

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return self.dp(nums)
        return max(self.dp(nums[1:]), self.dp(nums[:len(nums)-1]))