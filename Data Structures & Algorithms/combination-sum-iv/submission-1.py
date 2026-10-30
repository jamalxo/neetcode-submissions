class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}
        
        def dfs(current):
            if current == target:
                return 1
            if current > target:
                return 0
            
            if current in cache:
                return cache[current]
            
            res = 0
            for num in nums:
                res += dfs(current + num)
            
            cache[current] = res
            return cache[current]
        
        test = dfs(0)
        #print(cache)
        return test