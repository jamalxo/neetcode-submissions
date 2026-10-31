class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        results = []
        #boyers moore
        one = count_one = 0
        two = count_two = 0

        thresh = len(nums) // 3

        for i, n in enumerate(nums):
            if n == nums[one]:
                count_one +=1
            elif n == nums[two]:
                count_two +=1
            elif count_two == 0:
                two = i
                count_two = 1
            elif count_one == 0:
                one = i
                count_one = 1
            else:
                count_one -=1
                count_two -=1

        count_one = 0
        count_two = 0

        for i, n in enumerate(nums):
            if n == nums[one]:
                count_one +=1
            elif n == nums[two]:
                count_two +=1

        if count_one > thresh:
            results.append(nums[one])
        if count_two > thresh:
            results.append(nums[two])
        return results