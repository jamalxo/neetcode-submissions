import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2

        # find i where to split the arrays
        total = (len(a) + len(b))
        half = (total+1) // 2

        # cut first array
        if len(b) < len(a):
            a, b = b, a

        l = 0 
        r = len(a)-1

        while True:
            i = (l+r) // 2
            j = half - i - 2

            inf = 2**31 +1

            a_left = a[i] if i >= 0 else -inf
            a_right = a[i+1] if i+1 < len(a) else inf
            b_right = b[j+1] if j+1 < len(b) else inf
            b_left = b[j] if j >= 0 else -inf
            

            if a_left <= b_right and b_left <= a_right:
                if total % 2 != 0:
                    return max(a_left, b_left)
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                r = i - 1
            else:
                l = i + 1
            



