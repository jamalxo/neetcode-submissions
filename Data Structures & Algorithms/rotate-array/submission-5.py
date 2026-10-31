class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        curr = start = 0
        curr_val = nums[curr] 
        i = 0

        while i < len(nums):
            #print(nums, curr, curr_val)
            new_i = (curr+k) % len(nums)
            temp = nums[new_i]
            nums[new_i] = curr_val
            curr_val = temp
            curr = new_i
            i+=1
            if curr == start:
                curr = (curr+1) % len(nums)
                curr_val = nums[curr]
                start = curr