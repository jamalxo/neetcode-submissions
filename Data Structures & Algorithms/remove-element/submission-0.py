class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        to_delete = []
        for i, num in enumerate(nums):
            if num != val:
                k+=1
            else:
                to_delete.append(i)

        for i in to_delete:
            nums[i] = 99
        nums.sort()

        #print(k, nums)
        return k