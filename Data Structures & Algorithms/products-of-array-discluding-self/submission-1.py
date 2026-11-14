class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        res = [0] * len(nums)


        #populate
        curr = 1
        for i in range(len(nums)):
            if i - 1 < 0:
                left[i] = curr
            else:
                curr *= nums[i-1] 
                left[i] = curr

        curr = 1
        for i in range(len(nums)-1, -1, -1):
            if i + 1 >= len(nums):
                right[i] = curr
            else:
                curr *= nums[i+1] 
                right[i] = curr
        
        for i in range(len(nums)):
            res[i] = left[i] * right[i]
        
        return res