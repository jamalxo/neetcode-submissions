import sys
sys.setrecursionlimit(20000)
class Solution:

    def perfect(self, n):
        return (n**0.5).is_integer()


    def numSquares(self, n: int) -> int:
        nums = []

        for i in range(1, n+1):
            if self.perfect(i):
                nums.append(i)

        cache = {}

        def dfs(current):
            #print(current, nums)
            if current == n:
                return 0
            if current > n:
                return 2**31

            if current in cache:
                return cache[current]
            
            result = 2**31

            for j, coin in enumerate(nums):
                result = min(result, 1 + dfs(current + coin))
            
            cache[current] = result

            return cache[current]
        
        return dfs(0)
    