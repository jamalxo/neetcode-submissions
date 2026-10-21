class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums = sorted(nums)

        for i, value in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1
            while l < r:
                if value + nums[l] + nums[r] == 0:
                    res.append([value, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1                    # skip repeats of the number just used
                if value + nums[l] + nums[r] > 0:
                    r -= 1
                if value + nums[l] + nums[r] < 0:
                    l +=1
                
            
        return res
            