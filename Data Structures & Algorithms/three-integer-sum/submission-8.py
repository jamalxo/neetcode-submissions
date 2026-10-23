class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = sorted(nums)

        res = []

        for i in range(len(a)):
            if i > 0 and a[i] == a[i-1]:
                continue
            
            l = i + 1
            r = len(a) - 1 

            while l < r:
                if a[l] + a[r] + a[i] == 0:
                    res.append([a[l], a[r], a[i]])
                    # skip repeats of number used
                    l += 1
                    r -= 1
                    while l<r and a[l] == a[l-1]:
                        l+=1  
                elif a[l] + a[r] + a[i] > 0:
                    r -= 1
                else:
                    l += 1
        
        return res

