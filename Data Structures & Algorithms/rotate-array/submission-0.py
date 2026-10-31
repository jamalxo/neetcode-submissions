class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new = {}
        for i in range(len(nums)):
            new_i = (i + k) % (len(nums))
            new[new_i] = nums[i]
        
        print(new)

        for k,v in new.items():
            nums[k] = v
            
