class Solution:

    def xor(self, arr):
        res = 0

        for num in arr:
            res = res ^ num

        return res

    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []

        def dfs(i, arr):
            if i == len(nums):
                return arr
            if i > len(nums):
                return None
            
            # include or skip
            new = arr + [nums[i]]
            subsets.append(new)
            dfs(i+1, new)
            new2 = arr.copy()
            dfs(i+1, new2)

        dfs(0, [])

        summed = 0

        for sub in subsets:
            summed += self.xor(sub)
        
        return summed