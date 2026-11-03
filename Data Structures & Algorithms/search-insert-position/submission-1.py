class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0

        r = len(nums)-1


        while l < r:
            #print(l,r)
            mid = (l+r) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid
            else:
                return mid
        print(l,r)


        if nums[l] < target and l == len(nums)-1:
            l = l+1
        elif nums[l] > target and l == 0:
            l = 0
        
        return l