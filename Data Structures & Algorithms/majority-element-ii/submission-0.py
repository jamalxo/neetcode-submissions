from collections import Counter
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []

        thresh = len(nums) // 3
        #print(thresh)
        c = Counter(nums)

        for k,v in c.items():
            if v > thresh:
                res.append(k)

            
        return res