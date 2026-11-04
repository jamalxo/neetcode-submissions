class Solution:

    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        cache = {}

        def dfs(i, curr):
            if i == len(nums):
                return curr

            if (i, curr) in cache:
                return cache[(i, curr)]
            
            new = curr ^ nums[i]
            left = dfs(i+1, new)
            right = dfs(i+1, curr)

            cache[(i, curr)] = left + right

            return cache[(i, curr)]

        return dfs(0, 0)