class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #find closest
        l = 0 
        r = len(arr)-1
        closest = None

        while l < r:
            mid = (l+r) // 2

            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid
        print(l,r)
        
        l, r = l-1, l

        for _ in range(k):
            if l < 0:
                r+=1
            elif r >= len(arr):
                l-=1
            elif x-arr[l] <= arr[r] -x:
                l-=1
            else:
                r+=1
        return arr[l+1:r]