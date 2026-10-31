class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #boyer moore

        current = None
        for n in nums:
            if not current:
                current = (n, 1)
            if n == current[0]:
                current = (current[0], current[1]+1)
            else:
                current = (current[0], current[1]-1)
            if current[1] == 0:
                current = None
        
        return current[0]
