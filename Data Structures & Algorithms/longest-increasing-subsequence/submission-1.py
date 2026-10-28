class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [[-1] * len(nums) for _ in range(len(nums))]

        def dfs(i, prev):
            if i >= len(nums):
                return 0
            if cache[i][prev] != -1:
                return cache[i][prev]

            take = 0
            skip = 0
            # take
            if nums[prev] < nums[i] or prev == -1:
                take = 1 + dfs(i+1, i)

            skip = dfs(i+1, prev)

            cache[i][prev] = max(take, skip)
            return cache[i][prev]

        test = dfs(0, -1)

        return test