class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        

        def dfs(arr, i):
            
            summed = sum(arr)
            if arr and summed == target:
                self.res.append(arr.copy())
                return
            if arr and summed > target:
                return

            for i in range(i, len(nums)):
                new = list(arr)
                new.append(nums[i])
                dfs(new, i)
        
        dfs([], 0)
        
        return self.res
