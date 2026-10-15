class Solution:
    def binary_search(self, nums, target):
        l = 0
        r = len(nums)-1

        while l <= r:
            middle = (l+r) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        
        return None
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        pivot_index = 0

        while l <= r:
            if nums[l] < nums[r]:
                pivot_index = pivot_index if nums[pivot_index] < nums[l] else l

                break
            
            middle = (l+r) // 2
            pivot_index = pivot_index if nums[pivot_index] < nums[middle] else middle
            
            if nums[middle] >= nums[l]:
                l = middle + 1
            else:
                r = middle - 1

        ## binary search on the correct half
        one = self.binary_search(nums[:pivot_index:], target)
        two = self.binary_search(nums[pivot_index:], target)

        if one is not None:
            return one
        elif two is not None:
            return pivot_index + two
        else:
            return -1