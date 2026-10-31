class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        k= 0
        while i < len(nums):
            while i > 0 and i < len(nums) and nums[i] == nums[i-1]:
                k+=1
                del nums[i]
            i+=1
        print(nums, k)
        return len(nums)


