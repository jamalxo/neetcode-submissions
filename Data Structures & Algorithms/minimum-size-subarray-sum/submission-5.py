class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minL = 2**31

        l = 0
        r = 0
        current = 0

        while r <= len(nums):
            if current >= target:
                minL = min((r-l), minL)
                current -= nums[l]
                l += 1
            #make smaller 
            else:
                current += nums[r]
                r += 1
            if r == len(nums) and current < target:
                break
        
        return minL if minL != 2**31 else 0