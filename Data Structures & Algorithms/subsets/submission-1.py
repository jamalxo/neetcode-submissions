class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(i, arr):
            if i == len(nums):
                res.append(arr)
                return

            new = arr + [nums[i]]
            dfs(i+1, new)
            new2 = arr.copy()
            dfs(i+1, new2)

        dfs(0, [])

        return res
