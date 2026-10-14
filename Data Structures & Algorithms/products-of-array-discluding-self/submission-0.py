class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multi = []

        max_multi = nums[0]

        for i in range(1, len(nums)):
            max_multi = max_multi * nums[i]

        print(max_multi)
        
        for i, num in enumerate(nums):
            if num != 0:
                multi.append(max_multi//num)  
            else:
                tmp = 1
                for j in range(len(nums)):
                    if i != j:
                        tmp *= nums[j] 
                    else: 
                        continue
                multi.append(tmp)  

        return multi