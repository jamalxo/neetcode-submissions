class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        print(nums)
        res = []

        def dfs(i, arr):
            if len(arr) == k:
                res.append(arr)
                return
            if i >= len(nums):
                return
            print(i)
            new = arr + [nums[i]]
            dfs(i+1, new)
            dfs(i+1, arr)

        dfs(0, [])

        return res