class Solution:

    def xor(self, arr):
        res = 0

        for num in arr:
            res = res ^ num

        return res

    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []

        def dfs(i, curr):
            if i >= len(nums):
                subsets.append(curr)
                return None
            
            # include or skip
            new = curr ^ nums[i]
            dfs(i+1, new)
            dfs(i+1, curr)

        dfs(0, 0)
        print(subsets)

        return sum(subsets)