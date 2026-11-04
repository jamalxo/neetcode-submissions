class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, arr, seen):
            if len(arr) == len(nums):
                res.append(arr)
                return

            for i in range(len(nums)):
                if i not in seen:
                    new = arr + [nums[i]]
                    seen.add(i)
                    dfs(i, new, seen)
                    seen.remove(i)

        dfs(0, [], set())
        return res



        