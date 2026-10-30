class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        to_delete = []
        for i, num in enumerate(nums):
            print(nums)
            if num != val:
                nums[k] = num
                k+=1
            
        #print(k, nums)
        return k