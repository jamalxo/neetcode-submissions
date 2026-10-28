class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2

        if sum(nums) % 2 != 0:
            return False

        cache = [[-1] * (target+1) for _ in range(len(nums))]

        #print(cache)

        def dfs(i, total):
            if i >= len(nums) or total > target:
                return False
            if cache[i][total] != -1:
                return cache[i][total]

            if total == target:
                return True
            
            cache[i][total] = dfs(i+1, total+nums[i]) or dfs(i+1, total)

            return cache[i][total]


        return dfs(0, 0)