class Solution:

    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []

        def dfs(i, curr):
            if i == len(nums):
                return curr
            
            new = curr ^ nums[i]
            left = dfs(i+1, new)
            right = dfs(i+1, curr)

            return left + right

        return dfs(0, 0)

        #return sum(subsets)