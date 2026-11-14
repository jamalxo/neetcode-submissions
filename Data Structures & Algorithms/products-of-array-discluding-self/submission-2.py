class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        #populate
        curr = 1
        for i in range(len(nums)):
            if i - 1 < 0:
                res[i] = curr
            else:
                curr *= nums[i-1] 
                res[i] = curr

        curr = 1
        for i in range(len(nums)-1, -1, -1):
            if i + 1 >= len(nums):
                res[i] = curr * res[i]
            else:
                curr *= nums[i+1] 
                res[i] = curr * res[i]
        
        return res