class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if (sum(nums)) % 2 != 0:
            return False

        total = sum(nums) // 2

        cache = {}

        def dfs(i, curr):
            if i >= len(nums):
                #do something
                if curr == total:
                    return True
                else:
                    return False

            if (i, curr) in cache:
                return cache[(i, curr)]

            #take
            take = dfs(i+1, curr+nums[i])

            #skip
            skip = dfs(i+1, curr)

            cache[(i, curr)] = take or skip

            return take or skip


        return dfs(0, 0)